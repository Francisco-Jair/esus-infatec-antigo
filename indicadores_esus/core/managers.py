from datetime import timedelta

from django.apps import apps
from django.db import models
from django.db.models import (Case, Count, DateField, ExpressionWrapper, F,
                              OuterRef, Q, Subquery, When)
from django.db.models.functions import Coalesce

from indicadores_esus.esus.managers import (DIABETIC_CIAPS, DIABETIC_CIDS,
                                            HYPERTENSE_CIAPS, HYPERTENSE_CIDS,
                                            pregnancy_complete_ciaps_list,
                                            pregnancy_complete_cids_list)


class HealthTeamManager(models.Manager):

    def get_or_create_team(self, code, city, ine, name):
        model = apps.get_model(
            app_label='core',
            model_name='HealthTeam'
        )
        try:
            team = self.get(
                esus_code=code,
                city=city
            )
        except model.DoesNotExist:
            team = model(
                esus_code=code,
                ine=ine,
                name=name,
                city=city
            )
            team.save()
        except model.MultipleObjectsReturned:
            team = self.filter(
                esus_code=code,
                city=city
            ).order_by('id').first()
        return team


class HealthUnitManager(models.Manager):

    def get_or_create_unit(self, code, city, cnes, name, neighborhood):
        model = apps.get_model(
            app_label='core',
            model_name='HealthUnit'
        )
        try:
            unit = self.get(
                esus_code=code,
                city=city
            )
        except model.DoesNotExist:
            unit = model(
                esus_code=code,
                cnes=cnes,
                name=name,
                neighborhood=neighborhood,
                city=city
            )
            unit.save()
        except model.MultipleObjectsReturned:
            unit = self.filter(
                esus_code=code,
                city=city
            ).order_by('id').first()
        return unit


class PersonManager(models.Manager):

    def get_or_create_person(
        self, name, birth_date, gender, cpf=None, cns=None, citizen=None
    ):
        model = apps.get_model(
            app_label='core',
            model_name='Person'
        )
        city_model = apps.get_model(
            app_label='core',
            model_name='City'
        )
        address_model = apps.get_model(
            app_label='core',
            model_name='Address'
        )
        mother = father = ''

        if citizen:
            mother = citizen.no_mae.title() if citizen.no_mae else ''
            father = citizen.no_pai.title() if citizen.no_pai else ''
            street = citizen.ds_logradouro.title() if citizen.ds_logradouro else ''
            try:
                street_type = (
                    citizen.tp_logradouro.no_tipo_logradouro.title() 
                    if citizen.tp_logradouro.no_tipo_logradouro else ''
                )
            except:
                street_type = ''
            street_complete = f'{street_type} {street}'
            number = citizen.nu_numero if citizen.nu_numero else ''
            complement = citizen.ds_complemento if citizen.ds_complemento else ''
            neighborhood = citizen.no_bairro.title() if citizen.no_bairro else ''
            cep = citizen.ds_cep if citizen.ds_cep else ''
            try:
                city = city_model.objects.get(
                    ibge_code=citizen.co_localidade_endereco.co_ibge
                )
            except:
                city = None
        
        try:
            if cns and cpf:
                try:
                    person = self.get(
                        _cns=cns,
                        _cpf=cpf
                    )
                except model.MultipleObjectsReturned:
                    person = self.filter(
                        _cns=cns,
                        _cpf=cpf
                    ).order_by('id').first()
            elif cns:
                try:
                    person = self.get(
                        _cns=cns,
                    )
                except model.MultipleObjectsReturned:
                    person = self.filter(
                        _cns=cns,
                    ).order_by('id').first()

            elif cpf:
                try:
                    person = self.get(
                        _cpf=cpf
                    )
                except model.MultipleObjectsReturned:
                    person = self.filter(
                        _cpf=cpf
                    ).order_by('id').first()
            else:
                person = self.get(
                    _cpf='ZZZZZZZZZZZ'
                )
            if person:
                person.mother = mother
                person.father = father
            
        except model.DoesNotExist:
            person = model(
                _cpf=cpf,
                _cns=cns,
                name=name,
                birth_date=birth_date,
                gender=gender, 
                mother=mother, 
                father=father,
            )
        if not person:
            person = model(
                _cpf=cpf,
                _cns=cns,
                name=name,
                birth_date=birth_date,
                gender=gender, 
                mother=mother, 
                father=father,
            )
        person.save()
        
        if citizen:
            if not person.address_set.exists() and street_complete != ' ':
                address = address_model(
                    person=person,
                    street=street_complete,
                    number=number,
                    complement=complement,
                    city=city,
                    cep=cep,
                    neighborhood=neighborhood,
                )
                address.save()
            else:
                last_address = person.address_set.order_by('id').last()
                if last_address and last_address.street != street_complete and street_complete != ' ':
                    address = address_model(
                        person=person,
                        street=street_complete,
                        number=number,
                        complement=complement,
                        city=city,
                        cep=cep,
                        neighborhood=neighborhood,
                    )
                    address.save()

        return person


class RoleManager(models.Manager):

    def get_or_create_role(
        self, code, city, role_type, name, cns, individual_register, unit=None, 
        team=None, cpf=None, birth_date=None, gender=None, **kwargs
    ):
        role_model = apps.get_model(
            app_label='core',
            model_name='Role'
        )
        person_model = apps.get_model(
            app_label='core',
            model_name='Person'
        )
        citizen = kwargs.get('citizen', None)

        person = person_model.objects.get_or_create_person(
            name=name,
            birth_date=birth_date, 
            gender=gender,
            cpf=cpf,
            cns=cns,
            citizen=citizen
        )
        try:
            role = self.get(
                esus_code=code,
                role_type=role_type,
                city=city
            )
            role.individual_register = individual_register
        except role_model.DoesNotExist:
            role = role_model(
                esus_code=code,
                person=person,
                role_type=role_type,
                health_unit=unit, 
                health_team=team,
                city=city,
                individual_register=individual_register
            )
            
        except role_model.MultipleObjectsReturned:
            role = self.filter(
                esus_code=code,
                role_type=role_type,
                city=city
            ).order_by('id').first()
            role.individual_register = individual_register
        
        role.save()
        return role


class PregnantWomanManager(models.Manager):

    def get_pregnant_indicators_data(self, start_date=None, end_date=None):
        Appointment = apps.get_model(
            app_label='core',
            model_name='Appointment'
        )
        Procedure = apps.get_model(
            app_label='core',
            model_name='Procedure'
        )

        first_appointment = Appointment.objects.filter(
            patient=OuterRef('patient__pk'), date__gte=OuterRef('dum')
        ).order_by('date').values('date')[:1]
        
        queryset = self.get_queryset()

        queryset = queryset.select_related(
            'patient__person', 'patient__health_team', 'patient__health_unit'
        ).prefetch_related(
            'patient__patient_appointments', 
            'patient__patient_procedures',
        ).annotate(
            first_appointment_date=Coalesce(Subquery(first_appointment), None),
            twelth_week_limit=ExpressionWrapper(
                F('dum') + timedelta(weeks=13), output_field=DateField()
            ),
            first_appointment_until_12=Case(
                When(first_appointment_date__lt=F('twelth_week_limit'), then=True),
                default=False,                 
            ),
            medical_appointments_qty=Count(
                'patient__patient_appointments', 
                filter=Q(
                    Q(patient__patient_appointments__appointment_type='M')
                    & Q(patient__patient_appointments__date__gte=F('dum'))
                    & Q(patient__patient_appointments__date__lte=F('dpp'))
                    & Q(
                        Q(patient__patient_appointments__cids__code__in=pregnancy_complete_cids_list)
                        | Q(patient__patient_appointments__ciaps__code__in=pregnancy_complete_ciaps_list)
                    )
                ),
                distinct=True
            ),
            indicator_1_achieved=Case(
                When(
                    Q(
                        first_appointment_until_12=True, 
                        medical_appointments_qty__gte=6
                    ), 
                    then=True
                ),
                default=False
            ),
            hiv_sorology_qty=Count(
                'patient__patient_procedures',
                filter=Q(
                    patient__patient_procedures__procedure__procedure_code__in=Procedure.HIV_SOROLOGY,
                    patient__patient_procedures__evaluate_appointment__date__gte=F('dum'),
                    patient__patient_procedures__evaluate_appointment__date__lte=F('dpp'),
                ),
                distinct=True
            ),
            sifilis_sorology_qty=Count(
                'patient__patient_procedures',
                filter=Q(
                    patient__patient_procedures__procedure__procedure_code__in=Procedure.SIFILIS_SOROLOGY,
                    patient__patient_procedures__evaluate_appointment__date__gte=F('dum'),
                    patient__patient_procedures__evaluate_appointment__date__lte=F('dpp'),
                ),
                distinct=True
            ),
            hiv_quicktest_qty=Count(
                'patient__patient_procedures',
                filter=Q(
                    patient__patient_procedures__procedure__procedure_code__in=Procedure.HIV_QUICKTEST,
                    patient__patient_procedures__date__gte=F('dum'),
                    patient__patient_procedures__date__lte=F('dpp'),
                ),
                distinct=True
            ),
            sifilis_quicktest_qty=Count(
                'patient__patient_procedures',
                filter=Q(
                    patient__patient_procedures__procedure__procedure_code__in=Procedure.SIFILIS_QUICKTEST,
                    patient__patient_procedures__date__gte=F('dum'),
                    patient__patient_procedures__date__lte=F('dpp'),
                ),
                distinct=True
            ),
            procedures_qty=F('hiv_sorology_qty') + F('sifilis_sorology_qty')+ F('hiv_quicktest_qty') + F('sifilis_quicktest_qty'),
            indicator_2_achieved=Case(
                When(
                    Q(
                        Q(hiv_sorology_qty__gte=1) 
                        | Q(hiv_quicktest_qty__gte=1)
                    ) & Q(
                        Q(sifilis_sorology_qty__gte=1) 
                        | Q(sifilis_quicktest_qty__gte=1)
                    ) , 
                    then=True
                ),
                default=False
            ),
            dental_appointments_qty=Count(
                'patient__patient_appointments', 
                filter=Q(
                    patient__patient_appointments__appointment_type='O',
                    patient__patient_appointments__date__gte=F('dum'),
                    patient__patient_appointments__date__lte=F('dpp')
                ),
                distinct=True
            ),
            indicator_3_achieved=Case(
                When(
                    Q(
                        dental_appointments_qty__gte=1
                    ), 
                    then=True
                ),
                default=False
            ),
            counted=Case(
                When(
                    Q(sus_registered=True), 
                        then=True
                ),
                default=False
            )
        ).order_by(
            'patient__person__name'
        ).distinct()

        if start_date and end_date:
            queryset = queryset.filter(
                dpp__gte=start_date,
                dpp__lte=end_date,
            )
        elif start_date:
            queryset = queryset.filter(
                dpp__gte=start_date,
            )
        elif end_date:
            queryset = queryset.filter(
                dpp__lte=end_date,
            )
        return queryset


class WomanManager(models.Manager):

    def get_woman_indicators_data(self, start_date=None, end_date=None):
        Appointment = apps.get_model(
            app_label='core',
            model_name='Appointment'
        )
        Procedure = apps.get_model(
            app_label='core',
            model_name='Procedure'
        )
        
        queryset = self.get_queryset()

        queryset = queryset.select_related(
            'patient__person', 'patient__health_team', 'patient__health_unit'
        ).prefetch_related(
            'patient__patient_appointments', 
            'patient__patient_procedures',
        ).annotate(
            cytopathological_qty=Count(
                'patient__patient_procedures',
                filter=Q(
                    patient__patient_procedures__procedure__procedure_code__in=Procedure.CYTOPATHOLOGICAL,
                    patient__patient_procedures__date__gte=start_date,
                ),
                distinct=True
            ),
            indicator_4_achieved=Case(
                When(
                    Q(cytopathological_qty__gte=1), 
                    then=True
                ),
                default=False
            ),
        ).order_by(
            'patient__person__name'
        ).distinct()

        return queryset


class ChildManager(models.Manager):

    def get_child_indicators_data(self, start_date=None, end_date=None):
        Appointment = apps.get_model(
            app_label='core',
            model_name='Appointment'
        )
        Vaccination = apps.get_model(
            app_label='core',
            model_name='Vaccination'
        )
        
        queryset = self.get_queryset()

        queryset = queryset.select_related(
            'patient__person', 'patient__health_team', 'patient__health_unit'
        ).prefetch_related(
            'patient__patient_appointments', 
            'patient__patient_procedures',
            'patient__patient_vaccinations'
        ).annotate(
            # Quantidade de doses DTP
            dtp_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='46',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de doses Hepatite B
            hepb_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='9',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de doses Haemophilos B (Hib)
            hemb_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='17',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de doses Tetravalente (DTP + Hib)
            tetra_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='39',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de doses Pentavalente (DTPa/Hib/Pólio Inativa) / (DTP/HB/Hib)
            penta_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id__in=['29', '42'],
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de doses Hexavalente (DTPa+HB+Hib+VIP)
            hexa_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='43',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de primeiras doses Pentavalente (DTPa/Hib/Pólio Inativa) / (DTP/HB/Hib)
            penta_first_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id__in=['29', '42'],
                    patient__patient_vaccinations__dose__esus_id='1',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de segundas doses Pentavalente (DTPa/Hib/Pólio Inativa) / (DTP/HB/Hib)
            penta_second_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id__in=['29', '42'],
                    patient__patient_vaccinations__dose__esus_id='2',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses Tetravalente (DTP + Hib)
            tetra_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='39',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses Hepatite B
            hepb_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='9',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses DTP
            dtp_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='46',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses Haemophilos B (Hib)
            hemb_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='17',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses Hexavalente (DTPa+HB+Hib+VIP)
            hexa_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='43',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses Poliomielite inativada (VIP)
            vip_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='22',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses Pentavalente celular (DTP/HB/Hib)
            pentac_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='42',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            # Quantidade de terceiras doses Pentavalente acelular (DTPa/Hib/Pólio Inativa)
            pentaa_third_dose_qty=Count(
                'patient__patient_vaccinations',
                filter=Q(
                    patient__patient_vaccinations__vaccine__esus_id='29',
                    patient__patient_vaccinations__dose__esus_id='3',
                    patient__patient_vaccinations__date__gte=F(
                        'patient__person__birth_date'
                    ),
                ),
                distinct=True
            ),
            first_scenario=Case(
                When(
                    Q(
                        Q(penta_second_dose_qty__gte=1)
                        & Q(
                            Q(
                                # item a
                                Q(dtp_qty__gte=1)
                                & Q(hepb_qty__gte=1)
                                & Q(hemb_qty__gte=1)
                            ) | Q(
                                # item b
                                Q(tetra_qty__gte=1)
                                & Q(hepb_qty__gte=1)
                            ) | Q(
                                # item c
                                hexa_qty__gte=1
                            )
                        )
                    ), 
                    then=True
                ),
                default=False
            ),
            second_scenario=Case(
                When(
                    Q(
                        Q(penta_first_dose_qty__gte=1)
                        & Q(
                            Q(
                                # item a
                                Q(dtp_qty__gte=2)
                                & Q(hepb_qty__gte=2)
                                & Q(hemb_qty__gte=2)
                            ) | Q(
                                # item b
                                Q(tetra_qty__gte=2)
                                & Q(hepb_qty__gte=2)
                            ) | Q(
                                # item c
                                Q(tetra_qty__gte=1)
                                & Q(dtp_qty__gte=1)
                                & Q(hepb_qty__gte=2)
                                & Q(hemb_qty__gte=1)
                            ) | Q(
                                # item d
                                hexa_qty__gte=2
                            )
                        )
                    ), 
                    then=True
                ),
                default=False
            ),
            third_scenario=Case(
                When(
                    Q(
                        Q(penta_qty__lt=1)
                        & Q(
                            Q(
                                # item a
                                Q(tetra_third_dose_qty__gte=1)
                                & Q(hepb_third_dose_qty__gte=1)
                            ) | Q(
                                # item b
                                Q(dtp_third_dose_qty__gte=1)
                                & Q(hepb_third_dose_qty__gte=1)
                                & Q(hemb_third_dose_qty__gte=1)
                            )
                        )
                    ), 
                    then=True
                ),
                default=False
            ),
            indicator_5_achieved=Case(
                When(
                    Q(
                        Q(
                            hexa_third_dose_qty__gte=1
                        ) | Q(
                            Q(vip_third_dose_qty__gte=1)
                            & Q(pentac_third_dose_qty__gte=1)
                        ) | Q(
                            Q(hepb_third_dose_qty__gte=1)
                            & Q(pentaa_third_dose_qty__gte=1)
                        )
                    ), 
                    then=True
                ),
                When(
                    Q(first_scenario=True),
                    then=True
                ),
                When(
                    Q(second_scenario=True),
                    then=True
                ),
                When(
                    Q(third_scenario=True),
                    then=True
                ),
                default=False
            ),
        ).order_by(
            'patient__person__name'
        ).distinct()

        return queryset
    

class HypertensiveManager(models.Manager):

    def get_hypertensive_indicators_data(self, start_date=None, end_date=None):
        Appointment = apps.get_model(
            app_label='core',
            model_name='Appointment'
        )
        Vaccination = apps.get_model(
            app_label='core',
            model_name='Vaccination'
        )
        
        queryset = self.get_queryset()

        queryset = queryset.select_related(
            'patient__person', 'patient__health_team', 'patient__health_unit'
        ).prefetch_related(
            'patient__patient_appointments', 
            'patient__patient_procedures',
        ).annotate(
            hypertension_appointments_qty=Count(
                'patient__patient_appointments',
                filter=Q(
                    Q(patient__patient_appointments__appointment_type='M')
                    & Q(patient__patient_appointments__date__gte=start_date)
                    & Q(
                        Q(patient__patient_appointments__cids__code__in=HYPERTENSE_CIDS)
                        | Q(patient__patient_appointments__ciaps__code__in=HYPERTENSE_CIAPS)
                    )
                ),
                distinct=True
            ),
            blood_pressure_measure_qty=Count(
                'patient__patient_procedures',
                filter=Q(
                    patient__patient_procedures__procedure__procedure_code__in=['0301100039', 'ABPG033'],
                    patient__patient_procedures__date__gte=start_date,
                ),
                distinct=True
            ),
            indicator_6_achieved=Case(
                When(
                    Q(
                        hypertension_appointments_qty__gte=1,
                        blood_pressure_measure_qty__gte=1
                    ),  
                    then=True
                ),
                default=False
            ),
        ).order_by(
            'patient__person__name'
        ).distinct()

        return queryset
    

class DiabeticManager(models.Manager):

    def get_diabetic_indicators_data(self, start_date=None, end_date=None):
        Appointment = apps.get_model(
            app_label='core',
            model_name='Appointment'
        )
        Vaccination = apps.get_model(
            app_label='core',
            model_name='Vaccination'
        )
        
        queryset = self.get_queryset()

        queryset = queryset.select_related(
            'patient__person', 'patient__health_team', 'patient__health_unit'
        ).prefetch_related(
            'patient__patient_appointments', 
            'patient__patient_procedures',
        ).annotate(
            diabetes_appointments_qty=Count(
                'patient__patient_appointments',
                filter=Q(
                    Q(patient__patient_appointments__appointment_type='M')
                    & Q(patient__patient_appointments__date__gte=start_date)
                    & Q(
                        Q(patient__patient_appointments__cids__code__in=DIABETIC_CIDS)
                        | Q(patient__patient_appointments__ciaps__code__in=DIABETIC_CIAPS)
                    )
                ),
                distinct=True
            ),
            glycated_hemoglobin_qty=Count(
                'patient__patient_procedures',
                filter=Q(
                    patient__patient_procedures__procedure__procedure_code__in=['0202010503','ABEX008'],
                    patient__patient_procedures__date__gte=start_date,
                ),
                distinct=True
            ),
            indicator_7_achieved=Case(
                When(
                    Q(
                        diabetes_appointments_qty__gte=1,
                        glycated_hemoglobin_qty__gte=1
                    ),  
                    then=True
                ),
                default=False
            ),
        ).order_by(
            'patient__person__name'
        ).distinct()

        return queryset


class AppointmentManager(models.Manager):

    def get_or_create_appointment(
        self, code, appointment_type, city, patient, **kwargs
    ):
        Appointment = apps.get_model(
            app_label='core',
            model_name='Appointment'
        )
        
        HealthUnit = apps.get_model(
            app_label='core',
            model_name='HealthUnit'
        )
        unit_data = kwargs.get('health_unit')
        unit = None
        if unit_data:
            unit = HealthUnit.objects.get_or_create_unit(
                code=unit_data.co_seq_dim_unidade_saude,
                city=city,
                cnes=unit_data.nu_cnes,
                name=unit_data.no_unidade_saude.title(),
                neighborhood=unit_data.no_bairro,
            )

        HealthTeam = apps.get_model(
            app_label='core',
            model_name='HealthTeam'
        )
        team_data = kwargs.get('health_team')
        team = None
        if team_data:
            team = HealthTeam.objects.get_or_create_team(
                code=team_data.co_seq_dim_equipe,
                city=city,
                ine=team_data.nu_ine,
                name=team_data.no_equipe.title(),
            )
        
        date = kwargs.get('date')

        Role = apps.get_model(
            app_label='core',
            model_name='Role',
        )
        professional_data = kwargs.get('professional')
        professional = None
        if professional_data:
            professional = Role.objects.get_or_create_role(
                code=professional_data.co_seq_dim_profissional, 
                cns=professional_data.nu_cns, 
                individual_register=False,
                name=professional_data.no_profissional,
                role_type=2, city=city, 
            )

        CBO = apps.get_model(
            app_label='core',
            model_name='CBO',
        )
        cbo_data = kwargs.get('cbo')
        cbo = None
        if cbo_data:
            cbo = CBO.objects.get_or_create_cbo(
                code=cbo_data.nu_cbo,
                name=cbo_data.no_cbo.title(),
            )

        try:
            appointment = self.get(
                esus_code=code,
                appointment_type=appointment_type,
                city=city
            )
            appointment.health_unit = unit
            appointment.health_team = team
            appointment.date = date
            appointment.professional = professional
            appointment.cbo = cbo
        except Appointment.DoesNotExist:
            appointment = Appointment(
                esus_code=code,
                appointment_type=appointment_type,
                patient=patient,
                health_unit=unit, 
                health_team=team,
                city=city,
                date=date,
                professional=professional,
                cbo=cbo,
            )
        except Appointment.MultipleObjectsReturned:
            appointment = self.filter(
                esus_code=code,
                appointment_type=appointment_type,
                city=city
            ).order_by('id').first()

        appointment.save()
        
        return appointment


class CBOManager(models.Manager):

    def get_or_create_cbo(self, code, name):
        model = apps.get_model(
            app_label='core',
            model_name='CBO'
        )
        try:
            cbo = self.get(
                code=code,
            )
        except model.DoesNotExist:
            cbo = model(
                code=code,
                name=name,
            )
            cbo.save()
        except model.MultipleObjectsReturned:
            cbo = self.filter(
                code=code,
            ).order_by('id').first()
        return cbo


class ProcedureManager(models.Manager):

    def get_or_create_proc_type(self, esus_code, name, proc_code):
        model = apps.get_model(
            app_label='core',
            model_name='Procedure'
        )
        try:
            procedure = self.get(
                esus_code=esus_code,
            )
        except model.DoesNotExist:
            procedure = model(
                esus_code=esus_code,
                name=name.title() if name else '',
                procedure_code=proc_code
            )
            procedure.save()
        except model.MultipleObjectsReturned:
            procedure = model.filter(
                esus_code=esus_code
            ).order_by('id').first()
        return procedure


class PatientProcedureManager(models.Manager):

    def get_or_create_procedure(
        self, esus_code, patient, procedure, date, requested=None, 
        evaluated=None, **kwargs
    ):
        PatientProcedure = apps.get_model(
            app_label='core',
            model_name='PatientProcedure'
        )
        Procedure = apps.get_model(
            app_label='core',
            model_name='Procedure'
        )
        try:
            patient_procedure = self.get(
                esus_code=esus_code
            )
        except PatientProcedure.DoesNotExist:
            procedure_type = Procedure.objects.get_or_create_proc_type(
                esus_code=procedure.co_seq_dim_procedimento,
                name=procedure.ds_proced,
                proc_code=procedure.co_proced
            )
            patient_procedure = PatientProcedure(
                esus_code=esus_code,
                patient=patient,
                procedure=procedure_type,
                date=date,
                request_appointment=requested,
                evaluate_appointment=evaluated
            )
        except PatientProcedure.MultipleObjectsReturned:
            patient_procedure = self.filter(
                esus_code=esus_code
            ).order_by('id').first()
        
        if not patient_procedure.request_appointment and requested:
            patient_procedure.request_appointment = requested
        
        if not patient_procedure.evaluate_appointment and evaluated:
            patient_procedure.evaluate_appointment = evaluated

        city = kwargs.get('city')

        HealthUnit = apps.get_model(
            app_label='core',
            model_name='HealthUnit'
        )
        unit_data = kwargs.get('health_unit')
        unit = None
        if unit_data:
            unit = HealthUnit.objects.get_or_create_unit(
                code=unit_data.co_seq_dim_unidade_saude,
                city=city,
                cnes=unit_data.nu_cnes,
                name=unit_data.no_unidade_saude.title(),
                neighborhood=unit_data.no_bairro,
            )

        HealthTeam = apps.get_model(
            app_label='core',
            model_name='HealthTeam'
        )
        team_data = kwargs.get('health_team')
        team = None
        if team_data:
            team = HealthTeam.objects.get_or_create_team(
                code=team_data.co_seq_dim_equipe,
                city=city,
                ine=team_data.nu_ine,
                name=team_data.no_equipe.title(),
            )
        
        date = kwargs.get('date')

        Role = apps.get_model(
            app_label='core',
            model_name='Role',
        )
        professional_data = kwargs.get('professional')
        professional = None
        if professional_data:
            professional = Role.objects.get_or_create_role(
                code=professional_data.co_seq_dim_profissional, 
                cns=professional_data.nu_cns, 
                individual_register=False,
                name=professional_data.no_profissional,
                role_type=2, city=city, 
            )

        CBO = apps.get_model(
            app_label='core',
            model_name='CBO',
        )
        cbo_data = kwargs.get('cbo')
        cbo = None
        if cbo_data:
            cbo = CBO.objects.get_or_create_cbo(
                code=cbo_data.nu_cbo,
                name=cbo_data.no_cbo.title(),
            )
        
        if not patient_procedure.health_unit and unit:
            patient_procedure.health_unit = unit

        if not patient_procedure.health_team and team:
            patient_procedure.health_team = team

        if not patient_procedure.cbo and cbo:
            patient_procedure.cbo = cbo

        if not patient_procedure.professional and professional:
            patient_procedure.professional = professional

        patient_procedure.save()
        return patient_procedure


class VaccineManager(models.Manager):

    def get_or_create_vaccine(self, esus_id, name, acronym):
        model = apps.get_model(
            app_label='core',
            model_name='Vaccine'
        )
        try:
            vaccine = self.get(
                esus_id=esus_id,
            )
        except model.DoesNotExist:
            vaccine = model(
                esus_id=esus_id,
                name=name.title() if name else '',
                acronym=acronym
            )
            vaccine.save()
        except model.MultipleObjectsReturned:
            vaccine = self.filter(
                esus_id=esus_id
            ).order_by('id').first()
        return vaccine


class DoseManager(models.Manager):

    def get_or_create_dose(self, esus_id, name, acronym):
        Dose = apps.get_model(
            app_label='core',
            model_name='Dose'
        )
        try:
            dose = self.get(
                esus_id=esus_id,
            )
        except Dose.DoesNotExist:
            dose = Dose(
                esus_id=esus_id,
                name=name.title() if name else '',
                acronym=acronym
            )
            dose.save()
        except Dose.MultipleObjectsReturned:
            dose = self.filter(
                esus_id=esus_id
            ).order_by('id').first()
        return dose


class VaccinationManager(models.Manager):

    def get_or_create_vaccination(
        self, esus_code, patient, vaccine_type, date, dose_info, **kwargs
    ):
        Vaccination = apps.get_model(
            app_label='core',
            model_name='Vaccination'
        )
        Vaccine = apps.get_model(
            app_label='core',
            model_name='Vaccine'
        )
        Dose = apps.get_model(
            app_label='core',
            model_name='Dose'
        )
        dose = Dose.objects.get_or_create_dose(
            esus_id=dose_info.nu_identificador,
            name=dose_info.no_dose_imunobiologico,
            acronym=dose_info.sg_dose_imunobiologico
        )
        try:
            vaccination = self.get(
                esus_code=esus_code
            )
            
        except Vaccination.DoesNotExist:
            vaccine = Vaccine.objects.get_or_create_vaccine(
                esus_id=vaccine_type.nu_identificador,
                name=vaccine_type.no_imunobiologico,
                acronym=vaccine_type.sg_imunobiologico
            )
            vaccination = Vaccination(
                esus_code=esus_code,
                patient=patient,
                vaccine=vaccine,
                date=date,
                dose=dose
            )
        except Vaccination.MultipleObjectsReturned:
            vaccination = self.filter(
                esus_code=esus_code
            ).order_by('id').first()
            
        vaccination.dose = dose

        city = kwargs.get('city')

        HealthUnit = apps.get_model(
            app_label='core',
            model_name='HealthUnit'
        )
        unit_data = kwargs.get('health_unit')
        unit = None
        if unit_data:
            unit = HealthUnit.objects.get_or_create_unit(
                code=unit_data.co_seq_dim_unidade_saude,
                city=city,
                cnes=unit_data.nu_cnes,
                name=unit_data.no_unidade_saude.title(),
                neighborhood=unit_data.no_bairro,
            )

        HealthTeam = apps.get_model(
            app_label='core',
            model_name='HealthTeam'
        )
        team_data = kwargs.get('health_team')
        team = None
        if team_data:
            team = HealthTeam.objects.get_or_create_team(
                code=team_data.co_seq_dim_equipe,
                city=city,
                ine=team_data.nu_ine,
                name=team_data.no_equipe.title(),
            )
        
        date = kwargs.get('date')

        Role = apps.get_model(
            app_label='core',
            model_name='Role',
        )
        professional_data = kwargs.get('professional')
        professional = None
        if professional_data:
            professional = Role.objects.get_or_create_role(
                code=professional_data.co_seq_dim_profissional, 
                cns=professional_data.nu_cns, 
                individual_register=False,
                name=professional_data.no_profissional,
                role_type=2, city=city, 
            )

        CBO = apps.get_model(
            app_label='core',
            model_name='CBO',
        )
        cbo_data = kwargs.get('cbo')
        cbo = None
        if cbo_data:
            cbo = CBO.objects.get_or_create_cbo(
                code=cbo_data.nu_cbo,
                name=cbo_data.no_cbo.title(),
            )
        
        if not vaccination.health_unit and unit:
            vaccination.health_unit = unit

        if not vaccination.health_team and team:
            vaccination.health_team = team

        if not vaccination.cbo and cbo:
            vaccination.cbo = cbo

        if not vaccination.professional and professional:
            vaccination.professional = professional

        vaccination.save()
        return vaccination
