from django.contrib import admin

from indicadores_esus.core import models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'ibge_code', 'state', 'name'
    )
    search_fields = ('name', 'state', 'ibge_code')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('state', 'name')


@admin.register(models.HealthUnit)
class HealthUnitAdmin(admin.ModelAdmin):
    list_display = (
        'esus_code', 'name', 'neighborhood', 'city'
    )


@admin.register(models.HealthTeam)
class HealthTeamAdmin(admin.ModelAdmin):
    list_display = (
        'esus_code', 'name', 'ine', 'city'
    )


class AddressInline(admin.TabularInline):
    model = models.Address


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'name', '_cns', '_cpf'
    )
    search_fields = ('name','_cns', '_cpf')
    inlines = [
        AddressInline,
    ]


class AppointmentInline(admin.TabularInline):
    model = models.Appointment
    raw_id_fields = (
        'cbo', 'professional', 'city', 'health_unit', 'health_team', 'cids', 
        'ciaps'
    )
    extra = 0
    fk_name = 'patient'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('health_team', 'health_unit', 'professional', 'city', 'cbo')


class ProcedureInline(admin.TabularInline):
    model = models.PatientProcedure
    raw_id_fields = (
        'cbo', 'professional', 'health_unit', 'health_team', 'procedure', 
        'request_appointment', 'evaluate_appointment', 
    )
    extra = 0
    fk_name = 'patient'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('health_team', 'health_unit', 'professional', 'cbo')


class VaccinationInline(admin.TabularInline):
    model = models.Vaccination
    raw_id_fields = (
        'vaccine', 'dose', 'cbo', 'professional', 'health_unit', 'health_team',
    )
    extra = 0
    fk_name = 'patient'


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        'esus_code', 'person', 'health_team'
    )
    search_fields = ('esus_code', 'person__name', 'person___cns')
    raw_id_fields = (
        'person', 'health_team', 'health_unit', 'city'
    )
    inlines = (AppointmentInline, ProcedureInline, VaccinationInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('person', 'health_team', 'health_unit')


@admin.register(models.PatientIndicator)
class PatientIndicatorAdmin(admin.ModelAdmin):
    # list_display = (
    #     'patient', 'indicator', 'numerator'
    # )
    search_fields = ('person__name', )
    list_filter = ('indicator__indicator', 'indicator__type', 'numerator')


@admin.register(models.PregnantWoman)
class PregnantWomanAdmin(admin.ModelAdmin):
    search_fields = ('patient__person__name', )
    list_display = ('patient', 'dum', 'dpp')
    raw_id_fields = (
        'patient',
    )


@admin.register(models.Woman)
class WomanAdmin(admin.ModelAdmin):
    search_fields = ('patient__person__name', )
    list_display = ('patient', )
    raw_id_fields = (
        'patient',
    )


@admin.register(models.Child)
class ChildAdmin(admin.ModelAdmin):
    search_fields = ('patient__person__name', )
    list_display = ('patient', )
    raw_id_fields = (
        'patient',
    )


@admin.register(models.Hypertensive)
class HypertensiveAdmin(admin.ModelAdmin):
    search_fields = ('patient__person__name', )
    list_display = ('patient', )
    raw_id_fields = (
        'patient',
    )


@admin.register(models.Diabetic)
class DiabeticAdmin(admin.ModelAdmin):
    search_fields = ('patient__person__name', )
    list_display = ('patient', )
    raw_id_fields = (
        'patient',
    )


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient', 'appointment_type', 'date', 'health_unit', 'health_team'
    )
    list_filter = ('appointment_type', )
    search_fields = ('patient__person__name', )
    raw_id_fields = (
        'professional', 'patient', 'health_unit', 'health_team', 'city'
    )


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        
        return qs.select_related('health_unit', 'health_team', 'patient__person')


@admin.register(models.Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = (
        'procedure_code',
        'name'
    )
    search_fields = (
        'procedure_code',
        'name'
    ) 
    

@admin.register(models.PatientProcedure)
class PatientProcedureAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
    )
    search_fields = (
        'patient__person__name',
    )
    raw_id_fields = (
        'patient', 'request_appointment', 'evaluate_appointment', 
    )


@admin.register(models.Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = (
        'esus_id',
        'acronym',
        'name'
    )


@admin.register(models.Dose)
class DoseAdmin(admin.ModelAdmin):
    list_display = (
        'esus_id',
        'acronym',
        'name'
    )
