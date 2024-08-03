from django import db
from django.db import models

from indicadores_esus.esus.managers import (FatCadIndividualQueryset,
                                            FatCidadaoPecQueryset)


class TbFatCidadaoPec(models.Model):
    co_seq_fat_cidadao_pec = models.BigIntegerField(primary_key=True)
    co_cidadao = models.BigIntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    no_cidadao = models.CharField(max_length=500, blank=True, null=True)
    no_social_cidadao = models.CharField(max_length=500, blank=True, null=True)
    co_dim_tempo_nascimento = models.BigIntegerField(blank=True, null=True)
    co_dim_sexo = models.ForeignKey(
        'esus.TbDimSexo', on_delete=models.DO_NOTHING, db_column='co_dim_sexo',
        blank=True, null=True
    )
    # co_dim_identidade_genero = models.ForeignKey(
    #     'esus.TbDimIdentidadeGenero', on_delete=models.DO_NOTHING,
    #     db_column='co_dim_identidade_genero', blank=True, null=True
    # )
    nu_telefone_celular = models.CharField(max_length=100,
                                           blank=True, null=True)
    st_faleceu = models.IntegerField(blank=True, null=True)
    # st_lookup_etl = models.IntegerField(blank=True, null=True)
    st_deletar = models.IntegerField(blank=True, null=True)
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
    co_dim_unidade_saude_vinc = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING,
        db_column='co_dim_unidade_saude_vinc', blank=True, null=True
    )
    co_dim_equipe_vinc = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING,
        db_column='co_dim_equipe_vinc', blank=True, null=True
    )

    objects = FatCidadaoPecQueryset.as_manager()

    def __str__(self):
        return str(self.no_cidadao)

    class Meta:
        managed = False
        db_table = 'tb_fat_cidadao_pec'


class TbFatCadIndividual(models.Model):
    co_seq_fat_cad_individual = models.BigIntegerField(primary_key=True)
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_uuid_ficha_origem = models.CharField(max_length=92, blank=True, null=True)
    st_recusa_cadastro = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    st_desconhece_mae = models.IntegerField(blank=True, null=True)
    co_dim_profissional = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING,
        db_column='co_dim_profissional', blank=True, null=True
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING,
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_unidade_saude = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING,
        db_column='co_dim_unidade_saude', blank=True, null=True
    )
    co_dim_equipe = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING,
        db_column='co_dim_equipe', blank=True, null=True
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING,
        db_column='co_dim_tempo', blank=True, null=True
    )
    co_dim_tempo_validade = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING,
        db_column='co_dim_tempo_validade', blank=True, null=True,
        related_name='cad_individual_validade_set'
    )
    co_dim_tempo_validade_recusa = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING,
        db_column='co_dim_tempo_validade_recusa', blank=True, null=True,
        related_name='cad_individual_recusa_set'
    )
    co_dim_sexo = models.ForeignKey(
        'esus.TbDimSexo', on_delete=models.DO_NOTHING, db_column='co_dim_sexo',
        blank=True, null=True
    )
    co_dim_raca_cor = models.ForeignKey(
        'esus.TbDimRacaCor', on_delete=models.DO_NOTHING,
        db_column='co_dim_raca_cor', blank=True, null=True
    )
    co_dim_nacionalidade = models.ForeignKey(
        'esus.TbDimNacionalidade', on_delete=models.DO_NOTHING,
        db_column='co_dim_nacionalidade', blank=True, null=True
    )
    co_dim_pais_nascimento = models.ForeignKey(
        'esus.TbDimPais', on_delete=models.DO_NOTHING,
        db_column='co_dim_pais_nascimento', blank=True, null=True
    )
    co_dim_municipio_cidadao = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING,
        db_column='co_dim_municipio_cidadao', blank=True, null=True,
        related_name='municipio_cidadao_set'
    )
    nu_cns_responsavel = models.CharField(max_length=15, blank=True, null=True)
    # st_responsavel_familiar = models.IntegerField(blank=True, null=True)
    # st_frequenta_creche = models.IntegerField(blank=True, null=True)
    # st_frequenta_cuidador = models.IntegerField(blank=True, null=True)
    # st_participa_grupo_comunitario = models.IntegerField(blank=True, null=True)
    # st_plano_saude_privado = models.IntegerField(blank=True, null=True)
    # st_comunidade_tradicional = models.IntegerField(blank=True, null=True)
    # st_deficiencia = models.IntegerField(blank=True, null=True)
    # st_defi_auditiva = models.IntegerField(blank=True, null=True)
    # st_defi_intelectual_cognitiva = models.IntegerField(blank=True, null=True)
    # st_defi_outra = models.IntegerField(blank=True, null=True)
    # st_defi_visual = models.IntegerField(blank=True, null=True)
    # st_defi_fisica = models.IntegerField(blank=True, null=True)
    st_gestante = models.IntegerField(blank=True, null=True)
    # st_doenca_respiratoria = models.IntegerField(blank=True, null=True)
    # st_doenca_respira_asma = models.IntegerField(blank=True, null=True)
    # st_doenca_respira_dpoc_enfisem = models.IntegerField(blank=True, null=True)
    # st_doenca_respira_outra = models.IntegerField(blank=True, null=True)
    # st_doenca_respira_n_sabe = models.IntegerField(blank=True, null=True)
    # st_fumante = models.IntegerField(blank=True, null=True)
    # st_alcool = models.IntegerField(blank=True, null=True)
    # st_outra_droga = models.IntegerField(blank=True, null=True)
    st_hipertensao_arterial = models.IntegerField(blank=True, null=True)
    st_diabete = models.IntegerField(blank=True, null=True)
    # st_avc = models.IntegerField(blank=True, null=True)
    # st_infarto = models.IntegerField(blank=True, null=True)
    # st_hanseniase = models.IntegerField(blank=True, null=True)
    # st_tuberculose = models.IntegerField(blank=True, null=True)
    # st_cancer = models.IntegerField(blank=True, null=True)
    # st_internacao_12 = models.IntegerField(blank=True, null=True)
    # st_tratamento_psiquiatra = models.IntegerField(blank=True, null=True)
    # st_acamado = models.IntegerField(blank=True, null=True)
    # st_domiciliado = models.IntegerField(blank=True, null=True)
    # st_usa_planta_medicinal = models.IntegerField(blank=True, null=True)
    # st_doenca_cardiaca = models.IntegerField(blank=True, null=True)
    # st_doenca_card_insuficiencia = models.IntegerField(blank=True, null=True)
    # st_doenca_card_outro = models.IntegerField(blank=True, null=True)
    # st_doenca_card_n_sabe = models.IntegerField(blank=True, null=True)
    # st_problema_rins = models.IntegerField(blank=True, null=True)
    # st_problema_rins_insuficiencia = models.IntegerField(blank=True, null=True)
    # st_problema_rins_outro = models.IntegerField(blank=True, null=True)
    # st_problema_rins_nao_sabe = models.IntegerField(blank=True, null=True)
    # st_pic = models.IntegerField(blank=True, null=True)
    # st_morador_rua = models.IntegerField(blank=True, null=True)
    # st_recebe_beneficio = models.IntegerField(blank=True, null=True)
    # st_referencia_familiar = models.IntegerField(blank=True, null=True)
    # co_dim_frequencia_alimentacao = models.ForeignKey(
    #     'esus.TbDimFrequenciaAlimentacao', on_delete=models.DO_NOTHING,
    #     db_column='co_dim_frequencia_alimentacao', blank=True, null=True
    # )
    # st_orig_alimen_restaurante_pop = models.IntegerField(blank=True, null=True)
    # st_orig_alimen_doacao_reli = models.IntegerField(blank=True, null=True)
    # st_orig_alimen_doacao_rest = models.IntegerField(blank=True, null=True)
    # st_orig_alimen_doacao_popular = models.IntegerField(blank=True, null=True)
    # st_orig_alimen_outros = models.IntegerField(blank=True, null=True)
    # st_acompanhado_instituicao = models.IntegerField(blank=True, null=True)
    # st_visita_familiar_frequente = models.IntegerField(blank=True, null=True)
    # st_higiene_pessoal_acesso = models.IntegerField(blank=True, null=True)
    # st_hig_pess_banho = models.IntegerField(blank=True, null=True)
    # st_hig_pess_sanitario = models.IntegerField(blank=True, null=True)
    # st_hig_pess_higiene_bucal = models.IntegerField(blank=True, null=True)
    # st_hig_pess_outros = models.IntegerField(blank=True, null=True)
    # co_dim_tipo_parentesco = models.ForeignKey(
    #     'esus.TbDimTipoParentesco', on_delete=models.DO_NOTHING,
    #     db_column='co_dim_tipo_parentesco', blank=True, null=True
    # )
    co_dim_cbo = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, db_column='co_dim_cbo',
        blank=True, null=True
    )
    co_dim_tipo_escolaridade = models.ForeignKey(
        'esus.TbDimTipoEscolaridade', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_escolaridade', blank=True, null=True
    )
    # co_dim_situacao_trabalho = models.ForeignKey(
    #     'esus.TbDimSituacaoTrabalho', on_delete=models.DO_NOTHING,
    #     db_column='co_dim_situacao_trabalho', blank=True, null=True
    # )
    co_dim_tipo_orientacao_sexual = models.ForeignKey(
        'esus.TbDimTipoOrientacaoSexual', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_orientacao_sexual', blank=True, null=True
    )
    co_dim_tipo_saida_cadastro = models.ForeignKey(
        'esus.TbDimTipoSaidaCadastro', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_saida_cadastro', blank=True, null=True
    )
    co_dim_tipo_condicao_peso = models.ForeignKey(
        'esus.TbDimTipoCondicaoPeso', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_condicao_peso', blank=True, null=True
    )
    co_dim_tempo_morador_rua = models.ForeignKey(
        'esus.TbDimTempoMoradorRua', on_delete=models.DO_NOTHING,
        db_column='co_dim_tempo_morador_rua', blank=True, null=True
    )
    co_dim_etnia = models.ForeignKey(
        'esus.TbDimEtnia', on_delete=models.DO_NOTHING,
        db_column='co_dim_etnia', blank=True, null=True
    )
    co_dim_cbo_cidadao = models.ForeignKey(
        'esus.TbDimCbo', models.DO_NOTHING, db_column='co_dim_cbo_cidadao',
        blank=True, null=True, related_name='cbo_cidadao_set'
    )
    co_dim_identidade_genero = models.ForeignKey(
        'esus.TbDimIdentidadeGenero', on_delete=models.DO_NOTHING,
        db_column='co_dim_identidade_genero', blank=True, null=True
    )
    co_dim_faixa_etaria = models.ForeignKey(
        'esus.TbDimFaixaEtaria', on_delete=models.DO_NOTHING,
        db_column='co_dim_faixa_etaria', blank=True, null=True
    )
    # st_desconhece_pai = models.IntegerField(blank=True, null=True)
    # st_informar_orientacao_sexual = models.IntegerField(blank=True, null=True)
    # st_informar_identidade_genero = models.IntegerField(blank=True, null=True)
    # dt_naturalizacao = models.DateField(blank=True, null=True)
    # dt_entrada_brasil = models.DateField(blank=True, null=True)
    dt_obito = models.DateField(blank=True, null=True)
    # st_respons_crianca_adulto_resp = models.IntegerField(blank=True, null=True)
    # st_respons_crianca_outra_crian = models.IntegerField(blank=True, null=True)
    # st_respons_crianca_adolescente = models.IntegerField(blank=True, null=True)
    # st_respons_crianca_sozinha = models.IntegerField(blank=True, null=True)
    # st_respons_crianca_creche = models.IntegerField(blank=True, null=True)
    # st_respons_crianca_outro = models.IntegerField(blank=True, null=True)
    nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
    # st_processo_linha_tempo = models.IntegerField(blank=True, null=True)
    # st_processo_cidadao = models.IntegerField(blank=True, null=True)
    no_nome = models.CharField(max_length=500, blank=True, null=True)
    no_nome_social = models.CharField(max_length=500, blank=True, null=True)
    no_nome_mae = models.CharField(max_length=500, blank=True, null=True)
    no_nome_pai = models.CharField(max_length=500, blank=True, null=True)
    nu_nis = models.CharField(max_length=32, blank=True, null=True)
    # nu_portaria_naturalizacao = models.CharField(max_length=65,
    #                                              blank=True, null=True)
    nu_celular = models.CharField(max_length=33, blank=True, null=True)
    no_email = models.CharField(max_length=500, blank=True, null=True)
    nu_obito_do = models.CharField(max_length=32, blank=True, null=True)
    no_maternidade_referencia = models.CharField(max_length=500,
                                                 blank=True, null=True)
    no_causa_internacao12 = models.CharField(max_length=500,
                                             blank=True, null=True)
    # no_plantas_medicinais = models.CharField(max_length=500,
    #                                          blank=True, null=True)
    no_outra_condicao1 = models.CharField(max_length=500, blank=True, null=True)
    no_outra_condicao2 = models.CharField(max_length=500, blank=True, null=True)
    no_outra_condicao3 = models.CharField(max_length=500, blank=True, null=True)
    no_acompanhado_instituicao = models.CharField(max_length=500,
                                                  blank=True, null=True)
    no_visita_familiar_parentesco = models.CharField(max_length=500,
                                                     blank=True, null=True)
    # nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING,
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    st_gerado_automaticamente = models.IntegerField(blank=True, null=True)
    st_ficha_inativa = models.IntegerField(blank=True, null=True)
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING,
        db_column='co_fat_cidadao_pec', blank=True, null=True,
        related_name='cidadao_pec_set'
    )
    co_fat_cidadao_pec_responsvl = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING,
        db_column='co_fat_cidadao_pec_responsvl', blank=True, null=True,
        related_name='fat_cidadao_responsavel_set'
    )
    st_proc_operacionais = models.IntegerField(blank=True, null=True)
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
    nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
    co_dim_povo_comunidad_trad = models.ForeignKey(
        'esus.TbDimPovoComunidadTrad', on_delete=models.DO_NOTHING,
        db_column='co_dim_povo_comunidad_trad', blank=True, null=True
    )

    objects = FatCadIndividualQueryset.as_manager()

    def __str__(self):
        return str(self.no_nome)

    class Meta:
        managed = False
        db_table = 'tb_fat_cad_individual'


class TbFatAtendimentoIndividual(models.Model):
    co_seq_fat_atd_ind = models.BigIntegerField(primary_key=True)
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING,
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_profissional_1 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING,
        db_column='co_dim_profissional_1', blank=True, null=True
    )
    co_dim_profissional_2 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING,
        db_column='co_dim_profissional_2', blank=True, null=True,
        related_name='profissional2_fatatendindividual_set'
    )
    co_dim_cbo_1 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, db_column='co_dim_cbo_1',
        blank=True, null=True
    )
    co_dim_cbo_2 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, db_column='co_dim_cbo_2',
        blank=True, null=True, related_name='cbo2_fatatendindividual_set'
    )
    co_dim_unidade_saude_1 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING,
        db_column='co_dim_unidade_saude_1', blank=True, null=True
    )
    co_dim_unidade_saude_2 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING,
        db_column='co_dim_unidade_saude_2', blank=True, null=True,
        related_name='unidadesaude2_fatatendindividual_set'
    )
    co_dim_equipe_1 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING,
        db_column='co_dim_equipe_1', blank=True, null=True
    )
    co_dim_equipe_2 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING,
        db_column='co_dim_equipe_2', blank=True, null=True,
        related_name='equipe2_fatatendindividual_set'
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING,
        db_column='co_dim_tempo', blank=True, null=True
    )
    # co_dim_racionalidade_saude = models.ForeignKey(
    #     'esus.TbDimRacionalidadeSaude', on_delete=models.DO_NOTHING,
    #     db_column='co_dim_racionalidade_saude', blank=True, null=True
    # )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    co_dim_faixa_etaria = models.ForeignKey(
        'esus.TbDimFaixaEtaria', on_delete=models.DO_NOTHING,
        db_column='co_dim_faixa_etaria', blank=True, null=True
    )
    co_dim_sexo = models.ForeignKey(
        'esus.TbDimSexo', on_delete=models.DO_NOTHING, db_column='co_dim_sexo',
        blank=True, null=True
    )
    co_dim_turno = models.ForeignKey(
        'esus.TbDimTurno', on_delete=models.DO_NOTHING,
        db_column='co_dim_turno', blank=True, null=True
    )
    co_dim_local_atendimento = models.ForeignKey(
        'esus.TbDimLocalAtendimento', on_delete=models.DO_NOTHING,
        db_column='co_dim_local_atendimento', blank=True, null=True
    )
    co_dim_tipo_atendimento = models.ForeignKey(
        'esus.TbDimTipoAtendimento', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_atendimento', blank=True, null=True
    )
    nu_peso = models.FloatField(blank=True, null=True)
    nu_altura = models.FloatField(blank=True, null=True)
    nu_perimetro_cefalico = models.FloatField(blank=True, null=True)
    st_vacinacao_em_dia = models.IntegerField(blank=True, null=True)
    co_dim_aleitamento = models.ForeignKey(
        'esus.TbDimAleitamento', on_delete=models.DO_NOTHING,
        db_column='co_dim_aleitamento', blank=True, null=True
    )
    co_dim_tempo_dum = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING,
        db_column='co_dim_tempo_dum', blank=True, null=True,
        related_name='tempo_dum_atendindividual_set'
    )
    st_gravidez_planejada = models.IntegerField(blank=True, null=True)
    nu_idade_gestacional_semanas = models.IntegerField(blank=True, null=True)
    nu_gestas_previas = models.IntegerField(blank=True, null=True)
    nu_partos = models.IntegerField(blank=True, null=True)
    # co_dim_modalidade_ad = models.ForeignKey(
    #     'esus.TbDimModalidadeAd', on_delete=models.DO_NOTHING,
    #     db_column='co_dim_modalidade_ad', blank=True, null=True
    # )
    # st_ficou_em_observacao = models.IntegerField(blank=True, null=True)
    # st_nasf_avaliacao_diagnostico = models.IntegerField(blank=True, null=True)
    # st_nasf_proce_clin_terapeutico = models.IntegerField(blank=True, null=True)
    # st_nasf_prescricao_terapeutica = models.IntegerField(blank=True, null=True)
    # st_conduta_consulta_agendada = models.IntegerField(blank=True, null=True)
    # st_conduta_cuidd_conti_program = models.IntegerField(blank=True, null=True)
    # st_conduta_agendamento_grupos = models.IntegerField(blank=True, null=True)
    # st_conduta_agendamento_nasf = models.IntegerField(blank=True, null=True)
    # st_conduta_alta_episodio = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_interno_dia = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_serv_special = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_caps = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_intern_hospi = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_urgencia = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_servico_ad = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_intersetoria = models.IntegerField(blank=True, null=True)
    ds_filtro_cids = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_ciaps = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_proced_avaliados = models.CharField(max_length=4000,
                                                  blank=True, null=True)
    ds_filtro_proced_solicitados = models.CharField(max_length=4000,
                                                    blank=True, null=True)
    nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING,
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', models.DO_NOTHING,
        db_column='co_fat_cidadao_pec', blank=True, null=True,
        related_name='atendimentos_pec'
    )
    dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
    dt_final_atendimento = models.DateTimeField(blank=True, null=True)
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f'{self.co_seq_fat_atd_ind} - {self.dt_inicial_atendimento} - ' \
               f'{self.dt_final_atendimento}'

    class Meta:
        managed = False
        db_table = 'tb_fat_atendimento_individual'


class TbFatAtdIndProblemas(models.Model):
    co_seq_fat_atend_ind_problemas = models.BigIntegerField(primary_key=True)
    co_fat_atd_ind = models.ForeignKey(
        'esus.TbFatAtendimentoIndividual', on_delete=models.DO_NOTHING, 
        blank=True, null=True, related_name='atd_ind_problemas_set',
        db_column='co_fat_atd_ind'
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_profissional_1 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_1', blank=True, null=True
    )
    co_dim_profissional_2 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_2', blank=True, null=True, 
        related_name='profissional_problemas_set_2'
    )
    co_dim_cbo_1 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_1', blank=True, null=True
    )
    co_dim_cbo_2 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_2', blank=True, null=True, 
        related_name='cbo_problemas_set_2'
    )
    co_dim_unidade_saude_1 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_1', blank=True, null=True
    )
    co_dim_unidade_saude_2 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_2', blank=True, null=True,
        related_name='unidade_problemas_set_2'
    )
    co_dim_equipe_1 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_1', blank=True, null=True
    )
    co_dim_equipe_2 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_2', blank=True, null=True,
        related_name='equipe_problemas_set_2'
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    co_dim_cid = models.ForeignKey(
        'esus.TbDimCid', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cid', blank=True, null=True
    )
    co_dim_ciap = models.ForeignKey(
        'esus.TbDimCiap', on_delete=models.DO_NOTHING, 
        db_column='co_dim_ciap', blank=True, null=True
    )
    # nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True
    )
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_atend_ind_problemas)
    class Meta:
        managed = False
        db_table = 'tb_fat_atd_ind_problemas'


class TbFatRelOpGestante(models.Model):
    co_seq_fat_rel_op_gestante = models.BigIntegerField(primary_key=True)
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', 
        related_name='pec_cidadao_relop_gestantes_set'
    )
    co_gestacao = models.IntegerField(blank=True, null=True)
    co_peso = models.IntegerField(blank=True, null=True)
    dt_inicio_gestacao = models.DateField(blank=True, null=True)
    dt_inicio_puerperio = models.DateField(blank=True, null=True)
    dt_fim_puerperio = models.DateField(blank=True, null=True)
    dt_fao_ultimo = models.DateField(blank=True, null=True)
    dt_fvd_ultimo = models.DateField(blank=True, null=True)
    st_ultima_vacina_em_dia = models.IntegerField(blank=True, null=True)
    st_solicitacao_vdrl = models.IntegerField(blank=True, null=True)
    st_avaliacao_vdrl = models.IntegerField(blank=True, null=True)
    dt_fai_dum = models.DateField(blank=True, null=True)
    dt_ultima_fai_pre_natal = models.DateField(blank=True, null=True)
    dt_fai_puerperio = models.DateField(blank=True, null=True)
    nu_idade_gestacional = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.co_gestacao)

    class Meta:
        managed = False
        db_table = 'tb_fat_rel_op_gestante'


class TbFatAtdIndExames(models.Model):
    co_seq_fat_atd_ind_exames = models.BigIntegerField(primary_key=True)
    co_fat_atd_ind = models.ForeignKey(
        'esus.TbFatAtendimentoIndividual', on_delete=models.DO_NOTHING, 
        blank=True, null=True, related_name='atdind_exames_set',
        db_column='co_fat_atd_ind'
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_profissional_1 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_1', blank=True, null=True,
        related_name='profissional1_atdindexames_set'
    )
    co_dim_profissional_2 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_2', blank=True, null=True,
        related_name='profissional2_atdindexames_set'
    )
    co_dim_cbo_1 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_1', blank=True, null=True,
        related_name='cbo1_atdindexames_set'
    )
    co_dim_cbo_2 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_2', blank=True, null=True,
        related_name='cbo2_atdindexames_set'
    )
    co_dim_unidade_saude_1 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_1', blank=True, null=True,
        related_name='unidsaude1_atdindexames_set'
    )
    co_dim_unidade_saude_2 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_2', blank=True, null=True,
        related_name='unidsaude2_atdindexames_set'
    )
    co_dim_equipe_1 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_1', blank=True, null=True,
        related_name='equipe1_atdindexames_set'
    )
    co_dim_equipe_2 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_2', blank=True, null=True,
        related_name='equipe2_atdindexames_set'
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True,
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True
    )
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
    co_dim_procedimento = models.ForeignKey(
        'esus.TbDimProcedimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_procedimento', blank=True, null=True
    )
    dt_solicitacao = models.DateField(blank=True, null=True)
    dt_realizacao = models.DateField(blank=True, null=True)
    dt_resultado = models.DateField(blank=True, null=True)
    nu_resultado_valor = models.FloatField(blank=True, null=True)
    nu_resultado_dia = models.IntegerField(blank=True, null=True)
    nu_resultado_semana = models.IntegerField(blank=True, null=True)
    dt_resultado_data = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_atd_ind_exames)

    class Meta:
        managed = False
        db_table = 'tb_fat_atd_ind_exames'


class TbFatAtdIndProcedimentos(models.Model):
    co_seq_fat_atend_ind_proced = models.BigIntegerField(primary_key=True)
    co_fat_atd_ind = models.ForeignKey(
        'esus.TbFatAtendimentoIndividual', on_delete=models.DO_NOTHING, 
        blank=True, null=True, related_name='atdindprocedimentos_set',
        db_column='co_fat_atd_ind'
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_profissional_1 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_1', blank=True, null=True,
        related_name='profissional1_atdindprocedimentos_set'
    )
    co_dim_profissional_2 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_2', blank=True, null=True,
        related_name='profissional2_atdindprocedimentos_set'
    )
    co_dim_cbo_1 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_1', blank=True, null=True,
        related_name='cbo1_atdindprocedimentos_set'
    )
    co_dim_cbo_2 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_2', blank=True, null=True,
        related_name='cbo2_atdindprocedimentos_set'
    )
    co_dim_unidade_saude_1 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_1', blank=True, null=True,
        related_name='unidsaude1_atdindprocedimentos_set'
    )
    co_dim_unidade_saude_2 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_2', blank=True, null=True,
        related_name='unidsaude2_atdindprocedimentos_set'
    )
    co_dim_equipe_1 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_1', blank=True, null=True,
        related_name='equipe1_atdindprocedimentos_set'
    )
    co_dim_equipe_2 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_2', blank=True, null=True,
        related_name='equipe2_atdindprocedimentos_set'
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True,
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    co_dim_procedimento_avaliado = models.ForeignKey(
        'esus.TbDimProcedimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_procedimento_avaliado', blank=True, null=True,
        related_name='procedavaliado_atdindprocedimentos_set'    
    )
    co_dim_procedimento_solicitado = models.ForeignKey(
        'esus.TbDimProcedimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_procedimento_solicitado', blank=True, null=True,
        related_name='procedsolicitado_atdindprocedimentos_set'
    )
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True,
        related_name='cidadao_procedimentos_set'
    )
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_atend_ind_proced)

    class Meta:
        managed = False
        db_table = 'tb_fat_atd_ind_procedimentos'


class TbFatAtendimentoOdonto(models.Model):
    co_seq_fat_atd_odnt = models.BigIntegerField(primary_key=True)
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_profissional_1 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_1', blank=True, null=True,
        related_name='profissional1_atdodonto_set'
    )
    co_dim_profissional_2 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_2', blank=True, null=True,
        related_name='profissional2_atdodonto_set'
    )
    co_dim_cbo_1 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_1', blank=True, null=True,
        related_name='cbo1_atdodonto_set'
    )
    co_dim_cbo_2 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo_2', blank=True, null=True,
        related_name='cbo2_atdodonto_set'
    )
    co_dim_unidade_saude_1 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_1', blank=True, null=True,
        related_name='unidsaude1_atdodonto_set'
    )
    co_dim_unidade_saude_2 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_2', blank=True, null=True,
        related_name='unidsaude2_atdodonto_set'
    )
    co_dim_equipe_1 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_1', blank=True, null=True,
        related_name='equipe1_atdodonto_set'
    )
    co_dim_equipe_2 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_2', blank=True, null=True,
        related_name='equipe2_atdodonto_set'
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    co_dim_faixa_etaria = models.ForeignKey(
        'esus.TbDimFaixaEtaria', on_delete=models.DO_NOTHING, 
        db_column='co_dim_faixa_etaria', blank=True, null=True
    )
    co_dim_sexo = models.ForeignKey(
        'esus.TbDimSexo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_sexo', blank=True, null=True
    )
    co_dim_turno = models.ForeignKey(
        'esus.TbDimTurno', on_delete=models.DO_NOTHING, 
        db_column='co_dim_turno', blank=True, null=True
    )
    co_dim_local_atendimento = models.ForeignKey(
        'esus.TbDimLocalAtendimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_local_atendimento', blank=True, null=True
    )
    st_paciente_necessidades_espec = models.IntegerField(blank=True, null=True)
    st_gestante = models.IntegerField(blank=True, null=True)
    co_dim_tipo_atendimento = models.ForeignKey(
        'esus.TbDimTipoAtendimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_atendimento', blank=True, null=True
    )
    co_dim_tipo_consulta = models.ForeignKey(
        'esus.TbDimTipoConsultaOdonto', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_consulta', blank=True, null=True
    )
    # st_vigil_abscesso_dentoalveola = models.IntegerField(blank=True, null=True)
    # st_vigil_alterac_tecidos_moles = models.IntegerField(blank=True, null=True)
    # st_vigil_dor_dente = models.IntegerField(blank=True, null=True)
    # st_vigil_fendas_fissuras_labio = models.IntegerField(blank=True, null=True)
    # st_vigil_fluorose_dentaria = models.IntegerField(blank=True, null=True)
    # st_vigil_traumat_dentoalveolar = models.IntegerField(blank=True, null=True)
    # st_vigil_nao_identificado = models.IntegerField(blank=True, null=True)
    # st_fornecimento_escova_dental = models.IntegerField(blank=True, null=True)
    # st_fornecimento_creme_dental = models.IntegerField(blank=True, null=True)
    # st_fornecimento_fio_dental = models.IntegerField(blank=True, null=True)
    # st_conduta_consulta_agendada = models.IntegerField(blank=True, null=True)
    # st_conduta_outros_profissio_ab = models.IntegerField(blank=True, null=True)
    # st_conduta_agendamento_nasf = models.IntegerField(blank=True, null=True)
    # st_conduta_agendamento_grupos = models.IntegerField(blank=True, null=True)
    # st_conduta_alta_episodio = models.IntegerField(blank=True, null=True)
    # st_conduta_tratamento_concluid = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_necess_espec = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_cirurgia_bmf = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_endodontia = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_estomatologi = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_implantodont = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_odontopediat = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_ortod_ortop = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_periodontia = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_protese_dent = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_radiologia = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_outros = models.IntegerField(blank=True, null=True)
    # st_encaminhamento_nao_aplica = models.IntegerField(blank=True, null=True)
    ds_filtro_cids = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_ciaps = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_procedimentos = models.CharField(max_length=4000, blank=True, null=True)
    nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True,
        related_name='atendimentos_odontos_pec'
    )
    dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
    dt_final_atendimento = models.DateTimeField(blank=True, null=True)
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
    nu_peso = models.FloatField(blank=True, null=True)
    nu_altura = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_atd_odnt)

    class Meta:
        managed = False
        db_table = 'tb_fat_atendimento_odonto'


class TbFatProcedAtend(models.Model):
    co_seq_fat_proced_atend = models.BigIntegerField(primary_key=True)
    co_fat_procedimento = models.ForeignKey(
        'esus.TbFatProcedimento', on_delete=models.DO_NOTHING, 
        blank=True, null=True, db_column='co_fat_procedimento'
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_unidade_saude = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude', blank=True, null=True
    )
    co_dim_equipe = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe', blank=True, null=True
    )
    co_dim_profissional = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional', blank=True, null=True
    )
    co_dim_cbo = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo', blank=True, null=True
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    co_dim_sexo = models.ForeignKey(
        'esus.TbDimSexo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_sexo', blank=True, null=True
    )
    co_dim_turno = models.ForeignKey(
        'esus.TbDimTurno', on_delete=models.DO_NOTHING, 
        db_column='co_dim_turno', blank=True, null=True
    )
    co_dim_local_atendimento = models.ForeignKey(
        'esus.TbDimLocalAtendimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_local_atendimento', blank=True, null=True
    )
    co_dim_faixa_etaria = models.ForeignKey(
        'esus.TbDimFaixaEtaria', on_delete=models.DO_NOTHING, 
        db_column='co_dim_faixa_etaria', blank=True, null=True
    )
    st_escuta_inicial = models.IntegerField(blank=True, null=True)
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    ds_filtro_procedimento = models.CharField(max_length=4000, blank=True, null=True)
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True,
        related_name='cidadao_proced_set'
    )
    dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
    dt_final_atendimento = models.DateTimeField(blank=True, null=True)
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
    nu_peso = models.FloatField(blank=True, null=True)
    nu_altura = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_proced_atend)

    class Meta:
        managed = False
        db_table = 'tb_fat_proced_atend'


class TbFatProcedAtendProced(models.Model):
    co_seq_fat_proced_atend_proced = models.BigIntegerField(primary_key=True)
    co_fat_procedimento = models.ForeignKey(
        'esus.TbFatProcedimento', on_delete=models.DO_NOTHING, 
        blank=True, null=True, db_column='co_fat_procedimento'
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_unidade_saude = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude', blank=True, null=True
    )
    co_dim_equipe = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe', blank=True, null=True
    )
    co_dim_profissional = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional', blank=True, null=True
    )
    co_dim_cbo = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo', blank=True, null=True
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    co_dim_sexo = models.ForeignKey(
        'esus.TbDimSexo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_sexo', blank=True, null=True
    )
    co_dim_turno = models.ForeignKey(
        'esus.TbDimTurno', on_delete=models.DO_NOTHING, 
        db_column='co_dim_turno', blank=True, null=True
    )
    co_dim_local_atendimento = models.ForeignKey(
        'esus.TbDimLocalAtendimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_local_atendimento', blank=True, null=True
    )
    st_escuta_inicial = models.IntegerField(blank=True, null=True)
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    co_dim_procedimento = models.ForeignKey(
        'esus.TbDimProcedimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_procedimento', blank=True, null=True
    )
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp',
        blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True,
        related_name='cidadao_atend_proced_set'
    )
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_proced_atend_proced)
    
    class Meta:
        managed = False
        db_table = 'tb_fat_proced_atend_proced'


class TbFatVacinacao(models.Model):
    co_seq_fat_vacinacao = models.BigIntegerField(primary_key=True)
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_profissional = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional', blank=True, null=True
    )
    co_dim_cbo = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo', blank=True, null=True
    )
    co_dim_unidade_saude = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude', blank=True, null=True
    )
    co_dim_equipe = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe', blank=True, null=True
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    co_dim_faixa_etaria = models.ForeignKey(
        'esus.TbDimFaixaEtaria', on_delete=models.DO_NOTHING, 
        db_column='co_dim_faixa_etaria', blank=True, null=True
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    co_dim_turno = models.ForeignKey(
        'esus.TbDimTurno', on_delete=models.DO_NOTHING, 
        db_column='co_dim_turno', blank=True, null=True
    )
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_prontuario = models.CharField(max_length=30, blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    co_dim_sexo = models.ForeignKey(
        'esus.TbDimSexo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_sexo', blank=True, null=True
    )
    co_dim_local_atendimento = models.ForeignKey(
        'esus.TbDimLocalAtendimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_local_atendimento', blank=True, null=True
    )
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    st_viajante = models.IntegerField(blank=True, null=True)
    st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
    st_gestante = models.IntegerField(blank=True, null=True)
    st_puerpera = models.IntegerField(blank=True, null=True)
    ds_filtro_imunobiologico = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_estrategia_vacinacao = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_dose_imunobiologico = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_lote = models.CharField(max_length=4000, blank=True, null=True)
    ds_filtro_fabricante = models.CharField(max_length=4000, blank=True, null=True)
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True,
        related_name='cidadao_vacinacao_set'
    )
    dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
    dt_final_atendimento = models.DateTimeField(blank=True, null=True)
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
    ds_filtro_grupo_atendimento = models.CharField(max_length=4000, blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_vacinacao)
    class Meta:
        managed = False
        db_table = 'tb_fat_vacinacao'


class TbFatVacinacaoVacina(models.Model):
    co_seq_fat_vacinacao_vacina = models.BigIntegerField(primary_key=True)
    co_fat_vacinacao = models.ForeignKey(
        'esus.TbFatVacinacao', on_delete=models.DO_NOTHING,
        blank=True, null=True, db_column='co_fat_vacinacao',
        related_name='vacina_vacinacao_set'
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_profissional = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional', blank=True, null=True
    )
    co_dim_cbo = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo', blank=True, null=True
    )
    co_dim_unidade_saude = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude', blank=True, null=True
    )
    co_dim_equipe = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe', blank=True, null=True
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    co_dim_imunobiologico = models.ForeignKey(
        'esus.TbDimImunobiologico', on_delete=models.DO_NOTHING, 
        db_column='co_dim_imunobiologico', blank=True, null=True
    )
    co_dim_estrategia_vacinacao = models.ForeignKey(
        'esus.TbDimEstrategiaVacinacao', on_delete=models.DO_NOTHING, 
        db_column='co_dim_estrategia_vacinacao', blank=True, null=True
    )
    co_dim_dose_imunobiologico = models.ForeignKey(
        'esus.TbDimDoseImunobiologico', on_delete=models.DO_NOTHING, 
        db_column='co_dim_dose_imunobiologico', blank=True, null=True
    )
    no_lote = models.CharField(max_length=255, blank=True, null=True)
    no_fabricante = models.CharField(max_length=255, blank=True, null=True)
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_dim_grupo_atendimento = models.ForeignKey(
        'esus.TbDimGrupoAtendimento', on_delete=models.DO_NOTHING, 
        db_column='co_dim_grupo_atendimento', blank=True, null=True
    )
    st_registro_anterior = models.IntegerField(blank=True, null=True)
    co_dim_tempo_vacina_aplicada = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo_vacina_aplicada', blank=True, null=True,
        related_name='tempo_vacina_aplicada_set'
    )

    def __str__(self):
        return str(self.co_seq_fat_vacinacao_vacina)

    class Meta:
        managed = False
        db_table = 'tb_fat_vacinacao_vacina'


class TbFatProcedimento(models.Model):
    co_seq_fat_procedimento = models.BigIntegerField(primary_key=True)
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_unidade_saude = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude', blank=True, null=True
    )
    co_dim_equipe = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe', blank=True, null=True
    )
    co_dim_profissional = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional', blank=True, null=True
    )
    co_dim_cbo = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cbo', blank=True, null=True
    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nr_proc_consdd_pressao_arteria = models.IntegerField(blank=True, null=True)
    nr_proc_consdd_temperatura = models.IntegerField(blank=True, null=True)
    nr_proc_consdd_curativo_simple = models.IntegerField(blank=True, null=True)
    nr_proc_consdd_mate_exame_labo = models.IntegerField(blank=True, null=True)
    nr_proc_consdd_glicemia_capila = models.IntegerField(blank=True, null=True)
    nr_proc_consdd_medicao_altura = models.IntegerField(blank=True, null=True)
    nr_proc_consdd_medicao_peso = models.IntegerField(blank=True, null=True)
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )

    def __str__(self):
        return str(self.co_seq_fat_procedimento)
        
    class Meta:
        managed = False
        db_table = 'tb_fat_procedimento'


class TbFatAtendOdontoProblemas(models.Model):
    co_seq_fat_atnd_odonto_probl = models.BigIntegerField(primary_key=True)
    co_fat_atd_odnt = models.ForeignKey(
        'esus.TbFatAtendimentoOdonto', on_delete=models.DO_NOTHING, 
        blank=True, null=True, related_name='atd_odnt_problemas_set',
        db_column='co_fat_atd_odnt'
    )
    co_dim_tipo_ficha = models.ForeignKey(
        'esus.TbDimTipoFicha', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_ficha', blank=True, null=True
    )
    co_dim_municipio = models.ForeignKey(
        'esus.TbDimMunicipio', on_delete=models.DO_NOTHING, 
        db_column='co_dim_municipio', blank=True, null=True
    )
    co_dim_profissional_1 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_1', blank=True, null=True,
        related_name='professional_odonto_problemas_1'
    )
    co_dim_profissional_2 = models.ForeignKey(
        'esus.TbDimProfissional', on_delete=models.DO_NOTHING, 
        db_column='co_dim_profissional_2', blank=True, null=True,
        related_name='professional_odonto_problemas_2'
    )
    co_dim_cbo_1 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, db_column='co_dim_cbo_1', 
        blank=True, null=True, related_name='cbo_odonto_problemas_1'
    )
    co_dim_cbo_2 = models.ForeignKey(
        'esus.TbDimCbo', on_delete=models.DO_NOTHING, db_column='co_dim_cbo_2', 
        blank=True, null=True, related_name='cbo_odonto_problemas_2'
    )
    co_dim_unidade_saude_1 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_1', blank=True, null=True,
        related_name='unidade_odonto_problemas_1'
    )
    co_dim_unidade_saude_2 = models.ForeignKey(
        'esus.TbDimUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_dim_unidade_saude_2', blank=True, null=True,
        related_name='unidade_odonto_problemas_2'
    )
    co_dim_equipe_1 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_1', blank=True, null=True,
        related_name='equipe_odonto_problemas_1'
    )
    co_dim_equipe_2 = models.ForeignKey(
        'esus.TbDimEquipe', on_delete=models.DO_NOTHING, 
        db_column='co_dim_equipe_2', blank=True, null=True,
        related_name='equipe_odonto_problemas_2'

    )
    co_dim_tempo = models.ForeignKey(
        'esus.TbDimTempo', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tempo', blank=True, null=True
    )
    nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
    nu_atendimento = models.IntegerField(blank=True, null=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    co_dim_cid = models.ForeignKey(
        'esus.TbDimCid', on_delete=models.DO_NOTHING, db_column='co_dim_cid', 
        blank=True, null=True
    )
    co_dim_ciap = models.ForeignKey(
        'esus.TbDimCiap', on_delete=models.DO_NOTHING, db_column='co_dim_ciap', 
        blank=True, null=True
    )
    nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
    co_dim_tipo_origem_dado_transp = models.ForeignKey(
        'esus.TbDimTipoOrigemDadoTransp', on_delete=models.DO_NOTHING, 
        db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True
    )
    co_dim_cds_tipo_origem = models.ForeignKey(
        'esus.TbDimTipoOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_dim_cds_tipo_origem', blank=True, null=True
    )
    co_fat_cidadao_pec = models.ForeignKey(
        'esus.TbFatCidadaoPec', on_delete=models.DO_NOTHING, 
        db_column='co_fat_cidadao_pec', blank=True, null=True
    )
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_fat_atnd_odonto_probl)

    class Meta:
        managed = False
        db_table = 'tb_fat_atend_odonto_problemas'
