from datetime import datetime

import django_filters
from django.db.models import Exists, OuterRef, Q

from indicadores_esus.core import models
from indicadores_esus.core.utils import which_quadrimester


class CitizenFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='person__name',
        label='Nome',
        lookup_expr='icontains'
    )
    cpf = django_filters.CharFilter(
        field_name='person___cpf',
        label='CPF',
        lookup_expr='icontains'
    )
    cns = django_filters.CharFilter(
        field_name='person___cns',
        label='CNS',
        lookup_expr='icontains'
    )
    class Meta:
        model = models.Role
        fields = ['person___cpf', 'person___cns', 'person__name']


class PregnantWomanFilter(django_filters.FilterSet):
    SELECT_CHOICES = (
        ('SC', 'Sem consulta no mês'),
        ('QD', 'No quadrimestre')
    )
    name = django_filters.CharFilter(
        field_name='patient__person__name',
        label='Nome',
        lookup_expr='icontains'
    )
    cpf = django_filters.CharFilter(
        field_name='patient__person___cpf',
        label='CPF',
        lookup_expr='icontains'
    )
    cns = django_filters.CharFilter(
        field_name='patient__person___cns',
        label='CNS',
        lookup_expr='icontains',
    )
    cns_cpf_name = django_filters.CharFilter(
        label='Nome',
        method='filter_cns_cpf_name'
    )
    
    health_unit = django_filters.ModelChoiceFilter(
        field_name='patient__health_unit',
        label='Unidade de Saúde',
        queryset=models.HealthUnit.objects.all().order_by('name'),
        empty_label='Todas'
    )
    health_team = django_filters.ModelChoiceFilter(
        field_name='patient__health_team',
        label='Equipe de Saúde',
        queryset=models.HealthTeam.objects.all().order_by('name'),
        empty_label='Todas'
    )
    select_filter = django_filters.ChoiceFilter(
        label='Filtro',
        choices=SELECT_CHOICES,
        method='filter_select',
        empty_label='Todas'
    )

    def __init__(self, *args, **kwargs):
        query_dict = args[0].get('select_filter')
        queryset = kwargs.pop('queryset')
        on_quad = kwargs.pop('on_quad', False)
        if not query_dict and not on_quad:
            queryset = queryset.filter(
                dpp__gte=datetime.now().date()
            )
        super().__init__(queryset=queryset, *args, **kwargs)

    def filter_cns_cpf_name(self, queryset, name, value):
        return queryset.filter(
            Q(patient__person__name__icontains=value)
            | Q(patient__person___cpf__icontains=value)
            | Q(patient__person___cns__icontains=value)
        )

    def filter_select(self, queryset, name, value):
        current_date = datetime.now().date()
        appointments = models.Appointment.objects.filter(
            patient=OuterRef('pk'),
            date__month=current_date.month,
            date__year=current_date.year,
        )
        quadrimester = which_quadrimester(current_date)
        if value == 'SC':
            queryset = queryset.annotate(
                appointment_present_month=Exists(appointments)
            ).filter(
                appointment_present_month=False
            )
        elif value == 'QD':
            queryset = queryset.filter(
                dpp__range=(
                    quadrimester.evaluation_start, quadrimester.evaluation_end
                )
            )
        return queryset

    class Meta:
        model = models.PregnantWoman
        fields = [
            'patient__person___cpf', 'patient__person___cns', 
            'patient__person__name', 'patient__health_unit',
            'patient__health_team'
        ]


class WomanFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='patient__person__name',
        label='Nome',
        lookup_expr='icontains'
    )
    cpf = django_filters.CharFilter(
        field_name='patient__person___cpf',
        label='CPF',
        lookup_expr='icontains'
    )
    cns = django_filters.CharFilter(
        field_name='patient__person___cns',
        label='CNS',
        lookup_expr='icontains',
    )
    cns_cpf_name = django_filters.CharFilter(
        label='Nome',
        method='filter_cns_cpf_name'
    )
    health_unit = django_filters.ModelChoiceFilter(
        field_name='patient__health_unit',
        label='Unidade de Saúde',
        queryset=models.HealthUnit.objects.all().order_by('name'),
        empty_label='Todas'
    )
    health_team = django_filters.ModelChoiceFilter(
        field_name='patient__health_team',
        label='Equipe de Saúde',
        queryset=models.HealthTeam.objects.all().order_by('name'),
        empty_label='Todas'
    )

    def filter_cns_cpf_name(self, queryset, name, value):
        return queryset.filter(
            Q(patient__person__name__icontains=value)
            | Q(patient__person___cpf__icontains=value)
            | Q(patient__person___cns__icontains=value)
        )
    class Meta:
        model = models.Woman
        fields = [
            'patient__person___cpf', 'patient__person___cns', 
            'patient__person__name', 'patient__health_unit',
            'patient__health_team'
        ]


class ChildFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='patient__person__name',
        label='Nome',
        lookup_expr='icontains'
    )
    cpf = django_filters.CharFilter(
        field_name='patient__person___cpf',
        label='CPF',
        lookup_expr='icontains'
    )
    cns = django_filters.CharFilter(
        field_name='patient__person___cns',
        label='CNS',
        lookup_expr='icontains',
    )
    cns_cpf_name = django_filters.CharFilter(
        label='Nome',
        method='filter_cns_cpf_name'
    )
    health_unit = django_filters.ModelChoiceFilter(
        field_name='patient__health_unit',
        label='Unidade de Saúde',
        queryset=models.HealthUnit.objects.all().order_by('name'),
        empty_label='Todas'
    )
    health_team = django_filters.ModelChoiceFilter(
        field_name='patient__health_team',
        label='Equipe de Saúde',
        queryset=models.HealthTeam.objects.all().order_by('name'),
        empty_label='Todas'
    )

    def filter_cns_cpf_name(self, queryset, name, value):
        return queryset.filter(
            Q(patient__person__name__icontains=value)
            | Q(patient__person___cpf__icontains=value)
            | Q(patient__person___cns__icontains=value)
        )
    class Meta:
        model = models.Child
        fields = [
            'patient__person___cpf', 'patient__person___cns', 
            'patient__person__name', 'patient__health_unit',
            'patient__health_team'
        ]


class HypertensiveFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='patient__person__name',
        label='Nome',
        lookup_expr='icontains'
    )
    cpf = django_filters.CharFilter(
        field_name='patient__person___cpf',
        label='CPF',
        lookup_expr='icontains'
    )
    cns = django_filters.CharFilter(
        field_name='patient__person___cns',
        label='CNS',
        lookup_expr='icontains',
    )
    cns_cpf_name = django_filters.CharFilter(
        label='Nome',
        method='filter_cns_cpf_name'
    )
    health_unit = django_filters.ModelChoiceFilter(
        field_name='patient__health_unit',
        label='Unidade de Saúde',
        queryset=models.HealthUnit.objects.all().order_by('name'),
        empty_label='Todas'
    )
    health_team = django_filters.ModelChoiceFilter(
        field_name='patient__health_team',
        label='Equipe de Saúde',
        queryset=models.HealthTeam.objects.all().order_by('name'),
        empty_label='Todas'
    )

    def filter_cns_cpf_name(self, queryset, name, value):
        return queryset.filter(
            Q(patient__person__name__icontains=value)
            | Q(patient__person___cpf__icontains=value)
            | Q(patient__person___cns__icontains=value)
        )
    class Meta:
        model = models.Hypertensive
        fields = [
            'patient__person___cpf', 'patient__person___cns', 
            'patient__person__name', 'patient__health_unit',
            'patient__health_team'
        ]


class DiabeticFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='patient__person__name',
        label='Nome',
        lookup_expr='icontains'
    )
    cpf = django_filters.CharFilter(
        field_name='patient__person___cpf',
        label='CPF',
        lookup_expr='icontains'
    )
    cns = django_filters.CharFilter(
        field_name='patient__person___cns',
        label='CNS',
        lookup_expr='icontains',
    )
    cns_cpf_name = django_filters.CharFilter(
        label='Nome',
        method='filter_cns_cpf_name'
    )
    health_unit = django_filters.ModelChoiceFilter(
        field_name='patient__health_unit',
        label='Unidade de Saúde',
        queryset=models.HealthUnit.objects.all().order_by('name'),
        empty_label='Todas'
    )
    health_team = django_filters.ModelChoiceFilter(
        field_name='patient__health_team',
        label='Equipe de Saúde',
        queryset=models.HealthTeam.objects.all().order_by('name'),
        empty_label='Todas'
    )

    def filter_cns_cpf_name(self, queryset, name, value):
        return queryset.filter(
            Q(patient__person__name__icontains=value)
            | Q(patient__person___cpf__icontains=value)
            | Q(patient__person___cns__icontains=value)
        )
    class Meta:
        model = models.Diabetic
        fields = [
            'patient__person___cpf', 'patient__person___cns', 
            'patient__person__name', 'patient__health_unit',
            'patient__health_team'
        ]
