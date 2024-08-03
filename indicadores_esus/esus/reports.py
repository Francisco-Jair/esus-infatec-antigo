import datetime
import pandas as pd

from django.db.models import Prefetch, Count, Q
from indicadores_esus.esus.models import (
    TbFatCidadaoPec, TbFatAtendimentoIndividual, TbDimUnidadeSaude
)


def maiores_utilizadores():
    unidades = TbDimUnidadeSaude.objects.prefetch_related(
        Prefetch(
            lookup='tbfatatendimentoindividual_set',
            to_attr='atendimentos_list',
            queryset=TbFatAtendimentoIndividual.objects.filter(
                dt_final_atendimento__range=(
                    datetime.date(2022, 1, 1), datetime.date(2022, 12, 31)
                )
            )
        )
    ).annotate(
        qtd_consultas=Count(
            'tbfatatendimentoindividual', 
            filter=Q(
                tbfatatendimentoindividual__dt_final_atendimento__range=(
                    datetime.date(2022, 1, 1), datetime.datetime(2022, 12, 31)
                )
            ), 
            distinct=True
        )
    ).all()
    year = 2022

    for unidade in unidades:
        print(f'Iniciando {unidade.no_unidade_saude}')
        filtro_consultas = Q(
            atendimentos_pec__dt_final_atendimento__gte=datetime.date(2022, 1, 1),
            atendimentos_pec__dt_final_atendimento__lte=datetime.date(2022, 12, 31),
            atendimentos_pec__co_dim_unidade_saude_1=unidade
        )
        qs = TbFatCidadaoPec.objects.prefetch_related(
            Prefetch(
                lookup='atendimentos_pec',
                to_attr='atendimentos_list',
                queryset=TbFatAtendimentoIndividual.objects.filter(
                    dt_final_atendimento__gte=datetime.date(2022, 1, 1), 
                    dt_final_atendimento__lte=datetime.date(2022, 12, 31),
                    co_dim_unidade_saude_1=unidade
                )
            )
        ).annotate(
            qtd_consultas_2022_geral=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__gte=datetime.date(2022, 1, 1), 
                    atendimentos_pec__dt_final_atendimento__lte=datetime.date(2022, 12, 31),
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_janeiro=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=1,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_fevereiro=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=2,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_marco=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=3,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_abril=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=4,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ),
                distinct=True
            ),
            qtd_consultas_2022_maio=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=5,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_junho=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=6,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ),
                distinct=True
            ),
            qtd_consultas_2022_julho=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=7,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_agosto=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=8,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_setembro=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=9,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_outubro=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=10,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_novembro=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=11,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
            qtd_consultas_2022_dezembro=Count(
                'atendimentos_pec', 
                filter=Q(
                    atendimentos_pec__dt_final_atendimento__month=12,
                    atendimentos_pec__dt_final_atendimento__year=year,
                    atendimentos_pec__co_dim_unidade_saude_1=unidade
                ), 
                distinct=True
            ),
        ).filter(
            qtd_consultas_2022_geral__gt=0
        ).order_by(
            '-qtd_consultas_2022_geral'
        ).values(
            'no_cidadao',
            'nu_cns',
            'nu_cpf_cidadao',
            'qtd_consultas_2022_janeiro',
            'qtd_consultas_2022_fevereiro',
            'qtd_consultas_2022_marco',
            'qtd_consultas_2022_abril',
            'qtd_consultas_2022_maio',
            'qtd_consultas_2022_junho',
            'qtd_consultas_2022_julho',
            'qtd_consultas_2022_agosto',
            'qtd_consultas_2022_setembro',
            'qtd_consultas_2022_outubro',
            'qtd_consultas_2022_novembro',
            'qtd_consultas_2022_dezembro',
            'qtd_consultas_2022_geral'
        )

        df = pd.DataFrame(qs)
        df.to_excel(f'{unidade.no_unidade_saude.lower().replace(" ", "_")}.xlsx')
        print(f'Finalizado {unidade.no_unidade_saude}')

# atendimentos = TbFatAtendimentoIndividual.objects.filter(
#     dt_final_atendimento__range=(
#         datetime.date(2022, 1, 1), datetime.date(2022, 12, 31)
#     )
# ).select_related(
#     'co_fat_cidadao_pec',
#     'co_dim_unidade_saude_1'
# ).annotate(
#     qtd=Count(
#         'co_fat_cidadao_pec'
#     )
# ).order_by(
#     'dt_final_atendimento'
# ).values(
#     'co_fat_cidadao_pec__no_cidadao',
#     'co_fat_cidadao_pec__nu_cns',
#     'co_fat_cidadao_pec__nu_cpf_cidadao',
#     'co_dim_unidade_saude_1__no_unidade_saude',
#     'dt_inicial_atendimento',
#     'dt_final_atendimento',
#     'qtd'
# )

# atd_list = []
# for at in atendimentos:
#     atd_dict = {
#         'Nome': at['co_fat_cidadao_pec__no_cidadao'],
#         'CNS': at['co_fat_cidadao_pec__nu_cns'],
#         'CPF': at['co_fat_cidadao_pec__nu_cpf_cidadao'],
#         'Unidade de Saúde': at['co_dim_unidade_saude_1__no_unidade_saude'],
#         'Data': at['dt_final_atendimento'].strftime("%d/%m/%Y"),
#         'Quantidade': at['qtd']
#     }
#     atd_list.append(atd_dict)

# df = pd.DataFrame(atd_list)
# df.to_excel('pacientes.xlsx')