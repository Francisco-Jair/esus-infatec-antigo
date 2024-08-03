from django.db import models
from django.db.models import Sum

from indicadores_esus.indicator.managers import CalculatedIndicatorManager, IndicatorDataManager


INDICATOR_TYPE_CHOICES = (
    ('1', 'Indicador 1 - Proporção de gestantes com pelo menos 6 (seis) consultas pré-natal realizadas, sendo a 1ª até a 12ª semana de gestação'),
    ('2', 'Indicador 2 - Proporção de gestantes com realização de exames para sífilis e HIV'),
    ('3', 'Indicador 3 - Proporção de gestantes com atendimento odontológico realizado'),
    ('4', 'Indicador 4 - Proporção de mulheres com coleta de citopatológico na APS'),
    ('5', 'Indicador 5 - Proporção de crianças de 1(um) ano de idade vacinadas na APS contra Difeteria, Tétano, Coqueluche, Hepatite B, Infecções causadas por Haemophilus Influenzae tipo b e Poliomielite Inativada'),
    ('6', 'Indicador 6 - Proporção de pessoas com hipertensão, com consulta e pressão arterial aferida no semestre'),
    ('7', 'Indicador 7 - Proporção de pessoas com diabetes, com consulta e hemoglobina glicada solicitada no semestre')
)


class Indicator(models.Model):
    description = models.CharField('descrição', max_length=250, blank=True)
    isf = models.DecimalField('indicador sintético final', max_digits=6, decimal_places=2, blank=True, null=True)
    quadrimester = models.CharField('quadrimestre', max_length=7, blank=True)
    dt_init_evaluation = models.DateField('data inicial da avaliação', null=True, blank=True)
    dt_end_evaluation = models.DateField('data final da avaliação', null=True, blank=True)
    # TODO: Tornar o campo city obrigatório após estabelecer fixtures.
    city = models.ForeignKey('core.City', on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField('Ativo?', default=True)

    @property
    def get_isf(self):
        
        ind = CalculatedIndicator.objects.filter(
            indicator_id=self.pk, status='1'
        ).select_related(
            'pattern', 'indicator'
        ).order_by(
            '-updated_at'
        )
    
        if ind.count() != 7 or len(set([i.type for i in ind])) != 7:
            return 'Para o cálculo do indicador sintético final, todos os 7 indicadores devem ter sido calculados'

        isf = ind.aggregate(Sum('npi'))['npi__sum'] / 10
        
        return f'{isf:.2f}'.replace('.', ',')

    @property
    def is_consolidated(self):
        
        ind = CalculatedIndicator.objects.filter(
            indicator_id=self.pk, status='1'
        ).select_related(
            'pattern', 'indicator'
        ).order_by(
            '-updated_at'
        )
        if len(set([i.type for i in ind])) == 7:
            return True
        return False

    def set_only_one_active(self):
        indicators = Indicator.objects.filter(
            quadrimester=self.quadrimester, 
            is_active=True
        ).exclude(pk=self.pk)
        if indicators.exists():
            indicators.update(is_active=False)


    def save(self, *args, **kwargs):
        if self.is_active:
            self.set_only_one_active()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.description} - {self.quadrimester}'

    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'


class IndicatorPattern(models.Model):
    type = models.CharField('tipo', max_length=1, choices=INDICATOR_TYPE_CHOICES)
    parameter = models.PositiveSmallIntegerField('parâmetro')
    goal = models.PositiveSmallIntegerField('meta')
    weight = models.PositiveSmallIntegerField('peso')
    year = models.PositiveSmallIntegerField('ano')
    estimated_denominator = models.IntegerField('denominador estimado', blank=True, null=True) 
    is_active = models.BooleanField('Ativo?', default=True)

    def set_only_one_active(self):
        patterns = IndicatorPattern.objects.filter(
            type=self.type,
            year=self.year, 
            is_active=True
        ).exclude(pk=self.pk)
        if patterns.exists():
            patterns.update(is_active=False)


    def save(self, *args, **kwargs):
        if self.is_active:
            self.set_only_one_active()
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.type} - {self.year}'

    class Meta:
        verbose_name = 'Padrões para indicador'
        verbose_name_plural = 'Padrões para indicadores'

class CalculatedIndicator(models.Model):
    STATUS_CHOICES = (
        ('1', 'Gerado'),
        ('2', 'Calculando'),
        ('3', 'Removido')
    )

    indicator = models.ForeignKey(
        'indicator.Indicator', on_delete=models.CASCADE, 
        verbose_name='indicador', related_name='calculated_indicators'
    )
    pattern = models.ForeignKey(
        'indicator.IndicatorPattern', on_delete=models.SET_NULL, 
        null=True, blank=True
    )
    type = models.CharField('tipo', max_length=1, choices=INDICATOR_TYPE_CHOICES)
    denominator = models.IntegerField('denominador')
    numerator = models.IntegerField('numerador')
    indicator_index = models.DecimalField('indicador', max_digits=6, decimal_places=2)
    result = models.DecimalField('nota', max_digits=6, decimal_places=2, null=True, blank=True)
    npi = models.DecimalField('nota ponderada do indicador', max_digits=6, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    calculated_at = models.DateTimeField('calculada em', auto_now_add=True)
    updated_at = models.DateTimeField('atualizada em', auto_now=True)

    objects = CalculatedIndicatorManager()

    def set_only_one_active(self):
        indicators = CalculatedIndicator.objects.filter(
            indicator=self.indicator,
            type=self.type,
            status__in=['1', '2']
        ).exclude(pk=self.pk)
        if indicators.exists():
            indicators.update(status='3')

    def get_result(self):
        if self.pattern and self.pattern.goal > 0:
            result = (self.indicator_index / self.pattern.goal) * 100
            if result  > self.pattern.parameter:
                result = 10
            else:
                result = result / 10
            return result
    
    def get_npi(self):
        if self.pattern:
            npi = self.result * self.pattern.weight
            return npi

    def save(self, *args, **kwargs):
        if self.denominator > 0:
            self.indicator_index = (self.numerator / self.denominator) * 100
        
        if self.status in ['1', '2']:
            self.set_only_one_active()

        if self.pattern:
            self.result = self.get_result()
            self.npi = self.get_npi()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Indicador {self.type} - {self.indicator.quadrimester}'

    class Meta:
        verbose_name = 'Indicador calculado'
        verbose_name_plural = 'Indicadores calculados'


# class IndicatorData(models.Model):
#     indicator = models.ForeignKey(
#         'core.Indicator', on_delete=models.CASCADE, verbose_name='indicador'
#     )
#     name = models.CharField('nome', max_length=500, null=True, blank=True)
#     cns = models.CharField(max_length=15, null=True, blank=True)
#     cpf = models.CharField(max_length=11, null=True, blank=True)
#     dum = models.DateField('data da última menstruação', null=True, blank=True)
#     dpp = models.DateField('data provável de parto', null=True, blank=True)

#     objects = IndicatorDataManager()

#     def __str__(self):
#         desc = str(self.id)
#         if self.name is not None:
#             desc = self.name
#         elif self.cns is not None:
#             desc = self.cns
#         elif self.cpf is not None:
#             desc = self.cpf
        
#         return f'{self.indicator}-{desc}'

#     class Meta:
#         verbose_name = 'Dado do Indicador'
#         verbose_name_plural = 'Dados do Indicador'


# class IndicatorAppointmentData(models.Model):
#     person = models.ForeignKey(
#         'core.IndicatorData', on_delete=models.CASCADE,
#         related_name='person_appointments_set',
#         verbose_name='pessoa'    
#     )
#     appointment_id = models.BigIntegerField('ID do atendimento')
#     date = models.DateField('data')

#     def __str__(self):
#         return str(self.date)

#     class Meta:
#         verbose_name = 'Consulta'
#         verbose_name_plural = 'Consultas'    

