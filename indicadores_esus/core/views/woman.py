from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import Count, F, FloatField, Prefetch, Q
from django.db.models.functions import Cast
from django.shortcuts import render
from django.urls import reverse_lazy

from indicadores_esus.core import filters, models
from indicadores_esus.core.utils import paginate, which_quadrimester


def women_list(request):
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    oldest = quadrimester.evaluation_end - relativedelta(years=65)  # Exclusive
    youngest = quadrimester.evaluation_end - relativedelta(years=25)
    queryset = models.Woman.objects.get_woman_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=36)
    ).filter(
        patient__person__birth_date__gt=oldest,
        patient__person__birth_date__lte=youngest,
    )
    filter_obj = filters.WomanFilter(
        request.GET,
        queryset=queryset,
    )
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)
    page_obj = paginate(filter_obj.qs, page_size, page)

    total_objects = filter_obj.qs.count()

    indicator_4_achieved = filter_obj.qs.filter(indicator_4_achieved=True).count()

    indicator_summary = {
        "ind_4": indicator_4_achieved,
        "ind_4_percent": round(indicator_4_achieved / total_objects * 100, 2)
        if total_objects > 0
        else 0,
        "total": total_objects,
    }

    template_name = "core/woman/women_list.html"
    if "htmx" in request.path:
        template_name = "core/woman/women_partial.html"
    return render(
        request,
        template_name,
        {
            "page_obj": page_obj,
            "form": filter_obj.form,
            "filter_url": reverse_lazy("core:women_list_htmx"),
            "htmx_target": "#women_section",
            "summary": indicator_summary,
        },
    )


def print_women_list(request):
    template_name = "core/woman/print_women.html"
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    oldest = quadrimester.evaluation_end - relativedelta(years=65)  # Exclusive
    youngest = quadrimester.evaluation_end - relativedelta(years=25)

    women_subquery = models.Woman.objects.get_woman_indicators_data(
        start_date=quadrimester.evaluation_end - relativedelta(months=36),
    ).filter(
        patient__person__birth_date__gt=oldest,
        patient__person__birth_date__lte=youngest,
    )

    indicator_4_list = women_subquery.filter(indicator_4_achieved=True).values_list(
        "patient_id", flat=True
    )

    parameter = request.GET.get("type")
    show_summary = True
    if parameter == "achieved":
        show_summary = False
        queryset = (
            models.HealthUnit.objects.select_related("city")
            .prefetch_related(
                Prefetch(
                    lookup="role_set",
                    to_attr="patient_list",
                    queryset=models.Role.objects.select_related("person")
                    .prefetch_related(
                        Prefetch(
                            lookup="woman",
                            to_attr="woman_rec",
                            queryset=women_subquery,
                        )
                    )
                    .select_related("health_team")
                    .filter(
                        Q(
                            person__birth_date__gt=oldest,
                            person__birth_date__lte=youngest,
                        )
                        & Q(woman__isnull=False)
                        & Q(woman__patient_id__in=indicator_4_list)
                    )
                    .order_by("person__name")
                    .distinct(),
                )
            )
            .annotate(
                total_qty=Count(
                    "role__woman",
                    filter=Q(
                        role__person__birth_date__gt=oldest,
                        role__person__birth_date__lte=youngest,
                    ),
                    distinct=True,
                ),
                indicator_4_qty=Count(
                    "role__woman",
                    filter=Q(
                        role__person__birth_date__gt=oldest,
                        role__person__birth_date__lte=youngest,
                        role__woman__patient_id__in=indicator_4_list,
                    ),
                    distinct=True,
                ),
                indicator_4_percent=(F("indicator_4_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
            )
            .filter(
                role__person__birth_date__gt=oldest,
                role__person__birth_date__lte=youngest,
                role__woman__isnull=False,
                role__woman__patient_id__in=indicator_4_list,
            )
            .order_by("name")
            .distinct()
        )
    elif parameter == "not_achieved":
        show_summary = False
        queryset = (
            models.HealthUnit.objects.select_related("city")
            .prefetch_related(
                Prefetch(
                    lookup="role_set",
                    to_attr="patient_list",
                    queryset=models.Role.objects.select_related("person")
                    .prefetch_related(
                        Prefetch(
                            lookup="woman",
                            to_attr="woman_rec",
                            queryset=women_subquery,
                        )
                    )
                    .select_related("health_team")
                    .filter(
                        person__birth_date__gt=oldest,
                        person__birth_date__lte=youngest,
                        woman__isnull=False,
                    )
                    .exclude(
                        woman__patient_id__in=indicator_4_list,
                    )
                    .order_by("person__name")
                    .distinct(),
                )
            )
            .annotate(
                total_qty=Count(
                    "role__woman",
                    filter=Q(
                        role__person__birth_date__gt=oldest,
                        role__person__birth_date__lte=youngest,
                    ),
                    distinct=True,
                ),
                indicator_4_qty=Count(
                    "role__woman",
                    filter=Q(
                        role__person__birth_date__gt=oldest,
                        role__person__birth_date__lte=youngest,
                        role__woman__patient_id__in=indicator_4_list,
                    ),
                    distinct=True,
                ),
                indicator_4_percent=(F("indicator_4_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
            )
            .filter(
                role__person__birth_date__gt=oldest,
                role__person__birth_date__lte=youngest,
                role__woman__isnull=False,
                role__woman__patient_id__in=indicator_4_list,
            )
            .order_by("name")
            .distinct()
        )
    else:
        queryset = (
            models.HealthUnit.objects.select_related("city")
            .prefetch_related(
                Prefetch(
                    lookup="role_set",
                    to_attr="patient_list",
                    queryset=models.Role.objects.select_related("person")
                    .prefetch_related(
                        Prefetch(
                            lookup="woman",
                            to_attr="woman_rec",
                            queryset=women_subquery,
                        )
                    )
                    .select_related("health_team")
                    .filter(
                        person__birth_date__gt=oldest,
                        person__birth_date__lte=youngest,
                        woman__isnull=False,
                    )
                    .order_by("person__name")
                    .distinct(),
                )
            )
            .annotate(
                total_qty=Count(
                    "role__woman",
                    filter=Q(
                        role__person__birth_date__gt=oldest,
                        role__person__birth_date__lte=youngest,
                    ),
                    distinct=True,
                ),
                indicator_4_qty=Count(
                    "role__woman",
                    filter=Q(
                        role__person__birth_date__gt=oldest,
                        role__person__birth_date__lte=youngest,
                        role__woman__patient_id__in=indicator_4_list,
                    ),
                    distinct=True,
                ),
                indicator_4_percent=(F("indicator_4_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
            )
            .filter(
                role__person__birth_date__gt=oldest,
                role__person__birth_date__lte=youngest,
                role__woman__isnull=False,
            )
            .order_by("name")
            .distinct()
        )
    city = models.City.objects.get(name__iexact="caxias", state__iexact="ma")

    health_unit = request.GET.get("health_unit")

    if health_unit:
        queryset = queryset.filter(id=int(health_unit))

    context = {
        "obj": queryset,
        "city": city,
        "show_summary": show_summary,
        "quadrimester": {
            "quad": quadrimester.quad,
            "year": quadrimester.year,
        },
    }
    return render(request, template_name, context)


def woman_detail(request, pk):
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    obj = models.Woman.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by("id").last()
    procedures = obj.patient.patient_procedures.filter(
        procedure__procedure_code__in=models.Procedure.CYTOPATHOLOGICAL,
        date__gte=quadrimester.evaluation_end - relativedelta(months=36),
    ).order_by("-date")
    detail_data = {
        "obj": obj,
        "address": address,
        "procedures": procedures,
    }
    return render(request, "core/woman/woman_modal_partial.html", detail_data)


def print_woman_detail(request, pk):
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    obj = models.Woman.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by("id").last()
    procedures = obj.patient.patient_procedures.filter(
        procedure__procedure_code__in=models.Procedure.CYTOPATHOLOGICAL,
        date__gte=quadrimester.evaluation_end - relativedelta(months=36),
    ).order_by("-date")
    detail_data = {
        "obj": obj,
        "address": address,
        "procedures": procedures,
    }
    return render(request, "core/woman/woman_modal_print.html", detail_data)
