from django.db.models import Q


SQL_QUERY_EXAMPLE = '''SELECT ds_filtro_cids, ds_filtro_ciaps
FROM tb_fat_atendimento_individual
WHERE ds_filtro_cids LIKE '%|Z98|%';'''

from indicadores_esus.esus.models import TbFatAtendimentoIndividual, TbCdsAtendIndividual, TbCdsFichaAtendIndividual

gest = TbFatAtendimentoIndividual.objects.filter()

qcid = Q()
qciap = Q()
dtfim = f'{quad.dt_max_dum.year}{quad.dt_max_dum.month}{quad.dt_dt_max_dum.day}'
gest = TbFatAtendimentoIndividual.objects.filter(co_dim_tempo_dum__gte=dtini, co_dim_tempo_dum__lt=dtfim)

gest = TbFatAtendimentoIndividual.objects.filter(Q(co_dim_tempo_dum__gte=dtini) & Q(co_dim_tempo_dum__lt=dtfim) & Q(qciap))

gest = TbFatAtendimentoIndividual.objects.filter(
    Q(Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False))
    & Q(co_dim_tempo_dum__gte=dtini)
    & Q(co_dim_tempo_dum__lt=dtfim)
    & Q(qcid | qciap)
).distinct('nu_cns', 'nu_cpf_cidadao').order_by('nu_cns', 'nu_cpf_cidadao')


from indicadores_esus.core.utils import Quadrimester, set_date_to_int, set_int_to_date


quad = Quadrimester(year=2022, quad=1)
print(f'Quadrimestre {quad.abbrev}')
print(f'Data de início da extração: {quad.dt_ini_extracao}')
print(f'Data final da extração: {quad.dt_fim_extracao}')
print(f'Data de início da avaliação: {quad.dt_ini_avaliacao}')
print(f'Data final da avaliação: {quad.dt_fim_avaliacao}')

gest = Indicador1.objects.get_data(quad)

print(len(gest['numerador']))
print(len(gest['denominador']))
gest[0]

lista_gestantes = [g for g in gest if g['denominador']]

print(len(lista_gestantes))

lista_gestantes = [g for g in gest if g['numerador']]

print(len(lista_gestantes))

print(f"Numerador: {len(gest['numerador'])}")
print(f"Denominador: {len(gest['denominador'])}")
print(f"Indicador: {len(gest['numerador'])/len(gest['denominador'])*100}")