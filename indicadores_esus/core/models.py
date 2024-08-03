import uuid
from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

from indicadores_esus.core import managers
from indicadores_esus.core.utils import which_quadrimester


class City(models.Model):
    state = models.CharField('estado', max_length=2, choices=STATE_CHOICES)
    name = models.CharField('cidade', max_length=500)
    ibge_code = models.CharField('código IBGE', max_length=10, unique=True)

    def __str__(self):
        return f'{self.name}/{self.state}'

    class Meta:
        verbose_name = 'cidade'


class CID(models.Model):
    esus_id = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.code} - {self.name}'


class CIAP(models.Model):
    esus_id = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.code} - {self.name}'
    

class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Feminino'),
        ('M', 'Masculino')
    )
    _cpf = models.CharField(max_length=11, blank=True, null=True)
    _cns = models.CharField(max_length=16, blank=True, null=True)
    name = models.CharField(max_length=500)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True
    )
    mother = models.CharField(max_length=500, blank=True, null=True)
    father = models.CharField(max_length=500, blank=True, null=True)

    objects = managers.PersonManager()

    def __str__(self):
        return self.name

    @property
    def cpf(self):
        return self._cpf

    @property
    def cns(self):
        return self._cns


class Address(models.Model):
    person = models.ForeignKey('core.Person', on_delete=models.CASCADE)
    street = models.CharField(max_length=500, null=True, blank=True)
    number = models.CharField(max_length=25, null=True, blank=True)
    complement = models.CharField(max_length=50, blank=True, null=True)
    city = models.ForeignKey(
        'core.City', on_delete=models.SET_NULL, null=True, blank=True
    )
    neighborhood = models.CharField(
        'Bairro', max_length=255, null=True, blank=True
    )
    cep = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return self.street


class Role(models.Model):
    PATIENT = 1
    PROFESSIONAL = 2
    ROLE_TYPE_CHOICES = (
        (PATIENT, 'Paciente'),
        (PROFESSIONAL, 'Profissional')
    )
    esus_code = models.BigIntegerField('Código ESUS', null=True, blank=True)
    person = models.ForeignKey('core.Person', on_delete=models.CASCADE)
    role_type = models.PositiveSmallIntegerField(choices=ROLE_TYPE_CHOICES)
    health_unit = models.ForeignKey(
        'core.HealthUnit', on_delete=models.SET_NULL, null=True, blank=True
    )
    health_team = models.ForeignKey(
        'core.HealthTeam', on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(
        'core.City', on_delete=models.SET_NULL, null=True, blank=True
    )
    left_city = models.BooleanField(default=False)
    indicator = models.ManyToManyField('indicator.CalculatedIndicator')
    individual_register = models.BooleanField(default=True)

    objects = managers.RoleManager()

    def __str__(self):
        return self.person.name


class PregnantWoman(models.Model):
    patient = models.OneToOneField(
        'core.Role', on_delete=models.CASCADE, primary_key=True
    )
    dum = models.DateField(null=True, blank=True)
    dpp = models.DateField(null=True, blank=True)
    is_pregnant = models.BooleanField(default=False)
    sus_registered = models.BooleanField(default=False)

    objects = managers.PregnantWomanManager()

    @property
    def medical_appointments_quantity(self):
        appointments = self.patient.patient_appointments.filter(
            appointment_type='M'
        ).count()
        return appointments

    @property
    def dental_appointments_quantity(self):
        appointments = self.patient.patient_appointments.filter(
            appointment_type='O'
        ).count()
        return appointments

    @property
    def procedures_quantity(self):
        procedures = self.patient.patient_procedures.all().count()
        return procedures

    @property
    def hiv_procedures_quantity(self):
        procedures = self.patient.patient_procedures.filter(
            models.Q(
                procedure__procedure_code__in=Procedure.HIV_QUICKTEST,
            ) | models.Q(
                procedure__procedure_code__in=Procedure.HIV_SOROLOGY,
                evaluate_appointment__isnull=False
            )
        ).distinct().count()
        return procedures

    @property
    def sifilis_procedures_quantity(self):
        procedures = self.patient.patient_procedures.filter(
            models.Q(
                procedure__procedure_code__in=Procedure.SIFILIS_QUICKTEST,
            ) | models.Q(
                procedure__procedure_code__in=Procedure.SIFILIS_SOROLOGY,
                evaluate_appointment__isnull=False
            )
        ).distinct().count()
        return procedures

    @property
    def first_appointment(self):
        appointments = self.patient.patient_appointments.filter(
            appointment_type='M',
            date__gte=self.dum,
        )
        if self.dpp:
            appointments = appointments.filter(date__lte=self.dpp)
        
        return appointments.first()

    @property
    def first_appointment_week(self):
        if self.first_appointment:
            first_date = self.get_first_appointment().date
            difference = abs(first_date - self.dum).days
            weeks = difference // 7
            return weeks

    @property
    def birth_quadrimester(self):
        return which_quadrimester(self.dpp)

    @property
    def counts(self):
        current_quadrimester = which_quadrimester(datetime.now().date())
        if self.birth_quadrimester.abbrev == current_quadrimester.abbrev:
            return True
        return False

    @property
    def twelfth_week(self):
        limit = self.dum + relativedelta(weeks=13)
        return limit

    @property
    def first_appointment_before_twelfth_week(self):
        if self.first_appointment and self.first_appointment.date <= self.twelfth_week:
            return True
        return False
    
    @property
    def first_indicator_achieved(self):
        if (
            self.first_appointment_before_twelfth_week 
            and self.medical_appointments_quantity >= 6
        ):
            return True
        return False

    @property
    def indicator_1_msgs(self):
        msgs = []
        if self.first_indicator_achieved:
            msgs.append('O indicador foi alcançado!')
        else:
            if not self.first_appointment_before_twelfth_week:
                msgs.append(f'A primeira consulta foi realizada com mais de 12 semanas '
                f'do início da gestação. Ela deveria ter sido realizada até '
                f'{self.twelfth_week.strftime("%d/%m/%Y")} e foi realizada em ' 
                f'{self.first_appointment.date.strftime("%d/%m/%Y")}.')
            if self.medical_appointments_quantity < 6:
                msgs.append(f'Gestante com apenas '
                f'{self.medical_appointments_quantity} consulta(s) válidas(s).')
        return msgs

    @property
    def second_indicator_achieved(self):
        if (
            self.hiv_procedures_quantity > 0 
            and self.sifilis_procedures_quantity > 0
        ):
            return True
        return False

    @property
    def indicator_2_msgs(self):
        msgs = []
        if self.second_indicator_achieved:
            msgs.append('O indicador foi alcançado!')
        else:
            if (
                self.hiv_procedures_quantity <= 0 
                and self.sifilis_procedures_quantity <= 0
            ):
                msgs.append(
                    'Não foi realizado ou solicitado/avaliado exame de HIV e '
                    'sífilis'
                )
            elif self.hiv_procedures_quantity <= 0:
                msgs.append(
                    'Não foi realizado ou solicitado/avaliado exame de HIV'
                )
            elif self.sifilis_procedures_quantity <= 0:
                msgs.append(
                    'Não foi realizado ou solicitado/avaliado exame de sífilis'
                )
        return msgs

    @property
    def third_indicator_achieved(self):
        if self.dental_appointments_quantity > 0:
            return True
        return False

    @property
    def indicator_3_msgs(self):
        msgs = []
        if self.third_indicator_achieved:
            msgs.append('O indicador foi alcançado!')
        else:
            if self.dental_appointments_quantity <= 0:
                msgs.append('A gestante não possui nenhuma consulta '
                'odontológica.')
        return msgs


class Woman(models.Model):
    patient = models.OneToOneField(
        'core.Role', on_delete=models.CASCADE, primary_key=True
    )

    objects = managers.WomanManager()

    @property
    def cytopathological_quantity(self):
        current_date = datetime.now().date()
        quadrimester = which_quadrimester(current_date)
        procedures = self.patient.patient_procedures.filter(
            procedure__procedure_code__in=Procedure.CYTOPATHOLOGICAL,
            date__gte=quadrimester.evaluation_end - relativedelta(months=36)
        ).distinct().count()
        return procedures

    @property
    def fourth_indicator_achieved(self):
        if self.cytopathological_quantity > 0:
            return True
        return False

    @property
    def indicator_4_msgs(self):
        msgs = []
        if self.fourth_indicator_achieved:
            msgs.append('O indicador foi alcançado!')
        else:
            if self.cytopathological_quantity <= 0:
                msgs.append(
                    'Não foi realizada coleta de exame citopatológico nos '
                    'últimos três anos.'
                )
        return msgs


class Child(models.Model):
    patient = models.OneToOneField(
        'core.Role', on_delete=models.CASCADE, primary_key=True
    )
    sus_registered = models.BooleanField(default=False)

    objects = managers.ChildManager()

    @property
    def vaccines_qty(self):
        vaccines_qty = self.patient.patient_vaccinations.filter(
            vaccine__esus_id__in=Vaccine.INDICATOR_5_VACCINE_CODES,
            date__gte=self.patient.person.birth_date
        ).distinct().count()
        return vaccines_qty
    
    @property
    def hexa_third_dose(self):
        hexa_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='43',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if hexa_third_dose:
            return True
        return False
    
    @property
    def vip_third_dose(self):
        vip_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='22',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if vip_third_dose:
            return True
        return False
    
    @property
    def pentac_third_dose(self):
        pentac_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='42',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if pentac_third_dose:
            return True
        return False
    
    @property
    def pentaa_third_dose(self):
        pentaa_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='29',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if pentaa_third_dose:
            return True
        return False
    
    @property
    def hepatitis_b_third_dose(self):
        hepb_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='9',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if hepb_third_dose:
            return True
        return False
    
    @property
    def tetra_third_dose(self):
        tetra_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='39',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if tetra_third_dose:
            return True
        return False
    
    @property
    def dtp_third_dose(self):
        dtp_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='46',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if dtp_third_dose:
            return True
        return False
    
    @property
    def hemb_third_dose(self):
        hemb_third_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='17',
            dose__esus_id='3',
            date__gte=self.patient.person.birth_date
        ).exists()
        if hemb_third_dose:
            return True
        return False
    
    @property
    def penta_first_dose(self):
        penta_first_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id__in=['29', '42'],
            dose__esus_id='1',
            date__gte=self.patient.person.birth_date
        ).exists()
        if penta_first_dose:
            return True
        return False
    
    @property
    def penta_second_dose(self):
        penta_second_dose = self.patient.patient_vaccinations.filter(
            vaccine__esus_id__in=['29', '42'],
            dose__esus_id='2',
            date__gte=self.patient.person.birth_date
        ).exists()
        if penta_second_dose:
            return True
        return False
    
    @property
    def dtp_quantity(self):
        dtp_qty = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='46',
            date__gte=self.patient.person.birth_date
        ).distinct().count()
        return dtp_qty
    
    @property
    def hepatitis_b_quantity(self):
        hepb_qty = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='9',
            date__gte=self.patient.person.birth_date
        ).distinct().count()
        return hepb_qty

    @property
    def haemophilos_b_quantity(self):
        hemb_qty = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='17',
            date__gte=self.patient.person.birth_date
        ).distinct().count()
        return hemb_qty
    
    @property
    def tetra_quantity(self):
        tetra_qty = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='39',
            date__gte=self.patient.person.birth_date
        ).distinct().count()
        return tetra_qty
    
    @property
    def penta_quantity(self):
        penta_qty = self.patient.patient_vaccinations.filter(
            vaccine__esus_id__in=['29', '42'],
            date__gte=self.patient.person.birth_date
        ).distinct().count()
        return penta_qty
    
    @property
    def hexa_quantity(self):
        hexa_qty = self.patient.patient_vaccinations.filter(
            vaccine__esus_id='43',
            date__gte=self.patient.person.birth_date
        ).distinct().count()
        return hexa_qty
    
    @property
    def first_exceptional_scenario(self):
        if (
            self.penta_second_dose 
            and (
                (self.dtp_quantity >= 1 and self.hepatitis_b_quantity >= 1 and self.haemophilos_b_quantity >= 1)
                or (self.tetra_quantity >= 1 and self.hepatitis_b_quantity >= 1)
                or (self.hexa_quantity >= 1)
            )
        ):
            return True
        return False
    
    @property
    def second_exceptional_scenario(self):
        if (
            self.penta_first_dose 
            and (
                (self.dtp_quantity >= 2 and self.hepatitis_b_quantity >= 2 and self.haemophilos_b_quantity >= 2)
                or (self.tetra_quantity >= 2 and self.hepatitis_b_quantity >= 2)
                or (self.tetra_quantity >= 1 and self.dtp_quantity >= 1 and self.hepatitis_b_quantity >= 2 and self.haemophilos_b_quantity >= 1)
                or (self.hexa_quantity >= 2)
            )
        ):
            return True
        return False

    @property
    def third_exceptional_scenario(self):
        if (
            self.penta_quantity <= 0 
            and (
                (self.tetra_third_dose and self.hepb_third_dose)
                or (self.dtp_third_dose and self.hepb_third_dose and self.hemb_third_dose)
            )
        ):
            return True
        return False
    
    @property
    def fifth_indicator_achieved(self):
        if (
            self.hexa_third_dose 
            or (self.vip_third_dose and self.pentac_third_dose)
            or (self.hepb_third_dose and self.pentaa_third_dose)
            or self.first_scenario
            or self.second_scenario
            or self.third_scenario
        ):
            return True
        return False

    @property
    def indicator_5_msgs(self):
        msgs = []
        if self.fifth_indicator_achieved:
            msgs.append('O indicador foi alcançado!')
        else:
            msgs.append(
                'Não foram aplicadas todas as vacinas necesárias.'
            )
        return msgs


class Hypertensive(models.Model):
    patient = models.OneToOneField(
        'core.Role', on_delete=models.CASCADE, primary_key=True
    )

    objects = managers.HypertensiveManager()

    @property
    def hypertension_appointments_quantity(self):
        current_date = datetime.now().date()
        quadrimester = which_quadrimester(current_date)
        appointments = self.patient.patient_appointments.filter(
            date__gte=quadrimester.evaluation_end - relativedelta(months=6)
        ).distinct().count()
        return appointments
    
    @property
    def blood_pressure_measure_quantity(self):
        current_date = datetime.now().date()
        quadrimester = which_quadrimester(current_date)
        procedures = self.patient.patient_procedures.filter(
            procedure__procedure_code__in=['0301100039', 'ABPG033'],
            date__gte=quadrimester.evaluation_end - relativedelta(months=6)
        ).distinct().count()
        return procedures

    @property
    def sixth_indicator_achieved(self):
        if self.hypertension_appointments_quantity > 0 and self.blood_pressure_measure_quantity > 0:
            return True
        return False

    @property
    def indicator_6_msgs(self):
        msgs = []
        if self.sixth_indicator_achieved:
            msgs.append('O indicador foi alcançado!')
        else:
            if (
                self.hypertension_appointments_quantity <= 0 
                and self.blood_pressure_measure_quantity <= 0
            ):
                msgs.append(
                    'Não foi realizado atendimento para a condição de '
                    'hipertensão arterial nem aferição de pressão arterial nos '
                    '6 meses anteriores ao término do quadrimestre'
                )
            elif self.hypertension_appointments_quantity <= 0:
                msgs.append(
                    'Não foi realizado atendimento para a condição de '
                    'hipertensão arterial nos 6 meses anteriores ao término do '
                    'quadrimestre'
                )
            elif self.blood_pressure_measure_quantity <= 0:
                msgs.append(
                    'Não foi realizada aferição de pressão arterial nos 6 '
                    'meses anteriores ao término do quadrimestre'
                )
        return msgs


class Diabetic(models.Model):
    patient = models.OneToOneField(
        'core.Role', on_delete=models.CASCADE, primary_key=True
    )
    
    objects = managers.DiabeticManager()

    @property
    def diabetes_appointments_quantity(self):
        current_date = datetime.now().date()
        quadrimester = which_quadrimester(current_date)
        appointments = self.patient.patient_appointments.filter(
            date__gte=quadrimester.evaluation_end - relativedelta(months=6)
        ).distinct().count()
        return appointments
    
    @property
    def glycated_hemoglobin_quantity(self):
        current_date = datetime.now().date()
        quadrimester = which_quadrimester(current_date)
        procedures = self.patient.patient_procedures.filter(
            procedure__procedure_code__in=['0202010503','ABEX008'],
            date__gte=quadrimester.evaluation_end - relativedelta(months=6)
        ).distinct().count()
        return procedures

    @property
    def seventh_indicator_achieved(self):
        if self.diabetes_appointments_quantity > 0 and self.glycated_hemoglobin_quantity > 0:
            return True
        return False

    @property
    def indicator_7_msgs(self):
        msgs = []
        if self.seventh_indicator_achieved:
            msgs.append('O indicador foi alcançado!')
        else:
            if (
                self.diabetes_appointments_quantity <= 0 
                and self.glycated_hemoglobin_quantity <= 0
            ):
                msgs.append(
                    'Não foi realizado atendimento para a condição de '
                    'diabetes nem solicitado exame de hemoglobina glicada nos '
                    '6 meses anteriores ao término do quadrimestre'
                )
            elif self.diabetes_appointments_quantity <= 0:
                msgs.append(
                    'Não foi realizado atendimento para a condição de '
                    'diabetes nos 6 meses anteriores ao término do quadrimestre'
                )
            elif self.glycated_hemoglobin_quantity <= 0:
                msgs.append(
                    'Não foi solicitado exame de hemoglobina glicada nos 6 '
                    'meses anteriores ao término do quadrimestre'
                )
        return msgs

class CBO(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=500)

    objects = managers.CBOManager()

    def __str__(self):
        return f'{self.code} - {self.name}'


class Appointment(models.Model):
    APPOINTMENT_TYPES = (
        ('O', 'Odontologica'),
        ('M', 'Medica')
    )
    esus_code = models.BigIntegerField('Código ESUS', null=True, blank=True)
    appointment_type = models.CharField(max_length=1, choices=APPOINTMENT_TYPES)
    professional = models.ForeignKey(
        'core.Role', on_delete=models.CASCADE, 
        related_name='professional_appointments', null=True, blank=True
    )
    cbo = models.ForeignKey(
        'core.CBO', on_delete=models.SET_NULL, null=True, blank=True
    )
    patient = models.ForeignKey(
        'core.Role', on_delete=models.CASCADE, 
        related_name='patient_appointments'
    )
    city = models.ForeignKey(
        'core.City', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Cidade'
    )
    health_unit = models.ForeignKey(
        'core.HealthUnit', on_delete=models.SET_NULL, null=True, blank=True
    )
    health_team = models.ForeignKey(
        'core.HealthTeam', on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField(null=True, blank=True)
    pregnancy = models.BooleanField(default=False)
    abortion = models.BooleanField(default=False)
    cids_2 = models.CharField(max_length=500, null=True, blank=True)
    ciaps_2 = models.CharField(max_length=500, null=True, blank=True)
    cids = models.ManyToManyField('core.CID')
    ciaps = models.ManyToManyField('core.CIAP')

    objects = managers.AppointmentManager()

    def __str__(self):
        return str(self.esus_code)
    

class HealthUnit(models.Model):
    esus_code = models.BigIntegerField('Código ESUS', null=True, blank=True)
    cnes = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField('Nome', max_length=500, blank=True, null=True)
    street = models.CharField('Rua', max_length=500, blank=True)
    number = models.CharField('Número', max_length=25, blank=True)
    complement = models.CharField('Complemento', max_length=25, blank=True)
    neighborhood = models.CharField('Bairro', max_length=50, blank=True)
    city = models.ForeignKey(
        'core.City', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Cidade'
    )
    cep = models.CharField(max_length=8, blank=True)

    objects = managers.HealthUnitManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unidade de Saúde'
        verbose_name_plural = 'Unidades de Saúde'


class HealthTeam(models.Model):
    esus_code = models.BigIntegerField('Código ESUS', null=True, blank=True)
    ine = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField('Nome', max_length=255, blank=True, null=True)
    city = models.ForeignKey(
        'core.City', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Cidade'
    )

    objects = managers.HealthTeamManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Equipe de Saúde'
        verbose_name_plural = 'Equipes de Saúde'


class Procedure(models.Model):
    HIV_CODES = []
    SIFILIS_CODES = []

    HIV_QUICKTEST = ['0214010040', '0214010058', 'ABPG024']
    HIV_SOROLOGY = ['0202030300', 'ABEX018',]
    SIFILIS_QUICKTEST = ['0214010082', '0214010074', 'ABPG026']
    SIFILIS_SOROLOGY = ['0202031179', '0202031110', 'ABEX019']
    CYTOPATHOLOGICAL = ['0201020033', 'ABPG010']

    esus_code = models.BigIntegerField('Código ESUS', null=True, blank=True)
    name = models.CharField('Nome', max_length=500, blank=True, null=True)
    procedure_code = models.CharField(max_length=100, blank=True, null=True)

    objects = managers.ProcedureManager()

    def __str__(self):
        return self.name

class PatientProcedure(models.Model):
    esus_code = models.BigIntegerField('Código ESUS', null=True, blank=True)
    procedure = models.ForeignKey(
        'core.Procedure', on_delete=models.CASCADE, 
    )
    patient = models.ForeignKey(
        'core.Role', on_delete=models.CASCADE, 
        related_name='patient_procedures'
    )
    professional = models.ForeignKey(
        'core.Role', on_delete=models.CASCADE, 
        related_name='professional_procedures', null=True, blank=True
    )
    cbo = models.ForeignKey(
        'core.CBO', on_delete=models.SET_NULL, null=True, blank=True
    )
    request_appointment = models.ForeignKey(
        'core.Appointment', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='requested_procedures'
    )
    evaluate_appointment = models.ForeignKey(
        'core.Appointment', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='evaluated_procedures'
    )
    date = models.DateField(null=True, blank=True)
    health_unit = models.ForeignKey(
        'core.HealthUnit', on_delete=models.SET_NULL, null=True, blank=True
    )
    health_team = models.ForeignKey(
        'core.HealthTeam', on_delete=models.SET_NULL, null=True, blank=True
    )

    objects = managers.PatientProcedureManager()


class PatientIndicator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey('core.Role', on_delete=models.CASCADE)
    indicator = models.ForeignKey('indicator.CalculatedIndicator', on_delete=models.CASCADE)
    numerator = models.BooleanField(default=False)

    def __str__(self):
        return f'Indicador {self.indicator.type} - {self.indicator.indicator.quadrimester} - {self.patient.person}'


class Vaccine(models.Model):
    INDICATOR_5_VACCINE_CODES = ['9', '17', '22', '29', '39', '42', '43', '46']
    esus_id = models.CharField(max_length=255)
    acronym = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    objects = managers.VaccineManager()

    def __str__(self):
        return f'{self.acronym} - {self.name}'


class Dose(models.Model):
    esus_id = models.CharField(max_length=255)
    acronym = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    objects = managers.DoseManager()

    def __str__(self):
        return f'{self.acronym} - {self.name}'


class Vaccination(models.Model):
    esus_code = models.BigIntegerField('Código ESUS', null=True, blank=True)
    vaccine = models.ForeignKey(
        'core.Vaccine', on_delete=models.CASCADE, 
    )
    dose = models.ForeignKey(
        'core.Dose', on_delete=models.SET_NULL, null=True, blank=True
    )
    patient = models.ForeignKey(
        'core.Role', on_delete=models.CASCADE, 
        related_name='patient_vaccinations'
    )
    professional = models.ForeignKey(
        'core.Role', on_delete=models.CASCADE, 
        related_name='professional_vaccinations', null=True, blank=True
    )
    cbo = models.ForeignKey(
        'core.CBO', on_delete=models.SET_NULL, null=True, blank=True
    )
    date = models.DateField(null=True, blank=True)
    health_unit = models.ForeignKey(
        'core.HealthUnit', on_delete=models.SET_NULL, null=True, blank=True
    )
    health_team = models.ForeignKey(
        'core.HealthTeam', on_delete=models.SET_NULL, null=True, blank=True
    )

    objects = managers.VaccinationManager()
