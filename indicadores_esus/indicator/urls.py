from django.urls import path
from indicadores_esus.indicator.views import (
    indicator_list, indicator_team_list, indicator_unit_list
)


app_name = 'indicator'

urlpatterns = [
    path('lista_indicadores/', indicator_list, name='indicator_list'),
    path('indicador_equipe/', indicator_team_list, name='indicator_team'),
    path('indicador_unidade/', indicator_unit_list, name='indicator_unit'),
    # path(
    #     'lista_indicador1/', indicator1_data_list, name='indicator1_data_list'
    # ),
    # path(
    #     'lista_indicador1_htmx/', indicator1_data_list, 
    #     name='indicator1_data_list_htmx'
    # ),
    # path(
    #     'lista_indicador2/', indicator2_data_list, name='indicator2_data_list'
    # ),
    # path(
    #     'lista_indicador2_htmx/', indicator1_data_list, 
    #     name='indicator2_data_list_htmx'
    # ),
]
