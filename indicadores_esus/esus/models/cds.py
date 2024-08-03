from django.db import models


class TbCdsProf(models.Model):
    co_seq_cds_prof = models.BigIntegerField(primary_key=True)
    nu_cns = models.CharField(max_length=16, blank=True, null=True)
    nu_ine = models.CharField(max_length=255, blank=True, null=True)
    nu_cbo_2002 = models.CharField(max_length=10, blank=True, null=True)
    nu_cnes = models.CharField(max_length=255, blank=True, null=True)
    co_unico_cds_prof = models.CharField(unique=True, max_length=40)

    def __str__(self):
        return self.nu_cns

    class Meta:
        managed = False
        db_table = 'tb_cds_prof'


class TbCdsFichaAtendIndividual(models.Model):
    co_seq_cds_ficha_atend_indivdl = models.BigIntegerField(primary_key=True)
    dt_ficha = models.DateTimeField(blank=True, null=True)
    st_ficha = models.IntegerField(blank=True, null=True)
    tp_cds_origem = models.BigIntegerField(blank=True, null=True)
    co_unico_ficha = models.CharField(max_length=96)
    co_cds_prof = models.ForeignKey(
        'esus.TbCdsProf', on_delete=models.DO_NOTHING, db_column='co_cds_prof'
    )
    co_localidade_origem = models.ForeignKey(
        'esus.TbLocalidade', on_delete=models.DO_NOTHING,
        db_column='co_localidade_origem', blank=True, null=True
    )
    ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.co_unico_ficha

    class Meta:
        managed = False
        db_table = 'tb_cds_ficha_atend_individual'


class TbCdsAleitamentoMaterno(models.Model):
    co_cds_aleitamento_materno = models.BigIntegerField(primary_key=True)
    no_cds_aleitamento_materno = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.no_cds_aleitamento_materno

    class Meta:
        managed = False
        db_table = 'tb_cds_aleitamento_materno'


class TbCdsPic(models.Model):
    co_cds_pic = models.BigIntegerField(primary_key=True)
    no_cds_pic = models.CharField(max_length=255)
    no_cds_pic_filtro = models.CharField(max_length=255)

    def __str__(self):
        return self.no_cds_pic

    class Meta:
        managed = False
        db_table = 'tb_cds_pic'


class TbCdsTurno(models.Model):
    co_cds_turno = models.BigIntegerField(primary_key=True)
    no_cds_turno = models.CharField(max_length=255)
    no_identificador = models.CharField(max_length=255)

    def __str__(self):
        return self.no_cds_turno

    class Meta:
        managed = False
        db_table = 'tb_cds_turno'


class TbCdsAtendIndividual(models.Model):
    co_seq_cds_atend_individual = models.BigIntegerField(primary_key=True)
    co_cds_ficha_atend_individual = models.ForeignKey(
        'esus.TbCdsFichaAtendIndividual', on_delete=models.DO_NOTHING,
        db_column='co_cds_ficha_atend_individual'
    )
    co_prontuario = models.ForeignKey(
        'esus.TbProntuario', on_delete=models.DO_NOTHING,
        db_column='co_prontuario', blank=True, null=True
    )
    nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
    nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
    dt_nascimento = models.DateTimeField()
    co_local_atend = models.ForeignKey(
        'esus.TbLocalAtend', on_delete=models.DO_NOTHING,
        db_column='co_local_atend', blank=True, null=True
    )
    co_cds_aleitamento_materno = models.ForeignKey(
        'esus.TbCdsAleitamentoMaterno', on_delete=models.DO_NOTHING,
        db_column='co_cds_aleitamento_materno', blank=True, null=True
    )
    dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
    co_cds_pic = models.ForeignKey(
        'esus.TbCdsPic', on_delete=models.DO_NOTHING, db_column='co_cds_pic',
        blank=True, null=True
    )
    co_cid10 = models.ForeignKey(
        'esus.TbCid10', on_delete=models.DO_NOTHING, db_column='co_cid10',
        blank=True, null=True
    )
    st_ficou_observacao = models.IntegerField(blank=True, null=True)
    st_vacina_em_dia = models.IntegerField(blank=True, null=True)
    nu_idade_gestacional = models.IntegerField(blank=True, null=True)
    co_ad_modalidade = models.ForeignKey(
        'esus.TbAdModalidade', on_delete=models.DO_NOTHING,
        db_column='co_ad_modalidade', blank=True, null=True
    )
    nu_peso = models.FloatField(blank=True, null=True)
    nu_altura = models.FloatField(blank=True, null=True)
    co_sexo = models.ForeignKey(
        'esus.TbSexo', on_delete=models.DO_NOTHING, db_column='co_sexo',
        blank=True, null=True
    )
    tp_atend = models.ForeignKey(
        'esus.TbTipoAtend', on_delete=models.DO_NOTHING, db_column='tp_atend',
        blank=True, null=True
    )
    co_cds_turno = models.ForeignKey(
        'esus.TbCdsTurno', on_delete=models.DO_NOTHING,
        db_column='co_cds_turno', blank=True, null=True
    )
    st_gravidez_planejada = models.IntegerField(blank=True, null=True)
    qt_gestacao_previa = models.IntegerField(blank=True, null=True)
    qt_parto = models.IntegerField(blank=True, null=True)
    co_racionalidade_saude = models.ForeignKey(
        'esus.TbRacionalidadeSaude', on_delete=models.DO_NOTHING,
        db_column='co_racionalidade_saude', blank=True, null=True
    )
    nu_perimetro_cefalico = models.DecimalField(
        max_digits=19, decimal_places=4, blank=True, null=True
    )
    co_cid10_2 = models.ForeignKey(
        'esus.TbCid10', on_delete=models.DO_NOTHING, db_column='co_cid10_2',
        blank=True, null=True, related_name='cid10_atendindcds_2_set'
    )
    nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return str(self.co_seq_cds_atend_individual)

    class Meta:
        managed = False
        db_table = 'tb_cds_atend_individual'
