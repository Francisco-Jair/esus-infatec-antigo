from django.db import models

from indicadores_esus.esus.managers import EquipeQueryset, ProntuarioQueryset

class TbPais(models.Model):
    co_pais = models.BigIntegerField(primary_key=True)
    sg_pais_2 = models.CharField(max_length=2)
    sg_pais_3 = models.CharField(max_length=3, blank=True, null=True)
    no_pais_portugues = models.CharField(max_length=72)
    no_pais_ingles = models.CharField(max_length=72, blank=True, null=True)
    no_pais_portugues_filtro = models.CharField(max_length=72, blank=True,
                                                null=True)
    co_pais_cadsus = models.CharField(max_length=3, blank=True, null=True)
    st_ativo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_pais_portugues

    class Meta:
        managed = False
        db_table = 'tb_pais'


class TbUf(models.Model):
    co_uf = models.BigIntegerField(primary_key=True)
    co_pais = models.ForeignKey('esus.TbPais', on_delete=models.DO_NOTHING,
                                db_column='co_pais')
    sg_uf = models.CharField(max_length=2)
    nu_dne = models.CharField(max_length=2)
    no_uf = models.CharField(max_length=72)
    no_identificador = models.CharField(max_length=2)

    def __str__(self):
        return self.sg_uf

    class Meta:
        managed = False
        db_table = 'tb_uf'


class TbSituacaoLocalidade(models.Model):
    co_situacao_localidade = models.BigIntegerField(primary_key=True)
    no_situacao_localidade = models.CharField(max_length=100)
    sg_situacao_localidade = models.CharField(max_length=1)

    def __str__(self):
        return self.no_situacao_localidade

    class Meta:
        managed = False
        db_table = 'tb_situacao_localidade'


class TbTipoLocalidade(models.Model):
    co_tipo_localidade = models.BigIntegerField(primary_key=True)
    no_tipo_localidade = models.CharField(max_length=100)
    sg_tipo_localidade = models.CharField(max_length=1)
    no_identificador = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.no_tipo_localidade

    class Meta:
        managed = False
        db_table = 'tb_tipo_localidade'


class TbLocalidade(models.Model):
    co_localidade = models.BigIntegerField(primary_key=True)
    co_uf = models.ForeignKey('esus.TbUf', on_delete=models.DO_NOTHING,
                              db_column='co_uf')
    nu_dne = models.CharField(unique=True, max_length=8)
    no_localidade = models.CharField(max_length=72)
    nu_cep = models.CharField(max_length=8, blank=True, null=True)
    tp_localidade = models.ForeignKey('esus.TbTipoLocalidade',
                                      on_delete=models.DO_NOTHING,
                                      db_column='tp_localidade')
    co_situacao_localidade = models.ForeignKey(
        'esus.TbSituacaoLocalidade', on_delete=models.DO_NOTHING,
        db_column='co_situacao_localidade'
    )
    co_ibge = models.CharField(max_length=7, blank=True, null=True)
    no_localidade_filtro = models.CharField(max_length=72)
    st_ativo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_localidade

    class Meta:
        managed = False
        db_table = 'tb_localidade'


class TbCdsTipoCuidador(models.Model):
    co_cds_tipo_cuidador = models.BigIntegerField(primary_key=True)
    no_cds_tipo_cuidador = models.CharField(max_length=255)
    no_identificador = models.CharField(max_length=255)

    def __str__(self):
        return self.no_identificador

    class Meta:
        managed = False
        db_table = 'tb_cds_tipo_cuidador'


class TbNacionalidade(models.Model):
    co_nacionalidade = models.BigIntegerField(primary_key=True)
    no_nacionalidade = models.CharField(max_length=15)
    no_identificador = models.CharField(max_length=15)
    co_nacionalidade_cadsus = models.CharField(max_length=1,
                                               blank=True, null=True)

    def __str__(self):
        return self.no_nacionalidade

    class Meta:
        managed = False
        db_table = 'tb_nacionalidade'


class TbEscolaridade(models.Model):
    co_escolaridade = models.BigIntegerField(primary_key=True)
    no_escolaridade = models.CharField(max_length=255, blank=True, null=True)
    no_escolaridade_filtro = models.CharField(max_length=255,
                                              blank=True, null=True)

    def __str__(self):
        return self.no_escolaridade

    class Meta:
        managed = False
        db_table = 'tb_escolaridade'


class TbRacaCor(models.Model):
    co_raca_cor = models.BigIntegerField(primary_key=True)
    no_raca_cor = models.CharField(max_length=50)
    nu_ms = models.CharField(max_length=100, blank=True, null=True)
    no_identificador = models.CharField(max_length=255)
    co_raca_cor_cadsus = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.no_raca_cor

    class Meta:
        managed = False
        db_table = 'tb_raca_cor'


class TbEtnia(models.Model):
    co_etnia = models.BigIntegerField(primary_key=True)
    no_etnia = models.CharField(max_length=255)
    co_etnia_cadsus = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.no_etnia

    class Meta:
        managed = False
        db_table = 'tb_etnia'


class TbEstadoCivil(models.Model):
    co_estado_civil = models.BigIntegerField(primary_key=True)
    no_estado_civil = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_estado_civil

    class Meta:
        managed = False
        db_table = 'tb_estado_civil'


class TbCbo(models.Model):
    co_cbo = models.BigIntegerField(primary_key=True)
    no_cbo = models.CharField(max_length=255)
    no_cbo_filtro = models.CharField(max_length=255)
    co_cbo_2002 = models.CharField(max_length=10)
    st_disponivel_lotacao = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_cbo

    class Meta:
        managed = False
        db_table = 'tb_cbo'


class TbTipoLogradouro(models.Model):
    co_tipo_logradouro = models.BigIntegerField(primary_key=True)
    nu_dne = models.CharField(unique=True, max_length=3)
    no_tipo_logradouro = models.CharField(max_length=144)
    no_tipo_logradouro_filtro = models.CharField(max_length=144)
    co_tp_logradouro_cadsus = models.CharField(max_length=3,
                                               blank=True, null=True)
    nu_frequencia = models.BigIntegerField()
    st_ativo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_tipo_logradouro

    class Meta:
        managed = False
        db_table = 'tb_tipo_logradouro'


class TbCidadao(models.Model):
    co_seq_cidadao = models.BigIntegerField(primary_key=True)
    # co_unico_cidadao_prontuario = models.CharField(max_length=36,
    #                                                blank=True, null=True)
    # co_unico_prontuario = models.CharField(max_length=36, blank=True, null=True)
    st_desconhece_nome_mae = models.IntegerField()
    co_localidade = models.ForeignKey('esus.TbLocalidade',
                                      on_delete=models.DO_NOTHING,
                                      db_column='co_localidade',
                                      blank=True, null=True)
    nu_area = models.CharField(max_length=3, blank=True, null=True)
    nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
    nu_nis_pis_pasep = models.CharField(max_length=50, blank=True, null=True)
    dt_atualizado = models.DateTimeField(blank=True, null=True)
    nu_cns_responsavel = models.CharField(max_length=16, blank=True, null=True)
    no_responsavel = models.CharField(max_length=255, blank=True, null=True)
    dt_nascimento_responsavel = models.DateTimeField(blank=True, null=True)
    nu_cns_cuidador = models.CharField(max_length=16, blank=True, null=True)
    no_cuidador = models.CharField(max_length=255, blank=True, null=True)
    dt_nascimento_cuidador = models.DateTimeField(blank=True, null=True)
    tp_cds_cuidador = models.ForeignKey('esus.TbCdsTipoCuidador',
                                        on_delete=models.DO_NOTHING,
                                        db_column='tp_cds_cuidador',
                                        blank=True, null=True)
    co_unico_cidadao = models.CharField(max_length=96)
    co_nacionalidade = models.ForeignKey('esus.TbNacionalidade',
                                         on_delete=models.DO_NOTHING,
                                         db_column='co_nacionalidade')
    co_pais_nascimento = models.ForeignKey(
        'esus.TbPais', on_delete=models.DO_NOTHING,
        db_column='co_pais_nascimento', blank=True, null=True
    )
    co_unico_ultima_ficha = models.CharField(max_length=96,
                                             blank=True, null=True)
    dt_ultima_ficha = models.DateField(blank=True, null=True)
    st_registro_cadsus = models.IntegerField(blank=True, null=True)
    dt_atualizado_cadsus = models.DateField(blank=True, null=True)
    st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
    dt_naturalizacao = models.DateTimeField(blank=True, null=True)
    dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
    nu_portaria_naturalizacao = models.CharField(max_length=16,
                                                 blank=True, null=True)
    st_fora_area = models.IntegerField(blank=True, null=True)
    st_infrm_orientacao_sexual = models.IntegerField(blank=True, null=True)
    tp_orientacao_sexual = models.CharField(max_length=25,
                                            blank=True, null=True)
    st_infrm_identidade_genero = models.IntegerField(blank=True, null=True)
    tp_identidade_genero = models.CharField(max_length=25,
                                            blank=True, null=True)
    st_compartilhamento_prontuario = models.IntegerField(blank=True, null=True)
    st_ativo = models.IntegerField(blank=True, null=True)
    st_nao_possui_cuidador = models.IntegerField(blank=True, null=True)
    nu_cpf = models.CharField(max_length=11, blank=True, null=True)
    nu_cns = models.CharField(max_length=16, blank=True, null=True)
    no_cidadao = models.CharField(max_length=500, blank=True, null=True)
    no_cidadao_filtro = models.CharField(max_length=600, blank=True, null=True)
    co_escolaridade = models.ForeignKey(
        'esus.TbEscolaridade', on_delete=models.DO_NOTHING,
        db_column='co_escolaridade', blank=True, null=True)
    co_raca_cor = models.ForeignKey(
        'esus.TbRacaCor', on_delete=models.DO_NOTHING, db_column='co_raca_cor',
        blank=True, null=True
    )
    co_etnia = models.ForeignKey(
        'esus.TbEtnia', on_delete=models.DO_NOTHING, db_column='co_etnia',
        blank=True, null=True
    )
    co_estado_civil = models.ForeignKey(
        'esus.TbEstadoCivil', on_delete=models.DO_NOTHING,
        db_column='co_estado_civil', blank=True, null=True
    )
    co_cbo = models.ForeignKey(
        'esus.TbCbo', on_delete=models.DO_NOTHING, db_column='co_cbo',
        blank=True, null=True
    )
    dt_nascimento = models.DateField(blank=True, null=True)
    dt_obito = models.DateField(blank=True, null=True)
    no_mae = models.CharField(max_length=500, blank=True, null=True)
    no_mae_filtro = models.CharField(max_length=600, blank=True, null=True)
    no_pai = models.CharField(max_length=500, blank=True, null=True)
    no_social = models.CharField(max_length=255, blank=True, null=True)
    st_faleceu = models.IntegerField(blank=True, null=True)
    nu_documento_obito = models.CharField(max_length=255, blank=True, null=True)
    st_dados_obito_cadsus = models.IntegerField(blank=True, null=True)
    no_localidade_exterior = models.CharField(max_length=255,
                                              blank=True, null=True)
    co_pais_exterior = models.ForeignKey(
        'esus.TbPais', on_delete=models.DO_NOTHING,
        db_column='co_pais_exterior', blank=True, null=True,
        related_name='cidadao_pais_exterior_set'
    )
    ds_cep = models.CharField(max_length=8, blank=True, null=True)
    ds_complemento = models.CharField(max_length=50, blank=True, null=True)
    ds_ponto_referencia = models.CharField(max_length=100,
                                           blank=True, null=True)
    ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
    co_uf = models.ForeignKey(
        'esus.TbUf', on_delete=models.DO_NOTHING, db_column='co_uf',
        blank=True, null=True, related_name='uf_co_cidadao_set'
    )
    co_localidade_endereco = models.ForeignKey(
        'esus.TbLocalidade', on_delete=models.DO_NOTHING,
        db_column='co_localidade_endereco', blank=True, null=True,
        related_name='localidade_endereco_cidadao_set'
    )
    nu_numero = models.CharField(max_length=20, blank=True, null=True)
    st_sem_numero = models.IntegerField(blank=True, null=True)
    no_bairro = models.CharField(max_length=255, blank=True, null=True)
    no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
    tp_logradouro = models.ForeignKey(
        'esus.TbTipoLogradouro', on_delete=models.DO_NOTHING,
        db_column='tp_logradouro', blank=True, null=True
    )
    nu_telefone_residencial = models.CharField(max_length=255,
                                               blank=True, null=True)
    nu_telefone_celular = models.CharField(max_length=255,
                                           blank=True, null=True)
    nu_telefone_contato = models.CharField(max_length=255,
                                           blank=True, null=True)
    ds_email = models.CharField(max_length=255, blank=True, null=True)
    st_ativo_para_exibicao = models.IntegerField(blank=True, null=True)
    st_unificado = models.IntegerField()
    st_territorio_utiliza_cpf = models.IntegerField(blank=True, null=True)
    nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
    nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
    no_tipo_sanguineo = models.CharField(max_length=22, blank=True, null=True)
    no_sexo = models.CharField(max_length=24, blank=True, null=True)

    def __str__(self):
        if self.no_cidadao:
            return self.no_cidadao
        return str(self.co_seq_cidadao)

    class Meta:
        managed = False
        db_table = 'tb_cidadao'


class TbProntuario(models.Model):
    co_seq_prontuario = models.BigIntegerField(primary_key=True)
    # co_unico_prontuario = models.CharField(max_length=36)
    # co_unico_cidadao_prontuario = models.CharField(max_length=36)
    qt_referencia = models.BigIntegerField(blank=True, null=True)
    co_prontuario_grupo = models.BigIntegerField(blank=True, null=True)
    co_cidadao = models.OneToOneField(
        'esus.TbCidadao', on_delete=models.DO_NOTHING, db_column='co_cidadao',
        blank=True, null=True,
        related_name='prontuario'
    )
    st_cidadao_processado = models.IntegerField(blank=True, null=True)

    objects = ProntuarioQueryset.as_manager()

    def __str__(self):
        return str(self.co_seq_prontuario)

    class Meta:
        managed = False
        db_table = 'tb_prontuario'


class TbLocalAtend(models.Model):
    co_local_atend = models.BigIntegerField(primary_key=True)
    no_local_atend = models.CharField(max_length=255, blank=True, null=True)
    no_local_atend_filtro = models.CharField(max_length=100,
                                             blank=True, null=True)
    st_local_cds = models.IntegerField(blank=True, null=True)
    st_local_ad = models.IntegerField(blank=True, null=True)
    ds_local_atend_exibicao = models.CharField(max_length=100,
                                               blank=True, null=True)

    def __str__(self):
        return self.no_local_atend

    class Meta:
        managed = False
        db_table = 'tb_local_atend'


class TbTipoAgravo(models.Model):
    co_tipo_agravo = models.BigIntegerField(primary_key=True)
    no_tipo_agravo = models.CharField(max_length=255)
    no_identificador = models.CharField(max_length=50)

    def __str__(self):
        return self.no_tipo_agravo

    class Meta:
        managed = False
        db_table = 'tb_tipo_agravo'


class TbCid10(models.Model):
    co_cid10 = models.BigIntegerField(primary_key=True)
    nu_cid10 = models.CharField(max_length=4)
    tp_agravo = models.ForeignKey(
        'esus.TbTipoAgravo', on_delete=models.DO_NOTHING,
        db_column='tp_agravo'
    )
    no_cid10 = models.CharField(max_length=400)
    no_cid10_filtro = models.CharField(max_length=400)
    st_ativo = models.IntegerField()
    no_sexo = models.CharField(max_length=24, blank=True, null=True)

    def __str__(self):
        return self.no_cid10

    class Meta:
        managed = False
        db_table = 'tb_cid10'


class TbAdModalidade(models.Model):
    co_seq_ad_modalidade = models.BigIntegerField(primary_key=True)
    no_ad_modalidade = models.CharField(max_length=100, blank=True, null=True)
    no_identificador = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.no_ad_modalidade

    class Meta:
        managed = False
        db_table = 'tb_ad_modalidade'


class TbSexo(models.Model):
    co_sexo = models.BigIntegerField(primary_key=True)
    no_sexo = models.CharField(max_length=15)
    sg_sexo = models.CharField(max_length=1)
    no_identificador = models.CharField(max_length=30)
    co_sexo_cadsus = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.sg_sexo

    class Meta:
        managed = False
        db_table = 'tb_sexo'


class TbTipoAtend(models.Model):
    co_tipo_atend = models.BigIntegerField(primary_key=True)
    no_tipo_atend = models.CharField(max_length=255)
    no_identificador = models.CharField(max_length=255)

    def __str__(self):
        return self.no_tipo_atend

    class Meta:
        managed = False
        db_table = 'tb_tipo_atend'


class TbRacionalidadeSaude(models.Model):
    co_racionalidade_saude = models.BigIntegerField(primary_key=True)
    no_racionalidade_saude = models.CharField(max_length=255,
                                              blank=True, null=True)

    def __str__(self):
        return self.no_racionalidade_saude

    class Meta:
        managed = False
        db_table = 'tb_racionalidade_saude'


class TbTipoUnidadeSaude(models.Model):
    co_seq_tipo_unidade_saude = models.BigIntegerField(primary_key=True)
    no_tipo_unidade_saude = models.CharField(max_length=120)
    co_tipo_unidade_cnes = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.no_tipo_unidade_saude
    class Meta:
        managed = False
        db_table = 'tb_tipo_unidade_saude'


class TbSubtipoUnidadeSaude(models.Model):
    co_seq_subtp_unidade_saude = models.BigIntegerField(primary_key=True)
    co_tp_unidade_saude = models.ForeignKey(
        'esus.TbTipoUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_tp_unidade_saude'
    )
    co_subtp_unidade_saude = models.CharField(max_length=3)
    ds_subtp_unidade_saude = models.CharField(max_length=255)

    def __str__(self):
        return self.ds_subtp_unidade_saude
    class Meta:
        managed = False
        db_table = 'tb_subtipo_unidade_saude'
        unique_together = (('co_tp_unidade_saude', 'co_subtp_unidade_saude'),)


class TbUnidadeSaude(models.Model):
    nu_licenca_funcionamento = models.CharField(max_length=20, blank=True, null=True)
    tp_unidade_saude = models.ForeignKey(
        'esus.TbTipoUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='tp_unidade_saude', blank=True, null=True
    )
    co_seq_unidade_saude = models.BigIntegerField(primary_key=True)
    nu_cnes = models.CharField(max_length=20, blank=True, null=True)
    st_ativo = models.IntegerField(blank=True, null=True)
    nu_cnpj = models.CharField(max_length=14, blank=True, null=True)
    no_unidade_saude = models.CharField(max_length=255, blank=True, null=True)
    no_unidade_saude_filtro = models.CharField(max_length=255, blank=True, null=True)
    nu_telefone_comercial = models.CharField(max_length=255, blank=True, null=True)
    nu_telefone_comercial2 = models.CharField(max_length=255, blank=True, null=True)
    nu_telefone_fax = models.CharField(max_length=255, blank=True, null=True)
    ds_email = models.CharField(max_length=255, blank=True, null=True)
    ds_cep = models.CharField(max_length=8, blank=True, null=True)
    ds_complemento = models.CharField(max_length=50, blank=True, null=True)
    ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
    ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
    co_uf = models.ForeignKey(
        'esus.TbUf', on_delete=models.DO_NOTHING, 
        db_column='co_uf', blank=True, null=True
    )
    co_localidade_endereco = models.ForeignKey(
        'esus.TbLocalidade', on_delete=models.DO_NOTHING, 
        db_column='co_localidade_endereco', blank=True, null=True
    )
    nu_numero = models.CharField(max_length=20, blank=True, null=True)
    st_sem_numero = models.IntegerField(blank=True, null=True)
    no_bairro = models.CharField(max_length=255, blank=True, null=True)
    no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
    tp_logradouro = models.ForeignKey(
        'esus.TbTipoLogradouro', on_delete=models.DO_NOTHING, 
        db_column='tp_logradouro', blank=True, null=True
    )
    co_subtp_unidade_saude = models.ForeignKey(
        'esus.TbSubtipoUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_subtp_unidade_saude', blank=True, null=True
    )

    def __str__(self):
        return self.no_unidade_saude
    class Meta:
        managed = False
        db_table = 'tb_unidade_saude'


class TbTipoEquipe(models.Model):
    co_seq_tipo_equipe = models.BigIntegerField(primary_key=True)
    sg_tipo_equipe = models.CharField(max_length=30)
    no_tipo_equipe = models.CharField(max_length=200)
    sg_tipo_equipe_filtro = models.CharField(max_length=30, blank=True, null=True)
    no_tipo_equipe_filtro = models.CharField(max_length=200, blank=True, null=True)
    nu_ms = models.CharField(max_length=4)
    ds_tp_equipe = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return self.no_tipo_equipe
    class Meta:
        managed = False
        db_table = 'tb_tipo_equipe'


class TbEquipe(models.Model):
    co_seq_equipe = models.BigIntegerField(primary_key=True)
    nu_ine = models.CharField(max_length=255, blank=True, null=True)
    st_ativo = models.IntegerField()
    co_unidade_saude = models.ForeignKey(
        'esus.TbUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_unidade_saude'
    )
    qt_referencia = models.BigIntegerField(blank=True, null=True)
    tp_equipe = models.ForeignKey(
        'esus.TbTipoEquipe', on_delete=models.DO_NOTHING, 
        db_column='tp_equipe', blank=True, null=True
    )
    ds_area = models.CharField(max_length=255, blank=True, null=True)
    no_equipe = models.CharField(max_length=255, blank=True, null=True)
    no_equipe_filtro = models.CharField(max_length=255, blank=True, null=True)
    co_unico_equipe = models.CharField(unique=True, max_length=255, blank=True, null=True)

    objects = EquipeQueryset.as_manager()

    class Meta:
        managed = False
        db_table = 'tb_equipe'


class TbVacinacao(models.Model):
    co_seq_vacinacao = models.BigIntegerField(primary_key=True)
    st_gestante = models.IntegerField(blank=True, null=True)
    st_puerpera = models.IntegerField(blank=True, null=True)
    st_viajante = models.IntegerField(blank=True, null=True)
    st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
    co_atend_prof = models.ForeignKey(
        'esus.TbAtendProf', on_delete=models.DO_NOTHING, 
        db_column='co_atend_prof', blank=True, null=True
    )
    co_prontuario = models.ForeignKey(
        'esus.TbProntuario', on_delete=models.DO_NOTHING, 
        db_column='co_prontuario', blank=True, null=True,
        related_name='vacinacao_set'
    )

    def __str__(self):
        return str(self.co_seq_vacinacao)

    class Meta:
        managed = False
        db_table = 'tb_vacinacao'


class TbAtendProf(models.Model):
    co_seq_atend_prof = models.BigIntegerField(primary_key=True)
    dt_fim = models.DateTimeField(blank=True, null=True)
    dt_inicio = models.DateTimeField(blank=True, null=True)
    co_atend = models.ForeignKey(
        'esus.TbAtend', on_delete=models.DO_NOTHING, db_column='co_atend'
    )
    co_atend_prof_tipo_encam_intrn = models.ForeignKey(
        'esus.TbAtendProfTipoEncamIntrn', on_delete=models.DO_NOTHING, 
        db_column='co_atend_prof_tipo_encam_intrn', blank=True, null=True
    )
    co_lotacao = models.ForeignKey(
        'esus.TbLotacao', on_delete=models.DO_NOTHING, 
        db_column='co_lotacao', blank=True, null=True
    )
    tp_atend_prof = models.ForeignKey(
        'esus.TbTipoAtendProf', on_delete=models.DO_NOTHING, 
        db_column='tp_atend_prof'
    )
    st_atend_prof = models.ForeignKey(
        'esus.TbStatusAtendProf', on_delete=models.DO_NOTHING, 
        db_column='st_atend_prof'
    )
    st_atend_enviado = models.IntegerField(blank=True, null=True)
    co_unico_ad_cidadao = models.BigIntegerField(blank=True, null=True)
    co_classificacao_risco = models.ForeignKey(
        'esus.TbClassificacaoRisco', on_delete=models.DO_NOTHING, 
        db_column='co_classificacao_risco', blank=True, null=True
    )
    co_unico_atend_prof = models.CharField(max_length=96, blank=True, null=True)
    tp_atend = models.ForeignKey(
        'esus.TbTipoAtend', on_delete=models.DO_NOTHING, 
        db_column='tp_atend', blank=True, null=True
    )
    nu_conselho_classe = models.CharField(max_length=100, blank=True, null=True)
    co_uf_emissora_conselho_classe = models.ForeignKey(
        'esus.TbUf', on_delete=models.DO_NOTHING, 
        db_column='co_uf_emissora_conselho_classe', blank=True, null=True
    )
    co_conselho_classe = models.ForeignKey(
        'esus.TbConselhoClasse', on_delete=models.DO_NOTHING, 
        db_column='co_conselho_classe', blank=True, null=True
    )
    ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
    co_racionalidade_saude = models.ForeignKey(
        'esus.TbRacionalidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_racionalidade_saude', blank=True, null=True
    )
    co_lotacao_atend_compartilhado = models.ForeignKey(
        'esus.TbLotacao', on_delete=models.DO_NOTHING, 
        db_column='co_lotacao_atend_compartilhado', blank=True, null=True,
        related_name='lotacao_atend_compart_set'    
    )
    st_registro_historico = models.IntegerField(blank=True, null=True)
    nu_revisao = models.IntegerField(blank=True, null=True)
    st_cancelado = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_atend_prof)

    class Meta:
        managed = False
        db_table = 'tb_atend_prof'


class TbAtend(models.Model):
    co_seq_atend = models.BigIntegerField(primary_key=True)
    dt_fim = models.DateTimeField(blank=True, null=True)
    dt_inicio = models.DateTimeField()
    qt_referencia = models.BigIntegerField(blank=True, null=True)
    st_atend = models.ForeignKey(
        'esus.TbStatusAtend', on_delete=models.DO_NOTHING, db_column='st_atend'
    )
    co_agendado = models.OneToOneField(
        'esus.TbAgendado', on_delete=models.DO_NOTHING, 
        db_column='co_agendado', blank=True, null=True
    )
    co_lotacao = models.ForeignKey(
        'esus.TbLotacao', on_delete=models.DO_NOTHING, 
        db_column='co_lotacao', blank=True, null=True
    )
    co_classificacao_risco = models.ForeignKey(
        'esus.TbClassificacaoRisco', on_delete=models.DO_NOTHING, 
        db_column='co_classificacao_risco', blank=True, null=True
    )
    co_prontuario = models.ForeignKey(
        'esus.TbProntuario', on_delete=models.DO_NOTHING, 
        db_column='co_prontuario'
    )
    co_unidade_saude = models.ForeignKey(
        'esus.TbUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_unidade_saude'
    )
    co_atend_prof = models.ForeignKey(
        'esus.TbAtendProf', on_delete=models.DO_NOTHING, 
        db_column='co_atend_prof', blank=True, null=True
    )
    dt_encaminhamento = models.DateTimeField(blank=True, null=True)
    st_fechado_automaticamente = models.IntegerField(blank=True, null=True)
    nu_lotacao_anterior = models.BigIntegerField(blank=True, null=True)
    co_unico_atend = models.CharField(max_length=96, blank=True, null=True)
    tp_local_atend = models.ForeignKey(
        'esus.TbLocalAtend', on_delete=models.DO_NOTHING, 
        db_column='tp_local_atend', blank=True, null=True
    )
    st_registro_tardio = models.IntegerField()
    no_justificativa_reg_tardio = models.CharField(max_length=50, blank=True, null=True)
    dt_criacao_registro = models.DateTimeField(blank=True, null=True)
    dt_ultima_alteracao_status = models.DateTimeField()
    co_equipe = models.ForeignKey(
        'esus.TbEquipe', on_delete=models.DO_NOTHING,
        db_column='co_equipe', blank=True, null=True
    )

    def __str__(self):
        return str(self.co_seq_atend)
        
    class Meta:
        managed = False
        db_table = 'tb_atend'
    

class TbAtendProfTipoEncamIntrn(models.Model):
    co_seq_atend_prof_tipo_enc_int = models.BigIntegerField(primary_key=True)
    co_agendado = models.ForeignKey(
        'esus.TbAgendado', on_delete=models.DO_NOTHING, 
        db_column='co_agendado', blank=True, null=True
    )
    co_atend = models.ForeignKey(
        'esus.TbAtend', on_delete=models.DO_NOTHING, 
        db_column='co_atend', blank=True, null=True
    )
    co_lotacao = models.ForeignKey(
        'esus.TbLotacao', on_delete=models.DO_NOTHING, 
        db_column='co_lotacao', blank=True, null=True
    )
    tp_encam_interno = models.ForeignKey(
        'esus.TbTipoEncamInterno', on_delete=models.DO_NOTHING, 
        db_column='tp_encam_interno'
    )
    st_agendado = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_atend_prof_tipo_enc_int)

    class Meta:
        managed = False
        db_table = 'tb_atend_prof_tipo_encam_intrn'


class TbLotacao(models.Model):
    dt_desativacao_lotacao = models.DateTimeField(blank=True, null=True)
    co_cbo = models.ForeignKey(
        'esus.TbCbo', on_delete=models.DO_NOTHING, 
        db_column='co_cbo'
    )
    co_prof = models.ForeignKey(
        'esus.TbProf', on_delete=models.DO_NOTHING, db_column='co_prof'
    )
    co_unidade_saude = models.ForeignKey(
        'esus.TbUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_unidade_saude'
    )
    co_equipe = models.ForeignKey(
        'esus.TbEquipe', on_delete=models.DO_NOTHING, db_column='co_equipe',
        blank=True, null=True
    )
    co_ator_papel = models.BigIntegerField(primary_key=True)
    st_atualiza_perfil = models.IntegerField(blank=True, null=True)
    st_importada = models.IntegerField(blank=True, null=True)
    st_agenda_alterada_manual = models.IntegerField(blank=True, null=True)
    dt_ultima_tentativa_envio = models.DateTimeField(blank=True, null=True)
    st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
    st_ativo_agenda_online = models.IntegerField(blank=True, null=True)
    ds_ultima_tentativa = models.TextField(blank=True, null=True)
    co_unico_lotacao = models.CharField(unique=True, max_length=255, blank=True, null=True)

    def __str__(self):
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'tb_lotacao'


class TbTipoAtendProf(models.Model):
    co_tipo_atend_prof = models.BigIntegerField(primary_key=True)
    no_tipo_atend_prof = models.CharField(max_length=30)

    def __str__(self):
        return self.no_tipo_atend_prof

    class Meta:
        managed = False
        db_table = 'tb_tipo_atend_prof'


class TbStatusAtendProf(models.Model):
    co_status_atend_prof = models.BigIntegerField(primary_key=True)
    no_status_atend_prof = models.CharField(max_length=255)

    def __str__(self):
        return self.no_status_atend_prof

    class Meta:
        managed = False
        db_table = 'tb_status_atend_prof'


class TbClassificacaoRisco(models.Model):
    co_classificacao_risco = models.BigIntegerField(primary_key=True)
    no_classificacao_risco = models.CharField(max_length=50, blank=True, null=True)
    no_identificador = models.CharField(max_length=30)
    nu_ordem = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_classificacao_risco

    class Meta:
        managed = False
        db_table = 'tb_classificacao_risco'


class TbConselhoClasse(models.Model):
    co_conselho_classe = models.BigIntegerField(primary_key=True)
    sg_conselho_classe = models.CharField(max_length=255, blank=True, null=True)
    no_conselho_classe = models.CharField(max_length=200, blank=True, null=True)
    no_curto_conselho = models.CharField(max_length=400, blank=True, null=True)
    no_conselho_classe_filtro = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.sg_conselho_classe

    class Meta:
        managed = False
        db_table = 'tb_conselho_classe'


class TbStatusAtend(models.Model):
    co_status_atend = models.BigIntegerField(primary_key=True)
    no_status_atend = models.CharField(max_length=30)
    no_status_atend_filtro = models.CharField(max_length=30)
    no_identificador = models.CharField(max_length=30)

    def __str__(self):
        return self.no_status_atend

    class Meta:
        managed = False
        db_table = 'tb_status_atend'


class TbAgendado(models.Model):
    co_seq_agendado = models.BigIntegerField(primary_key=True)
    dt_agendado = models.DateTimeField(blank=True, null=True)
    hr_inicial_agendado = models.DateTimeField(blank=True, null=True)
    ds_observacao = models.CharField(max_length=400, blank=True, null=True)
    st_agendado = models.ForeignKey(
        'esus.TbSituacaoAgendado', on_delete=models.DO_NOTHING, 
        db_column='st_agendado'
    )
    co_lotacao_agendada = models.ForeignKey(
        'esus.TbLotacao', on_delete=models.DO_NOTHING, 
        db_column='co_lotacao_agendada', blank=True, null=True
    )
    co_motivo_reserva = models.ForeignKey(
        'esus.TbMotivoReserva', on_delete=models.DO_NOTHING, 
        db_column='co_motivo_reserva', blank=True, null=True
    )
    ds_outro_motivo_reserva = models.CharField(max_length=600, blank=True, null=True)
    co_origem = models.ForeignKey(
        'esus.TbOrigem', on_delete=models.DO_NOTHING, 
        db_column='co_origem', blank=True, null=True
    )
    co_prontuario = models.ForeignKey(
        'esus.TbProntuario', on_delete=models.DO_NOTHING, 
        db_column='co_prontuario', blank=True, null=True
    )
    co_lotacao_criadora = models.ForeignKey(
        'esus.TbLotacao', on_delete=models.DO_NOTHING, 
        db_column='co_lotacao_criadora', blank=True, null=True,
        related_name='lotacao_criadora_agendado_set'
    )
    dt_criacao = models.DateTimeField(blank=True, null=True)
    uuid_agendamento = models.CharField(unique=True, max_length=36, blank=True, null=True)
    dt_ultima_tentativa_envio = models.DateTimeField(blank=True, null=True)
    st_sincronizacao = models.CharField(max_length=48)
    ds_ultima_tentativa = models.TextField(blank=True, null=True)
    st_cidadao_agendamento_online = models.CharField(max_length=48, blank=True, null=True)
    st_fora_ubs = models.IntegerField()
    co_local_atend = models.ForeignKey(
        'esus.TbLocalAtend', on_delete=models.DO_NOTHING, 
        db_column='co_local_atend', blank=True, null=True
    )
    tp_agendamento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_agendado'


class TbTipoEncamInterno(models.Model):
    co_tipo_encam_interno = models.BigIntegerField(primary_key=True)
    no_tipo_encam_interno = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.no_tipo_encam_interno
    class Meta:
        managed = False
        db_table = 'tb_tipo_encam_interno'


class TbProf(models.Model):
    co_seq_prof = models.BigIntegerField(primary_key=True)
    nu_conselho_classe = models.CharField(max_length=100, blank=True, null=True)
    co_uf_emissora_conselho_classe = models.ForeignKey(
        'esus.TbUf', on_delete=models.DO_NOTHING, 
        db_column='co_uf_emissora_conselho_classe', blank=True, null=True,
        related_name='uf_emis_cons_classe_prof_set'
    )
    co_conselho_classe = models.ForeignKey(
        'esus.TbConselhoClasse', on_delete=models.DO_NOTHING, 
        db_column='co_conselho_classe', blank=True, null=True
    )
    nu_cpf = models.CharField(max_length=11, blank=True, null=True)
    nu_cns = models.CharField(max_length=16, blank=True, null=True)
    no_profissional = models.CharField(max_length=500, blank=True, null=True)
    no_profissional_filtro = models.CharField(max_length=600, blank=True, null=True)
    dt_nascimento = models.DateField(blank=True, null=True)
    nu_telefone = models.CharField(max_length=255, blank=True, null=True)
    ds_email = models.CharField(max_length=255, blank=True, null=True)
    ds_cep = models.CharField(max_length=8, blank=True, null=True)
    ds_complemento = models.CharField(max_length=50, blank=True, null=True)
    ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
    ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
    co_uf = models.ForeignKey(
        'esus.TbUf', on_delete=models.DO_NOTHING, db_column='co_uf', 
        blank=True, null=True
    )
    co_localidade_endereco = models.ForeignKey(
        'esus.TbLocalidade', on_delete=models.DO_NOTHING, 
        db_column='co_localidade_endereco', blank=True, null=True
    )
    nu_numero = models.CharField(max_length=20, blank=True, null=True)
    st_sem_numero = models.IntegerField(blank=True, null=True)
    no_bairro = models.CharField(max_length=255, blank=True, null=True)
    no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
    tp_logradouro = models.ForeignKey(
        'esus.TbTipoLogradouro', on_delete=models.DO_NOTHING, 
        db_column='tp_logradouro', blank=True, null=True
    )
    co_usuario = models.ForeignKey(
        'esus.TbUsuario', on_delete=models.DO_NOTHING, 
        db_column='co_usuario', blank=True, null=True
    )
    no_sexo = models.CharField(max_length=24, blank=True, null=True)

    def __str__(self):
        return self.no_profissional

    class Meta:
        managed = False
        db_table = 'tb_prof'


class TbSituacaoAgendado(models.Model):
    co_situacao_agendado = models.BigIntegerField(primary_key=True)
    no_situacao_agendado = models.CharField(max_length=50, blank=True, null=True)
    no_identificador = models.CharField(max_length=30)

    def __str__(self):
        return self.no_situacao_agendado

    class Meta:
        managed = False
        db_table = 'tb_situacao_agendado'


class TbMotivoReserva(models.Model):
    co_motivo_reserva = models.BigIntegerField(primary_key=True)
    no_motivo_reserva = models.CharField(max_length=50)

    def __str__(self):
        return self.no_motivo_reserva

    class Meta:
        managed = False
        db_table = 'tb_motivo_reserva'


class TbOrigem(models.Model):
    co_origem = models.BigIntegerField(primary_key=True)
    ds_origem = models.CharField(max_length=30)
    no_identificador = models.CharField(max_length=30)

    def __str__(self):
        return self.ds_origem

    class Meta:
        managed = False
        db_table = 'tb_origem'


class TbUsuario(models.Model):
    co_seq_usuario = models.BigIntegerField(primary_key=True)
    st_bloqueado = models.IntegerField()
    ds_senha = models.CharField(max_length=255, blank=True, null=True)
    st_trocar_senha = models.IntegerField()
    co_ator = models.ForeignKey(
        'esus.TbAtor', on_delete=models.DO_NOTHING, 
        db_column='co_ator', blank=True, null=True
    )
    dt_ultima_atualizacao_senha = models.DateField(blank=True, null=True)
    st_termo_uso = models.IntegerField(blank=True, null=True)
    st_forcar_troca_senha = models.IntegerField()
    nr_tentativas_acesso = models.IntegerField()
    ds_login = models.CharField(unique=True, max_length=255, blank=True, null=True)
    dt_envio_email_recuperar_senha = models.DateTimeField(blank=True, null=True)
    st_visualizou_novidades = models.IntegerField(blank=True, null=True)
    st_pesquisa_respondida = models.IntegerField(blank=True, null=True)
    dt_primeiro_login_versao = models.DateTimeField(blank=True, null=True)
    dt_pesquisa_respondida = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.ds_login

    class Meta:
        managed = False
        db_table = 'tb_usuario'


class TbAtor(models.Model):
    co_seq_ator = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return str(self.co_seq_ator)

    class Meta:
        managed = False
        db_table = 'tb_ator'


class TbRegistroVacinacao(models.Model):
    co_seq_registro_vacinacao = models.BigIntegerField(primary_key=True)
    co_estrategia_vacinacao = models.ForeignKey(
        'esus.TbEstrategiaVacinacao', on_delete=models.DO_NOTHING, 
        db_column='co_estrategia_vacinacao', blank=True, null=True
    )
    co_dim_imunobiologico = models.ForeignKey(
        'esus.TbImunobiologico', on_delete=models.DO_NOTHING, 
        db_column='co_imunobiologico', blank=True, null=True
    )
    co_dim_dose_imunobiologico = models.ForeignKey(
        'esus.TbDoseImunobiologico', on_delete=models.DO_NOTHING, 
        db_column='co_dose_imunobiologico', blank=True, null=True
    )
    co_via_adm_vacina = models.ForeignKey(
        'esus.TbViaAdmVacina', on_delete=models.DO_NOTHING, 
        db_column='co_via_adm_vacina', blank=True, null=True
    )
    co_local_apl_vacina = models.ForeignKey(
        'esus.TbLocalAplVacina', on_delete=models.DO_NOTHING, 
        db_column='co_local_apl_vacina', blank=True, null=True
    )
    co_vacinacao = models.ForeignKey(
        'esus.TbVacinacao', on_delete=models.DO_NOTHING, 
        db_column='co_vacinacao', blank=True, null=True,
        related_name='vacinacao_registros_set'
    )
    co_tipo_registro_vacinacao = models.ForeignKey(
        'esus.TbTipoRegistroVacinacao', on_delete=models.DO_NOTHING, 
        db_column='co_tipo_registro_vacinacao', blank=True, null=True
    )
    st_registro_anterior = models.IntegerField(blank=True, null=True)
    dt_aprazamento = models.DateField(blank=True, null=True)
    dt_aplicacao = models.DateTimeField(blank=True, null=True)
    co_imunobiologico_lote = models.ForeignKey(
        'esus.TbImunobiologicoLote', on_delete=models.DO_NOTHING, 
        db_column='co_imunobiologico_lote', blank=True, null=True
    )
    ds_observacoes = models.CharField(max_length=300, blank=True, null=True)
    co_grupo_atendimento = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_registro_vacinacao)

    class Meta:
        managed = False
        db_table = 'tb_registro_vacinacao'


class TbEstrategiaVacinacao(models.Model):
    co_estrategia_vacinacao = models.BigIntegerField(primary_key=True)
    nu_estrategia_vacinacao = models.CharField(max_length=10, blank=True, null=True)
    no_estrategia_vacinacao = models.CharField(max_length=255, blank=True, null=True)
    no_estrategia_vacinacao_filtro = models.CharField(max_length=255, blank=True, null=True)
    no_identificador = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_estrategia_vacinacao

    class Meta:
        managed = False
        db_table = 'tb_estrategia_vacinacao'


class TbImunobiologico(models.Model):
    nu_identificador = models.BigIntegerField(primary_key=True, db_column='co_imunobiologico')
    sg_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    no_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    no_filtro_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    co_classe_imunobiologico = models.ForeignKey(
        'esus.TbClasseImunobiologico', on_delete=models.DO_NOTHING, 
        db_column='co_classe_imunobiologico', blank=True, null=True
    )
    st_ativo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.no_imunobiologico

    class Meta:
        managed = False
        db_table = 'tb_imunobiologico'


class TbDoseImunobiologico(models.Model):
    nu_identificador = models.BigIntegerField(primary_key=True, db_column='co_dose_imunobiologico')
    sg_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    no_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    nu_ordem = models.IntegerField(blank=True, null=True)
    no_apresentacao_dose = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_dose_imunobiologico

    class Meta:
        managed = False
        db_table = 'tb_dose_imunobiologico'


class TbViaAdmVacina(models.Model):
    co_via_adm_vacina = models.BigIntegerField(primary_key=True)
    no_via_adm_vacina = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_via_adm_vacina

    class Meta:
        managed = False
        db_table = 'tb_via_adm_vacina'


class TbLocalAplVacina(models.Model):
    co_local_apl_vacina = models.BigIntegerField(primary_key=True)
    no_local_apl_vacina = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_local_apl_vacina

    class Meta:
        managed = False
        db_table = 'tb_local_apl_vacina'


class TbTipoRegistroVacinacao(models.Model):
    co_tipo_registro_vacinacao = models.BigIntegerField(primary_key=True)
    no_tipo_registro_vacinacao = models.CharField(max_length=255, blank=True, null=True)
    no_identificador = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_tipo_registro_vacinacao

    class Meta:
        managed = False
        db_table = 'tb_tipo_registro_vacinacao'


class TbImunobiologicoLote(models.Model):
    co_seq_imunobiologico_lote = models.BigIntegerField(primary_key=True)
    co_imunobiologico = models.ForeignKey(
        'esus.TbImunobiologico', on_delete=models.DO_NOTHING, 
        db_column='co_imunobiologico', blank=True, null=True
    )
    ds_lote = models.CharField(max_length=255, blank=True, null=True)
    ds_lote_filtro = models.CharField(max_length=255, blank=True, null=True)
    ds_lote_fabricante_filtro = models.CharField(max_length=255, blank=True, null=True)
    dt_validade = models.DateField(blank=True, null=True)
    co_imunobiologico_fabricante = models.BigIntegerField(blank=True, null=True)
    st_ativo = models.IntegerField()
    co_unidade_saude = models.ForeignKey(
        'esus.TbUnidadeSaude', on_delete=models.DO_NOTHING, 
        db_column='co_unidade_saude', blank=True, null=True
    )

    def __str__(self):
        return self.ds_lote

    class Meta:
        managed = False
        db_table = 'tb_imunobiologico_lote'


class TbClasseImunobiologico(models.Model):
    co_classe_imunobiologico = models.BigIntegerField(primary_key=True)
    no_classe_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
    no_identificador = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_classe_imunobiologico
    class Meta:
        managed = False
        db_table = 'tb_classe_imunobiologico'
