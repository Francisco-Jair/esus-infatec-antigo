import django_filters
from indicadores_esus.esus.models import TbCidadao


class CitizenFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='no_cidadao',
                                     label='Nome',
                                     lookup_expr='icontains')
    local = django_filters.CharFilter(field_name='co_localidade__no_localidade',
                                      label='Local',
                                      lookup_expr='icontains')

    class Meta:
        model = TbCidadao
        fields = ['no_cidadao', 'co_localidade']
