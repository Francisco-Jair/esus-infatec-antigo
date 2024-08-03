from datetime import datetime

from django.db.models import Count, Exists, F, FloatField, OuterRef, Prefetch, Q
from django.db.models.functions import Cast
from django.shortcuts import render
from django.urls import reverse_lazy

from indicadores_esus.core import filters, models
from indicadores_esus.core.utils import paginate, which_quadrimester
from indicadores_esus.esus.managers import (
    pregnancy_complete_ciaps_list,
    pregnancy_complete_cids_list,
)


def pregnant_women_list(request):
    queryset = models.PregnantWoman.objects.get_pregnant_indicators_data()

    filter_obj = filters.PregnantWomanFilter(request.GET, queryset=queryset)
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)
    page_obj = paginate(filter_obj.qs, page_size, page)
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)
    on_quadrimester = filter_obj.qs.filter(
        dpp__range=(quadrimester.evaluation_start, quadrimester.evaluation_end)
    ).count()
    appointments = models.Appointment.objects.filter(
        patient=OuterRef("pk"),
        date__month=current_date.month,
        date__year=current_date.year,
    )
    no_appointments_on_current_month = (
        filter_obj.qs.annotate(appointment_present_month=Exists(appointments))
        .filter(appointment_present_month=False)
        .count()
    )

    total_objects = filter_obj.qs.count()

    indicator_1_achieved = filter_obj.qs.filter(indicator_1_achieved=True).count()
    indicator_2_achieved = filter_obj.qs.filter(indicator_2_achieved=True).count()
    indicator_3_achieved = filter_obj.qs.filter(indicator_3_achieved=True).count()

    indicator_summary = {
        "ind_1": indicator_1_achieved,
        "ind_1_percent": round(indicator_1_achieved / total_objects * 100, 2)
        if total_objects > 0
        else 0,
        "ind_2": indicator_2_achieved,
        "ind_2_percent": round(indicator_2_achieved / total_objects * 100, 2)
        if total_objects > 0
        else 0,
        "ind_3": indicator_3_achieved,
        "ind_3_percent": round(indicator_3_achieved / total_objects * 100, 2)
        if total_objects > 0
        else 0,
        "total": total_objects,
    }

    template_name = "core/pregnant_woman/pregnant_list.html"
    if "htmx" in request.path:
        template_name = "core/pregnant_woman/pregnant_partial.html"
    return render(
        request,
        template_name,
        {
            "page_obj": page_obj,
            "form": filter_obj.form,
            "filter_url": reverse_lazy("core:pregnant_list_htmx"),
            "htmx_target": "#pregnant_section",
            "on_quadrimester": on_quadrimester,
            "no_apponintments_on_month": no_appointments_on_current_month,
            "summary": indicator_summary,
        },
    )


def print_pregnant_woman_list(request):
    template_name = "core/pregnant_woman/print_pregnant.html"
    current_date = datetime.now().date()
    quadrimester = which_quadrimester(current_date)

    pregnant_subquery = models.PregnantWoman.objects.get_pregnant_indicators_data(
        start_date=quadrimester.evaluation_start, end_date=quadrimester.evaluation_end
    )

    indicator_1_list = pregnant_subquery.filter(indicator_1_achieved=True).values_list(
        "patient_id", flat=True
    )

    indicator_2_list = pregnant_subquery.filter(indicator_2_achieved=True).values_list(
        "patient_id", flat=True
    )

    indicator_3_list = pregnant_subquery.filter(indicator_3_achieved=True).values_list(
        "patient_id", flat=True
    )

    all_achieved_list = (
        list(indicator_1_list) + list(indicator_2_list) + list(indicator_3_list)
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
                            lookup="pregnantwoman",
                            to_attr="pregnant_rec",
                            queryset=pregnant_subquery,
                        )
                    )
                    .select_related("health_team")
                    .filter(
                        Q(
                            pregnantwoman__dpp__range=(
                                quadrimester.evaluation_start,
                                quadrimester.evaluation_end,
                            )
                        )
                        & Q(pregnantwoman__isnull=False)
                        & Q(pregnantwoman__patient_id__in=indicator_1_list)
                        & Q(pregnantwoman__patient_id__in=indicator_2_list)
                        & Q(pregnantwoman__patient_id__in=indicator_3_list)
                    )
                    .order_by("person__name")
                    .distinct(),
                )
            )
            .annotate(
                total_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                    ),
                    distinct=True,
                ),
                indicator_1_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_1_list,
                    ),
                    distinct=True,
                ),
                indicator_1_percent=(F("indicator_1_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
                indicator_2_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_2_list,
                    ),
                    distinct=True,
                ),
                indicator_2_percent=(F("indicator_2_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
                indicator_3_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_3_list,
                    ),
                    distinct=True,
                ),
                indicator_3_percent=(F("indicator_3_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
            )
            .filter(
                role__pregnantwoman__dpp__range=(
                    quadrimester.evaluation_start,
                    quadrimester.evaluation_end,
                ),
                role__pregnantwoman__isnull=False,
                role__pregnantwoman__patient_id__in=all_achieved_list,
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
                            lookup="pregnantwoman",
                            to_attr="pregnant_rec",
                            queryset=pregnant_subquery,
                        )
                    )
                    .select_related("health_team")
                    .filter(
                        pregnantwoman__dpp__range=(
                            quadrimester.evaluation_start,
                            quadrimester.evaluation_end,
                        ),
                        pregnantwoman__isnull=False,
                    )
                    .exclude(
                        Q(pregnantwoman__patient_id__in=indicator_1_list)
                        & Q(pregnantwoman__patient_id__in=indicator_2_list)
                        & Q(pregnantwoman__patient_id__in=indicator_3_list)
                    )
                    .order_by("person__name")
                    .distinct(),
                )
            )
            .annotate(
                total_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                    ),
                    distinct=True,
                ),
                indicator_1_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_1_list,
                    ),
                    distinct=True,
                ),
                indicator_1_percent=(F("indicator_1_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
                indicator_2_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_2_list,
                    ),
                    distinct=True,
                ),
                indicator_2_percent=(F("indicator_2_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
                indicator_3_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_3_list,
                    ),
                    distinct=True,
                ),
                indicator_3_percent=(F("indicator_3_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
            )
            .filter(
                role__pregnantwoman__dpp__range=(
                    quadrimester.evaluation_start,
                    quadrimester.evaluation_end,
                ),
                role__pregnantwoman__isnull=False,
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
                            lookup="pregnantwoman",
                            to_attr="pregnant_rec",
                            queryset=pregnant_subquery,
                        )
                    )
                    .select_related("health_team")
                    .filter(
                        pregnantwoman__dpp__range=(
                            quadrimester.evaluation_start,
                            quadrimester.evaluation_end,
                        ),
                        pregnantwoman__isnull=False,
                    )
                    .order_by("person__name")
                    .distinct(),
                )
            )
            .annotate(
                total_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                    ),
                    distinct=True,
                ),
                indicator_1_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_1_list,
                    ),
                    distinct=True,
                ),
                indicator_1_percent=(F("indicator_1_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
                indicator_2_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_2_list,
                    ),
                    distinct=True,
                ),
                indicator_2_percent=(F("indicator_2_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
                indicator_3_qty=Count(
                    "role__pregnantwoman",
                    filter=Q(
                        role__pregnantwoman__dpp__gte=quadrimester.evaluation_start,
                        role__pregnantwoman__dpp__lte=quadrimester.evaluation_end,
                        role__pregnantwoman__patient_id__in=indicator_3_list,
                    ),
                    distinct=True,
                ),
                indicator_3_percent=(F("indicator_3_qty") * 100)
                / Cast(F("total_qty"), output_field=FloatField()),
            )
            .filter(
                role__pregnantwoman__dpp__range=(
                    quadrimester.evaluation_start,
                    quadrimester.evaluation_end,
                ),
                role__pregnantwoman__isnull=False,
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


def pregnant_detail(request, pk):
    obj = models.PregnantWoman.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by("id").last()
    appointments = obj.patient.patient_appointments.all().order_by("-date")
    detail_data = {
        "obj": obj,
        "address": address,
        "medical_appointments": appointments.filter(
            Q(appointment_type="M")
            & Q(
                Q(cids__code__in=pregnancy_complete_cids_list)
                | Q(ciaps__code__in=pregnancy_complete_ciaps_list)
            )
        ),
        "dental_appointments": appointments.filter(appointment_type="O"),
        "procedures": obj.patient.patient_procedures.filter(
            procedure__procedure_code__in=(
                models.Procedure.HIV_QUICKTEST
                + models.Procedure.HIV_SOROLOGY
                + models.Procedure.SIFILIS_CODES
                + models.Procedure.SIFILIS_QUICKTEST
            )
        ),
    }
    return render(
        request, "core/pregnant_woman/pregnant_modal_partial.html", detail_data
    )


def print_pregnant_detail(request, pk):
    obj = models.PregnantWoman.objects.get(pk=pk)
    address = obj.patient.person.address_set.order_by("id").last()
    appointments = obj.patient.patient_appointments.all().order_by("-date")
    detail_data = {
        "obj": obj,
        "address": address,
        "medical_appointments": appointments.filter(
            Q(appointment_type="M")
            & Q(
                Q(cids__code__in=pregnancy_complete_cids_list)
                | Q(ciaps__code__in=pregnancy_complete_ciaps_list)
            )
        ),
        "dental_appointments": appointments.filter(appointment_type="O"),
        "procedures": obj.patient.patient_procedures.filter(
            procedure__procedure_code__in=(
                models.Procedure.HIV_QUICKTEST
                + models.Procedure.HIV_SOROLOGY
                + models.Procedure.SIFILIS_CODES
                + models.Procedure.SIFILIS_QUICKTEST
            )
        ),
    }
    return render(request, "core/pregnant_woman/pregnant_modal_print.html", detail_data)
