import pandas as pd
from datetime import datetime, date
from django.db.models import Q
from indicadores_esus.core import models

city = models.City.objects.get(state='MA', name='Caxias')

def import_health_units(city):
    from indicadores_esus.esus.models import TbDimUnidadeSaude
    
    units = TbDimUnidadeSaude.objects.all()

    for u in units:
        ne = u.no_bairro if u.no_bairro else ''
        h = models.HealthUnit(
            esus_code=u.co_seq_dim_unidade_saude, cnes=u.nu_cnes, 
            name=u.no_unidade_saude, neighborhood=ne, city=city, street='', 
            number='', complement=''
        )
        h.save()


def import_health_teams(city):
    from indicadores_esus.esus.models import TbDimEquipe

    teams = TbDimEquipe.objects.all()

    for t in teams:
        h = models.HealthTeam(
            esus_code=t.co_seq_dim_equipe, ine=t.nu_ine, name=t.no_equipe.title(), 
            city=city
        )
        h.save()


def load_sus_pregnant_data():
    file_name = input('Insira o nome completo do arquivo a importar, com a extensão: ')
    df = pd.read_csv(file_name, sep=';', encoding='latin-1', header=8, skipfooter=5, engine='python')
    print(df)
    print(
        'Certifique-se que o cabeçalho e o rodapé do arquivo estão alinhados '
        'com os dados a serem importados e os formatos de CNS e CPF estão ' 
        'completos'
    )
    process = input('Deseja continuar? (S/N): ')
    if process.lower() == 'n':
        print('Saindo sem executar importação...')
        return
    df['CNS'] = df['CNS'].astype(str)
    df['CPF'] = df['CPF'].apply(lambda x: str(x).split('.')[0].zfill(11))
    df['CNES'] = df['CNES'].astype(str)
    df['INE'] = df['INE'].astype(str)
    cpf_list = [cpf for cpf in df['CPF'].values.tolist() if cpf.isdigit()]
    cns_list = [cns for cns in df['CNS'].values.tolist() if cns.isdigit()]
    print(f'Lista de CPFs: {cpf_list}')
    print(f'Lista de CNSs: {cns_list}')
    cnes_list = list(set([cnes for cnes in df['CNES'].values.tolist() if cnes.isdigit()]))
    ine_list = list(set([ine for ine in df['INE'].values.tolist() if ine.isdigit()]))

    pregnant_quad_total = models.PregnantWoman.objects.filter(
        dpp__gte=date(2023, 1, 1), dpp__lte=date(2023, 4, 30)
    ).order_by('dpp')
    
    print(f'{pregnant_quad_total.count()} gestantes no quadrimestre')

    pregnant_qs = models.PregnantWoman.objects.filter(
        Q(patient__person___cpf__in=cpf_list)
        | Q(patient__person___cns__in=cns_list)
    ).order_by('patient__person__name')
    print(f'{pregnant_qs.count()} gestantes encontradas na planilha')

    print(f'{pregnant_qs.filter(sus_registered=True).count()} gestantes com cadastro no SUS')

    for q in pregnant_qs:
        print(
            f'{q.patient.person.name} - DN {q.patient.person.birth_date} - '
            f'DUM {q.dum} - DPP {q.dpp}',
            end=' - '
        )
        
        if len(df.loc[df['CPF'] == q.patient.person.cpf]) > 0:
            row = df.loc[df['CPF'] == q.patient.person.cpf]
        elif len(df.loc[df['CNS'] == q.patient.person.cns]) > 0:
            row = df.loc[df['CNS'] == q.patient.person.cns]
        else:
            continue
        print('Registrada')
        q.dum = datetime.strptime(row['Inicio'].values[0], "%d/%m/%Y").date()
        q.dpp = datetime.strptime(row['Fim'].values[0], "%d/%m/%Y").date()
        health_unit = models.HealthUnit.objects.filter(cnes=row['CNES'].values[0]).first()
        health_team = models.HealthTeam.objects.filter(ine=row['INE'].values[0]).first()
        
        # print(row['CNES'].values[0], health_unit)
        # print(row['INE'].values[0], health_team)
        q.sus_registered = True
        if health_unit:
            q.patient.health_unit = health_unit
            # q.patient.save()
        if health_team:
            q.patient.health_team = health_team
            # q.patient.save()
        q.save()
