from dateutil.relativedelta import relativedelta
from django.apps import apps
from django.db import models
from django.db.models import Q

from indicadores_esus.core.models import (CBO, CIAP, CID, Appointment, Child,
                                          City, Diabetic, HealthTeam,
                                          HealthUnit, Hypertensive,
                                          PatientIndicator, PatientProcedure,
                                          Person, PregnantWoman, Role,
                                          Vaccination, Woman)
from indicadores_esus.core.utils import set_int_to_date
from indicadores_esus.esus.models import (TbCidadao, TbFatCidadaoPec,
                                          TbProntuario)


class CalculatedIndicatorManager(models.Manager):

    def save_data_indicator(self, data, indicator):
        for i, p in enumerate(data.get('denominator')):
            try:
                appointment_city = p.appointments[0].co_dim_municipio
            except (AttributeError, IndexError):
                appointment_city = p.individual_registers[0].co_dim_municipio
            
            city = City.objects.get(ibge_code=appointment_city.co_ibge)
            linked_health_unit = None
            if hasattr(p.co_dim_unidade_saude_vinc, 'co_seq_dim_unidade_saude'):
                linked_health_unit = HealthUnit.objects.get_or_create_unit(
                    code=p.co_dim_unidade_saude_vinc.co_seq_dim_unidade_saude,
                    city=city,
                    cnes=p.co_dim_unidade_saude_vinc.nu_cnes,
                    name=p.co_dim_unidade_saude_vinc.no_unidade_saude.title(),
                    neighborhood=p.co_dim_unidade_saude_vinc.no_bairro,
                )
            linked_health_team = None
            if hasattr(p.co_dim_equipe_vinc, 'co_seq_dim_equipe'):
                linked_health_team = HealthTeam.objects.get_or_create_team(
                    code=p.co_dim_equipe_vinc.co_seq_dim_equipe,
                    city=city,
                    ine=p.co_dim_equipe_vinc.nu_ine,
                    name=p.co_dim_equipe_vinc.no_equipe.title(),
                )

            gender = ''
            if p.co_dim_sexo_id == 2:
                gender = 'F'
            elif p.co_dim_sexo_id == 1:
                gender = 'M'
            try:
                birth_date = set_int_to_date(p.co_dim_tempo_nascimento)
            except ValueError:
                birth_date = None

            citizen = TbCidadao.objects.filter(
                Q(Q(nu_cpf__isnull=False) & Q(nu_cpf=p.nu_cpf_cidadao))
                | Q(Q(nu_cns__isnull=False) & Q(nu_cns=p.nu_cns))
            ).order_by('-dt_atualizado').first()

            individual_register = True if len(p.individual_registers) > 0 else False

            name = p.no_cidadao.title() if p.no_cidadao else 'SEM NOME REGISTRADO'
            patient = Role.objects.get_or_create_role(
                code=p.co_seq_fat_cidadao_pec, role_type=1, city=city, 
                unit=linked_health_unit, team=linked_health_team,
                cpf=p.nu_cpf_cidadao, cns=p.nu_cns, 
                individual_register=individual_register, name=name,
                gender=gender, birth_date=birth_date, citizen=citizen,
            )

            if indicator.type in ['1', '2', '3']:
                try:
                    pregnancy_status = True if p.individual_registers[0] == 1 else False
                except IndexError:
                    pregnancy_status = False
                pregnant = PregnantWoman.objects.get_or_create(patient=patient)
                pregnant[0].dum = p.dum
                pregnant[0].dpp = p.dpp
                pregnant[0].is_pregnant = pregnancy_status
                pregnant[0].save()

                for app in p.appointments:
                    appointment = Appointment.objects.get_or_create_appointment(
                        code=app.co_seq_fat_atd_ind,
                        appointment_type='M',
                        city=city,
                        patient=patient,
                        date=app.dt_inicial_atendimento.date(),
                        health_unit=app.co_dim_unidade_saude_1,
                        health_team=app.co_dim_equipe_1,
                        professional=app.co_dim_profissional_1,
                        cbo=app.co_dim_cbo_1
                    )

                    for proc in app.hiv_sifilis_requested_procedures:
                        PatientProcedure.objects.get_or_create_procedure(
                            patient=patient,
                            esus_code=proc.co_seq_fat_atend_ind_proced,
                            procedure=proc.co_dim_procedimento_solicitado,
                            date=proc.co_dim_tempo.dt_registro,
                            health_unit=proc.co_dim_unidade_saude_1,
                            health_team=proc.co_dim_equipe_1,
                            professional=proc.co_dim_profissional_1,
                            cbo=proc.co_dim_cbo_1,
                            requested=appointment,
                            city=city,
                        )

                    for proc in app.hiv_sifilis_evaluated_procedures:
                        PatientProcedure.objects.get_or_create_procedure(
                            patient=patient,
                            esus_code=proc.co_seq_fat_atend_ind_proced,
                            procedure=proc.co_dim_procedimento_solicitado,
                            date=proc.co_dim_tempo.dt_registro,
                            health_unit=proc.co_dim_unidade_saude_1,
                            health_team=proc.co_dim_equipe_1,
                            professional=proc.co_dim_profissional_1,
                            cbo=proc.co_dim_cbo_1,
                            evaluated=appointment,
                            city=city,
                        )
                    
                    for cond in app.pregnancy_condition:
                        cid = CID.objects.get_or_create(
                            esus_id=cond.co_dim_cid.co_seq_dim_cid,
                            code=cond.co_dim_cid.nu_cid,
                            name=cond.co_dim_cid.no_cid.title()
                        )
                        ciap = CIAP.objects.get_or_create(
                            esus_id=cond.co_dim_ciap.co_seq_dim_ciap,
                            code=cond.co_dim_ciap.nu_ciap,
                            name=cond.co_dim_ciap.no_ciap.title()
                        )

                        appointment.cids.add(cid[0])
                        appointment.ciaps.add(ciap[0])

                for dental in p.dental_appointments:
                    dental_appointment = Appointment.objects.get_or_create_appointment(
                        code=dental.co_seq_fat_atd_odnt,
                        appointment_type='O',
                        city=city,
                        patient=patient,
                        date=dental.dt_inicial_atendimento.date(),
                        health_unit=dental.co_dim_unidade_saude_1,
                        health_team=dental.co_dim_equipe_1,
                        professional=dental.co_dim_profissional_1,
                        cbo=dental.co_dim_cbo_1,
                        cids=dental.ds_filtro_cids,
                        ciaps=dental.ds_filtro_ciaps,
                    )

                    for cond in dental.conditions_list:
                        cid = CID.objects.get_or_create(
                            esus_id=cond.co_dim_cid.co_seq_dim_cid,
                            code=cond.co_dim_cid.nu_cid,
                            name=cond.co_dim_cid.no_cid.title()
                        )
                        ciap = CIAP.objects.get_or_create(
                            esus_id=cond.co_dim_ciap.co_seq_dim_ciap,
                            code=cond.co_dim_ciap.nu_ciap,
                            name=cond.co_dim_ciap.no_ciap.title()
                        )

                        dental_appointment.cids.add(cid[0])
                        dental_appointment.ciaps.add(ciap[0])
                
                for proc in p.all_procedures:
                    PatientProcedure.objects.get_or_create_procedure(
                        patient=patient,
                        esus_code=proc.co_seq_fat_proced_atend_proced,
                        procedure=proc.co_dim_procedimento,
                        date=proc.co_dim_tempo.dt_registro,
                        health_unit=proc.co_dim_unidade_saude,
                        health_team=proc.co_dim_equipe,
                        professional=proc.co_dim_profissional,
                        cbo=proc.co_dim_cbo,
                        city=city,
                    )
                
            elif indicator.type == '4':
                woman = Woman.objects.get_or_create(patient=patient)
                woman[0].save()

                for proc in p.cytopathological_procedures_1:
                    PatientProcedure.objects.get_or_create_procedure(
                        patient=patient,
                        esus_code=proc.co_seq_fat_atend_ind_proced,
                        procedure=proc.co_dim_procedimento_solicitado,
                        date=proc.co_dim_tempo.dt_registro,
                        health_unit=proc.co_dim_unidade_saude_1,
                        health_team=proc.co_dim_equipe_1,
                        professional=proc.co_dim_profissional_1,
                        cbo=proc.co_dim_cbo_1,
                        city=city,
                    )

                for proc in p.cytopathological_procedures_2:
                    PatientProcedure.objects.get_or_create_procedure(
                        patient=patient,
                        esus_code=proc.co_seq_fat_proced_atend_proced,
                        procedure=proc.co_dim_procedimento,
                        date=proc.co_dim_tempo.dt_registro,
                        health_unit=proc.co_dim_unidade_saude,
                        health_team=proc.co_dim_equipe,
                        professional=proc.co_dim_profissional,
                        cbo=proc.co_dim_cbo,
                        city=city,
                    )
            
            elif indicator.type == '5':
                child = Child.objects.get_or_create(patient=patient)
                child[0].save()

                for vaccination in p.vaccinations:
                    if hasattr(vaccination, 'all_vaccines'):
                        for vaccine in vaccination.all_vaccines:
                            Vaccination.objects.get_or_create_vaccination(
                                esus_code=vaccine.co_seq_fat_vacinacao_vacina,
                                patient=patient,
                                vaccine_type=vaccine.co_dim_imunobiologico,
                                date=vaccine.co_dim_tempo.dt_registro,
                                dose_info=vaccine.co_dim_dose_imunobiologico,
                                health_unit=vaccine.co_dim_unidade_saude,
                                health_team=vaccine.co_dim_equipe,
                                professional=vaccine.co_dim_profissional,
                                cbo=vaccine.co_dim_cbo,
                                city=city,
                            )

            elif indicator.type == '6':
                hypertensive = Hypertensive.objects.get_or_create(patient=patient)
                hypertensive[0].save()

                for app in p.appointments:
                    appointment = Appointment.objects.get_or_create_appointment(
                        code=app.co_seq_fat_atd_ind,
                        appointment_type='M',
                        city=city,
                        patient=patient,
                        date=app.dt_inicial_atendimento.date(),
                        health_unit=app.co_dim_unidade_saude_1,
                        health_team=app.co_dim_equipe_1,
                        professional=app.co_dim_profissional_1,
                        cbo=app.co_dim_cbo_1,
                        cids=app.ds_filtro_cids,
                        ciaps=app.ds_filtro_ciaps,
                    )

                    for proc in app.blood_pressure_measure_requested_procedures:
                        PatientProcedure.objects.get_or_create_procedure(
                            patient=patient,
                            esus_code=proc.co_seq_fat_atend_ind_proced,
                            procedure=proc.co_dim_procedimento_solicitado,
                            date=proc.co_dim_tempo.dt_registro,
                            requested=appointment,
                            health_unit=proc.co_dim_unidade_saude_1,
                            health_team=proc.co_dim_equipe_1,
                            professional=proc.co_dim_profissional_1,
                            cbo=proc.co_dim_cbo_1,
                            city=city,
                        )

                    for proc in app.blood_pressure_measure_evaluated_procedures:
                        PatientProcedure.objects.get_or_create_procedure(
                            patient=patient,
                            esus_code=proc.co_seq_fat_atend_ind_proced,
                            procedure=proc.co_dim_procedimento_solicitado,
                            date=proc.co_dim_tempo.dt_registro,
                            evaluated=appointment,
                            health_unit=proc.co_dim_unidade_saude_1,
                            health_team=proc.co_dim_equipe_1,
                            professional=proc.co_dim_profissional_1,
                            cbo=proc.co_dim_cbo_1,
                            city=city,
                        )

                    for cond in app.hypertensive_condition:
                        cid = CID.objects.get_or_create(
                            esus_id=cond.co_dim_cid.co_seq_dim_cid,
                            code=cond.co_dim_cid.nu_cid,
                            name=cond.co_dim_cid.no_cid.title()
                        )
                        ciap = CIAP.objects.get_or_create(
                            esus_id=cond.co_dim_ciap.co_seq_dim_ciap,
                            code=cond.co_dim_ciap.nu_ciap,
                            name=cond.co_dim_ciap.no_ciap.title()
                        )

                        appointment.cids.add(cid[0])
                        appointment.ciaps.add(ciap[0])

                for proc in p.pressure_measure_2:
                    PatientProcedure.objects.get_or_create_procedure(
                        patient=patient,
                        esus_code=proc.co_seq_fat_proced_atend_proced,
                        procedure=proc.co_dim_procedimento,
                        date=proc.co_dim_tempo.dt_registro,
                        health_unit=proc.co_dim_unidade_saude,
                        health_team=proc.co_dim_equipe,
                        professional=proc.co_dim_profissional,
                        cbo=proc.co_dim_cbo,
                        city=city,
                    )

            elif indicator.type == '7':
                diabetic = Diabetic.objects.get_or_create(patient=patient)
                diabetic[0].save()

                for app in p.appointments:
                    appointment = Appointment.objects.get_or_create_appointment(
                        code=app.co_seq_fat_atd_ind,
                        appointment_type='M',
                        city=city,
                        patient=patient,
                        date=app.dt_inicial_atendimento.date(),
                        health_unit=app.co_dim_unidade_saude_1,
                        health_team=app.co_dim_equipe_1,
                        professional=app.co_dim_profissional_1,
                        cbo=app.co_dim_cbo_1,
                        cids=app.ds_filtro_cids,
                        ciaps=app.ds_filtro_ciaps,
                    )

                    for proc in app.glycated_hemoglobin_requested_procedures:
                        PatientProcedure.objects.get_or_create_procedure(
                            patient=patient,
                            esus_code=proc.co_seq_fat_atend_ind_proced,
                            procedure=proc.co_dim_procedimento_solicitado,
                            date=proc.co_dim_tempo.dt_registro,
                            requested=appointment,
                            health_unit=proc.co_dim_unidade_saude_1,
                            health_team=proc.co_dim_equipe_1,
                            professional=proc.co_dim_profissional_1,
                            cbo=proc.co_dim_cbo_1,
                            city=city,
                        )

                    for proc in app.glycated_hemoglobin_evaluated_procedures:
                        PatientProcedure.objects.get_or_create_procedure(
                            patient=patient,
                            esus_code=proc.co_seq_fat_atend_ind_proced,
                            procedure=proc.co_dim_procedimento_solicitado,
                            date=proc.co_dim_tempo.dt_registro,
                            evaluated=appointment,
                            health_unit=proc.co_dim_unidade_saude_1,
                            health_team=proc.co_dim_equipe_1,
                            professional=proc.co_dim_profissional_1,
                            cbo=proc.co_dim_cbo_1,
                            city=city,
                        )
                    
                    for cond in app.diabetic_condition:
                        cid = CID.objects.get_or_create(
                            esus_id=cond.co_dim_cid.co_seq_dim_cid,
                            code=cond.co_dim_cid.nu_cid,
                            name=cond.co_dim_cid.no_cid.title()
                        )
                        ciap = CIAP.objects.get_or_create(
                            esus_id=cond.co_dim_ciap.co_seq_dim_ciap,
                            code=cond.co_dim_ciap.nu_ciap,
                            name=cond.co_dim_ciap.no_ciap.title()
                        )

                        appointment.cids.add(cid[0])
                        appointment.ciaps.add(ciap[0])

                for proc in p.glycated_hemoglobin_2:
                    PatientProcedure.objects.get_or_create_procedure(
                        patient=patient,
                        esus_code=proc.co_seq_fat_proced_atend_proced,
                        procedure=proc.co_dim_procedimento,
                        date=proc.co_dim_tempo.dt_registro,
                        health_unit=proc.co_dim_unidade_saude,
                        health_team=proc.co_dim_equipe,
                        professional=proc.co_dim_profissional,
                        cbo=proc.co_dim_cbo,
                        city=city,
                    )

            numerator=False
            if p in data.get('numerator'):
                numerator = True

            p_indicator = PatientIndicator(
                patient=patient, indicator=indicator, numerator=numerator
            )
            p_indicator.save()

            print(f"{i+1} de {len(data.get('denominator'))} - {p_indicator}")

    
    def get_data_indicator_1(self, quad=None, indicator=None):
        pregnant_women = TbFatCidadaoPec.objects.pregnant_women(quad)
        
        denominator_list = []
        numerator_list = []

        for p in pregnant_women:
            abortion = False

            temp_dum = p.appointments[0].co_dim_tempo_dum.dt_registro
            ig = p.appointments[0].nu_idade_gestacional_semanas
            dt_first_appointment = p.appointments[0].co_dim_tempo.dt_registro
            dum_ig = (dt_first_appointment - relativedelta(weeks=ig)) if ig is not None else temp_dum
            dum = temp_dum if temp_dum <= dum_ig else dum_ig
            dpp = dum + relativedelta(days=294)

            valid_appointments = []

            for app in p.appointments:
                
                if dum <= app.co_dim_tempo.dt_registro <= dpp:
                    valid_appointments.append(app)
                    if len(app.abortion_condition) > 0:
                        abortion = True

                elif app.co_dim_tempo.dt_registro > dpp:
                    temp_dum = app.co_dim_tempo_dum.dt_registro
                    ig = app.nu_idade_gestacional_semanas
                    dt_first_appointment = app.co_dim_tempo.dt_registro
                    dum_ig = (dt_first_appointment - relativedelta(weeks=ig)) if ig is not None else temp_dum
                    dum = temp_dum if temp_dum <= dum_ig else dum_ig
                    dpp = dum + relativedelta(days=294)
                    abortion = False if len(app.abortion_condition) == 0 else True
                    valid_appointments = [app]
            
            uuid_list = []
            
            for v in valid_appointments:
                v.duplicated = False
                if v.nu_uuid_ficha in uuid_list:
                    v.duplicated = True
                else:
                    uuid_list.append(v.nu_uuid_ficha)

            valid_appointments = [va for va in valid_appointments if not va.duplicated]

            if not abortion and (quad.evaluation_start <= dpp <= quad.evaluation_end):
                denominator_list.append(p)
                if len(valid_appointments) >= 6 and dt_first_appointment < (dum + relativedelta(weeks=13)):
                    numerator_list.append(p)

            p.dum = dum
            p.dpp = dpp
            p.appointments = valid_appointments

        data = {
            'denominator': denominator_list,
            'numerator': numerator_list
        }
        self.save_data_indicator(data, indicator)
        return data

    def get_data_indicator_2(self, quad=None, indicator=None):
        pregnant_women = TbFatCidadaoPec.objects.pregnant_women(quad)
        
        denominator_list = []
        numerator_list = []

        for p in pregnant_women:
            abortion = False
            has_hiv_sifilis_test = False
            temp_dum = p.appointments[0].co_dim_tempo_dum.dt_registro
            ig = p.appointments[0].nu_idade_gestacional_semanas
            dt_first_appointment = p.appointments[0].co_dim_tempo.dt_registro
            dum_ig = (dt_first_appointment - relativedelta(weeks=ig)) if ig is not None else temp_dum
            dum = temp_dum if temp_dum <= dum_ig else dum_ig
            dpp = dum + relativedelta(days=294)

            valid_appointments = []

            for app in p.appointments:
                
                if dum <= app.co_dim_tempo.dt_registro <= dpp:
                    valid_appointments.append(app)
                    if len(app.abortion_condition) > 0:
                        abortion = True
                    if len(app.hiv_sifilis_evaluated_procedures) > 0:
                        has_hiv_sifilis_test = True    
                elif app.co_dim_tempo.dt_registro > dpp:
                    temp_dum = app.co_dim_tempo_dum.dt_registro
                    ig = app.nu_idade_gestacional_semanas
                    dt_first_appointment = app.co_dim_tempo.dt_registro
                    dum_ig = (dt_first_appointment - relativedelta(weeks=ig)) if ig is not None else temp_dum
                    dum = temp_dum if temp_dum <= dum_ig else dum_ig
                    dpp = dum + relativedelta(days=294)
                    abortion = False if len(app.abortion_condition) == 0 else True
                    has_hiv_sifilis_test = False if len(app.hiv_sifilis_evaluated_procedures) == 0 else True
                    valid_appointments = [app]
            
            uuid_list = []
            
            for v in valid_appointments:
                v.duplicated = False
                if v.nu_uuid_ficha in uuid_list:
                    v.duplicated = True
                else:
                    uuid_list.append(v.nu_uuid_ficha)

            valid_appointments = [va for va in valid_appointments if not va.duplicated]
            
            if not abortion and (quad.evaluation_start <= dpp <= quad.evaluation_end):
                denominator_list.append(p)
                if has_hiv_sifilis_test:
                    numerator_list.append(p)

            p.dum = dum
            p.dpp = dpp
            p.appointments = valid_appointments

        data = {
            'denominator': denominator_list,
            'numerator': numerator_list
        }
        self.save_data_indicator(data, indicator)
        return data

    def get_data_indicator_3(self, quad=None, indicator=None):
        pregnant_women = TbFatCidadaoPec.objects.pregnant_women(quad)
        
        denominator_list = []
        numerator_list = []

        for p in pregnant_women:
            abortion = False
            has_dental_appointment = False
            temp_dum = p.appointments[0].co_dim_tempo_dum.dt_registro
            ig = p.appointments[0].nu_idade_gestacional_semanas
            dt_first_appointment = p.appointments[0].co_dim_tempo.dt_registro
            dum_ig = (dt_first_appointment - relativedelta(weeks=ig)) if ig is not None else temp_dum
            dum = temp_dum if temp_dum <= dum_ig else dum_ig
            dpp = dum + relativedelta(days=294)

            valid_appointments = []

            for app in p.appointments:
                
                if dum <= app.co_dim_tempo.dt_registro <= dpp:
                    valid_appointments.append(app)
                    if len(app.abortion_condition) > 0:
                        abortion = True    
                elif app.co_dim_tempo.dt_registro > dpp:
                    temp_dum = app.co_dim_tempo_dum.dt_registro
                    ig = app.nu_idade_gestacional_semanas
                    dt_first_appointment = app.co_dim_tempo.dt_registro
                    dum_ig = (dt_first_appointment - relativedelta(weeks=ig)) if ig is not None else temp_dum
                    dum = temp_dum if temp_dum <= dum_ig else dum_ig
                    dpp = dum + relativedelta(days=294)
                    abortion = False if len(app.abortion_condition) == 0 else True
                    
                    valid_appointments = [app]

            uuid_list = []
            
            for v in valid_appointments:
                v.duplicated = False
                if v.nu_uuid_ficha in uuid_list:
                    v.duplicated = True
                else:
                    uuid_list.append(v.nu_uuid_ficha)

            valid_appointments = [va for va in valid_appointments if not va.duplicated]

            for dent in p.dental_appointments:
                if dum <= dent.co_dim_tempo.dt_registro <= dpp:
                    has_dental_appointment = True
                    break

            if not abortion and (quad.evaluation_start <= dpp <= quad.evaluation_end):
                denominator_list.append(p)
                if has_dental_appointment:
                    numerator_list.append(p)

            p.dum = dum
            p.dpp = dpp
            p.appointments = valid_appointments

        data = {
            'denominator': denominator_list,
            'numerator': numerator_list
        }
        self.save_data_indicator(data, indicator)
        return data

    def get_data_indicator_4(self, quad=None, indicator=None):
        women = TbFatCidadaoPec.objects.women(quad)

        denominator_list = list(women)
        numerator_list = [
            w for w in women if len(w.cytopathological_procedures_1) > 0 or len(w.cytopathological_procedures_2) > 0  
        ]

        data = {
            'denominator': denominator_list,
            'numerator': numerator_list
        }
        self.save_data_indicator(data, indicator)
        return data

    def get_data_indicator_5(self, quad=None, indicator=None):
        
        qs1 = TbFatCidadaoPec.objects.children(quad)
        print('FATPEC', qs1.count())
        cns_list = qs1.exclude(nu_cns__isnull=True).values_list('nu_cns', flat=True)
        cpf_list = qs1.exclude(nu_cpf_cidadao__isnull=True).values_list('nu_cpf_cidadao', flat=True)
        qs2 = TbProntuario.objects.children(quad)
        print('PRONT', qs2.count())
        
        excluded = qs2.exclude(
            Q(co_cidadao__nu_cns__in=cns_list)
            | Q(co_cidadao__nu_cpf__in=cpf_list)
        )
        print('EXCLUIDOS', excluded.count())
        
        denominator_list = list(qs1)
        numerator_list = []

        for c in qs1:
            numerator = first_scenario = second_scenario = third_scenario = tetra_third_dose = hepb_third_dose = dtp_third_dose = haemb_third_dose = False
            vax_list = []
            dtp = hepb = haemb = tetra = hexa = 0

            for pront in qs2:
                if (
                    (c.nu_cns is not None and c.nu_cns == pront.co_cidadao.nu_cns) 
                    or (c.nu_cpf_cidadao is not None and c.nu_cpf_cidadao == pront.co_cidadao.nu_cpf)
                ):
                    for va in pront.vaccinations:
                        c.vaccinations.append(va)

            for v in c.vaccinations:
                if len(v.vip_pentac) > 0 or len(v.hexa) > 0 or len(v.pentaa_hep) > 0:
                    numerator_list.append(c)
                    numerator = True
                    break
                else:
                    for vc in v.vaccines:
                        vax_list.append(vc)
                        if str(vc.co_dim_imunobiologico.nu_identificador) in ['29', '42']:
                            if str(vc.co_dim_dose_imunobiologico.nu_identificador) == '2':
                                first_scenario = True
                            elif str(vc.co_dim_dose_imunobiologico.nu_identificador) == '1':
                                second_scenario = True
                            else:
                                third_scenario = True
                        if str(vc.co_dim_imunobiologico.nu_identificador) == '46':
                            dtp += 1
                            if str(vc.co_dim_dose_imunobiologico.nu_identificador) == '3':
                                dtp_third_dose = True
                        elif str(vc.co_dim_imunobiologico.nu_identificador) == '9':
                            hepb += 1
                            if str(vc.co_dim_dose_imunobiologico.nu_identificador) == '3':
                                hepb_third_dose = True
                        elif str(vc.co_dim_imunobiologico.nu_identificador) == '17':
                            haemb += 1
                            if str(vc.co_dim_dose_imunobiologico.nu_identificador) == '3':
                                haemb_third_dose = True
                        elif str(vc.co_dim_imunobiologico.nu_identificador) == '39':
                            tetra += 1
                            if str(vc.co_dim_dose_imunobiologico.nu_identificador) == '3':
                                tetra_third_dose = True
                        elif str(vc.co_dim_imunobiologico.nu_identificador) == '43':
                            hexa += 1

            if numerator:
                continue

            if ((
                first_scenario 
                and (
                    (dtp >= 1 and hepb >= 1 and haemb >= 1)
                    or (tetra >= 1 and hepb >= 1)
                    or hexa >= 1
                )
            )
            or (
                second_scenario 
                and (
                    (dtp >= 2 and hepb >= 2 and haemb >= 2)
                    or (tetra >= 2 and hepb >= 2)
                    or (tetra >= 1 and dtp >= 1 and hepb >= 2 and haemb >= 1)
                    or hexa >= 2
                )
            )
            or (
                third_scenario
                and (
                    (tetra_third_dose and hepb_third_dose)
                    or (dtp_third_dose and hepb_third_dose and haemb_third_dose)
                )
            )):
                numerator_list.append(c)

        data = {
            'denominator': denominator_list,
            'numerator': numerator_list
        }
        self.save_data_indicator(data, indicator)
        return data

    def get_data_indicator_6(self, quad=None, indicator=None):
        hypertensives = TbFatCidadaoPec.objects.hypertensives(quad)

        denominator_list = list(hypertensives)
        numerator_list = [
            h for h in hypertensives if len(h.appointments) > 0 and (len(h.pressure_measure_1) > 0 or len(h.pressure_measure_2) > 0)  
        ]

        data = {
            'denominator': denominator_list,
            'numerator': numerator_list
        }
        self.save_data_indicator(data, indicator)
        return data

    def get_data_indicator_7(self, quad=None, indicator=None):
        diabetics = TbFatCidadaoPec.objects.diabetics(quad)

        denominator_list = list(diabetics)
        numerator_list = [
            d for d in diabetics if len(d.appointments) > 0 and (len(d.glycated_hemoglobin_1) > 0 or len(d.glycated_hemoglobin_2) > 0)  
        ]

        data = {
            'denominator': denominator_list,
            'numerator': numerator_list
        }
        self.save_data_indicator(data, indicator)
        return data

    def get_all_indicators(self, quad=None):
        for ind in range(1, 8):
            self.get_indicator(indicator_type=str(ind), quad=quad)

    def get_indicator(self, indicator_type, quad=None):
        indicator_model = apps.get_model(
                app_label='indicator', 
                model_name='Indicator'
        )
        pattern_model = apps.get_model(
                app_label='indicator',
                model_name='IndicatorPattern'
        )
        try:
            base_indicator = indicator_model.objects.get(
                quadrimester=quad.abbrev,
                dt_init_evaluation=quad.evaluation_start,
                dt_end_evaluation=quad.evaluation_end,
                is_active=True
            )
        except indicator_model.DoesNotExist:
            base_indicator = indicator_model.objects.create(
                quadrimester=quad.abbrev,
                dt_init_evaluation=quad.evaluation_start,
                dt_end_evaluation=quad.evaluation_end,
                is_active=True
            )

        try:
            pattern = pattern_model.objects.get(
                type=indicator_type,
                is_active=True
            )
        except pattern_model.DoesNotExist:
            pattern = None
        
        indicator = self.create(
            numerator=0,
            denominator=0,
            indicator=base_indicator,
            pattern=pattern,
            indicator_index=0,
            type=indicator_type,
            status='2'
        )

        if indicator_type == '1':
            data = self.get_data_indicator_1(quad, indicator=indicator)
        elif indicator_type == '2':
            data = self.get_data_indicator_2(quad, indicator=indicator)
        elif indicator_type == '3':
            data = self.get_data_indicator_3(quad, indicator=indicator)
        elif indicator_type == '4':
            data = self.get_data_indicator_4(quad, indicator=indicator)
        elif indicator_type == '5':
            data = self.get_data_indicator_5(quad, indicator=indicator)
        elif indicator_type == '6':
            data = self.get_data_indicator_6(quad, indicator=indicator)        
        elif indicator_type == '7':
            data = self.get_data_indicator_7(quad, indicator=indicator)
    
       
        # TODO: Reativar após refatoração > salvar registros de cidadãos apenas uma vez.
        # data_model.objects.save_data(indicator, data)
        indicator.numerator=len(data['numerator'])
        indicator.denominator=len(data['denominator'])
        indicator.status = '1'
        
        indicator.save()
        return indicator


class IndicatorDataManager(models.Manager):

    def save_data(self, indicator, data):
        appointment_model = apps.get_model(
            app_label='core', 
            model_name='IndicatorAppointmentData'
        )
        for p in data['denominator']:
            person = self.create(
                indicator=indicator,
                name=p.no_cidadao,
                cns=p.nu_cns,
                cpf=p.nu_cpf_cidadao,
                dum=p.dum,
                dpp=p.dpp    
            )
            for a in p.appointments:
                appointment_model.objects.create(
                    person=person,
                    appointment_id=a.co_seq_fat_atd_ind,
                    date=a.co_dim_tempo.dt_registro    
                )
