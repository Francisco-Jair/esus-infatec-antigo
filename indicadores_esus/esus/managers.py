import datetime

from dateutil.relativedelta import relativedelta
from django.apps import apps
from django.db import models
from django.db.models import Exists, OuterRef, Prefetch, Q

from indicadores_esus.core.utils import set_date_to_int

PREGNANCY_CIAPS = [
    '|W03|', '|W05|', '|W29|', '|W71|', '|W78|', '|W79|', '|W80|', '|W81|',
    '|W84|', '|W85|', '|ABP001|'
]

ABORTION_CIAPS = ['|W82|', '|W83|']

ABORTION_CIDS = ['|O02|', '|O03|', '|O05|', '|O06|', '|O04|', '|Z303|']

PREGNANCY_CIDS = [
    '|O11|', '|O120|', '|O121|', '|O122|', '|O13|', '|O140|', '|O141|',
    '|O149|', '|O150|', '|O151|', '|O159|', '|O16|', '|O200|', '|O208|',
    '|O209|', '|O210|', '|O211|', '|O212|', '|O218|', '|O219|', '|O220|',
    '|O221|', '|O222|', '|O223|', '|O224|', '|O225|', '|O228|', '|O229|',
    '|O230|', '|O231|', '|O232|', '|O233|', '|O234|', '|O235|', '|O239|',
    '|O299|', '|O300|', '|O301|', '|O302|', '|O308|', '|O309|', '|O311|',
    '|O312|', '|O318|', '|O320|', '|O321|', '|O322|', '|O323|', '|O324|',
    '|O325|', '|O326|', '|O328|', '|O329|', '|O330|', '|O331|', '|O332|',
    '|O333|', '|O334|', '|O335|', '|O336|', '|O337|', '|O338|', '|O752|',
    '|O753|', '|O990|', '|O991|', '|O992|', '|O993|', '|O994|', '|O240|',
    '|O241|', '|O242|', '|O243|', '|O244|', '|O249|', '|O25|', '|O260|',
    '|O261|', '|O263|', '|O264|', '|O265|', '|O268|', '|O269|', '|O280|',
    '|O281|', '|O282|', '|O283|', '|O284|', '|O285|', '|O288|', '|O289|',
    '|O290|', '|O291|', '|O292|', '|O293|', '|O294|', '|O295|', '|O296|',
    '|O298|', '|O009|', '|O339|', '|O340|', '|O341|', '|O342|', '|O343|',
    '|O344|', '|O345|', '|O346|', '|O347|', '|O348|', '|O349|', '|O350|',
    '|O351|', '|O352|', '|O353|', '|O354|', '|O355|', '|O356|', '|O357|',
    '|O358|', '|O359|', '|O360|', '|O361|', '|O362|', '|O363|', '|O365|',
    '|O366|', '|O367|', '|O368|', '|O369|', '|O40|', '|O410|', '|O411|',
    '|O418|', '|O419|', '|O430|', '|O431|', '|O438|', '|O439|', '|O440|',
    '|O441|', '|O460|', '|O468|', '|O469|', '|O470|', '|O471|', '|O479|',
    '|O48|', '|O995|', '|O996|', '|O997|', '|Z640|', '|O00|', '|O10|', '|O12|',
    '|O14|', '|O15|', '|O20|', '|O21|', '|O22|', '|O23|', '|O24|', '|O26|',
    '|O28|', '|O29|', '|O30|', '|O31|', '|O32|', '|O33|', '|O34|', '|O35|',
    '|O36|', '|O41|', '|O43|', '|O44|', '|O46|', '|O47|', '|O98|', '|Z34|',
    '|Z35|', '|Z36|', '|Z321|', '|Z33|', '|Z340|', '|Z340|', '|Z348|', '|Z349|',
    '|Z350|', '|Z351|', '|Z352|', '|Z353|', '|Z354|', '|Z357|', '|Z358|',
    '|Z359|'
]

CBO_MED_ENF = ['2251', '2252', '2253', '2231', '2235']

HYPERTENSE_CIAPS = ['K86', 'K87', 'ABP005']

HYPERTENSE_CIDS = [
    'I10', 'I11', 'I110', 'I119', 'I12', 'I120', 'I129', 'I13', 'I130', 'I131',
    'I132', 'I139', 'I15', 'I150', 'I151', 'I152', 'I158', 'I159', 'I270', 
    'I272', 'O10', 'O100', 'O101', 'O102', 'O103', 'O104', 'O109', 'O11'
]

DIABETIC_CIAPS = ['T89', 'T90', 'ABP006']

DIABETIC_CIDS = [
    'E10', 'E100', 'E101', 'E102', 'E103', 'E104', 'E105', 'E106', 'E107', 
    'E108', 'E109', 'E11', 'E110', 'E111', 'E112', 'E113', 'E114', 'E115', 
    'E116', 'E117', 'E118', 'E119', 'E12', 'E120', 'E121', 'E122', 'E123', 
    'E124', 'E125', 'E126', 'E127', 'E128', 'E129', 'E13', 'E130', 'E131', 
    'E132', 'E133', 'E134', 'E135', 'E136', 'E137', 'E138', 'E139', 'E14', 
    'E140', 'E141', 'E142', 'E143', 'E144', 'E145', 'E146', 'E147', 'E148',
    'E149', 'O240', 'O241', 'O242', 'O243', 'P702'
]

pregnancy_ciaps_list = [x.replace('|', '') for x in PREGNANCY_CIAPS]
pregnancy_cids_list = [x.replace('|', '') for x in PREGNANCY_CIDS]
abortion_ciaps_list = [x.replace('|', '') for x in ABORTION_CIAPS]
abortion_cids_list = [x.replace('|', '') for x in ABORTION_CIDS]

pregnancy_complete_ciaps_list = pregnancy_ciaps_list + abortion_ciaps_list
pregnancy_complete_cids_list = pregnancy_cids_list + abortion_cids_list

def get_pregnancy_cids_query():
    """
    Monta a consulta aos CIDs válidos para classificação da condição de gestante
    """
    qcid = Q()
    for cid in PREGNANCY_CIDS:
        qcid |= Q(ds_filtro_cids__icontains=cid)
    return qcid


def get_abortion_cids_query():
    """
    Monta a consulta aos CIDs para identificação de abortos
    """
    qcid = Q()
    for cid in ABORTION_CIDS:
        qcid |= Q(ds_filtro_cids__icontains=cid)
    return qcid


def get_pregnancy_ciaps_query():
    """
    Monta a consulta aos CIAPs válidos para classificação da condição de gestante
    """
    qciap = Q()
    for ciap in PREGNANCY_CIAPS:
        qciap |= Q(ds_filtro_ciaps__icontains=ciap)
    return qciap


def get_abortion_ciaps_query():
    """
    Monta a consulta aos CIAPs para identificação de abortos
    """
    qciap = Q()
    for ciap in ABORTION_CIAPS:
        qciap |= Q(ds_filtro_ciaps__icontains=ciap)
    return qciap


def get_pregnancy_cbos1_query():
    """
    Monta a consulta aos CBOs válidos para atendimento a gestante (campo CBO1)
    """
    qcbo1 = Q()
    for cbo in CBO_MED_ENF:
        qcbo1 |= Q(co_dim_cbo_1__nu_cbo__startswith=cbo)
    return qcbo1


def get_pregnancy_cbos2_query():
    """
    Monta a consulta aos CBOs válidos para atendimento a gestante (campo CBO2)
    """
    qcbo2 = Q()
    for cbo in CBO_MED_ENF:
        qcbo2 |= Q(co_dim_cbo_2__nu_cbo__startswith=cbo)
    return qcbo2


def fatatdind_model():
    return apps.get_model(
        app_label='esus', 
        model_name='TbFatAtendimentoIndividual'
    )


def fatatdindprob_model():
    return apps.get_model(
        app_label='esus', 
        model_name='TbFatAtdIndProblemas'
    )


def fatatdindproced_model():
    return apps.get_model(
        app_label='esus', 
        model_name='TbFatAtdIndProcedimentos'
    )


def fatatdindexame_model():
    return apps.get_model(
        app_label='esus', 
        model_name='TbFatAtdIndExames'
    )


def fatatdodonto_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbFatAtendimentoOdonto'
    )


def fatatdodntprob_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbFatAtendOdontoProblemas'
    )


def dimcbo_model(): 
    return apps.get_model(
        app_label='esus', 
        model_name='TbDimCbo'
    )


def dimproced_model():
    return apps.get_model(
        app_label='esus', 
        model_name='TbDimProcedimento'
    )


def fatcadind_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbFatCadIndividual'
    )


def equipe_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbEquipe'
    )


def dimequipe_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbDimEquipe'
    )


def fatatdproced_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbFatProcedAtendProced'
    )


def fatvacinacao_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbFatVacinacao'
    )


def fatvacinacaovacina_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbFatVacinacaoVacina'
    )


def dimimunobiologico_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbDimImunobiologico'
    )


def registro_vacinacao_model():
    return apps.get_model(
        app_label='esus',
        model_name='TbRegistroVacinacao'
    )


def cbos_list():
    return dimcbo_model().objects.doctors_and_nurses(
    ).values_list(
        'co_seq_dim_cbo', flat=True
    )


def cbo_assistant_list(): 
    return dimcbo_model().objects.assistant_nurses(
    ).values_list(
        'co_seq_dim_cbo', flat=True
    )


def cbo_complete_list():
    return list(cbos_list()) + list(cbo_assistant_list())


def cbo_dentist_list():
    return dimcbo_model().objects.dentists(
    ).values_list(
        'co_seq_dim_cbo', flat=True
    )


def quick_test_list():
    return dimproced_model().objects.hiv_sifilis_quick_test(
    ).values_list(
        'co_seq_dim_procedimento', flat=True
    )

def sorology_list():
    return dimproced_model().objects.hiv_sifilis_sorology(
    ).values_list(
        'co_seq_dim_procedimento', flat=True
    )

def cytopathological_list():
    return dimproced_model().objects.cytopathological_collection(
    ).values_list(
        'co_seq_dim_procedimento', flat=True
    )


def valid_teams_list():
    return dimequipe_model().objects.valid_teams(
    ).values_list(
        'co_seq_dim_equipe', flat=True
    )


def immunobiological_list():
    return dimimunobiologico_model().objects.for_children(
    ).values_list('co_seq_dim_imunobiologico', flat=True)


def blood_pressure_measure_list():
    return dimproced_model().objects.blood_pressure_measure(
    ).values_list(
        'co_seq_dim_procedimento', flat=True
    )


def glycated_hemoglobin_list():
    return dimproced_model().objects.glycated_hemoglobin(
    ).values_list(
        'co_seq_dim_procedimento', flat=True
    )


class DimCboQueryset(models.QuerySet):    
            
    def doctors_and_nurses(self):
        qs = self.filter(
            Q(nu_cbo__startswith='2251')
            | Q(nu_cbo__startswith='2252')
            | Q(nu_cbo__startswith='2253')
            | Q(nu_cbo__startswith='2231')
            | Q(nu_cbo__startswith='2235')
        )
        return qs

    def assistant_nurses(self):
        qs = self.filter(
            nu_cbo__startswith='3222'
        )
        return qs

    def dentists(self):
        qs = self.filter(
            nu_cbo__startswith='2232'
        )
        return qs


class DimProcedimentoQueryset(models.QuerySet):

    def hiv_sifilis_quick_test(self):
        qs = self.filter(
            co_proced__in=[
                '0214010040',
                '0214010058',
                '0214010074',
                '0214010082',
                'ABPG024',
                'ABPG026'
            ]
        )
        return qs
    
    def hiv_sifilis_sorology(self):
        qs = self.filter(
            co_proced__in=[
                '0202031110',
                '0202030300',
                '0202031179',
                'ABEX018',
                'ABEX019'
            ]
        )
        return qs

    def cytopathological_collection(self):
        qs = self.filter(
            co_proced__in=[
                '0201020033',
                'ABPG010'
            ]
        )
        return qs

    def blood_pressure_measure(self):
        qs = self.filter(
            co_proced__in=[
                '0301100039',
                'ABPG033'
            ]
        )
        return qs

    def glycated_hemoglobin(self):
        qs = self.filter(
            co_proced__in=[
                '0202010503',
                'ABEX008'
            ]
        )
        return qs

class EquipeQueryset(models.QuerySet):

    def valid_teams(self):
        qs = self.filter(
            tp_equipe__nu_ms__in=['70', '76']
        )
        return qs


class DimEquipeQueryset(models.QuerySet):

    def valid_teams(self):
        team_list = equipe_model().objects.valid_teams(
        ).values_list('nu_ine', flat=True)
        
        qs = self.filter(
            nu_ine__in=team_list
        )
        return qs


class DimImunobiologicoQueryset(models.QuerySet):

    def for_children(self):
        qs = self.filter(
            nu_identificador__in=[
                '09', '17', '22', '29', '39', '42', '43', '46'
            ]
        )
        return qs


class FatCidadaoPecQueryset(models.QuerySet):

    def complete_data(self):
        qs = self.prefetch_related(
            # TODAS AS CONSULTAS MÉDICAS
            Prefetch(
                lookup='atendimentos_pec',
                to_attr='all_medical_appointments_list',
                queryset=fatatdind_model().objects.prefetch_related(
                    # TODOS OS PROBLEMAS/CONDIÇÕES AVALIADOS NA CONSULTA
                    Prefetch(
                        lookup='atd_ind_problemas_set',
                        to_attr='all_conditions_list',
                        queryset=fatatdindprob_model().objects.select_related(
                            'co_dim_cid', 'co_dim_ciap'
                        ).order_by(
                            'co_seq_fat_atend_ind_problemas'
                        )
                    ),
                    # TODOS OS PROCEDIMENTOS SOLICITADOS/AVALIADOS NA CONSULTA MÉDICA
                    Prefetch(
                        lookup='atdindprocedimentos_set',
                        to_attr='all_procedures_list',
                        queryset=fatatdindproced_model().objects.select_related(
                            'co_dim_tempo', 'co_dim_procedimento_avaliado',
                            'co_dim_procedimento_solicitado',
                            'co_dim_profissional_1', 'co_dim_cbo_1', 
                            'co_dim_unidade_saude_1', 'co_dim_equipe_1'
                        ).order_by(
                            'co_dim_tempo'
                        )
                    ),
                    # TODOS OS EXAMES REGITRADOS NA CONSULTA MÉDICA
                    Prefetch(
                        lookup='atdind_exames_set',
                        to_attr='all_exams_list',
                        queryset=fatatdindexame_model().objects.select_related(
                            'co_dim_tempo', 'co_dim_profissional_1', 
                            'co_dim_cbo_1', 'co_dim_unidade_saude_1', 
                            'co_dim_equipe_1'
                        ).order_by(
                            'co_dim_tempo'
                        )
                    ),
                ).select_related(
                    'co_dim_tempo', 'co_dim_municipio', 'co_dim_profissional_1',
                    'co_dim_cbo_1', 'co_dim_unidade_saude_1', 'co_dim_equipe_1'
                ).order_by(
                    'co_dim_tempo'
                )
            ),
            # TODAS AS CONSULTAS ODONTOLÓGICAS
            Prefetch(
                lookup='atendimentos_odontos_pec',
                to_attr='all_dental_appointments_list',
                queryset=fatatdodonto_model().objects.select_related(
                    'co_dim_tempo', 'co_dim_municipio', 'co_dim_profissional_1',
                    'co_dim_cbo_1', 'co_dim_unidade_saude_1', 'co_dim_equipe_1'
                ).order_by(
                    'co_dim_tempo'
                )
            ),
            # TODOS OS REGISTROS DE CADASTROS INDIVIDUAIS
            Prefetch(
                lookup='cidadao_pec_set',
                to_attr='all_individual_registers_list',
                queryset=fatcadind_model().objects.select_related(
                    'co_dim_municipio'
                ).order_by(
                    'co_dim_tempo'
                )
            ),
            # TODOS OS PROCEDIMENTOS
            Prefetch(
                lookup='cidadao_atend_proced_set',
                to_attr='all_procedures_list',
                queryset=fatatdproced_model().objects.select_related(
                    'co_dim_cbo', 'co_dim_procedimento', 'co_dim_tempo',
                    'co_dim_profissional', 'co_dim_unidade_saude', 
                    'co_dim_equipe'
                ).order_by(
                    'co_dim_tempo'
                )
            ),
            # TODAS AS VACINAÇÕES
            Prefetch(
                lookup='cidadao_vacinacao_set',
                to_attr='all_vaccinations_list',
                queryset=fatvacinacao_model().objects.prefetch_related(
                    # TODAS AS VACINAS
                    Prefetch(
                        lookup='vacina_vacinacao_set',
                        to_attr='all_vaccines_list',
                        queryset=fatvacinacaovacina_model().objects.select_related(
                            'co_dim_imunobiologico', 
                            'co_dim_tempo', 
                            'co_dim_dose_imunobiologico'
                            'co_dim_cbo',
                            'co_dim_profissional', 
                            'co_dim_unidade_saude', 
                            'co_dim_equipe'
                        )
                    )
                )
            ),
        ).filter(
            Q(
                Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False)
            )
        ).select_related(
            'co_dim_unidade_saude_vinc', 'co_dim_equipe_vinc'
        ).order_by(
            'nu_cns', 'nu_cpf_cidadao'
        )

        return qs

    def pregnant_women(self, quad=None):
        
        if quad is None:
            extraction_start = datetime.datetime.now().date() - relativedelta(months=9)
            extraction_end = datetime.datetime.now().date()
        else: 
            extraction_start = quad.extraction_start
            extraction_end = quad.extraction_end

        qs = self.prefetch_related(
            Prefetch(
                lookup='atendimentos_pec',
                to_attr='appointments',
                queryset=fatatdind_model().objects.filter(
                    Q(Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False))
                    & Q(co_dim_sexo=2)
                    & Q(co_dim_tempo__gte=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(
                        Q(co_dim_cbo_1_id__in=cbos_list()) 
                        | Q(co_dim_cbo_2_id__in=cbos_list())
                    )
                    & Q(
                        Exists(
                            fatatdindprob_model().objects.filter(
                                Q(co_fat_atd_ind=OuterRef('co_seq_fat_atd_ind'))
                                & Q(
                                    Q(co_dim_ciap__nu_ciap__in=pregnancy_complete_ciaps_list) 
                                    | Q(co_dim_cid__nu_cid__in=pregnancy_complete_cids_list)
                                )
                            )
                        )
                    )        
                ).prefetch_related(
                    Prefetch(
                        lookup='atd_ind_problemas_set',
                        to_attr='pregnancy_condition',
                        queryset = fatatdindprob_model().objects.filter(
                            Q(
                                Q(co_dim_ciap__nu_ciap__in=pregnancy_ciaps_list) 
                                | Q(co_dim_cid__nu_cid__in=pregnancy_cids_list)
                            )
                        ).select_related(
                            'co_dim_cid', 'co_dim_ciap'
                        ).order_by(
                            'co_seq_fat_atend_ind_problemas'
                        ).distinct()
                    ),
                    Prefetch(
                        lookup='atd_ind_problemas_set',
                        to_attr='abortion_condition',
                        queryset = fatatdindprob_model().objects.filter(
                            Q(
                                Q(co_dim_ciap__nu_ciap__in=abortion_ciaps_list) 
                                | Q(co_dim_cid__nu_cid__in=abortion_cids_list)
                            )
                        ).select_related(
                            'co_dim_cid', 'co_dim_ciap'
                        ).order_by(
                            'co_seq_fat_atend_ind_problemas'
                        ).distinct()
                    ),
                    Prefetch(
                        lookup='atdindprocedimentos_set',
                        to_attr='hiv_sifilis_evaluated_procedures',
                        queryset=fatatdindproced_model().objects.filter(
                            Q(
                                Q(co_dim_procedimento_avaliado_id__in=sorology_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbos_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbos_list())
                                )   
                            )
                            | Q(
                                Q(co_dim_procedimento_avaliado_id__in=quick_test_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbo_complete_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbo_complete_list())
                                )
                            )    
                        ).select_related(
                            'co_dim_tempo', 'co_dim_profissional_1', 
                            'co_dim_cbo_1', 'co_dim_unidade_saude_1', 
                            'co_dim_equipe_1'
                        ).distinct()
                    ),
                    Prefetch(
                        lookup='atdindprocedimentos_set',
                        to_attr='hiv_sifilis_requested_procedures',
                        queryset=fatatdindproced_model().objects.filter(
                            Q(
                                Q(co_dim_procedimento_solicitado_id__in=sorology_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbos_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbos_list())
                                )   
                            )
                            | Q(
                                Q(co_dim_procedimento_solicitado_id__in=quick_test_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbo_complete_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbo_complete_list())
                                )
                            )    
                        ).select_related(
                            'co_dim_tempo', 'co_dim_profissional_1', 
                            'co_dim_cbo_1', 'co_dim_unidade_saude_1', 
                            'co_dim_equipe_1'
                        ).distinct()
                    )
                ).select_related(
                    'co_dim_tempo', 'co_dim_municipio', 'co_dim_profissional_1',
                    'co_dim_cbo_1'
                ).order_by(
                    'co_dim_tempo'
                ).distinct()
            ),
            Prefetch(
                lookup='atendimentos_odontos_pec',
                to_attr='dental_appointments',
                queryset=fatatdodonto_model().objects.filter(
                    Q(co_dim_tempo__gte=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(
                        Q(co_dim_cbo_1_id__in=cbo_dentist_list()) 
                        | Q(co_dim_cbo_2_id__in=cbo_dentist_list())
                    )
                ).prefetch_related(
                    Prefetch(
                        lookup='atd_odnt_problemas_set',
                        to_attr='conditions_list',
                        queryset=fatatdodntprob_model().objects.select_related(
                            'co_dim_cid', 'co_dim_ciap'
                        ).order_by(
                            'co_seq_fat_atnd_odonto_probl'
                        ).distinct()
                    ),
                ).select_related(
                    'co_dim_tempo', 'co_dim_municipio', 'co_dim_profissional_1',
                    'co_dim_cbo_1'
                ).order_by(
                    'co_dim_tempo'
                ).distinct()
            ),
            Prefetch(
                lookup='cidadao_pec_set',
                to_attr='individual_registers',
                queryset=fatcadind_model().objects.all(
                ).select_related(
                    'co_dim_municipio'
                ).order_by('co_dim_tempo_id').distinct()
            ),
            Prefetch(
                lookup='cidadao_atend_proced_set',
                to_attr='all_procedures',
                queryset=fatatdproced_model().objects.filter(
                    co_dim_tempo__gte=set_date_to_int(extraction_start),
                    co_dim_tempo__lte=set_date_to_int(extraction_end)
                ).select_related(
                    'co_dim_cbo', 'co_dim_procedimento', 'co_dim_tempo',
                    'co_dim_profissional', 'co_dim_unidade_saude', 
                    'co_dim_equipe'
                ).distinct()
            ),
        ).filter(
            Q(
                Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False)
            )
            & Q(
                Exists(
                    fatatdind_model().objects.filter(
                        Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                        & Q(Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False))
                        & Q(co_dim_sexo=2)
                        & Q(co_dim_tempo__gte=set_date_to_int(extraction_start))
                        & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                        & Q(
                            Q(co_dim_cbo_1_id__in=cbos_list()) 
                            | Q(co_dim_cbo_2_id__in=cbos_list())
                        )
                        & Q(
                            Exists(
                                fatatdindprob_model().objects.filter(
                                    Q(co_fat_atd_ind=OuterRef('co_seq_fat_atd_ind'))
                                    & Q(
                                        Q(co_dim_ciap__nu_ciap__in=pregnancy_complete_ciaps_list) 
                                        | Q(co_dim_cid__nu_cid__in=pregnancy_complete_cids_list)
                                    )
                                )
                            )
                        )        
                    )
                )
            )
            & Q(co_dim_sexo=2)
        ).select_related(
            'co_dim_unidade_saude_vinc', 'co_dim_equipe_vinc'
        ).distinct(
            'nu_cns', 'nu_cpf_cidadao'
        ).order_by(
            'nu_cns', 'nu_cpf_cidadao'
        )

        return qs

    def women(self, quad=None):
        
        if quad is None:
            min_birth_date = datetime.datetime.now().date() - relativedelta(years=65)
            max_birth_date = datetime.datetime.now().date() - relativedelta(years=25)
            extraction_start = datetime.datetime.now().date() - relativedelta(months=36)
            extraction_end = datetime.datetime.now().date()
        else:
            min_birth_date = quad.evaluation_end - relativedelta(years=65)
            max_birth_date = quad.evaluation_end - relativedelta(years=25) 
            extraction_start = quad.evaluation_end - relativedelta(months=36)
            extraction_end = quad.extraction_end

        qs = self.prefetch_related(
            Prefetch(
                lookup='cidadao_procedimentos_set',
                to_attr='cytopathological_procedures_1',
                queryset=fatatdindproced_model().objects.filter(
                    Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(
                        Q(co_dim_procedimento_avaliado_id__in=cytopathological_list())
                        | Q(co_dim_procedimento_solicitado_id__in=cytopathological_list())
                    )
                    & Q(
                        Q(co_dim_cbo_1_id__in=cbos_list())
                        | Q(co_dim_cbo_2_id__in=cbos_list())
                    )
                )
            ),
            Prefetch(
                lookup='cidadao_atend_proced_set',
                to_attr='cytopathological_procedures_2',
                queryset=fatatdproced_model().objects.filter(
                    Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(co_dim_procedimento_id__in=cytopathological_list())
                    & Q(co_dim_cbo__in=cbos_list()) 
                )
            ),
            Prefetch(
                lookup='cidadao_pec_set',
                to_attr='individual_registers',
                queryset=fatcadind_model().objects.all(
                ).select_related(
                    'co_dim_municipio'
                )
            )                    
        ).filter(
            Q(
                Exists(
                    fatcadind_model().objects.filter(
                        Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                        & Q(
                            Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False)
                        )
                        & ~Q(co_dim_tipo_saida_cadastro_id__in=[1, 2])
                        & Q(co_dim_sexo=2)
                        & Q(dt_nascimento__gt=min_birth_date)
                        & Q(dt_nascimento__lte=max_birth_date)
                        & Q(co_dim_equipe_id__in=valid_teams_list())
                    )
                )
            )
            & Q(co_dim_sexo=2) 
        ).select_related(
            'co_dim_unidade_saude_vinc', 'co_dim_equipe_vinc'
        ).distinct(
            'nu_cns', 'nu_cpf_cidadao'
        ).order_by(
            'nu_cns', 'nu_cpf_cidadao'
        )

        return qs    


    def children(self, quad=None):

        if quad is None:
            min_birth_date = datetime.datetime.now().date() - relativedelta(months=24)
            max_birth_date = datetime.datetime.now().date() - relativedelta(months=12)
        else:
            min_birth_date = quad.evaluation_start - relativedelta(months=12)
            max_birth_date = quad.evaluation_end - relativedelta(months=12) 

        print(min_birth_date)
        print(max_birth_date)

        qs = self.prefetch_related(
            Prefetch(
                lookup='cidadao_vacinacao_set',
                to_attr='vaccinations',
                queryset=fatvacinacao_model().objects.prefetch_related(
                    Prefetch(
                        lookup='vacina_vacinacao_set',
                        to_attr='all_vaccines',
                        queryset=fatvacinacaovacina_model().objects.all().select_related(
                            'co_dim_imunobiologico', 
                            'co_dim_tempo', 
                            'co_dim_dose_imunobiologico'
                        )
                    ),
                    Prefetch(
                        lookup='vacina_vacinacao_set',
                        to_attr='vaccines',
                        queryset=fatvacinacaovacina_model().objects.filter(
                            co_dim_imunobiologico_id__in=immunobiological_list()
                        ).select_related(
                            'co_dim_imunobiologico'
                        )
                    ),
                    Prefetch(
                        lookup='vacina_vacinacao_set',
                        to_attr='vip_pentac',
                        queryset=fatvacinacaovacina_model().objects.filter(
                            co_dim_imunobiologico__nu_identificador__in=['22', '42'],
                            co_dim_dose_imunobiologico__nu_identificador='3'
                        ).select_related(
                            'co_dim_imunobiologico',
                            'co_dim_dose_imunobiologico',
                        )
                    ),
                    Prefetch(
                        lookup='vacina_vacinacao_set',
                        to_attr='hexa',
                        queryset=fatvacinacaovacina_model().objects.filter(
                            co_dim_imunobiologico__nu_identificador='43',
                            co_dim_dose_imunobiologico__nu_identificador='3'
                        ).select_related(
                            'co_dim_imunobiologico',
                            'co_dim_dose_imunobiologico',
                        )
                    ),
                    Prefetch(
                        lookup='vacina_vacinacao_set',
                        to_attr='pentaa_hep',
                        queryset=fatvacinacaovacina_model().objects.filter(
                            co_dim_imunobiologico__nu_identificador__in=['9', '29'],
                            co_dim_dose_imunobiologico__nu_identificador='3'
                        ).select_related(
                            'co_dim_imunobiologico',
                            'co_dim_dose_imunobiologico',
                        )
                    )
                )
            ),
            Prefetch(
                lookup='cidadao_pec_set',
                to_attr='individual_registers',
                queryset=fatcadind_model().objects.all(
                ).select_related(
                    'co_dim_municipio'
                )
            )
        ).filter(
            Q(
                Exists(
                    fatcadind_model().objects.filter(
                        Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                        & Q(
                            Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False)
                        )
                        & ~Q(co_dim_tipo_saida_cadastro_id__in=[1, 2])
                        & Q(dt_nascimento__gte=min_birth_date)
                        & Q(dt_nascimento__lte=max_birth_date)
                        & Q(co_dim_equipe_id__in=valid_teams_list())
                    )
                )
            )
        ).select_related(
            'co_dim_unidade_saude_vinc', 'co_dim_equipe_vinc'
        ).distinct(
            'nu_cns', 'nu_cpf_cidadao'
        ).order_by(
            'nu_cns', 'nu_cpf_cidadao'
        )

        return qs
    
    def hypertensives(self, quad=None):
        if quad is None:
            extraction_start = datetime.datetime.now().date() - relativedelta(months=6)
            extraction_end = datetime.datetime.now().date()
        else:
            # TODO: Corrigir dia do início da extração.
            extraction_start = quad.evaluation_end - relativedelta(months=6)
            extraction_end = quad.extraction_end

        qs = self.prefetch_related(
            Prefetch(
                lookup='atendimentos_pec',
                to_attr='appointments',
                queryset=fatatdind_model().objects.filter(
                    Q(Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False))
                    & Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(
                        Q(co_dim_cbo_1_id__in=cbos_list()) 
                        | Q(co_dim_cbo_2_id__in=cbos_list())
                    )
                    & Q(
                        Exists(
                            fatatdindprob_model().objects.filter(
                                Q(co_fat_atd_ind=OuterRef('co_seq_fat_atd_ind'))
                                & Q(
                                    Q(co_dim_ciap__nu_ciap__in=HYPERTENSE_CIAPS) 
                                    | Q(co_dim_cid__nu_cid__in=HYPERTENSE_CIDS)
                                )
                            )
                        )
                    )
                ).prefetch_related(
                    Prefetch(
                        lookup='atdindprocedimentos_set',
                        to_attr='blood_pressure_measure_evaluated_procedures',
                        queryset=fatatdindproced_model().objects.filter(
                            Q(
                                Q(co_dim_procedimento_avaliado_id__in=blood_pressure_measure_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbos_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbos_list())
                                )   
                            )
                            | Q(
                                Q(co_dim_procedimento_avaliado_id__in=blood_pressure_measure_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbo_complete_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbo_complete_list())
                                )
                            )    
                        ).select_related(
                            'co_dim_tempo'
                        )
                    ),
                    Prefetch(
                        lookup='atdindprocedimentos_set',
                        to_attr='blood_pressure_measure_requested_procedures',
                        queryset=fatatdindproced_model().objects.filter(
                            Q(
                                Q(co_dim_procedimento_solicitado_id__in=blood_pressure_measure_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbos_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbos_list())
                                )   
                            )
                            | Q(
                                Q(co_dim_procedimento_solicitado_id__in=blood_pressure_measure_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbo_complete_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbo_complete_list())
                                )
                            )    
                        ).select_related(
                            'co_dim_tempo'
                        )
                    ),
                    Prefetch(
                        lookup='atd_ind_problemas_set',
                        to_attr='hypertensive_condition',
                        queryset = fatatdindprob_model().objects.filter(
                            Q(
                                Q(co_dim_ciap__nu_ciap__in=HYPERTENSE_CIAPS) 
                                | Q(co_dim_cid__nu_cid__in=HYPERTENSE_CIDS)
                            )
                        ).select_related(
                            'co_dim_cid', 'co_dim_ciap'
                        ).order_by(
                            'co_seq_fat_atend_ind_problemas'
                        ).distinct()
                    ),
                ).select_related(
                    'co_dim_tempo', 'co_dim_municipio', 
                )
            ),
            Prefetch(
                lookup='cidadao_procedimentos_set',
                to_attr='pressure_measure_1',
                queryset=fatatdindproced_model().objects.filter(
                    Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(
                        Q(co_dim_procedimento_avaliado_id__in=blood_pressure_measure_list())
                        | Q(co_dim_procedimento_solicitado_id__in=blood_pressure_measure_list())
                    )
                    & Q(
                        Q(co_dim_cbo_1_id__in=cbo_complete_list())
                        | Q(co_dim_cbo_2_id__in=cbo_complete_list())
                    )
                )
            ),
            Prefetch(
                lookup='cidadao_atend_proced_set',
                to_attr='pressure_measure_2',
                queryset=fatatdproced_model().objects.filter(
                    Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(co_dim_procedimento_id__in=blood_pressure_measure_list())
                    & Q(co_dim_cbo__in=cbo_complete_list()) 
                )
            ),
            Prefetch(
                lookup='cidadao_pec_set',
                to_attr='individual_registers',
                queryset=fatcadind_model().objects.all(
                ).select_related(
                    'co_dim_municipio'
                )
            )
        ).filter(
            Q(
                Exists(
                    fatcadind_model().objects.filter(
                        Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                        & Q(
                            Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False)
                        )
                        & ~Q(co_dim_tipo_saida_cadastro_id__in=[1, 2])
                        & Q(co_dim_equipe_id__in=valid_teams_list())
                    )
                )
            )
            & Q(
                Q(
                    Exists(
                        fatcadind_model().objects.filter(
                            Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                            & Q(st_hipertensao_arterial=1)
                        )
                    )
                )
                | Q(
                    Exists(
                        fatatdind_model().objects.filter(
                            Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                            & Q(Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False))
                            & Q(
                                Q(co_dim_cbo_1_id__in=cbos_list()) 
                                | Q(co_dim_cbo_2_id__in=cbos_list())
                            )
                            & Q(
                                Exists(
                                    fatatdindprob_model().objects.filter(
                                        Q(co_fat_atd_ind=OuterRef('co_seq_fat_atd_ind'))
                                        & Q(
                                            Q(co_dim_ciap__nu_ciap__in=HYPERTENSE_CIAPS) 
                                            | Q(co_dim_cid__nu_cid__in=HYPERTENSE_CIDS)
                                        )
                                    )
                                )
                            )        
                        )
                    )
                )
            )  
        ).select_related(
            'co_dim_unidade_saude_vinc', 'co_dim_equipe_vinc'
        ).distinct(
            'nu_cns', 'nu_cpf_cidadao'
        ).order_by(
            'nu_cns', 'nu_cpf_cidadao'
        )

        return qs

    def diabetics(self, quad=None):
        if quad is None:
            extraction_start = datetime.datetime.now().date() - relativedelta(months=6)
            extraction_end = datetime.datetime.now().date()
        else:
            # TODO: Corrigir dia do início da extração.
            extraction_start = quad.evaluation_end - relativedelta(months=6)
            extraction_end = quad.extraction_end

        qs = self.prefetch_related(
            Prefetch(
                lookup='atendimentos_pec',
                to_attr='appointments',
                queryset=fatatdind_model().objects.filter(
                    Q(Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False))
                    & Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(
                        Q(co_dim_cbo_1_id__in=cbos_list()) 
                        | Q(co_dim_cbo_2_id__in=cbos_list())
                    )
                    & Q(
                        Exists(
                            fatatdindprob_model().objects.filter(
                                Q(co_fat_atd_ind=OuterRef('co_seq_fat_atd_ind'))
                                & Q(
                                    Q(co_dim_ciap__nu_ciap__in=DIABETIC_CIAPS) 
                                    | Q(co_dim_cid__nu_cid__in=DIABETIC_CIDS)
                                )
                            )
                        )
                    )
                ).prefetch_related(
                    Prefetch(
                        lookup='atdindprocedimentos_set',
                        to_attr='glycated_hemoglobin_evaluated_procedures',
                        queryset=fatatdindproced_model().objects.filter(
                            Q(
                                Q(co_dim_procedimento_avaliado_id__in=glycated_hemoglobin_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbos_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbos_list())
                                )   
                            )
                            | Q(
                                Q(co_dim_procedimento_avaliado_id__in=glycated_hemoglobin_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbo_complete_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbo_complete_list())
                                )
                            )    
                        ).select_related(
                            'co_dim_tempo'
                        )
                    ),
                    Prefetch(
                        lookup='atdindprocedimentos_set',
                        to_attr='glycated_hemoglobin_requested_procedures',
                        queryset=fatatdindproced_model().objects.filter(
                            Q(
                                Q(co_dim_procedimento_solicitado_id__in=glycated_hemoglobin_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbos_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbos_list())
                                )   
                            )
                            | Q(
                                Q(co_dim_procedimento_solicitado_id__in=glycated_hemoglobin_list())
                                & Q(
                                    Q(co_dim_cbo_1_id__in=cbo_complete_list()) 
                                    | Q(co_dim_cbo_2_id__in=cbo_complete_list())
                                )
                            )    
                        ).select_related(
                            'co_dim_tempo'
                        )
                    ),
                    Prefetch(
                        lookup='atd_ind_problemas_set',
                        to_attr='diabetic_condition',
                        queryset = fatatdindprob_model().objects.filter(
                            Q(
                                Q(co_dim_ciap__nu_ciap__in=DIABETIC_CIAPS) 
                                | Q(co_dim_cid__nu_cid__in=DIABETIC_CIDS)
                            )
                        ).select_related(
                            'co_dim_cid', 'co_dim_ciap'
                        ).order_by(
                            'co_seq_fat_atend_ind_problemas'
                        ).distinct()
                    ),
                ).select_related(
                    'co_dim_tempo', 'co_dim_municipio', 
                )
            ),
            Prefetch(
                lookup='cidadao_procedimentos_set',
                to_attr='glycated_hemoglobin_1',
                queryset=fatatdindproced_model().objects.filter(
                    Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(
                        Q(co_dim_procedimento_avaliado_id__in=glycated_hemoglobin_list())
                        | Q(co_dim_procedimento_solicitado_id__in=glycated_hemoglobin_list())
                    )
                    & Q(
                        Q(co_dim_cbo_1_id__in=cbos_list())
                        | Q(co_dim_cbo_2_id__in=cbos_list())
                    )
                )
            ),
            Prefetch(
                lookup='cidadao_atend_proced_set',
                to_attr='glycated_hemoglobin_2',
                queryset=fatatdproced_model().objects.filter(
                    Q(co_dim_tempo__gt=set_date_to_int(extraction_start))
                    & Q(co_dim_tempo__lte=set_date_to_int(extraction_end))
                    & Q(co_dim_procedimento_id__in=glycated_hemoglobin_list())
                    & Q(co_dim_cbo__in=cbos_list()) 
                )
            ),
            Prefetch(
                lookup='cidadao_pec_set',
                to_attr='individual_registers',
                queryset=fatcadind_model().objects.all(
                ).select_related(
                    'co_dim_municipio'
                )
            )
        ).filter(
            Q(
                Exists(
                    fatcadind_model().objects.filter(
                        Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                        & Q(
                            Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False)
                        )
                        & ~Q(co_dim_tipo_saida_cadastro_id__in=[1, 2])
                        & Q(co_dim_equipe_id__in=valid_teams_list())
                    )
                )
            )
            & Q(
                Q(
                    Exists(
                        fatcadind_model().objects.filter(
                            Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                            & Q(st_diabete=1)
                        )
                    )
                )
                | Q(
                    Exists(
                        fatatdind_model().objects.filter(
                            Q(co_fat_cidadao_pec=OuterRef('co_seq_fat_cidadao_pec'))
                            & Q(Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False))
                            & Q(
                                Q(co_dim_cbo_1_id__in=cbos_list()) 
                                | Q(co_dim_cbo_2_id__in=cbos_list())
                            )
                            & Q(
                                Exists(
                                    fatatdindprob_model().objects.filter(
                                        Q(co_fat_atd_ind=OuterRef('co_seq_fat_atd_ind'))
                                        & Q(
                                            Q(co_dim_ciap__nu_ciap__in=DIABETIC_CIAPS) 
                                            | Q(co_dim_cid__nu_cid__in=DIABETIC_CIDS)
                                        )
                                    )
                                )
                            )        
                        )
                    )
                )
            )  
        ).select_related(
            'co_dim_unidade_saude_vinc', 'co_dim_equipe_vinc'
        ).distinct(
            'nu_cns', 'nu_cpf_cidadao'
        ).order_by(
            'nu_cns', 'nu_cpf_cidadao'
        )

        return qs    


class FatCadIndividualQueryset(models.QuerySet):

    def women(self, quad=None):
        
        if quad is None:
            min_birth_date = datetime.datetime.now().date() - relativedelta(years=64)
            max_birth_date = datetime.datetime.now().date() - relativedelta(years=25)
        else:
            min_birth_date = quad.evaluation_end - relativedelta(years=64)
            max_birth_date = quad.evaluation_end - relativedelta(years=25) 

        qs = self.filter(
            Q(
                Q(nu_cns__isnull=False) | Q(nu_cpf_cidadao__isnull=False)
            )
            & Q(co_dim_sexo=2)
            & Q(dt_nascimento__gt=min_birth_date)
            & Q(dt_nascimento__lt=max_birth_date)
            & ~Q(co_dim_tipo_saida_cadastro__in=[1, 2])
        ).distinct(
            'nu_cns', 'nu_cpf_cidadao'
        ).order_by(
            'nu_cns', 'nu_cpf_cidadao'
        )

        return qs    


class ProntuarioQueryset(models.QuerySet):

    def children(self, quad=None):

        if quad is None:
            min_birth_date = datetime.datetime.now().date() - relativedelta(months=24)
            max_birth_date = datetime.datetime.now().date() - relativedelta(months=12)
            
        else:
            min_birth_date = quad.evaluation_start - relativedelta(months=12)
            max_birth_date = quad.evaluation_end - relativedelta(months=12) 

        qs = self.prefetch_related(
            Prefetch(
                lookup='vacinacao_set',
                to_attr='vaccinations',
                queryset=(
                    apps.get_model(
                        app_label='esus', 
                        model_name='TbVacinacao'
                    ).objects.prefetch_related(
                        Prefetch(
                            lookup='vacinacao_registros_set', 
                            to_attr='vaccines',
                            queryset=registro_vacinacao_model().objects.select_related(
                                'co_dim_imunobiologico',
                                'co_dim_dose_imunobiologico'
                            )
                        ),
                        Prefetch(
                            lookup='vacinacao_registros_set', 
                            to_attr='vip_pentac',
                            queryset=registro_vacinacao_model().objects.filter(
                                co_dim_imunobiologico__in=[22, 42],
                                co_dim_dose_imunobiologico=3
                            ).select_related(
                                'co_dim_imunobiologico',
                                'co_dim_dose_imunobiologico'
                            )
                        ),
                        Prefetch(
                            lookup='vacinacao_registros_set', 
                            to_attr='hexa',
                            queryset=registro_vacinacao_model().objects.filter(
                                co_dim_imunobiologico=43,
                                co_dim_dose_imunobiologico=3
                            ).select_related(
                                'co_dim_imunobiologico',
                                'co_dim_dose_imunobiologico'
                            )
                        ),
                        Prefetch(
                            lookup='vacinacao_registros_set', 
                            to_attr='pentaa_hep',
                            queryset=registro_vacinacao_model().objects.filter(
                                co_dim_imunobiologico__in=[9, 29],
                                co_dim_dose_imunobiologico=3
                            ).select_related(
                                'co_dim_imunobiologico',
                                'co_dim_dose_imunobiologico'
                            )
                        )
                    )
                )
            )
        ).select_related(
            'co_cidadao'
        ).filter(
            Q(
                Q(co_cidadao__nu_cns__isnull=False) | Q(co_cidadao__nu_cpf__isnull=False)
            )
            & Q(co_cidadao__dt_nascimento__gte=min_birth_date)
            & Q(co_cidadao__dt_nascimento__lte=max_birth_date)
        )

        return qs
