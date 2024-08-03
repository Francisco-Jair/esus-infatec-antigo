from django.contrib import admin

from indicadores_esus.indicator.models import IndicatorPattern,CalculatedIndicator


# class IndicatorDataInline(admin.TabularInline):
#     model = IndicatorData    


# @admin.register(Indicator)
# class IndicatorAdmin(admin.ModelAdmin):
#     list_display = (
#         'type', 'numerator', 'denominator', 'indicator', 'dt_init_evaluation',
#         'dt_end_evaluation', 'calculated_at', 'updated_at'
#     )
#     inlines = [
#         IndicatorDataInline,
#     ]


@admin.register(IndicatorPattern)
class IndicatorPatternAdmin(admin.ModelAdmin):
    list_display = (
        'type', 'parameter', 'goal', 'weight', 'year', 'estimated_denominator',
        'is_active'
    )


@admin.register(CalculatedIndicator)
class CalculatedIndicatorAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'type', 'calculated_at', 'status')
    list_filter = ('status', )
