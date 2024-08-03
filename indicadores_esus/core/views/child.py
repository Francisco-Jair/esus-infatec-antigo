from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import Count, F, FloatField, Prefetch, Q
from django.db.models.functions import Cast
from django.shortcuts import render
from django.urls import reverse_lazy

from indicadores_esus.core import filters, models
from indicadores_esus.core.utils import paginate, which_quadrimester


def children_list(request):
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    oldest = quadrimester.evaluation_start - relativedelta(months=12)
    youngest = quadrimester.evaluation_end - relativedelta(months=12)
    queryset = models.Child.objects.get_child_indicators_data().filter(
        patient__person__birth_date__gte=oldest,
        patient__person__birth_date__lte=youngest
    )
    filter_obj = filters.ChildFilter(
        request.GET, 
        queryset=queryset,
    )
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    page_obj = paginate(filter_obj.qs, page_size, page)

    total_objects = filter_obj.qs.count()
    
    indicator_5_achieved = filter_obj.qs.filter(indicator_5_achieved=True).count()
    
    indicator_summary = {
        'ind_5': indicator_5_achieved,
        'ind_5_percent': round(indicator_5_achieved / total_objects * 100, 2) if total_objects > 0 else 0,
        'total': total_objects
    }

    template_name = 'core/child/children_list.html'
    if 'htmx' in request.path:
        template_name = 'core/child/children_partial.html'
    return render(request, template_name, {
        'page_obj': page_obj, 'form': filter_obj.form,
        'filter_url': reverse_lazy('core:children_list_htmx'),
        'htmx_target': '#children_section',
        'summary': indicator_summary
    })


def print_children_list(request):
    template_name = 'core/child/print_children.html'
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    oldest = quadrimester.evaluation_start - relativedelta(months=12)
    youngest = quadrimester.evaluation_end - relativedelta(months=12)

    children_subquery = models.Child.objects.get_child_indicators_data().filter(
        patient__person__birth_date__gte=oldest,
        patient__person__birth_date__lte=youngest
    )
    
    indicator_5_list = children_subquery.filter(
        indicator_5_achieved=True
    ).values_list(
        'patient_id', flat=True
    )

    parameter = request.GET.get('type')
    show_summary = True
    if parameter == 'achieved':
        show_summary = False
        queryset = models.HealthUnit.objects.select_related(
            'city'
        ).prefetch_related(
            Prefetch(
                lookup='role_set',
                to_attr='patient_list',
                queryset=models.Role.objects.select_related(
                    'person'
                ).prefetch_related(
                    Prefetch(
                        lookup='child',
                        to_attr='child_rec',
                        queryset=children_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    Q(
                        person__birth_date__gt=oldest,
                        person__birth_date__lte=youngest
                    )
                    & Q(child__isnull=False)
                    & Q(child__patient_id__in=indicator_5_list)
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__child', 
                filter=Q(
                    role__person__birth_date__gt=oldest,
                    role__person__birth_date__lte=youngest,
                ), 
                distinct=True
            ),
            indicator_5_qty=Count(
                'role__child', 
                filter=Q(
                    role__person__birth_date__gt=oldest,
                    role__person__birth_date__lte=youngest,
                    role__child__patient_id__in=indicator_5_list,
                ), 
                distinct=True
            ),
            indicator_5_percent=(F('indicator_5_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__person__birth_date__gt=oldest,
            role__person__birth_date__lte=youngest,
            role__child__isnull=False,
            role__child__patient_id__in=indicator_5_list,
        ).order_by(
            'name'
        ).distinct()
    elif parameter == 'not_achieved':
        show_summary = False
        queryset = models.HealthUnit.objects.select_related(
            'city'
        ).prefetch_related(
            Prefetch(
                lookup='role_set',
                to_attr='patient_list',
                queryset=models.Role.objects.select_related(
                    'person'
                ).prefetch_related(
                    Prefetch(
                        lookup='child',
                        to_attr='child_rec',
                        queryset=children_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    person__birth_date__gt=oldest,
                    person__birth_date__lte=youngest,
                    child__isnull=False
                ).exclude(
                    child__patient_id__in=indicator_5_list,
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__child', 
                filter=Q(
                    role__person__birth_date__gt=oldest,
                    role__person__birth_date__lte=youngest,
                ), 
                distinct=True
            ),
            indicator_5_qty=Count(
                'role__child', 
                filter=Q(
                    role__person__birth_date__gt=oldest,
                    role__person__birth_date__lte=youngest,
                    role__child__patient_id__in=indicator_5_list,
                ), 
                distinct=True
            ),
            indicator_5_percent=(F('indicator_5_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__person__birth_date__gt=oldest,
            role__person__birth_date__lte=youngest,
            role__child__isnull=False,
            role__child__patient_id__in=indicator_5_list,
        ).order_by(
            'name'
        ).distinct()
    else:
        queryset = models.HealthUnit.objects.select_related(
            'city'
        ).prefetch_related(
            Prefetch(
                lookup='role_set',
                to_attr='patient_list',
                queryset=models.Role.objects.select_related(
                    'person'
                ).prefetch_related(
                    Prefetch(
                        lookup='child',
                        to_attr='child_rec',
                        queryset=children_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    person__birth_date__gt=oldest,
                    person__birth_date__lte=youngest,
                    child__isnull=False
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__child', 
                filter=Q(
                    role__person__birth_date__gt=oldest,
                    role__person__birth_date__lte=youngest,
                ), 
                distinct=True
            ),
            indicator_5_qty=Count(
                'role__child', 
                filter=Q(
                    role__person__birth_date__gt=oldest,
                    role__person__birth_date__lte=youngest,
                    role__child__patient_id__in=indicator_5_list,
                ), 
                distinct=True
            ),
            indicator_5_percent=(F('indicator_5_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__person__birth_date__gt=oldest,
            role__person__birth_date__lte=youngest,
            role__child__isnull=False,
        ).order_by(
            'name'
        ).distinct()
    city = models.City.objects.get(name__iexact='caxias', state__iexact='ma')
    
    health_unit = request.GET.get('health_unit')

    if health_unit:
        queryset = queryset.filter(id=int(health_unit))

    context = {
        'obj': queryset,
        'city': city,
        'show_summary': show_summary,
        'quadrimester': {
            'quad': quadrimester.quad,
            'year': quadrimester.year,
        }
    }
    return render(request, template_name, context)


def child_detail(request, pk):
    obj = models.Child.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by('id').last()
    vaccines = obj.patient.patient_vaccinations.filter(
        vaccine__esus_id__in=models.Vaccine.INDICATOR_5_VACCINE_CODES,
        date__gte=obj.patient.person.birth_date
    ).order_by('-date')
    detail_data = {
        'obj': obj,
        'address': address,
        'vaccines': vaccines,
    }
    return render(request, 'core/child/child_modal_partial.html', detail_data)


def print_child_detail(request, pk):
    obj = models.Child.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by('id').last()
    vaccines = obj.patient.patient_vaccinations.filter(
        vaccine__esus_id__in=models.Vaccine.INDICATOR_5_VACCINE_CODES,
        date__gte=obj.patient.person.birth_date
    ).order_by('-date')
    detail_data = {
        'obj': obj,
        'address': address,
        'vaccines': vaccines,
    }
    return render(request, 'core/child/child_modal_print.html', detail_data)
