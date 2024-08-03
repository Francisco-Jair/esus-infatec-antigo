from django.contrib import admin
from indicadores_esus.esus.models import (
    TbFatCidadaoPec, TbFatCadIndividual, TbFatAtendimentoIndividual,
    TbCidadao
)


@admin.register(TbFatCidadaoPec)
class FatCidadaoPecAdmin(admin.ModelAdmin):
    list_display = ('co_seq_fat_cidadao_pec', 'co_cidadao', 'no_cidadao')
    search_fields = ['co_seq_fat_cidadao_pec']


@admin.register(TbFatCadIndividual)
class FatCadIndividualAdmin(admin.ModelAdmin):
    list_display = ('co_seq_fat_cad_individual', 'no_nome', 'st_gestante')
    fields = (
        'co_seq_fat_cad_individual', 'no_nome', 'st_gestante', 'nu_cpf_cidadao',
        'nu_cns', 'dt_nascimento', 'co_dim_cds_tipo_origem', 'co_fat_cidadao_pec'
    )
    search_fields = ['no_nome']


@admin.register(TbFatAtendimentoIndividual)
class FatAtendimentoIndividualAdmin(admin.ModelAdmin):
    list_display = (
        'co_seq_fat_atd_ind', 'nu_cns', 'nu_cpf_cidadao', 'co_dim_municipio',
        'dt_inicial_atendimento', 'dt_final_atendimento', 'co_dim_tempo_dum',
        'co_fat_cidadao_pec'
    )
    fields = (
        'co_seq_fat_atd_ind', 'co_dim_municipio', 'dt_inicial_atendimento',
        'dt_final_atendimento'
    )
    search_fields = ['co_seq_fat_atd_ind', 'nu_cns']


@admin.register(TbCidadao)
class CidadaoAdmin(admin.ModelAdmin):
    list_display = ('co_seq_cidadao', 'no_cidadao')
    fields = ('co_seq_cidadao', 'no_cidadao')
    search_fields = ['no_cidadao']
