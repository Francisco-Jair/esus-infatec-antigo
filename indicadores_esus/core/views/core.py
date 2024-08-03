from datetime import datetime

import pandas as pd
from dateutil.relativedelta import relativedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from indicadores_esus.core import filters, forms, models
from indicadores_esus.core.utils import (Quadrimester, paginate,
                                         which_quadrimester)
from indicadores_esus.indicator.models import IndicatorPattern


class HomeView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/index.html'


class UserView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/user_system.html'
class TabelaView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/tabela_partial.html'

class TabelaHipView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/hypertensive_partial.html'


class print_woman_list(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/print_woman.html'


class print_vaccines_list(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/print_vaccines.html'


def search_citizen(request):
    filtered = filters.CitizenFilter(
        request.GET, 
        queryset=models.Role.objects.select_related(
            'person'
        ).all().order_by('person__name')
    )
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 100)
    page_obj = paginate(filtered.qs, page_size, page)
    template_name = 'core/search_citizen.html'
    if 'htmx' in request.path:
        template_name = 'core/citizen_list_partial.html'
    return render(request, template_name, {
        'page_obj': page_obj, 'form': filtered.form,
        'filter_url': reverse_lazy('core:citizen_list_htmx'),
    })


def load_sus_pregnant_data(data):
    df = pd.read_csv("dados-detalhados-gestante-Q1-23.csv", sep=';', encoding='latin-1', header=5, skipfooter=3)
    df['CNS'] = df['CNS'].astype(str)
    df['CPF'] = df['CPF'].apply(lambda x: str(x).split('.')[0].zfill(11))
    cpf_list = [cpf for cpf in df['CPF'].values.tolist() if cpf.isdigit()]
    cns_list = [cns for cns in df['CNS'].values.tolist() if cns.isdigit()]
    
    pregnant_qs = models.PregnantWoman.objects.filter(
        Q(patient__person___cpf__in=cpf_list)
        | Q(patient__person___cns__in=cns_list)
    )
    
    for q in pregnant_qs:
        print(
            f'{q.patient.person.name} - DN {q.patient.person.birth_date} - '
            f'DUM {q.dum} - DPP {q.dpp}'
        )
        
        if len(df.loc[df['CPF'] == q.patient.person.cpf]) > 0:
            row = df.loc[df['CPF'] == q.patient.person.cpf]
        elif len(df.loc[df['CNS'] == q.patient.person.cns]) > 0:
            row = df.loc[df['CNS'] == q.patient.person.cns]
        else:
            continue
        q.dum = datetime.strptime(row['Inicio'].values[0], "%d/%m/%Y").date()
        q.dpp = datetime.strptime(row['Fim'].values[0], "%d/%m/%Y").date()
        q.sus_registered = True
        q.save()


def upload_sus_table(request):
    if request.method == 'POST':
        form = UploadTableForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['table_file']
            load_data(filehandle)

    return render(request, 'core/contracts/upload_table.html',
                  {'form': UploadTableForm()})


class BuscarCidadoView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/buscar_cidadao.html'


class VacionaView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/buscar_cidadao.html'


class LinksUteisVew(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/links_uteis.html'

class ImpressaoGestante(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/print_pregnant.html'


class ACSRotaView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/ACS_MAP.html'


class FiltroGestantesVew(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/gestantes_indicador_filtro.html'


class FiltroAllVew(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'core/filtro.html'


def home_dashboard(request):
    current_date = datetime.now().date()
    current_quadrimester = which_quadrimester(current_date)
    quadrimester = current_quadrimester
    selected_quadrimester = request.GET.get('quadrimester')
    if selected_quadrimester:
        quad = selected_quadrimester.split('/')[0].replace('Q', '')
        year = selected_quadrimester.split('/')[1]
        quadrimester = Quadrimester(quad=quad, year=year)
    
    scope = None
    health_unit = request.GET.get('health_unit')
    health_team = request.GET.get('health_team')

    if health_unit:
        scope = models.HealthUnit.objects.get(id=health_unit).name

    if health_team:
        scope = models.HealthTeam.objects.get(id=health_team).name

    form = forms.HomeForm(initial={'quadrimester': quadrimester.abbrev})

    pregnant_queryset = models.PregnantWoman.objects.get_pregnant_indicators_data().filter(
        dpp__range=(quadrimester.evaluation_start, quadrimester.evaluation_end)
    )
    pregnant_obj = filters.PregnantWomanFilter(
        request.GET,
        on_quad=True,
        queryset=pregnant_queryset 
    )
    total_pregnant = pregnant_obj.qs.count()
    
    oldest_woman = quadrimester.evaluation_end - relativedelta(years=65) # Exclusive
    youngest_woman = quadrimester.evaluation_end - relativedelta(years=25)
    woman_queryset = models.Woman.objects.get_woman_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=36)
    ).filter(
        patient__person__birth_date__gt=oldest_woman,
        patient__person__birth_date__lte=youngest_woman
    )
    woman_obj = filters.WomanFilter(
        request.GET, 
        queryset=woman_queryset,
    )
    total_woman = woman_obj.qs.count()

    oldest_child = quadrimester.evaluation_start - relativedelta(months=12)
    youngest_child = quadrimester.evaluation_end - relativedelta(months=12)
    child_queryset = models.Child.objects.get_child_indicators_data().filter(
        patient__person__birth_date__gte=oldest_child,
        patient__person__birth_date__lte=youngest_child
    )
    child_obj = filters.ChildFilter(
        request.GET, 
        queryset=child_queryset,
    )
    total_child = child_obj.qs.count()

    hypertensive_queryset = models.Hypertensive.objects.get_hypertensive_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=6)
    ).all()
    hypertensive_obj = filters.HypertensiveFilter(
        request.GET, 
        queryset=hypertensive_queryset,
    )
    total_hypertensive = hypertensive_obj.qs.count()

    diabetic_queryset = models.Diabetic.objects.get_diabetic_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=6)
    ).all()
    diabetic_obj = filters.DiabeticFilter(
        request.GET, 
        queryset=diabetic_queryset,
    )
    total_diabetic = diabetic_obj.qs.count()

    indicator_1_achieved = pregnant_obj.qs.filter(indicator_1_achieved=True).count()
    indicator_2_achieved = pregnant_obj.qs.filter(indicator_2_achieved=True).count()
    indicator_3_achieved = pregnant_obj.qs.filter(indicator_3_achieved=True).count()
    indicator_4_achieved = woman_obj.qs.filter(indicator_4_achieved=True).count()
    indicator_5_achieved = child_obj.qs.filter(indicator_5_achieved=True).count()
    indicator_6_achieved = hypertensive_obj.qs.filter(indicator_6_achieved=True).count()
    indicator_7_achieved = diabetic_obj.qs.filter(indicator_7_achieved=True).count()

    indicator_summary = {
        'indicator_1':{
            'numerator': indicator_1_achieved,
            'denominator': total_pregnant,
            'percent': round(indicator_1_achieved / total_pregnant * 100, 2) if total_pregnant > 0 else 0,
        },
        'indicator_2':{
            'numerator': indicator_2_achieved,
            'denominator': total_pregnant,
            'percent': round(indicator_2_achieved / total_pregnant * 100, 2) if total_pregnant > 0 else 0,
        },
        'indicator_3':{
            'numerator': indicator_3_achieved,
            'denominator': total_pregnant,
            'percent': round(indicator_3_achieved / total_pregnant * 100, 2) if total_pregnant > 0 else 0,
        },
        'indicator_4':{
            'numerator': indicator_4_achieved,
            'denominator': total_woman,
            'percent': round(indicator_4_achieved / total_woman * 100, 2) if total_woman > 0 else 0,
        },
        'indicator_5':{
            'numerator': indicator_5_achieved,
            'denominator': total_child,
            'percent': round(indicator_5_achieved / total_child * 100, 2) if total_child > 0 else 0,
        },
        'indicator_6':{
            'numerator': indicator_6_achieved,
            'denominator': total_hypertensive,
            'percent': round(indicator_6_achieved / total_hypertensive * 100, 2) if total_hypertensive > 0 else 0,
        },
        'indicator_7':{
            'numerator': indicator_7_achieved,
            'denominator': total_diabetic,
            'percent': round(indicator_7_achieved / total_diabetic * 100, 2) if total_diabetic > 0 else 0,
        },
    }

    try:
        indicator_1_pattern = IndicatorPattern.objects.get(type='1')
        indicator_2_pattern = IndicatorPattern.objects.get(type='2')
        indicator_3_pattern = IndicatorPattern.objects.get(type='3')
        indicator_4_pattern = IndicatorPattern.objects.get(type='4')
        indicator_5_pattern = IndicatorPattern.objects.get(type='5')
        indicator_6_pattern = IndicatorPattern.objects.get(type='6')
        indicator_7_pattern = IndicatorPattern.objects.get(type='7')

        if indicator_1_pattern and indicator_1_pattern.goal > 0:
            indicator_1_result = (indicator_summary['indicator_1']['percent'] / indicator_1_pattern.goal) * 100
            if indicator_1_result  > indicator_1_pattern.parameter:
                indicator_1_result = 10
            else:
                indicator_1_result = indicator_1_result / 10

            indicator_1_npi = indicator_1_result * indicator_1_pattern.weight
            indicator_summary['indicator_1']['goal'] = indicator_1_pattern.goal
            indicator_summary['indicator_1']['rounded_percent'] = round(indicator_summary['indicator_1']['percent'])

        if indicator_2_pattern and indicator_2_pattern.goal > 0:
            indicator_2_result = (indicator_summary['indicator_2']['percent'] / indicator_2_pattern.goal) * 100
            if indicator_2_result  > indicator_2_pattern.parameter:
                indicator_2_result = 10
            else:
                indicator_2_result = indicator_2_result / 10

            indicator_2_npi = indicator_2_result * indicator_2_pattern.weight
            indicator_summary['indicator_2']['goal'] = indicator_2_pattern.goal
            indicator_summary['indicator_2']['rounded_percent'] = round(indicator_summary['indicator_2']['percent'])

        if indicator_3_pattern and indicator_3_pattern.goal > 0:
            indicator_3_result = (indicator_summary['indicator_3']['percent'] / indicator_3_pattern.goal) * 100
            if indicator_3_result  > indicator_3_pattern.parameter:
                indicator_3_result = 10
            else:
                indicator_3_result = indicator_3_result / 10

            indicator_3_npi = indicator_3_result * indicator_3_pattern.weight
            indicator_summary['indicator_3']['goal'] = indicator_3_pattern.goal
            indicator_summary['indicator_3']['rounded_percent'] = round(indicator_summary['indicator_3']['percent'])

        if indicator_4_pattern and indicator_4_pattern.goal > 0:
            indicator_4_result = (indicator_summary['indicator_4']['percent'] / indicator_4_pattern.goal) * 100
            if indicator_4_result  > indicator_4_pattern.parameter:
                indicator_4_result = 10
            else:
                indicator_4_result = indicator_4_result / 10

            indicator_4_npi = indicator_4_result * indicator_4_pattern.weight
            indicator_summary['indicator_4']['goal'] = indicator_4_pattern.goal
            indicator_summary['indicator_4']['rounded_percent'] = round(indicator_summary['indicator_4']['percent'])

        if indicator_5_pattern and indicator_5_pattern.goal > 0:
            indicator_5_result = (indicator_summary['indicator_5']['percent'] / indicator_5_pattern.goal) * 100
            if indicator_5_result  > indicator_5_pattern.parameter:
                indicator_5_result = 10
            else:
                indicator_5_result = indicator_5_result / 10

            indicator_5_npi = indicator_5_result * indicator_5_pattern.weight
            indicator_summary['indicator_5']['goal'] = indicator_5_pattern.goal
            indicator_summary['indicator_5']['rounded_percent'] = round(indicator_summary['indicator_5']['percent'])

        if indicator_6_pattern and indicator_6_pattern.goal > 0:
            indicator_6_result = (indicator_summary['indicator_6']['percent'] / indicator_6_pattern.goal) * 100
            if indicator_6_result  > indicator_6_pattern.parameter:
                indicator_6_result = 10
            else:
                indicator_6_result = indicator_6_result / 10

            indicator_6_npi = indicator_6_result * indicator_6_pattern.weight
            indicator_summary['indicator_6']['goal'] = indicator_6_pattern.goal
            indicator_summary['indicator_6']['rounded_percent'] = round(indicator_summary['indicator_6']['percent'])
        
        if indicator_7_pattern and indicator_7_pattern.goal > 0:
            indicator_7_result = (indicator_summary['indicator_7']['percent'] / indicator_7_pattern.goal) * 100
            if indicator_7_result  > indicator_7_pattern.parameter:
                indicator_7_result = 10
            else:
                indicator_7_result = indicator_7_result / 10

            indicator_7_npi = indicator_7_result * indicator_7_pattern.weight
            indicator_summary['indicator_7']['goal'] = indicator_7_pattern.goal
            indicator_summary['indicator_7']['rounded_percent'] = round(indicator_summary['indicator_7']['percent'])
        
        isf = (
            indicator_1_npi + indicator_2_npi + indicator_3_npi + 
            indicator_4_npi + indicator_5_npi + indicator_6_npi + indicator_7_npi
        ) / 10
    except:
        isf = None

    if isf:
        indicator_summary['ISF'] = round(isf, 2)

    template_name = 'core/index.html'
    
    return render(request, template_name, {
        'form': form,
        'summary': indicator_summary,
        'scope': scope
    })