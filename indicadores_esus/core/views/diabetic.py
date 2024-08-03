from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import Count, F, FloatField, Prefetch, Q
from django.db.models.functions import Cast
from django.shortcuts import render
from django.urls import reverse_lazy

from indicadores_esus.core import filters, models
from indicadores_esus.core.utils import paginate, which_quadrimester
from indicadores_esus.esus.managers import DIABETIC_CIAPS, DIABETIC_CIDS


def diabetics_list(request):
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    queryset = models.Diabetic.objects.get_diabetic_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=6)
    ).all()
    filter_obj = filters.DiabeticFilter(
        request.GET, 
        queryset=queryset,
    )
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    page_obj = paginate(filter_obj.qs, page_size, page)

    total_objects = filter_obj.qs.count()
    
    indicator_7_achieved = filter_obj.qs.filter(indicator_7_achieved=True).count()
    
    indicator_summary = {
        'ind_7': indicator_7_achieved,
        'ind_7_percent': round(indicator_7_achieved / total_objects * 100, 2) if total_objects > 0 else 0,
        'total': total_objects
    }

    template_name = 'core/diabetic/diabetic_list.html'
    if 'htmx' in request.path:
        template_name = 'core/diabetic/diabetic_partial.html'
    return render(request, template_name, {
        'page_obj': page_obj, 'form': filter_obj.form,
        'filter_url': reverse_lazy('core:diabetics_list_htmx'),
        'htmx_target': '#diabetic_section',
        'summary': indicator_summary
    })

def print_diabetics_list(request):
    template_name = 'core/diabetic/print_diabetics.html'
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    
    diabetics_subquery = models.Diabetic.objects.get_diabetic_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=6)
    ).all()
    
    indicator_7_list = diabetics_subquery.filter(
        indicator_7_achieved=True
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
                        lookup='diabetic',
                        to_attr='diabetic_rec',
                        queryset=diabetics_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    Q(diabetic__isnull=False)
                    & Q(diabetic__patient_id__in=indicator_7_list)
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__diabetic', 
                distinct=True
            ),
            indicator_7_qty=Count(
                'role__diabetic', 
                filter=Q(
                    role__diabetic__patient_id__in=indicator_7_list,
                ), 
                distinct=True
            ),
            indicator_7_percent=(F('indicator_7_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__diabetic__isnull=False,
            role__diabetic__patient_id__in=indicator_7_list,
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
                        lookup='diabetic',
                        to_attr='diabetic_rec',
                        queryset=diabetics_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    diabetic__isnull=False
                ).exclude(
                    diabetic__patient_id__in=indicator_7_list,
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__diabetic', 
                distinct=True
            ),
            indicator_7_qty=Count(
                'role__diabetic', 
                filter=Q(
                    role__diabetic__patient_id__in=indicator_7_list,
                ), 
                distinct=True
            ),
            indicator_7_percent=(F('indicator_7_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__diabetic__isnull=False,
            role__diabetic__patient_id__in=indicator_7_list,
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
                        lookup='diabetic',
                        to_attr='diabetic_rec',
                        queryset=diabetics_subquery,
                    )
                ).select_related(
                    'health_team'
                ).filter(
                    diabetic__isnull=False
                ).order_by(
                    'person__name'
                ).distinct()
            )
        ).annotate(
            total_qty=Count(
                'role__diabetic', 
                distinct=True
            ),
            indicator_7_qty=Count(
                'role__diabetic', 
                filter=Q(
                    role__diabetic__patient_id__in=indicator_7_list,
                ), 
                distinct=True
            ),
            indicator_7_percent=(F('indicator_7_qty') * 100) / Cast(
                F('total_qty'), output_field=FloatField()
            ),
        ).filter(
            role__diabetic__isnull=False,
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


def diabetic_detail(request, pk):
    obj = models.Diabetic.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by('id').last()
    appointments = obj.patient.patient_appointments.all().order_by('-date')
    detail_data = {
        'obj': obj,
        'address': address,
        'medical_appointments': appointments.filter(
            Q(appointment_type='M')
            & Q(
                Q(cids__code__in=DIABETIC_CIDS)
                | Q(ciaps__code__in=DIABETIC_CIAPS)
            )
        ),
        'procedures': obj.patient.patient_procedures.filter(
            procedure__procedure_code__in=['0202010503','ABEX008']
        )
    }
    return render(request, 'core/diabetic/diabetic_modal_partial.html', detail_data)


def print_diabetic_detail(request, pk):
    obj = models.Diabetic.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by('id').last()
    appointments = obj.patient.patient_appointments.all().order_by('-date')
    detail_data = {
        'obj': obj,
        'address': address,
        'medical_appointments': appointments.filter(
            Q(appointment_type='M')
            & Q(
                Q(cids__code__in=DIABETIC_CIDS)
                | Q(ciaps__code__in=DIABETIC_CIAPS)
            )
        ),
        'procedures': obj.patient.patient_procedures.filter(
            procedure__procedure_code__in=['0202010503','ABEX008']
        )
    }
    return render(request, 'core/diabetic/diabetic_modal_print.html', detail_data)
