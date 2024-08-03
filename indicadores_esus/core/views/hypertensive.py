from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import Count, F, FloatField, Prefetch, Q
from django.db.models.functions import Cast
from django.shortcuts import render
from django.urls import reverse_lazy

from indicadores_esus.core import filters, models
from indicadores_esus.core.utils import paginate, which_quadrimester
from indicadores_esus.esus.managers import HYPERTENSE_CIAPS, HYPERTENSE_CIDS


def hypertensives_list(request):
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    queryset = models.Hypertensive.objects.get_hypertensive_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=6)
    ).all()
    filter_obj = filters.HypertensiveFilter(
        request.GET, 
        queryset=queryset,
    )
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    page_obj = paginate(filter_obj.qs, page_size, page)

    total_objects = filter_obj.qs.count()
    
    indicator_6_achieved = filter_obj.qs.filter(indicator_6_achieved=True).count()
    
    indicator_summary = {
        'ind_6': indicator_6_achieved,
        'ind_6_percent': round(indicator_6_achieved / total_objects * 100, 2) if total_objects > 0 else 0,
        'total': total_objects
    }

    template_name = 'core/hypertensive/hypertensive_list.html'
    if 'htmx' in request.path:
        template_name = 'core/hypertensive/hypertensive_partial.html'
    return render(request, template_name, {
        'page_obj': page_obj, 'form': filter_obj.form,
        'filter_url': reverse_lazy('core:hypertensives_list_htmx'),
        'htmx_target': '#hypertensive_section',
        'summary': indicator_summary
    })

def print_hypertensives_list(request):
    template_name = 'core/hypertensive/print_hypertensives.html'
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    
    hypertensives_subquery = models.Hypertensive.objects.get_hypertensive_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=6)
    ).all()
    
    indicator_6_list = hypertensives_subquery.filter(
        indicator_6_achieved=True
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
                        lookup='hypertensive',
                        to_attr='hypertensive_rec',
                        queryset=hypertensives_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    Q(hypertensive__isnull=False)
                    & Q(hypertensive__patient_id__in=indicator_6_list)
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__hypertensive', 
                distinct=True
            ),
            indicator_6_qty=Count(
                'role__hypertensive', 
                filter=Q(
                    role__hypertensive__patient_id__in=indicator_6_list,
                ), 
                distinct=True
            ),
            indicator_6_percent=(F('indicator_6_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__hypertensive__isnull=False,
            role__hypertensive__patient_id__in=indicator_6_list,
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
                        lookup='hypertensive',
                        to_attr='hypertensive_rec',
                        queryset=hypertensives_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    hypertensive__isnull=False
                ).exclude(
                    hypertensive__patient_id__in=indicator_6_list,
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__hypertensive', 
                distinct=True
            ),
            indicator_6_qty=Count(
                'role__hypertensive', 
                filter=Q(
                    role__hypertensive__patient_id__in=indicator_6_list,
                ), 
                distinct=True
            ),
            indicator_6_percent=(F('indicator_6_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__hypertensive__isnull=False,
            role__hypertensive__patient_id__in=indicator_6_list,
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
                        lookup='hypertensive',
                        to_attr='hypertensive_rec',
                        queryset=hypertensives_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    hypertensive__isnull=False
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__hypertensive', 
                distinct=True
            ),
            indicator_6_qty=Count(
                'role__hypertensive', 
                filter=Q(
                    role__hypertensive__patient_id__in=indicator_6_list,
                ), 
                distinct=True
            ),
            indicator_6_percent=(F('indicator_6_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__hypertensive__isnull=False,
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


def hypertensive_detail(request, pk):
    obj = models.Hypertensive.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by('id').last()
    appointments = obj.patient.patient_appointments.all().order_by('-date')
    detail_data = {
        'obj': obj,
        'address': address,
        'medical_appointments': appointments.filter(
            Q(appointment_type='M')
            & Q(
                Q(cids__code__in=HYPERTENSE_CIDS)
                | Q(ciaps__code__in=HYPERTENSE_CIAPS)
            )
        ),
        'procedures': obj.patient.patient_procedures.filter(
            procedure__procedure_code__in=['0301100039', 'ABPG033']
        )
    }
    return render(request, 'core/hypertensive/hypertensive_modal_partial.html', detail_data)


def print_hypertensive_detail(request, pk):
    obj = models.Hypertensive.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by('id').last()
    appointments = obj.patient.patient_appointments.all().order_by('-date')
    detail_data = {
        'obj': obj,
        'address': address,
        'medical_appointments': appointments.filter(
            Q(appointment_type='M')
            & Q(
                Q(cids__code__in=HYPERTENSE_CIDS)
                | Q(ciaps__code__in=HYPERTENSE_CIAPS)
            )
        ),
        'procedures': obj.patient.patient_procedures.filter(
            procedure__procedure_code__in=['0301100039', 'ABPG033']
        )
    }
    return render(request, 'core/hypertensive/hypertensive_modal_print.html', detail_data)
