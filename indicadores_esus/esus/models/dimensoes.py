from django.db import models

from indicadores_esus.esus.managers import (DimCboQueryset, DimEquipeQueryset,
                                            DimImunobiologicoQueryset,
                                            DimProcedimentoQueryset)


class TbDimTipoFicha(models.Model):
    co_seq_dim_tipo_ficha = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_tipo_ficha = models.CharField(max_length=500, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nu_identificador

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_ficha'


class TbDimPais(models.Model):
    co_seq_dim_pais = models.BigIntegerField(primary_key=True)
    no_pais = models.CharField(max_length=500, blank=True, null=True)
    co_cadsus = models.CharField(max_length=6, blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_pais

    class Meta:
        managed = False
        db_table = 'tb_dim_pais'


class TbDimUf(models.Model):
    co_seq_dim_uf = models.BigIntegerField(primary_key=True)
    no_identificador = models.CharField(max_length=10, blank=True, null=True)
    no_uf = models.CharField(max_length=500, blank=True, null=True)
    sg_uf = models.CharField(max_length=10, blank=True, null=True)
    co_dim_pais = models.ForeignKey(
        'esus.TbDimPais', on_delete=models.DO_NOTHING, db_column='co_dim_pais',
        blank=True, null=True
    )
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.sg_uf

    class Meta:
        managed = False
        db_table = 'tb_dim_uf'


class TbDimMunicipio(models.Model):
    co_seq_dim_municipio = models.BigIntegerField(primary_key=True)
    no_municipio = models.CharField(max_length=500, blank=True, null=True)
    co_ibge = models.CharField(max_length=10, blank=True, null=True)
    co_dim_uf = models.ForeignKey(
        'esus.TbDimUf', on_delete=models.DO_NOTHING, db_column='co_dim_uf',
        blank=True, null=True
    )
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.no_municipio}/{self.co_dim_uf}'

    class Meta:
        managed = False
        db_table = 'tb_dim_municipio'


class TbDimProfissional(models.Model):
    co_seq_dim_profissional = models.BigIntegerField(primary_key=True)
    nu_cns = models.CharField(max_length=15, blank=True, null=True)
    no_profissional = models.CharField(max_length=255, blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_profissional

    class Meta:
        managed = False
        db_table = 'tb_dim_profissional'


class TbDimUnidadeSaude(models.Model):
    co_seq_dim_unidade_saude = models.BigIntegerField(primary_key=True)
    nu_cnes = models.CharField(max_length=20, blank=True, null=True)
    no_unidade_saude = models.CharField(max_length=500, blank=True, null=True)
    no_bairro = models.CharField(max_length=500, blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_unidade_saude

    class Meta:
        managed = False
        db_table = 'tb_dim_unidade_saude'


class TbDimEquipe(models.Model):
    co_seq_dim_equipe = models.BigIntegerField(primary_key=True)
    nu_ine = models.CharField(max_length=20, blank=True, null=True)
    no_equipe = models.CharField(max_length=255, blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    objects = DimEquipeQueryset.as_manager()

    def __str__(self):
        return self.no_equipe

    class Meta:
        managed = False
        db_table = 'tb_dim_equipe'


class TbDimTempo(models.Model):
    co_seq_dim_tempo = models.BigIntegerField(primary_key=True)
    dt_registro = models.DateField(blank=True, null=True)
    nu_dia = models.SmallIntegerField(blank=True, null=True)
    nu_mes = models.SmallIntegerField(blank=True, null=True)
    nu_ano = models.IntegerField(blank=True, null=True)
    ds_dia_semana = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.dt_registro)

    class Meta:
        managed = False
        db_table = 'tb_dim_tempo'


class TbDimSexo(models.Model):
    co_seq_dim_sexo = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_sexo = models.CharField(max_length=100, blank=True, null=True)
    sg_sexo = models.CharField(max_length=100, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.sg_sexo

    class Meta:
        managed = False
        db_table = 'tb_dim_sexo'


class TbDimRacaCor(models.Model):
    co_seq_dim_raca_cor = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=50, blank=True, null=True)
    nu_ms = models.CharField(max_length=50, blank=True, null=True)
    ds_raca_cor = models.CharField(max_length=500, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_raca_cor

    class Meta:
        managed = False
        db_table = 'tb_dim_raca_cor'


class TbDimNacionalidade(models.Model):
    co_seq_dim_nacionalidade = models.BigIntegerField(primary_key=True)
    co_nacionalidade = models.CharField(max_length=2, blank=True, null=True)
    no_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_nacionalidade = models.CharField(max_length=100, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_identificador

    class Meta:
        managed = False
        db_table = 'tb_dim_nacionalidade'


class TbDimFrequenciaAlimentacao(models.Model):
    co_seq_dim_frequencia_aliment = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_dim_frequencia_alimentacao = models.CharField(max_length=500,
                                                     blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_dim_frequencia_alimentacao

    class Meta:
        managed = False
        db_table = 'tb_dim_frequencia_alimentacao'


class TbDimTipoParentesco(models.Model):
    co_seq_dim_tipo_parentesco = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_tipo_parentesco = models.CharField(max_length=500, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ds_tipo_parentesco

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_parentesco'


class TbDimCbo(models.Model):
    co_seq_dim_cbo = models.BigIntegerField(primary_key=True)
    nu_cbo = models.CharField(max_length=20, blank=True, null=True)
    no_cbo = models.CharField(max_length=500, blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    objects = DimCboQueryset.as_manager()

    def __str__(self):
        return self.no_cbo

    class Meta:
        managed = False
        db_table = 'tb_dim_cbo'


class TbDimTipoEscolaridade(models.Model):
    co_seq_dim_tipo_escolaridade = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_dim_tipo_escolaridade = models.CharField(max_length=500,
                                                blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ds_dim_tipo_escolaridade

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_escolaridade'


class TbDimSituacaoTrabalho(models.Model):
    co_seq_dim_situacao_trabalho = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_dim_situacao_trabalho = models.CharField(max_length=500,
                                                blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ds_dim_situacao_trabalho

    class Meta:
        managed = False
        db_table = 'tb_dim_situacao_trabalho'


class TbDimTipoOrientacaoSexual(models.Model):
    co_seq_dim_tipo_orientacao_sxl = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_dim_tipo_orientacao_sexual = models.CharField(max_length=500,
                                                     blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_dim_tipo_orientacao_sexual

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_orientacao_sexual'


class TbDimTipoSaidaCadastro(models.Model):
    co_seq_dim_tipo_saida_cadastro = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_dim_tipo_saida_cadastro = models.CharField(max_length=500,
                                                  blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_dim_tipo_saida_cadastro

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_saida_cadastro'


class TbDimTipoCondicaoPeso(models.Model):
    co_seq_dim_tipo_condicao_peso = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_dim_tipo_condicao_peso = models.CharField(max_length=500,
                                                 blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_dim_tipo_condicao_peso

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_condicao_peso'


class TbDimTempoMoradorRua(models.Model):
    co_seq_dim_tempo_morador_rua = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_dim_tempo_morador_rua = models.CharField(max_length=500,
                                                blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_dim_tempo_morador_rua

    class Meta:
        managed = False
        db_table = 'tb_dim_tempo_morador_rua'


class TbDimEtnia(models.Model):
    co_seq_dim_etnia = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    no_etnia = models.CharField(max_length=500, blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_etnia

    class Meta:
        managed = False
        db_table = 'tb_dim_etnia'


class TbDimIdentidadeGenero(models.Model):
    co_seq_dim_identidade_genero = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_identidade_genero = models.CharField(max_length=500,
                                            blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_identidade_genero

    class Meta:
        managed = False
        db_table = 'tb_dim_identidade_genero'


class TbDimFaixaEtaria(models.Model):
    co_seq_dim_faixa_etaria = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_faixa_etaria = models.CharField(max_length=500, blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)
    nu_faixa_inicial_anos = models.IntegerField(blank=True, null=True)
    nu_faixa_final_anos = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_faixa_etaria

    class Meta:
        managed = False
        db_table = 'tb_dim_faixa_etaria'


class TbDimTipoOrigemDadoTransp(models.Model):
    co_seq_dim_tp_orgm_dado_transp = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=255, blank=True, null=True)
    no_tipo_origem_dado_transp = models.CharField(max_length=255,
                                                  blank=True, null=True)

    def __str__(self):
        return self.no_tipo_origem_dado_transp

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_origem_dado_transp'


class TbDimTipoOrigem(models.Model):
    co_seq_dim_tipo_origem = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=255, blank=True, null=True)
    no_tipo_origem = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_tipo_origem

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_origem'


class TbDimPovoComunidadTrad(models.Model):
    co_seq_dim_povo_comunidad_trad = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=10, blank=True, null=True)
    ds_povo_comunidade_tradicional = models.CharField(max_length=100,
                                                      blank=True, null=True)

    def __str__(self):
        return self.ds_povo_comunidade_tradicional

    class Meta:
        managed = False
        db_table = 'tb_dim_povo_comunidad_trad'


class TbDimRacionalidadeSaude(models.Model):
    co_seq_dim_racionalidade_saude = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    no_racionalidade_saude = models.CharField(max_length=500,
                                              blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_racionalidade_saude

    class Meta:
        managed = False
        db_table = 'tb_dim_racionalidade_saude'


class TbDimTurno(models.Model):
    co_seq_dim_turno = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_turno = models.CharField(max_length=500, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_turno

    class Meta:
        managed = False
        db_table = 'tb_dim_turno'


class TbDimLocalAtendimento(models.Model):
    co_seq_dim_local_atendimento = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_local_atendimento = models.CharField(max_length=500,
                                            blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ds_local_atendimento

    class Meta:
        managed = False
        db_table = 'tb_dim_local_atendimento'


class TbDimTipoAtendimento(models.Model):
    co_seq_dim_tipo_atendimento = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_tipo_atendimento = models.CharField(max_length=500,
                                           blank=True, null=True)
    co_dim_tipo_atendimento_pai = models.ForeignKey(
        'esus.TbDimTipoAtendimento', on_delete=models.DO_NOTHING,
        db_column='co_dim_tipo_atendimento_pai', blank=True, null=True
    )
    co_ordem = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.ds_tipo_atendimento

    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_atendimento'


class TbDimAleitamento(models.Model):
    co_seq_dim_aleitamento = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_aleitamento = models.CharField(max_length=500, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_aleitamento

    class Meta:
        managed = False
        db_table = 'tb_dim_aleitamento'


class TbDimModalidadeAd(models.Model):
    co_seq_dim_modalidade_ad = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_modalidade_ad = models.CharField(max_length=500, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_modalidade_ad

    class Meta:
        managed = False
        db_table = 'tb_dim_modalidade_ad'


class TbDimCiap(models.Model):
    co_seq_dim_ciap = models.BigIntegerField(primary_key=True)
    nu_ciap = models.CharField(max_length=10, blank=True, null=True)
    no_ciap = models.CharField(max_length=500, blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nu_ciap

    class Meta:
        managed = False
        db_table = 'tb_dim_ciap'


class TbDimCid(models.Model):
    co_seq_dim_cid = models.BigIntegerField(primary_key=True)
    nu_cid = models.CharField(max_length=10, blank=True, null=True)
    no_cid = models.CharField(max_length=500, blank=True, null=True)
    st_ativo = models.IntegerField(blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nu_cid

    class Meta:
        managed = False
        db_table = 'tb_dim_cid'


class TbDimProcedimento(models.Model):
    co_seq_dim_procedimento = models.BigIntegerField(primary_key=True)
    co_proced = models.CharField(max_length=100, blank=True, null=True)
    ds_proced = models.CharField(max_length=500, blank=True, null=True)
    co_seq_dim_proced_ref_ab = models.BigIntegerField(blank=True, null=True)
    co_pai = models.ForeignKey(
        'esus.TbDimProcedimento', on_delete=models.DO_NOTHING, 
        db_column='co_pai', blank=True, null=True
    )
    st_registro_valido = models.IntegerField(blank=True, null=True)
    ds_filtro = models.CharField(max_length=350, blank=True, null=True)

    objects = DimProcedimentoQueryset.as_manager()

    def __str__(self):
        return self.ds_proced
    class Meta:
        managed = False
        db_table = 'tb_dim_procedimento'


class TbDimTipoConsultaOdonto(models.Model):
    co_seq_dim_tipo_cnsulta_odonto = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=100, blank=True, null=True)
    ds_tipo_consulta_odonto = models.CharField(max_length=500, blank=True, null=True)
    co_ordem = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ds_tipo_consulta_odonto
    class Meta:
        managed = False
        db_table = 'tb_dim_tipo_consulta_odonto'


class TbDimImunobiologico(models.Model):
    co_seq_dim_imunobiologico = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=255, blank=True, null=True)
    sg_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    no_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)
    st_registro_valido = models.IntegerField(blank=True, null=True)

    objects = DimImunobiologicoQueryset.as_manager()

    def __str__(self):
        return self.no_imunobiologico
    class Meta:
        managed = False
        db_table = 'tb_dim_imunobiologico'


class TbDimEstrategiaVacinacao(models.Model):
    co_seq_dim_estrategia_vacnacao = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=10, blank=True, null=True)
    nu_estrategia_vacinacao = models.CharField(max_length=255, blank=True, null=True)
    no_estrategia_vacinacao = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_estrategia_vacinacao
    class Meta:
        managed = False
        db_table = 'tb_dim_estrategia_vacinacao'


class TbDimDoseImunobiologico(models.Model):
    co_seq_dim_dose_imunobiologico = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=255, blank=True, null=True)
    sg_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    no_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    ds_filtro = models.CharField(max_length=255, blank=True, null=True)
    nu_ordem = models.IntegerField(blank=True, null=True)
    no_apresentacao_dose = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_dose_imunobiologico
    class Meta:
        managed = False
        db_table = 'tb_dim_dose_imunobiologico'


class TbDimGrupoAtendimento(models.Model):
    co_seq_dim_grupo_atendimento = models.BigIntegerField(primary_key=True)
    nu_identificador = models.CharField(max_length=10, blank=True, null=True)
    ds_grupo_atendimento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ds_grupo_atendimento
    class Meta:
        managed = False
        db_table = 'tb_dim_grupo_atendimento'
