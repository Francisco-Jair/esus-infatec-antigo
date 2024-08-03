import time

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Exists, OuterRef, Prefetch, Q, Sum
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django_q.tasks import async_task

from indicadores_esus.core.models import (HealthTeam, HealthUnit,
                                          PatientIndicator, Role)
from indicadores_esus.core.utils import Quadrimester, paginate
from indicadores_esus.indicator.forms import (CalculateIndicatorForm,
                                              IndicatorTeamForm)
from indicadores_esus.indicator.models import CalculatedIndicator, Indicator


def indicator_list(request):
    indicators = Indicator.objects.filter(
        is_active=True
    ).prefetch_related(
        Prefetch(
            lookup='calculated_indicators',
            to_attr='calculated_indicators_list',
            queryset=CalculatedIndicator.objects.filter(
                status__in=['1', '2']
            ).order_by('type').select_related('pattern')
        ),
    ).order_by('-dt_end_evaluation')
    indicators_list = []
    for ind in indicators:
        ind_dict = {
            'indicators': ind,
            'quadrimester': ind.quadrimester,
            'get_isf': ind.get_isf,
        }
        for calc in ind.calculated_indicators_list:
            print(calc)
            ind_dict[calc.type] = {
                'numerator': calc.numerator,
                'denominator': calc.denominator,
                'index': calc.indicator_index
            }
        indicators_list.append(ind_dict)
    form = CalculateIndicatorForm()
    if request.method == 'POST':
        quad = Quadrimester(
            year=request.POST.get('year'), 
            quad=request.POST.get('quadrimester')
        )
        indicator_type = request.POST.get('type')
        if indicator_type == 'T':
            async_task(CalculatedIndicator.objects.get_all_indicators, quad)    
        else:
            async_task(CalculatedIndicator.objects.get_indicator, indicator_type, quad)
        time.sleep(3)

    return render(request, 'indicator/indicator_list.html', {
        'page_obj': indicators_list, 'form': form
    })


def indicator_team_list(request):
    form = IndicatorTeamForm(request.GET)
    
    indicators = []
    if form.is_valid():
        indicators = CalculatedIndicator.objects.filter(
            status=1, indicator=form.cleaned_data.get('indicator')
        ).order_by('type')
    
    indicator_dict = {}
    for calculated in indicators:
        teams = HealthTeam.objects.prefetch_related(
            Prefetch(
                lookup='role_set',
                to_attr='denominator',
                queryset=Role.objects.filter(
                    Q(
                        Exists(
                            PatientIndicator.objects.filter(
                                patient_id=OuterRef('pk'),
                                indicator=calculated,
                            )
                        )
                    )
                    & Q(role_type=1)    
                )
            ), 
            Prefetch(
                lookup='role_set',
                to_attr='numerator',
                queryset=Role.objects.filter(
                    Q(
                        Exists(
                            PatientIndicator.objects.filter(
                                patient_id=OuterRef('pk'),
                                indicator=calculated,
                                numerator=True
                            )
                        )
                    )
                    & Q(role_type=1)    
                )
            )
        ).all().order_by('name')

        team_list = []
        for team in teams:
            denominator = len(team.denominator)
            numerator = len(team.numerator)
            try:
                indicator = round((numerator / denominator) * 100)
            except ZeroDivisionError:
                indicator = 0
            
            health_team = {
                'ine': team.ine,
                'name': team.name,
                'denominator': denominator,
                'numerator': numerator,
                'indicator': indicator
            }
            team_list.append(health_team)

        no_team = PatientIndicator.objects.filter(
            indicator=indicator,
            patient__health_team__isnull=True
        )
        denominator = no_team.count()
        numerator = no_team.filter(numerator=True).count()
        try:
            indicator = round((numerator / denominator) * 100)
        except ZeroDivisionError:
            indicator = 0
        health_team = {
            'ine': 'N/A',
            'name': 'Sem equipe vinculada',
            'denominator': denominator,
            'numerator': numerator,
            'indicator': indicator
        }
        team_list.append(health_team)
        indicator_dict[calculated.get_type_display()] = team_list

    return render(request, 'indicator/indicator_team.html', {
        'page_obj': indicator_dict, 'form': form
    })


def indicator_unit_list(request):
    form = IndicatorTeamForm(request.GET)
    
    indicators = []
    if form.is_valid():
        indicators = CalculatedIndicator.objects.filter(
            status=1, indicator=form.cleaned_data.get('indicator')
        ).order_by('type')
    
    indicator_dict = {}
    for calculated in indicators:
        units = HealthUnit.objects.prefetch_related(
            Prefetch(
                lookup='role_set',
                to_attr='denominator',
                queryset=Role.objects.filter(
                    Q(
                        Exists(
                            PatientIndicator.objects.filter(
                                patient_id=OuterRef('pk'),
                                indicator=calculated,
                            )
                        )
                    )
                    & Q(role_type=1)    
                )
            ), 
            Prefetch(
                lookup='role_set',
                to_attr='numerator',
                queryset=Role.objects.filter(
                    Q(
                        Exists(
                            PatientIndicator.objects.filter(
                                patient_id=OuterRef('pk'),
                                indicator=calculated,
                                numerator=True
                            )
                        )
                    )
                    & Q(role_type=1)    
                )
            )
        ).all().order_by('name')

        unit_list = []
        for unit in units:
            denominator = len(unit.denominator)
            numerator = len(unit.numerator)
            try:
                indicator = round((numerator / denominator) * 100)
            except ZeroDivisionError:
                indicator = 0
            
            health_unit = {
                'cnes': unit.cnes,
                'name': unit.name,
                'denominator': denominator,
                'numerator': numerator,
                'indicator': indicator
            }
            unit_list.append(health_unit)

        no_unit = PatientIndicator.objects.filter(
            indicator=indicator,
            patient__health_unit__isnull=True
        )
        denominator = no_unit.count()
        numerator = no_unit.filter(numerator=True).count()
        try:
            indicator = round((numerator / denominator) * 100)
        except ZeroDivisionError:
            indicator = 0
        health_unit = {
            'cnes': 'N/A',
            'name': 'Sem unidade vinculada',
            'denominator': denominator,
            'numerator': numerator,
            'indicator': indicator
        }
        unit_list.append(health_unit)
        indicator_dict[calculated.get_type_display()] = unit_list

    return render(request, 'indicator/indicator_unit.html', {
        'page_obj': indicator_dict, 'form': form
    })
class IndicadorEquipeView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'indicator/indicadores_equipe.html'


class IndicadorUnidadeeView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'indicator/indicador_unidade.html'


# def indicator1_data_list(request):
#     indicator_choice = request.GET.get('indicator', None)
#     indicator = Indicator.objects.filter(
#         type=1,
#         status=1
#     ).order_by('updated_at').last()
#     if indicator_choice is not None:
#         indicator = Indicator.objects.get(
#             type=1,
#             status=1, 
#             id=indicator_choice
#         )
#     data = IndicatorData.objects.filter(
#         indicator=indicator
#     ).prefetch_related(
#         'person_appointments_set'
#     ).order_by(
#         'name'
#     )
    
#     page = request.GET.get('page', 1)
#     page_size = request.GET.get('page_size', 100)
#     page_obj = paginate(data, page_size, page)
#     template_name = 'core/indicator1_data_list.html'
#     if 'htmx' in request.path:
#         template_name = 'core/indicator1_data_list_partial.html'
#     return render(request, template_name, {
#         'page_obj': page_obj,
#         'filter_url': reverse_lazy('indicadores:indicator1_data_list_htmx'),
#         'indicator': indicator
#     })


# def indicator2_data_list(request):
#     indicator_choice = request.GET.get('indicator', None)
#     indicator = Indicator.objects.filter(
#         type=2,
#         status=1
#     ).order_by('updated_at').last()
#     if indicator_choice is not None:
#         indicator = Indicator.objects.get(
#             type=2,
#             status=1, 
#             id=indicator_choice
#         )
#     data = IndicatorData.objects.filter(
#         indicator=indicator
#     ).prefetch_related(
#         'person_appointments_set'
#     ).order_by(
#         'name'
#     )
#     page = request.GET.get('page', 1)
#     page_size = request.GET.get('page_size', 100)
#     page_obj = paginate(data, page_size, page)
#     template_name = 'core/indicator1_data_list.html'
#     if 'htmx' in request.path:
#         template_name = 'core/indicator1_data_list_partial.html'
#     return render(request, template_name, {
#         'page_obj': page_obj,
#         'filter_url': reverse_lazy('indicadores:indicator1_data_list_htmx'),
#         'indicator': indicator
#     })
