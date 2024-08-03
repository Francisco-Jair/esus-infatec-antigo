# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class TbMigracaoDados(models.Model):
#     installed_rank = models.DecimalField(primary_key=True, max_digits=38, decimal_places=0)
#     version = models.CharField(max_length=50, blank=True, null=True)
#     description = models.CharField(max_length=200)
#     type = models.CharField(max_length=20)
#     script = models.CharField(max_length=1000)
#     checksum = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
#     installed_by = models.CharField(max_length=100)
#     installed_on = models.DateTimeField()
#     execution_time = models.DecimalField(max_digits=38, decimal_places=0)
#     success = models.BooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'TB_MIGRACAO_DADOS'
#
#
# class RlAntecedenteCiap(models.Model):
#     co_prontuario = models.OneToOneField('TbAntecedente', models.DO_NOTHING, db_column='co_prontuario', primary_key=True)
#     co_ciap = models.ForeignKey('TbCiap', models.DO_NOTHING, db_column='co_ciap')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_antecedente_ciap'
#         unique_together = (('co_prontuario', 'co_ciap'),)
#
#
# class RlAtendProced(models.Model):
#     co_seq_atend_proced = models.BigIntegerField(primary_key=True)
#     st_obrigatorio = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.ForeignKey('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof')
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#     co_cid10_principal = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_principal', blank=True, null=True)
#     st_automatico = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_atend_proced'
#
#
# class RlAtendProfAdTipoInelegvl(models.Model):
#     co_atend_prof_ad = models.OneToOneField('TbAtendProfAd', models.DO_NOTHING, db_column='co_atend_prof_ad', primary_key=True)
#     tp_ad_inelegivel = models.ForeignKey('TbAdTipoInelegivel', models.DO_NOTHING, db_column='tp_ad_inelegivel')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_atend_prof_ad_tipo_inelegvl'
#         unique_together = (('co_atend_prof_ad', 'tp_ad_inelegivel'),)
#
#
# class RlAtendProfConduta(models.Model):
#     co_atend_prof = models.OneToOneField('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof', primary_key=True)
#     tp_cds_conduta = models.ForeignKey('TbCdsTipoConduta', models.DO_NOTHING, db_column='tp_cds_conduta')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_atend_prof_conduta'
#         unique_together = (('co_atend_prof', 'tp_cds_conduta'),)
#
#
# class RlAtendProfOdontoTipoEncm(models.Model):
#     co_atend_prof_odonto = models.OneToOneField('TbAtendProfOdonto', models.DO_NOTHING, db_column='co_atend_prof_odonto', primary_key=True)
#     tp_encam_odonto = models.ForeignKey('TbTipoEncamOdonto', models.DO_NOTHING, db_column='tp_encam_odonto')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_atend_prof_odonto_tipo_encm'
#         unique_together = (('co_atend_prof_odonto', 'tp_encam_odonto'),)
#
#
# class RlAtendProfOdontoTipoFrnc(models.Model):
#     co_atend_prof_odonto = models.OneToOneField('TbAtendProfOdonto', models.DO_NOTHING, db_column='co_atend_prof_odonto', primary_key=True)
#     tp_fornecimento_odonto = models.ForeignKey('TbTipoFornecOdonto', models.DO_NOTHING, db_column='tp_fornecimento_odonto')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_atend_prof_odonto_tipo_frnc'
#         unique_together = (('co_atend_prof_odonto', 'tp_fornecimento_odonto'),)
#
#
# class RlAtendProfPic(models.Model):
#     co_cds_pic = models.ForeignKey('TbCdsPic', models.DO_NOTHING, db_column='co_cds_pic')
#     co_atend_prof = models.OneToOneField('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_atend_prof_pic'
#         unique_together = (('co_atend_prof', 'co_cds_pic'),)
#
#
# class RlAtendTipoServico(models.Model):
#     tp_servico = models.ForeignKey('TbTipoServico', models.DO_NOTHING, db_column='tp_servico')
#     co_atend = models.OneToOneField('TbAtend', models.DO_NOTHING, db_column='co_atend', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_atend_tipo_servico'
#         unique_together = (('co_atend', 'tp_servico'),)
#
#
# class RlAtorPapelPerfil(models.Model):
#     co_ator_papel = models.OneToOneField('TbAtorPapel', models.DO_NOTHING, db_column='co_ator_papel', primary_key=True)
#     co_perfil = models.ForeignKey('TbPerfil', models.DO_NOTHING, db_column='co_perfil')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_ator_papel_perfil'
#         unique_together = (('co_ator_papel', 'co_perfil'),)
#
#
# class RlCalendarioVacnlGrupoAlvo(models.Model):
#     co_calendario_vacnl_grupo_alvo = models.BigIntegerField(primary_key=True)
#     co_calendario_vacinal = models.ForeignKey('TbCalendarioVacinal', models.DO_NOTHING, db_column='co_calendario_vacinal', blank=True, null=True)
#     co_grupo_alvo_vacinacao = models.ForeignKey('TbGrupoAlvoVacinacao', models.DO_NOTHING, db_column='co_grupo_alvo_vacinacao', blank=True, null=True)
#     co_faixa_etaria_vacinacao = models.ForeignKey('TbFaixaEtariaVacinacao', models.DO_NOTHING, db_column='co_faixa_etaria_vacinacao', blank=True, null=True)
#     ds_faixa_etaria = models.CharField(max_length=255, blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_calendario_vacnl_grupo_alvo'
#
#
# class RlCdsAtendDomProced(models.Model):
#     co_cds_atend_domiciliar = models.OneToOneField('TbCdsAtendDomiciliar', models.DO_NOTHING, db_column='co_cds_atend_domiciliar', primary_key=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_dom_proced'
#         unique_together = (('co_cds_atend_domiciliar', 'co_proced'),)
#
#
# class RlCdsAtendDomSituacaoPres(models.Model):
#     co_cds_atend_domiciliar = models.OneToOneField('TbCdsAtendDomiciliar', models.DO_NOTHING, db_column='co_cds_atend_domiciliar', primary_key=True)
#     co_cds_situacao_presente = models.ForeignKey('TbCdsTipoSituacaoPresente', models.DO_NOTHING, db_column='co_cds_situacao_presente')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_dom_situacao_pres'
#         unique_together = (('co_cds_atend_domiciliar', 'co_cds_situacao_presente'),)
#
#
# class RlCdsAtendIndividualCiap(models.Model):
#     co_cds_atend_individual = models.OneToOneField('TbCdsAtendIndividual', models.DO_NOTHING, db_column='co_cds_atend_individual', primary_key=True)
#     co_ciap = models.ForeignKey('TbCiap', models.DO_NOTHING, db_column='co_ciap')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_individual_ciap'
#         unique_together = (('co_cds_atend_individual', 'co_ciap'),)
#
#
# class RlCdsAtendIndividualCondut(models.Model):
#     co_cds_atend_individual = models.OneToOneField('TbCdsAtendIndividual', models.DO_NOTHING, db_column='co_cds_atend_individual', primary_key=True)
#     tp_cds_conduta = models.ForeignKey('TbCdsTipoConduta', models.DO_NOTHING, db_column='tp_cds_conduta')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_individual_condut'
#         unique_together = (('co_cds_atend_individual', 'tp_cds_conduta'),)
#
#
# class RlCdsAtendIndividualExame(models.Model):
#     co_cds_atend_individual = models.OneToOneField('TbCdsAtendIndividual', models.DO_NOTHING, db_column='co_cds_atend_individual', primary_key=True)
#     co_exame = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_exame')
#     st_solicitado_avaliado = models.CharField(max_length=1)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_individual_exame'
#         unique_together = (('co_cds_atend_individual', 'co_exame', 'st_solicitado_avaliado'),)
#
#
# class RlCdsAtendIndividualNasf(models.Model):
#     co_cds_atend_individual = models.OneToOneField('TbCdsAtendIndividual', models.DO_NOTHING, db_column='co_cds_atend_individual', primary_key=True)
#     tp_cds_atend_nasf = models.ForeignKey('TbCdsTipoAtendNasf', models.DO_NOTHING, db_column='tp_cds_atend_nasf')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_individual_nasf'
#         unique_together = (('co_cds_atend_individual', 'tp_cds_atend_nasf'),)
#
#
# class RlCdsAtendOdontTipVigBuc(models.Model):
#     co_cds_atend_odonto = models.OneToOneField('TbCdsAtendOdonto', models.DO_NOTHING, db_column='co_cds_atend_odonto', primary_key=True)
#     tp_cds_vig_saude_bucal = models.ForeignKey('TbCdsTipoVigSaudeBucal', models.DO_NOTHING, db_column='tp_cds_vig_saude_bucal')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_odont_tip_vig_buc'
#         unique_together = (('co_cds_atend_odonto', 'tp_cds_vig_saude_bucal'),)
#
#
# class RlCdsAtendOdontoProced(models.Model):
#     co_cds_atend_odonto = models.OneToOneField('TbCdsAtendOdonto', models.DO_NOTHING, db_column='co_cds_atend_odonto', primary_key=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#     qt_atend_odonto_proced = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_odonto_proced'
#         unique_together = (('co_cds_atend_odonto', 'co_proced'),)
#
#
# class RlCdsAtendOdontoTipoCnslt(models.Model):
#     co_cds_atend_odonto = models.OneToOneField('TbCdsAtendOdonto', models.DO_NOTHING, db_column='co_cds_atend_odonto', primary_key=True)
#     tp_consulta_odonto = models.ForeignKey('TbTipoConsultaOdonto', models.DO_NOTHING, db_column='tp_consulta_odonto')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_odonto_tipo_cnslt'
#         unique_together = (('co_cds_atend_odonto', 'tp_consulta_odonto'),)
#
#
# class RlCdsAtendOdontoTipoEncam(models.Model):
#     co_cds_atend_odonto = models.OneToOneField('TbCdsAtendOdonto', models.DO_NOTHING, db_column='co_cds_atend_odonto', primary_key=True)
#     tp_encam_odonto = models.ForeignKey('TbTipoEncamOdonto', models.DO_NOTHING, db_column='tp_encam_odonto')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_odonto_tipo_encam'
#         unique_together = (('co_cds_atend_odonto', 'tp_encam_odonto'),)
#
#
# class RlCdsAtendOdontoTipoFornc(models.Model):
#     co_cds_atend_odonto = models.OneToOneField('TbCdsAtendOdonto', models.DO_NOTHING, db_column='co_cds_atend_odonto', primary_key=True)
#     tp_fornecimento_odonto = models.ForeignKey('TbTipoFornecOdonto', models.DO_NOTHING, db_column='tp_fornecimento_odonto')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_atend_odonto_tipo_fornc'
#         unique_together = (('co_cds_atend_odonto', 'tp_fornecimento_odonto'),)
#
#
# class RlCdsAvalElegAdTipoInelg(models.Model):
#     co_cds_aval_elegibilidade = models.OneToOneField('TbCdsAvalElegibilidade', models.DO_NOTHING, db_column='co_cds_aval_elegibilidade', primary_key=True)
#     tp_ad_inelegivel = models.ForeignKey('TbAdTipoInelegivel', models.DO_NOTHING, db_column='tp_ad_inelegivel')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_aval_eleg_ad_tipo_inelg'
#         unique_together = (('co_cds_aval_elegibilidade', 'tp_ad_inelegivel'),)
#
#
# class RlCdsAvalElegCdsSitucPrs(models.Model):
#     co_cds_aval_elegibilidade = models.OneToOneField('TbCdsAvalElegibilidade', models.DO_NOTHING, db_column='co_cds_aval_elegibilidade', primary_key=True)
#     tp_cds_situacao_presente = models.ForeignKey('TbCdsTipoSituacaoPresente', models.DO_NOTHING, db_column='tp_cds_situacao_presente')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_aval_eleg_cds_situc_prs'
#         unique_together = (('co_cds_aval_elegibilidade', 'tp_cds_situacao_presente'),)
#
#
# class RlCdsFichaAtendIndivdlPrf(models.Model):
#     co_cds_ficha_atend_individual = models.OneToOneField('TbCdsFichaAtendIndividual', models.DO_NOTHING, db_column='co_cds_ficha_atend_individual', primary_key=True)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_ficha_atend_indivdl_prf'
#         unique_together = (('co_cds_ficha_atend_individual', 'co_cds_prof'),)
#
#
# class RlCdsFichaAtendOdontoProf(models.Model):
#     co_cds_ficha_atend_odonto = models.OneToOneField('TbCdsFichaAtendOdonto', models.DO_NOTHING, db_column='co_cds_ficha_atend_odonto', primary_key=True)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_ficha_atend_odonto_prof'
#         unique_together = (('co_cds_ficha_atend_odonto', 'co_cds_prof'),)
#
#
# class RlCdsFichaAtivColPratica(models.Model):
#     co_cds_ficha_ativ_col = models.OneToOneField('TbCdsFichaAtivCol', models.DO_NOTHING, db_column='co_cds_ficha_ativ_col', primary_key=True)
#     co_cds_ativ_col_pratica = models.ForeignKey('TbCdsAtivColPratica', models.DO_NOTHING, db_column='co_cds_ativ_col_pratica')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_ficha_ativ_col_pratica'
#         unique_together = (('co_cds_ficha_ativ_col', 'co_cds_ativ_col_pratica'),)
#
#
# class RlCdsFichaAtivColProf(models.Model):
#     co_cds_ficha_ativ_col = models.OneToOneField('TbCdsFichaAtivCol', models.DO_NOTHING, db_column='co_cds_ficha_ativ_col', primary_key=True)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_ficha_ativ_col_prof'
#         unique_together = (('co_cds_ficha_ativ_col', 'co_cds_prof'),)
#
#
# class RlCdsFichaAtivColPubAlvo(models.Model):
#     co_cds_ficha_ativ_col = models.ForeignKey('TbCdsFichaAtivCol', models.DO_NOTHING, db_column='co_cds_ficha_ativ_col')
#     co_cds_ativ_col_publico_alvo = models.OneToOneField('TbCdsAtivColPublicoAlvo', models.DO_NOTHING, db_column='co_cds_ativ_col_publico_alvo', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_ficha_ativ_col_pub_alvo'
#         unique_together = (('co_cds_ativ_col_publico_alvo', 'co_cds_ficha_ativ_col'),)
#
#
# class RlCdsFichaAtivColTema(models.Model):
#     co_cds_ficha_ativ_col = models.ForeignKey('TbCdsFichaAtivCol', models.DO_NOTHING, db_column='co_cds_ficha_ativ_col')
#     co_cds_ativ_col_tema = models.OneToOneField('TbCdsAtivColTema', models.DO_NOTHING, db_column='co_cds_ativ_col_tema', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_ficha_ativ_col_tema'
#         unique_together = (('co_cds_ativ_col_tema', 'co_cds_ficha_ativ_col'),)
#
#
# class RlCdsProcedAdmMedicamento(models.Model):
#     co_cds_proced = models.OneToOneField('RlProcedCdsProced', models.DO_NOTHING, db_column='co_cds_proced', primary_key=True)
#     co_proced = models.BigIntegerField()
#     co_cds_adm_medicamento = models.ForeignKey('TbCdsAdmMedicamento', models.DO_NOTHING, db_column='co_cds_adm_medicamento')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_proced_adm_medicamento'
#         unique_together = (('co_cds_proced', 'co_proced', 'co_cds_adm_medicamento'),)
#
#
# class RlCdsProntuarioUnidadeSaud(models.Model):
#     co_prontuario = models.OneToOneField('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', primary_key=True)
#     co_ator_papel = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_ator_papel')
#     nu_prontuario_interno = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_prontuario_unidade_saud'
#         unique_together = (('co_prontuario', 'co_ator_papel'),)
#
#
# class RlCdsVisitaDomMotivo(models.Model):
#     co_cds_visita_domiciliar = models.OneToOneField('TbCdsVisitaDomiciliar', models.DO_NOTHING, db_column='co_cds_visita_domiciliar', primary_key=True)
#     co_cds_visita_dom_motivo = models.ForeignKey('TbCdsVisitaDomMotivo', models.DO_NOTHING, db_column='co_cds_visita_dom_motivo')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_cds_visita_dom_motivo'
#         unique_together = (('co_cds_visita_domiciliar', 'co_cds_visita_dom_motivo'),)
#
#
# class RlCiapCid10(models.Model):
#     co_ciap = models.OneToOneField('TbCiap', models.DO_NOTHING, db_column='co_ciap', primary_key=True)
#     co_cid10 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_ciap_cid10'
#         unique_together = (('co_ciap', 'co_cid10'),)
#
#
# class RlEvolAvalTpVigSaudeBucl(models.Model):
#     co_evolucao_avaliacao = models.OneToOneField('TbEvolucaoAvaliacao', models.DO_NOTHING, db_column='co_evolucao_avaliacao', primary_key=True)
#     co_tipo_vig_saude_bucal = models.ForeignKey('TbCdsTipoVigSaudeBucal', models.DO_NOTHING, db_column='co_tipo_vig_saude_bucal')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_evol_aval_tp_vig_saude_bucl'
#         unique_together = (('co_evolucao_avaliacao', 'co_tipo_vig_saude_bucal'),)
#
#
# class RlEvolucaoAvaliacaoCiapCid(models.Model):
#     co_seq_evolucao_aval_ciap_cid = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof')
#     co_ciap = models.ForeignKey('TbCiap', models.DO_NOTHING, db_column='co_ciap', blank=True, null=True)
#     co_cid10 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10', blank=True, null=True)
#     ds_nota = models.CharField(max_length=400, blank=True, null=True)
#     co_unico_problema = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_evolucao_avaliacao_ciap_cid'
#
#
# class RlEvolucaoOdontoParteBucal(models.Model):
#     co_evolucao_odonto = models.OneToOneField('TbEvolucaoOdonto', models.DO_NOTHING, db_column='co_evolucao_odonto', primary_key=True)
#     co_parte_bucal = models.ForeignKey('TbParteBucal', models.DO_NOTHING, db_column='co_parte_bucal')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_evolucao_odonto_parte_bucal'
#         unique_together = (('co_evolucao_odonto', 'co_parte_bucal'),)
#
#
# class RlEvolucaoOdontoProced(models.Model):
#     co_evolucao_odonto = models.OneToOneField('TbEvolucaoOdonto', models.DO_NOTHING, db_column='co_evolucao_odonto', primary_key=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_evolucao_odonto_proced'
#         unique_together = (('co_evolucao_odonto', 'co_proced'),)
#
#
# class RlEvolucaoPlanoCiap(models.Model):
#     co_seq_evolucao_plano_ciap = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof')
#     co_ciap = models.ForeignKey('TbCiap', models.DO_NOTHING, db_column='co_ciap', blank=True, null=True)
#     ds_nota = models.CharField(max_length=400, blank=True, null=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_evolucao_plano_ciap'
#
#
# class RlEvolucaoSubjetivoCiap(models.Model):
#     co_seq_evolucao_subjetivo_ciap = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof')
#     co_ciap = models.ForeignKey('TbCiap', models.DO_NOTHING, db_column='co_ciap')
#     ds_nota = models.CharField(max_length=400, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_evolucao_subjetivo_ciap'
#
#
# class RlGrupoAtivColCidadao(models.Model):
#     co_seq_grp_ativ_col_cidadao = models.BigIntegerField(primary_key=True)
#     co_grupo = models.ForeignKey('TbGrupoAtivCol', models.DO_NOTHING, db_column='co_grupo')
#     co_cidadao = models.ForeignKey('TbCidadaoGrupoAtivCol', models.DO_NOTHING, db_column='co_cidadao')
#     st_cidadao = models.CharField(max_length=32, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_grupo_ativ_col_cidadao'
#         unique_together = (('co_grupo', 'co_cidadao'),)
#
#
# class RlGrupoAtivColProf(models.Model):
#     co_seq_grp_ativ_col_prof = models.BigIntegerField(primary_key=True)
#     co_grupo = models.ForeignKey('TbGrupoAtivCol', models.DO_NOTHING, db_column='co_grupo')
#     co_prof = models.ForeignKey('TbProfGrupoAtivCol', models.DO_NOTHING, db_column='co_prof')
#     st_prof = models.CharField(max_length=32, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_grupo_ativ_col_prof'
#         unique_together = (('co_grupo', 'co_prof'),)
#
#
# class RlGrupoCondicaoCiapCid(models.Model):
#     co_seq_grupo_ciap_cid = models.BigIntegerField(primary_key=True)
#     co_grupo_condicao = models.ForeignKey('TbGrupoCondicaoSaude', models.DO_NOTHING, db_column='co_grupo_condicao')
#     co_ciap = models.ForeignKey('TbCiap', models.DO_NOTHING, db_column='co_ciap', blank=True, null=True)
#     co_cid10 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_grupo_condicao_ciap_cid'
#
#
# class RlHistoricoCabecalho(models.Model):
#     co_ficha_origem_concatenacao = models.ForeignKey(
#         'TbHistoricoCabecalho', on_delete=models.DO_NOTHING,
#         db_column='co_ficha_origem_concatenacao', related_name='rl_historicos'
#     )
#     co_ficha_concatenada = models.OneToOneField('TbHistoricoCabecalho', models.DO_NOTHING, db_column='co_ficha_concatenada', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_historico_cabecalho'
#
#
# class RlPerfilCboPadrao(models.Model):
#     co_cbo = models.OneToOneField('TbCbo', models.DO_NOTHING, db_column='co_cbo', primary_key=True)
#     no_perfil_padrao = models.CharField(max_length=100)
#     no_perfil_padrao_ad = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_perfil_cbo_padrao'
#         unique_together = (('co_cbo', 'no_perfil_padrao'),)
#
#
# class RlProcedAtributoComplem(models.Model):
#     co_proced = models.OneToOneField('TbProced', models.DO_NOTHING, db_column='co_proced', primary_key=True)
#     co_atributo_complem = models.ForeignKey('TbAtributoComplem', models.DO_NOTHING, db_column='co_atributo_complem')
#     dt_competencia = models.CharField(max_length=60)
#     st_ativo = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'rl_proced_atributo_complem'
#         unique_together = (('co_proced', 'co_atributo_complem'),)
#
#
# class RlProcedCbo(models.Model):
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#     co_cbo = models.OneToOneField('TbCbo', models.DO_NOTHING, db_column='co_cbo', primary_key=True)
#     dt_competencia = models.CharField(max_length=6)
#     st_ativo = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'rl_proced_cbo'
#         unique_together = (('co_cbo', 'co_proced'),)
#
#
# class RlProcedCdsProced(models.Model):
#     co_cds_proced = models.OneToOneField('TbCdsProced', models.DO_NOTHING, db_column='co_cds_proced', primary_key=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_proced_cds_proced'
#         unique_together = (('co_cds_proced', 'co_proced'),)
#
#
# class RlProcedCid10(models.Model):
#     co_cid10 = models.OneToOneField('TbCid10', models.DO_NOTHING, db_column='co_cid10', primary_key=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#     dt_competencia = models.CharField(max_length=6)
#     st_ativo = models.IntegerField()
#     st_cid_principal = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_proced_cid10'
#         unique_together = (('co_cid10', 'co_proced'),)
#
#
# class RlProcedExameDetalhe(models.Model):
#     co_seq_proced_exame_detalhe = models.BigIntegerField(primary_key=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced', blank=True, null=True)
#     co_exame_detalhe = models.ForeignKey('TbExameDetalhe', models.DO_NOTHING, db_column='co_exame_detalhe', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_proced_exame_detalhe'
#
#
# class RlProcedGrupoExame(models.Model):
#     co_seq_proced_grupo_exame = models.BigIntegerField(primary_key=True)
#     co_grupo_exame = models.ForeignKey('TbGrupoExame', models.DO_NOTHING, db_column='co_grupo_exame')
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_proced_grupo_exame'
#         unique_together = (('co_grupo_exame', 'co_proced'),)
#
#
# class RlProcedTipoRegistro(models.Model):
#     co_proced = models.OneToOneField('TbProced', models.DO_NOTHING, db_column='co_proced', primary_key=True)
#     tp_registro = models.ForeignKey('TbTipoRegistro', models.DO_NOTHING, db_column='tp_registro')
#     dt_competencia = models.CharField(max_length=6)
#     st_ativo = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'rl_proced_tipo_registro'
#         unique_together = (('co_proced', 'tp_registro'),)
#
#
# class RlProfMunicipio(models.Model):
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade')
#     co_ator_papel = models.OneToOneField('TbProf', models.DO_NOTHING, db_column='co_ator_papel', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_prof_municipio'
#         unique_together = (('co_ator_papel', 'co_localidade'),)
#
#
# class RlQstAssociacaoOpcaoPergnt(models.Model):
#     co_qst_associacao_pergunta = models.OneToOneField('TbQstAssociacaoPergunta', models.DO_NOTHING, db_column='co_qst_associacao_pergunta', primary_key=True)
#     co_qst_opcao_pergunta = models.ForeignKey('TbQstOpcaoPergunta', models.DO_NOTHING, db_column='co_qst_opcao_pergunta')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_qst_associacao_opcao_pergnt'
#         unique_together = (('co_qst_associacao_pergunta', 'co_qst_opcao_pergunta'),)
#
#
# class RlQstRespostaOpcaoPergunta(models.Model):
#     co_qst_resposta = models.OneToOneField('TbQstResposta', models.DO_NOTHING, db_column='co_qst_resposta', primary_key=True)
#     co_qst_opcao_pergunta = models.ForeignKey('TbQstOpcaoPergunta', models.DO_NOTHING, db_column='co_qst_opcao_pergunta')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_qst_resposta_opcao_pergunta'
#         unique_together = (('co_qst_resposta', 'co_qst_opcao_pergunta'),)
#
#
# class RlRecursoAcao(models.Model):
#     co_recurso = models.BigIntegerField(primary_key=True)
#     nu_acao = models.IntegerField()
#     nu_obrigacao = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'rl_recurso_acao'
#         unique_together = (('co_recurso', 'nu_acao', 'nu_obrigacao'),)
#
#
# class RlTipoAtendProcedAutomatic(models.Model):
#     co_proced_automatico = models.OneToOneField('TbProcedAutomatico', models.DO_NOTHING, db_column='co_proced_automatico', primary_key=True)
#     tp_atend = models.ForeignKey('TbTipoAtend', models.DO_NOTHING, db_column='tp_atend')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_tipo_atend_proced_automatic'
#         unique_together = (('co_proced_automatico', 'tp_atend'),)
#
#
# class RlTipoConsultaOdntPrcAuto(models.Model):
#     co_proced_automatico = models.OneToOneField('TbProcedAutomatico', models.DO_NOTHING, db_column='co_proced_automatico', primary_key=True)
#     tp_consulta_odonto = models.ForeignKey('TbTipoConsultaOdonto', models.DO_NOTHING, db_column='tp_consulta_odonto')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_tipo_consulta_odnt_prc_auto'
#         unique_together = (('co_proced_automatico', 'tp_consulta_odonto'),)
#
#
# class RlTipoEncamOdontoProcdAut(models.Model):
#     co_proced_automatico = models.OneToOneField('TbProcedAutomatico', models.DO_NOTHING, db_column='co_proced_automatico', primary_key=True)
#     tp_encam_odonto = models.ForeignKey('TbTipoEncamOdonto', models.DO_NOTHING, db_column='tp_encam_odonto')
#
#     class Meta:
#         managed = False
#         db_table = 'rl_tipo_encam_odonto_procd_aut'
#         unique_together = (('co_proced_automatico', 'tp_encam_odonto'),)
#
#
# class RlUnidadeSaudeComplexidade(models.Model):
#     co_ator_papel = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_ator_papel')
#     co_complexidade = models.OneToOneField('TbComplexidade', models.DO_NOTHING, db_column='co_complexidade', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_unidade_saude_complexidade'
#         unique_together = (('co_complexidade', 'co_ator_papel'),)
#
#
# class RlUnidadeSaudeHorus(models.Model):
#     co_unidade_saude = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude')
#     co_unidade_saude_horus = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude_horus')
#     co_seq_unidade_saude_horus = models.BigIntegerField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_unidade_saude_horus'
#
#
# class RlUnidadeSaudeTipoServico(models.Model):
#     tp_servico = models.ForeignKey('TbTipoServico', models.DO_NOTHING, db_column='tp_servico')
#     co_ator_papel = models.OneToOneField('TbUnidadeSaude', models.DO_NOTHING, db_column='co_ator_papel', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'rl_unidade_saude_tipo_servico'
#         unique_together = (('co_ator_papel', 'tp_servico'),)
#
#
# class RlViaAdmLocalAplVacina(models.Model):
#     co_via_adm_vacina = models.BigIntegerField(primary_key=True)
#     co_local_apl_vacina = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'rl_via_adm_local_apl_vacina'
#         unique_together = (('co_via_adm_vacina', 'co_local_apl_vacina'),)
#
#
# class SpringSession(models.Model):
#     primary_id = models.CharField(primary_key=True, max_length=36)
#     session_id = models.CharField(unique=True, max_length=36)
#     creation_time = models.BigIntegerField()
#     last_access_time = models.BigIntegerField()
#     max_inactive_interval = models.IntegerField()
#     expiry_time = models.BigIntegerField()
#     principal_name = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'spring_session'
#
#
# class SpringSessionAttributes(models.Model):
#     session_primary = models.OneToOneField(SpringSession, models.DO_NOTHING, primary_key=True)
#     attribute_name = models.CharField(max_length=200)
#     attribute_bytes = models.BinaryField()
#
#     class Meta:
#         managed = False
#         db_table = 'spring_session_attributes'
#         unique_together = (('session_primary', 'attribute_name'),)
#
#
# class TaAdmGeral(models.Model):
#     co_seq_taadmgeral = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     st_instalacao_terminada = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_adm_geral'
#
#
# class TaAdmMunicipal(models.Model):
#     co_seq_taadmmunicipal = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     ds_autorizacao = models.CharField(max_length=225, blank=True, null=True)
#     st_instalacao_terminada = models.IntegerField(blank=True, null=True)
#     dt_inativacao = models.DateTimeField(blank=True, null=True)
#     dt_adicao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_adm_municipal'
#
#
# class TaAtivacaoAgendamentoOnline(models.Model):
#     co_seq_taativacaoagendamentnln = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_ativacao_agendamento_on = models.BigIntegerField(blank=True, null=True)
#     co_prof = models.BigIntegerField(blank=True, null=True)
#     dt_evento = models.DateTimeField(blank=True, null=True)
#     st_ativado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_ativacao_agendamento_online'
#
#
# class TaAtorPapel(models.Model):
#     co_seq_taatorpapel = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_ator_papel = models.BigIntegerField(blank=True, null=True)
#     no_tipo_ator_papel = models.CharField(max_length=100, blank=True, null=True)
#     co_prof = models.BigIntegerField(blank=True, null=True)
#     ds_modulo_inicial = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_ator_papel'
#
#
# class TaAtorPapelPerfil(models.Model):
#     co_seq_taatorpapelperfil = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     co_perfil = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_ator_papel_perfil'
#
#
# class TaCboAtend(models.Model):
#     co_seq_tacboatend = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     qt_tempo_consulta = models.IntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_seq_cbo_atend = models.BigIntegerField(blank=True, null=True)
#     st_disponivel_lotacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cbo_atend'
#
#
# class TaCfgAgenda(models.Model):
#     co_seq_tacfgagenda = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_config_agenda = models.BigIntegerField(blank=True, null=True)
#     co_entidade_configurada = models.BigIntegerField(blank=True, null=True)
#     co_tipo_cfg_agenda = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cfg_agenda'
#
#
# class TaCfgAgendaDetalhe(models.Model):
#     co_seq_tacfgagendadetalhe = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_config_agenda_detalhe = models.BigIntegerField(blank=True, null=True)
#     co_dia_semana = models.BigIntegerField(blank=True, null=True)
#     co_periodo = models.BigIntegerField(blank=True, null=True)
#     horario_inicial = models.CharField(max_length=5, blank=True, null=True)
#     horario_final = models.CharField(max_length=5, blank=True, null=True)
#     co_cfg_agenda = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cfg_agenda_detalhe'
#
#
# class TaCfgAgendaMunicipal(models.Model):
#     co_seq_tacfgagendamunicipal = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_cfg_agenda_municipal = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     nu_duracao_atendimento_padrao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cfg_agenda_municipal'
#
#
# class TaCfgAgendaOnlineDetalhe(models.Model):
#     co_seq_tacfgagendaonlinedetalh = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_cfg_agenda_online_dtlh = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_dia_semana = models.BigIntegerField(blank=True, null=True)
#     ds_horario = models.CharField(max_length=5, blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     uuid_horario_agenda_online = models.CharField(max_length=36, blank=True, null=True)
#     st_registro_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cfg_agenda_online_detalhe'
#
#
# class TaCfgRnds(models.Model):
#     co_seq_tacfgrnds = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_cfg_rnds = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     no_certificado = models.CharField(max_length=255, blank=True, null=True)
#     ds_senha_certificado = models.CharField(max_length=255, blank=True, null=True)
#     dt_inclusao = models.DateTimeField(blank=True, null=True)
#     dt_habilitacao = models.DateTimeField(blank=True, null=True)
#     dt_validade_certificado = models.DateTimeField(blank=True, null=True)
#     co_identificador_solicitante = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cfg_rnds'
#
#
# class TaCidadao(models.Model):
#     co_seq_tacidadao = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_unico_cidadao_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     co_unico_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     st_desconhece_nome_mae = models.IntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     nu_area = models.CharField(max_length=3, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     nu_nis_pis_pasep = models.CharField(max_length=50, blank=True, null=True)
#     dt_atualizado = models.DateTimeField(blank=True, null=True)
#     nu_cns_responsavel = models.CharField(max_length=16, blank=True, null=True)
#     no_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_responsavel = models.DateTimeField(blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=16, blank=True, null=True)
#     no_cuidador = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_cuidador = models.DateTimeField(blank=True, null=True)
#     tp_cds_cuidador = models.BigIntegerField(blank=True, null=True)
#     co_unico_cidadao = models.CharField(max_length=96, blank=True, null=True)
#     co_nacionalidade = models.BigIntegerField(blank=True, null=True)
#     co_pais_nascimento = models.BigIntegerField(blank=True, null=True)
#     co_unico_ultima_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ultima_ficha = models.DateField(blank=True, null=True)
#     st_registro_cadsus = models.IntegerField(blank=True, null=True)
#     dt_atualizado_cadsus = models.DateField(blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateTimeField(blank=True, null=True)
#     dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
#     nu_portaria_naturalizacao = models.CharField(max_length=16, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     st_infrm_orientacao_sexual = models.IntegerField(blank=True, null=True)
#     tp_orientacao_sexual = models.CharField(max_length=25, blank=True, null=True)
#     st_infrm_identidade_genero = models.IntegerField(blank=True, null=True)
#     tp_identidade_genero = models.CharField(max_length=25, blank=True, null=True)
#     st_compartilhamento_prontuario = models.IntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_nao_possui_cuidador = models.IntegerField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=500, blank=True, null=True)
#     no_cidadao_filtro = models.CharField(max_length=600, blank=True, null=True)
#     co_escolaridade = models.BigIntegerField(blank=True, null=True)
#     co_raca_cor = models.BigIntegerField(blank=True, null=True)
#     co_etnia = models.BigIntegerField(blank=True, null=True)
#     co_estado_civil = models.BigIntegerField(blank=True, null=True)
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     dt_obito = models.DateField(blank=True, null=True)
#     no_mae = models.CharField(max_length=500, blank=True, null=True)
#     no_mae_filtro = models.CharField(max_length=600, blank=True, null=True)
#     no_pai = models.CharField(max_length=500, blank=True, null=True)
#     no_social = models.CharField(max_length=255, blank=True, null=True)
#     st_faleceu = models.IntegerField(blank=True, null=True)
#     nu_documento_obito = models.CharField(max_length=255, blank=True, null=True)
#     st_dados_obito_cadsus = models.IntegerField(blank=True, null=True)
#     no_localidade_exterior = models.CharField(max_length=255, blank=True, null=True)
#     co_pais_exterior = models.BigIntegerField(blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_localidade_endereco = models.BigIntegerField(blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     nu_telefone_residencial = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_celular = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_contato = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo_para_exibicao = models.IntegerField(blank=True, null=True)
#     st_unificado = models.IntegerField(blank=True, null=True)
#     st_territorio_utiliza_cpf = models.IntegerField(blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#     no_tipo_sanguineo = models.CharField(max_length=22, blank=True, null=True)
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cidadao'
#
#
# class TaCidadaoVinculacaoEquipe(models.Model):
#     co_seq_tacidadaovinculacaoequp = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_cidadao_vinculacao_eqp = models.BigIntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     co_unico_cadastro_individual = models.CharField(max_length=96, blank=True, null=True)
#     st_envio = models.IntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     st_usar_cadastro_individual = models.IntegerField(blank=True, null=True)
#     st_saida_cadastro_obito = models.IntegerField(blank=True, null=True)
#     st_saida_cadastro_territorio = models.IntegerField(blank=True, null=True)
#     dt_atualizacao_cadastro = models.DateTimeField(blank=True, null=True)
#     co_prof_cadastrante_cds = models.BigIntegerField(blank=True, null=True)
#     co_lotacao_cadastrante_pec = models.BigIntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     nu_cnes = models.CharField(max_length=7, blank=True, null=True)
#     nu_ine = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_cidadao_vinculacao_equipe'
#
#
# class TaCompartilhamentoProntuario(models.Model):
#     co_seq_tacompartilhamentoprntr = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_compartilha_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_usuario = models.BigIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     dt_ultima_alteracao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_compartilhamento_prontuario'
#
#
# class TaConfigAgendaFechamento(models.Model):
#     co_seq_taconfigagendafechament = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     dt_inicio = models.DateTimeField(blank=True, null=True)
#     dt_fim = models.DateTimeField(blank=True, null=True)
#     ds_motivo = models.CharField(max_length=4000, blank=True, null=True)
#     co_seq_config_agenda_fechament = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     no_ident_motivo_fechamento = models.CharField(max_length=30, blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     st_registro_ativo = models.IntegerField(blank=True, null=True)
#     uuid_fechamento = models.CharField(max_length=36, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_config_agenda_fechamento'
#
#
# class TaConfigAtencaoDomiciliar(models.Model):
#     co_seq_taconfigatencaodomicilr = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_config_atencao_domicilr = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     qt_tempo_duracao_consulta = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_config_atencao_domiciliar'
#
#
# class TaConfigAtendDomiciliar(models.Model):
#     co_seq_taconfigatenddomiciliar = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_config_atend_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_equipe_pai = models.BigIntegerField(blank=True, null=True)
#     co_equipe_filho = models.BigIntegerField(blank=True, null=True)
#     co_config_atencao_domiciliar = models.BigIntegerField(blank=True, null=True)
#     tp_config_atend_domiciliar = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_config_atend_domiciliar'
#
#
# class TaConfigSistema(models.Model):
#     co_seq_taconfigsistema = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_config_sistema = models.CharField(max_length=255, blank=True, null=True)
#     ds_config_sistema = models.CharField(max_length=255, blank=True, null=True)
#     st_disponivel_sistema = models.IntegerField(blank=True, null=True)
#     ds_texto = models.CharField(max_length=255, blank=True, null=True)
#     ds_inteiro = models.IntegerField(blank=True, null=True)
#     ds_binario = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_config_sistema'
#
#
# class TaEquipe(models.Model):
#     co_seq_taequipe = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_equipe = models.BigIntegerField(blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     tp_equipe = models.BigIntegerField(blank=True, null=True)
#     ds_area = models.CharField(max_length=255, blank=True, null=True)
#     no_equipe = models.CharField(max_length=255, blank=True, null=True)
#     no_equipe_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_equipe = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_equipe'
#
#
# class TaGestorEstadual(models.Model):
#     co_seq_tagestorestadual = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_gestor_estadual'
#
#
# class TaGestorMunicipal(models.Model):
#     co_seq_tagestormunicipal = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_gestor_municipal'
#
#
# class TaGrupoExame(models.Model):
#     co_seq_tagrupoexame = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_grupo_exame = models.BigIntegerField(blank=True, null=True)
#     no_grupo_exame = models.CharField(max_length=255, blank=True, null=True)
#     nu_idade_minima = models.IntegerField(blank=True, null=True)
#     nu_idade_maxima = models.IntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_grupo_exame'
#
#
# class TaImunobiologicoLote(models.Model):
#     co_seq_taimunobiologicolote = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_imunobiologico_lote = models.BigIntegerField(blank=True, null=True)
#     co_imunobiologico = models.BigIntegerField(blank=True, null=True)
#     ds_lote = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_filtro = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_fabricante_filtro = models.CharField(max_length=255, blank=True, null=True)
#     dt_validade = models.DateField(blank=True, null=True)
#     co_imunobiologico_fabricante = models.BigIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_imunobiologico_lote'
#
#
# class TaIntegracaoHorus(models.Model):
#     co_seq_taintegracaohorus = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     dt_habilitar_integracao = models.DateTimeField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     tp_erro_teste_horus = models.CharField(max_length=50, blank=True, null=True)
#     co_unidade_saude_padrao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_integracao_horus'
#
#
# class TaLotacao(models.Model):
#     co_seq_talotacao = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     dt_desativacao_lotacao = models.DateTimeField(blank=True, null=True)
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     co_prof = models.BigIntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_equipe = models.BigIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     st_atualiza_perfil = models.IntegerField(blank=True, null=True)
#     st_importada = models.IntegerField(blank=True, null=True)
#     st_agenda_alterada_manual = models.IntegerField(blank=True, null=True)
#     dt_ultima_tentativa_envio = models.DateTimeField(blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     st_ativo_agenda_online = models.IntegerField(blank=True, null=True)
#     ds_ultima_tentativa = models.TextField(blank=True, null=True)
#     co_unico_lotacao = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_lotacao'
#
#
# class TaNodo(models.Model):
#     co_seq_tanodo = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_nodo = models.BigIntegerField(blank=True, null=True)
#     no_servidor = models.CharField(max_length=60, blank=True, null=True)
#     ds_nome = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_conexao = models.IntegerField(blank=True, null=True)
#     dt_testeconexao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_nodo'
#
#
# class TaPerfil(models.Model):
#     co_seq_taperfil = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_perfil = models.BigIntegerField(blank=True, null=True)
#     no_perfil = models.CharField(max_length=100, blank=True, null=True)
#     no_perfil_filtro = models.CharField(max_length=50, blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     no_perfil_padrao = models.CharField(max_length=100, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     no_tipo_perfil = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_perfil'
#
#
# class TaPerfilRecurso(models.Model):
#     co_seq_taperfilrecurso = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_perfil_recurso = models.BigIntegerField(blank=True, null=True)
#     co_perfil = models.BigIntegerField(blank=True, null=True)
#     no_recurso = models.CharField(max_length=400, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_perfil_recurso'
#
#
# class TaProcedGrupoExame(models.Model):
#     co_seq_taprocedgrupoexame = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_proced_grupo_exame = models.BigIntegerField(blank=True, null=True)
#     co_grupo_exame = models.BigIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_proced_grupo_exame'
#
#
# class TaProf(models.Model):
#     co_seq_taprof = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_prof = models.BigIntegerField(blank=True, null=True)
#     nu_conselho_classe = models.CharField(max_length=100, blank=True, null=True)
#     co_uf_emissora_conselho_classe = models.BigIntegerField(blank=True, null=True)
#     co_conselho_classe = models.BigIntegerField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     no_profissional = models.CharField(max_length=500, blank=True, null=True)
#     no_profissional_filtro = models.CharField(max_length=600, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     nu_telefone = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_localidade_endereco = models.BigIntegerField(blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     co_usuario = models.BigIntegerField(blank=True, null=True)
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_prof'
#
#
# class TaProfMunicipio(models.Model):
#     co_seq_taprofmunicipio = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_prof_municipio'
#
#
# class TaRetificacaoAtend(models.Model):
#     co_seq_taretificacaoatend = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1, blank=True, null=True)
#     dt_auditoria = models.DateTimeField(blank=True, null=True)
#     co_seq_retificacao_atend = models.BigIntegerField(blank=True, null=True)
#     bl_conteudo_atendimento = models.BinaryField(blank=True, null=True)
#     co_unico_atend_prof = models.CharField(max_length=96, blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     dt_exclusao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_retificacao_atend'
#
#
# class TaServidorSmtp(models.Model):
#     co_seq_taservidorsmtp = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_servidor_smtp = models.BigIntegerField(blank=True, null=True)
#     no_host = models.CharField(max_length=255, blank=True, null=True)
#     nu_porta = models.CharField(max_length=5, blank=True, null=True)
#     ds_usuario = models.CharField(max_length=255, blank=True, null=True)
#     ds_senha = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     st_usuario_email = models.IntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     dt_registro = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_servidor_smtp'
#
#
# class TaTipoServico(models.Model):
#     co_seq_tatiposervico = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_tipo_servico = models.BigIntegerField(blank=True, null=True)
#     no_tipo_servico = models.CharField(max_length=50, blank=True, null=True)
#     no_tipo_servico_filtro = models.CharField(max_length=50, blank=True, null=True)
#     st_interno = models.IntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_tipo_servico'
#
#
# class TaUnidadeSaude(models.Model):
#     co_seq_taunidadesaude = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     nu_licenca_funcionamento = models.CharField(max_length=20, blank=True, null=True)
#     tp_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_seq_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     nu_cnpj = models.CharField(max_length=14, blank=True, null=True)
#     no_unidade_saude = models.CharField(max_length=255, blank=True, null=True)
#     no_unidade_saude_filtro = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_comercial = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_comercial2 = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_fax = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_localidade_endereco = models.BigIntegerField(blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     co_subtp_unidade_saude = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_unidade_saude'
#
#
# class TaUnidadeSaudeComplexidade(models.Model):
#     co_seq_taunidadesaudecomplexdd = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     co_complexidade = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_unidade_saude_complexidade'
#
#
# class TaUnidadeSaudeHorus(models.Model):
#     co_seq_taunidadesaudehorus = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_unidade_saude_horus = models.BigIntegerField(blank=True, null=True)
#     co_seq_unidade_saude_horus = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_unidade_saude_horus'
#
#
# class TaUnidadeSaudeTipoServico(models.Model):
#     co_seq_taunidadesaudetiposervc = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     tp_servico = models.BigIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_unidade_saude_tipo_servico'
#
#
# class TaUsuario(models.Model):
#     co_seq_tausuario = models.BigIntegerField(primary_key=True)
#     co_tipo_auditoria = models.CharField(max_length=1)
#     dt_auditoria = models.DateTimeField()
#     co_seq_usuario = models.BigIntegerField(blank=True, null=True)
#     st_bloqueado = models.IntegerField(blank=True, null=True)
#     ds_senha = models.CharField(max_length=255, blank=True, null=True)
#     st_trocar_senha = models.IntegerField(blank=True, null=True)
#     co_ator = models.BigIntegerField(blank=True, null=True)
#     dt_ultima_atualizacao_senha = models.DateField(blank=True, null=True)
#     st_termo_uso = models.IntegerField(blank=True, null=True)
#     st_forcar_troca_senha = models.IntegerField(blank=True, null=True)
#     nr_tentativas_acesso = models.IntegerField(blank=True, null=True)
#     ds_login = models.CharField(max_length=255, blank=True, null=True)
#     dt_envio_email_recuperar_senha = models.DateTimeField(blank=True, null=True)
#     st_visualizou_novidades = models.IntegerField(blank=True, null=True)
#     st_pesquisa_respondida = models.IntegerField(blank=True, null=True)
#     dt_primeiro_login_versao = models.DateTimeField(blank=True, null=True)
#     dt_pesquisa_respondida = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ta_usuario'
#
#
# class TbAdCidadao(models.Model):
#     co_seq_ad_cidadao = models.BigIntegerField(primary_key=True)
#     co_equipe = models.ForeignKey('TbEquipe', models.DO_NOTHING, db_column='co_equipe', blank=True, null=True)
#     dt_admissao = models.DateTimeField(blank=True, null=True)
#     co_ad_modalidade = models.ForeignKey('TbAdModalidade', models.DO_NOTHING, db_column='co_ad_modalidade', blank=True, null=True)
#     co_ad_origem = models.ForeignKey('TbAdOrigem', models.DO_NOTHING, db_column='co_ad_origem', blank=True, null=True)
#     no_especificacao_origem = models.CharField(max_length=255, blank=True, null=True)
#     co_cid10_principal = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_principal', blank=True, null=True)
#     co_cid10_causa_associada = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_causa_associada', blank=True, null=True)
#     co_ad_destino = models.ForeignKey('TbAdDestino', models.DO_NOTHING, db_column='co_ad_destino', blank=True, null=True)
#     dt_saida = models.DateTimeField(blank=True, null=True)
#     dt_ultima_visita = models.DateTimeField(blank=True, null=True)
#     dt_proxima_visita = models.DateTimeField(blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     co_cid10_secundario_2 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_secundario_2', blank=True, null=True)
#     dt_reg_obito = models.DateTimeField(blank=True, null=True)
#     st_cidadao_sincronizado = models.IntegerField(blank=True, null=True)
#     st_dt_saida_restaurada = models.IntegerField(blank=True, null=True)
#     st_dt_saida_futura = models.IntegerField(blank=True, null=True)
#     nu_documento_obito = models.CharField(max_length=16, blank=True, null=True)
#     co_unico_ad_cidadao_obito = models.BigIntegerField(blank=True, null=True)
#     co_unico_ad_cidadao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_cidadao'
#
#
# class TbAdCidadaoHistorico(models.Model):
#     co_seq_ad_cidadao_historico = models.BigIntegerField(primary_key=True)
#     co_unico_ad_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_ad_modalidade = models.ForeignKey('TbAdModalidade', models.DO_NOTHING, db_column='co_ad_modalidade', blank=True, null=True)
#     co_prof = models.ForeignKey('TbProf', models.DO_NOTHING, db_column='co_prof', blank=True, null=True)
#     dt_registro = models.DateTimeField(blank=True, null=True)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_cidadao_historico'
#
#
# class TbAdDestino(models.Model):
#     co_seq_ad_destino = models.BigIntegerField(primary_key=True)
#     no_ad_destino = models.CharField(max_length=100, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_destino'
#
#
# class TbAdModalidade(models.Model):
#     co_seq_ad_modalidade = models.BigIntegerField(primary_key=True)
#     no_ad_modalidade = models.CharField(max_length=100, blank=True, null=True)
#     no_identificador = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_modalidade'
#
#
# class TbAdOrigem(models.Model):
#     co_ad_origem = models.BigIntegerField(primary_key=True)
#     no_ad_origem = models.CharField(max_length=100, blank=True, null=True)
#     nu_ordem_origem = models.IntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_origem'
#
#
# class TbAdQuestao(models.Model):
#     co_seq_ad_questao = models.BigIntegerField(primary_key=True)
#     ds_ad_questao = models.CharField(max_length=255, blank=True, null=True)
#     co_ad_cidadao = models.ForeignKey(TbAdCidadao, models.DO_NOTHING, db_column='co_ad_cidadao', blank=True, null=True)
#     st_ad_questao = models.BigIntegerField(blank=True, null=True)
#     nu_ordem = models.IntegerField(blank=True, null=True)
#     co_situacao_presente = models.BigIntegerField(blank=True, null=True)
#     co_unico_ad_questao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_questao'
#
#
# class TbAdResposta(models.Model):
#     co_seq_ad_resposta = models.BigIntegerField(primary_key=True)
#     co_unico_ad_questao = models.BigIntegerField(blank=True, null=True)
#     st_ad_resposta = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof_ad = models.ForeignKey('TbAtendProfAd', models.DO_NOTHING, db_column='co_atend_prof_ad', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_resposta'
#
#
# class TbAdSyncEntity(models.Model):
#     co_seq_ad_sync_entity = models.BigIntegerField(primary_key=True)
#     nu_token = models.CharField(max_length=100)
#     co_value = models.BigIntegerField(blank=True, null=True)
#     tp_sync_entity = models.CharField(max_length=30)
#     ds_value = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_sync_entity'
#
#
# class TbAdTipoElegivel(models.Model):
#     co_ad_tipo_elegivel = models.BigIntegerField(primary_key=True)
#     no_ad_tipo_elegivel = models.CharField(max_length=100)
#     no_identificador = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_tipo_elegivel'
#
#
# class TbAdTipoInelegivel(models.Model):
#     co_ad_tipo_inelegivel = models.BigIntegerField(primary_key=True)
#     no_ad_tipo_inelegivel = models.CharField(max_length=150)
#     no_identificador = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_tipo_inelegivel'
#
#
# class TbAdTransmissaoSessao(models.Model):
#     co_unico_transmissao_sessao = models.CharField(primary_key=True, max_length=36)
#     dt_tempo_sessao = models.DateTimeField(blank=True, null=True)
#     ds_conteudo = models.BinaryField(blank=True, null=True)
#     ds_dado_usuario = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ad_transmissao_sessao'
#
#
# class TbAdmGeral(models.Model):
#     co_ator_papel = models.OneToOneField('TbAtorPapel', models.DO_NOTHING, db_column='co_ator_papel', primary_key=True)
#     st_instalacao_terminada = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_adm_geral'
#
#
# class TbAdmMunicipal(models.Model):
#     co_ator_papel = models.OneToOneField('TbAtorPapel', models.DO_NOTHING, db_column='co_ator_papel', primary_key=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade', blank=True, null=True)
#     ds_autorizacao = models.CharField(max_length=225, blank=True, null=True)
#     st_instalacao_terminada = models.IntegerField(blank=True, null=True)
#     dt_inativacao = models.DateTimeField(blank=True, null=True)
#     dt_adicao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_adm_municipal'
#
#
# class TbAgendado(models.Model):
#     co_seq_agendado = models.BigIntegerField(primary_key=True)
#     dt_agendado = models.DateTimeField(blank=True, null=True)
#     hr_inicial_agendado = models.DateTimeField(blank=True, null=True)
#     ds_observacao = models.CharField(max_length=400, blank=True, null=True)
#     st_agendado = models.ForeignKey('TbSituacaoAgendado', models.DO_NOTHING, db_column='st_agendado')
#     co_lotacao_agendada = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao_agendada', blank=True, null=True)
#     co_motivo_reserva = models.ForeignKey('TbMotivoReserva', models.DO_NOTHING, db_column='co_motivo_reserva', blank=True, null=True)
#     ds_outro_motivo_reserva = models.CharField(max_length=600, blank=True, null=True)
#     co_origem = models.ForeignKey('TbOrigem', models.DO_NOTHING, db_column='co_origem', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     co_lotacao_criadora = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao_criadora', blank=True, null=True)
#     dt_criacao = models.DateTimeField(blank=True, null=True)
#     uuid_agendamento = models.CharField(unique=True, max_length=36, blank=True, null=True)
#     dt_ultima_tentativa_envio = models.DateTimeField(blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48)
#     ds_ultima_tentativa = models.TextField(blank=True, null=True)
#     st_cidadao_agendamento_online = models.CharField(max_length=48, blank=True, null=True)
#     st_fora_ubs = models.IntegerField()
#     co_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='co_local_atend', blank=True, null=True)
#     tp_agendamento = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_agendado'
#
#
# class TbAlergia(models.Model):
#     co_seq_alergia = models.BigIntegerField(primary_key=True)
#     co_categoria_agente_causador = models.ForeignKey('TbCategoriaAgenteCausador', models.DO_NOTHING, db_column='co_categoria_agente_causador')
#     no_substancia_especifica = models.CharField(max_length=300)
#     no_substancia_especifica_filtr = models.CharField(max_length=300)
#     co_ultima_alergia_evolucao = models.ForeignKey('TbAlergiaEvolucao', models.DO_NOTHING, db_column='co_ultima_alergia_evolucao', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     co_unico_alergia = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_alergia'
#
#
# class TbAlergiaEvolucao(models.Model):
#     co_seq_alergia_evolucao = models.BigIntegerField(primary_key=True)
#     co_unico_alergia = models.BigIntegerField(blank=True, null=True)
#     no_manifestacoes = models.CharField(max_length=800, blank=True, null=True)
#     dt_instalacao = models.DateField(blank=True, null=True)
#     st_alergia_avaliada = models.IntegerField(blank=True, null=True)
#     co_criticidade_alergia = models.ForeignKey('TbCriticidadeAlergia', models.DO_NOTHING, db_column='co_criticidade_alergia')
#     no_evolucao = models.CharField(max_length=800, blank=True, null=True)
#     co_atend_prof = models.ForeignKey('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_alergia_evolucao'
#
#
# class TbAlimBebida(models.Model):
#     co_alim_bebida = models.BigIntegerField(primary_key=True)
#     ds_alim_bebida = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_alim_bebida'
#
#
# class TbAntecedente(models.Model):
#     co_prontuario = models.OneToOneField('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', primary_key=True)
#     ds_cirurgia = models.CharField(max_length=400, blank=True, null=True)
#     ds_internacao = models.CharField(max_length=400, blank=True, null=True)
#     ds_alergia_medicamento = models.CharField(max_length=400, blank=True, null=True)
#     ds_observacao = models.CharField(max_length=400, blank=True, null=True)
#     ds_aborto = models.CharField(max_length=255, blank=True, null=True)
#     ds_parto = models.CharField(max_length=255, blank=True, null=True)
#     qt_aborto = models.CharField(max_length=255, blank=True, null=True)
#     ds_natimorto = models.CharField(max_length=255, blank=True, null=True)
#     ds_recem_nascido = models.CharField(max_length=255, blank=True, null=True)
#     ds_cesaria = models.CharField(max_length=255, blank=True, null=True)
#     ds_parto_domiciliar = models.CharField(max_length=255, blank=True, null=True)
#     ds_filho_vivo = models.CharField(max_length=255, blank=True, null=True)
#     ds_obito_antes_primeira_semana = models.CharField(max_length=255, blank=True, null=True)
#     ds_gestacao = models.CharField(max_length=255, blank=True, null=True)
#     ds_parto_vaginal = models.CharField(max_length=255, blank=True, null=True)
#     ds_obito_apos_primeira_semana = models.CharField(max_length=255, blank=True, null=True)
#     dt_ultimo_parto = models.DateTimeField(blank=True, null=True)
#     qt_recem_nascido_acima = models.CharField(max_length=255, blank=True, null=True)
#     qt_nascidos_vivos = models.CharField(max_length=255, blank=True, null=True)
#     st_parto_menos_de_um_ano = models.IntegerField(blank=True, null=True)
#     dt_ultima_atualizacao_pessoal = models.DateTimeField(blank=True, null=True)
#     dt_ultima_atualizacao_gestacnl = models.DateTimeField(blank=True, null=True)
#     nu_peso = models.CharField(max_length=255, blank=True, null=True)
#     nu_altura = models.CharField(max_length=255, blank=True, null=True)
#     nu_perimetro_cefalico = models.CharField(max_length=255, blank=True, null=True)
#     nu_apgar_um = models.CharField(max_length=255, blank=True, null=True)
#     nu_apgar_cinco = models.CharField(max_length=255, blank=True, null=True)
#     nu_apgar_dez = models.CharField(max_length=255, blank=True, null=True)
#     tp_gravidez = models.CharField(max_length=255, blank=True, null=True)
#     tp_parto = models.CharField(max_length=255, blank=True, null=True)
#     nu_ig_semanas = models.CharField(max_length=255, blank=True, null=True)
#     nu_ig_dias = models.CharField(max_length=255, blank=True, null=True)
#     dt_ultima_atualizacao_puericu = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_antecedente'
#
#
# class TbAntecedenteHistorico(models.Model):
#     co_seq_antecedente_historico = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_antecedente_historico'
#
#
# class TbAntecedenteItem(models.Model):
#     co_seq_antecedente_item = models.BigIntegerField(primary_key=True)
#     co_antecedente_historico = models.ForeignKey(TbAntecedenteHistorico, models.DO_NOTHING, db_column='co_antecedente_historico', blank=True, null=True)
#     ds_valor_item = models.CharField(max_length=255, blank=True, null=True)
#     st_valor_item = models.IntegerField(blank=True, null=True)
#     tp_antecedente_item = models.ForeignKey('TbAntecedenteTipoItem', models.DO_NOTHING, db_column='tp_antecedente_item', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_antecedente_item'
#
#
# class TbAntecedenteTipoItem(models.Model):
#     co_antecedente_tipo_item = models.BigIntegerField(primary_key=True)
#     no_antecedente_tipo_item = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_antecedente_tipo_item'
#
#
# class TbAplicacaoMedicamento(models.Model):
#     co_aplicacao_medicamento = models.BigIntegerField(primary_key=True)
#     no_aplicacao_medicamento = models.CharField(max_length=100)
#     no_aplicacao_med_filtro = models.CharField(max_length=100, blank=True, null=True)
#     nu_frequencia_instalacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_aplicacao_medicamento'
#
#
# class TbArcada(models.Model):
#     co_parte_bucal = models.OneToOneField('TbParteBucal', models.DO_NOTHING, db_column='co_parte_bucal', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_arcada'
#
#
# class TbArquivo(models.Model):
#     co_seq_arquivo = models.BigIntegerField(primary_key=True)
#     dt_inicio_geracao = models.DateTimeField()
#     st_arquivo = models.CharField(max_length=50)
#     ds_identificador = models.CharField(max_length=50)
#     bl_arquivo = models.BinaryField(blank=True, null=True)
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario')
#     ds_formato = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_arquivo'
#
#
# class TbAtend(models.Model):
#     co_seq_atend = models.BigIntegerField(primary_key=True)
#     dt_fim = models.DateTimeField(blank=True, null=True)
#     dt_inicio = models.DateTimeField()
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     st_atend = models.ForeignKey('TbStatusAtend', models.DO_NOTHING, db_column='st_atend')
#     co_agendado = models.OneToOneField(TbAgendado, models.DO_NOTHING, db_column='co_agendado', blank=True, null=True)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     co_classificacao_risco = models.ForeignKey('TbClassificacaoRisco', models.DO_NOTHING, db_column='co_classificacao_risco', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario')
#     co_unidade_saude = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude')
#     co_atend_prof = models.ForeignKey('TbAtendProf', models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     dt_encaminhamento = models.DateTimeField(blank=True, null=True)
#     st_fechado_automaticamente = models.IntegerField(blank=True, null=True)
#     nu_lotacao_anterior = models.BigIntegerField(blank=True, null=True)
#     co_unico_atend = models.CharField(max_length=96, blank=True, null=True)
#     tp_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='tp_local_atend', blank=True, null=True)
#     st_registro_tardio = models.IntegerField()
#     no_justificativa_reg_tardio = models.CharField(max_length=50, blank=True, null=True)
#     dt_criacao_registro = models.DateTimeField(blank=True, null=True)
#     dt_ultima_alteracao_status = models.DateTimeField()
#     co_equipe = models.ForeignKey('TbEquipe', models.DO_NOTHING, db_column='co_equipe', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend'
#
#
# class TbAtendProf(models.Model):
#     co_seq_atend_prof = models.BigIntegerField(primary_key=True)
#     dt_fim = models.DateTimeField(blank=True, null=True)
#     dt_inicio = models.DateTimeField(blank=True, null=True)
#     co_atend = models.ForeignKey(TbAtend, models.DO_NOTHING, db_column='co_atend')
#     co_atend_prof_tipo_encam_intrn = models.ForeignKey('TbAtendProfTipoEncamIntrn', models.DO_NOTHING, db_column='co_atend_prof_tipo_encam_intrn', blank=True, null=True)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     tp_atend_prof = models.ForeignKey('TbTipoAtendProf', models.DO_NOTHING, db_column='tp_atend_prof')
#     st_atend_prof = models.ForeignKey('TbStatusAtendProf', models.DO_NOTHING, db_column='st_atend_prof')
#     st_atend_enviado = models.IntegerField(blank=True, null=True)
#     co_unico_ad_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_classificacao_risco = models.ForeignKey('TbClassificacaoRisco', models.DO_NOTHING, db_column='co_classificacao_risco', blank=True, null=True)
#     co_unico_atend_prof = models.CharField(max_length=96, blank=True, null=True)
#     tp_atend = models.ForeignKey('TbTipoAtend', models.DO_NOTHING, db_column='tp_atend', blank=True, null=True)
#     nu_conselho_classe = models.CharField(max_length=100, blank=True, null=True)
#     co_uf_emissora_conselho_classe = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf_emissora_conselho_classe', blank=True, null=True)
#     co_conselho_classe = models.ForeignKey('TbConselhoClasse', models.DO_NOTHING, db_column='co_conselho_classe', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_racionalidade_saude = models.ForeignKey('TbRacionalidadeSaude', models.DO_NOTHING, db_column='co_racionalidade_saude', blank=True, null=True)
#     co_lotacao_atend_compartilhado = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao_atend_compartilhado', blank=True, null=True)
#     st_registro_historico = models.IntegerField(blank=True, null=True)
#     nu_revisao = models.IntegerField(blank=True, null=True)
#     st_cancelado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend_prof'
#
#
# class TbAtendProfAd(models.Model):
#     co_atend_prof_ad = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof_ad', primary_key=True)
#     st_elegivel = models.IntegerField(blank=True, null=True)
#     co_ad_origem = models.ForeignKey(TbAdOrigem, models.DO_NOTHING, db_column='co_ad_origem', blank=True, null=True)
#     co_ad_modalidade = models.ForeignKey(TbAdModalidade, models.DO_NOTHING, db_column='co_ad_modalidade', blank=True, null=True)
#     co_ad_destino = models.ForeignKey(TbAdDestino, models.DO_NOTHING, db_column='co_ad_destino', blank=True, null=True)
#     co_ad_tipo_elegivel = models.ForeignKey(TbAdTipoElegivel, models.DO_NOTHING, db_column='co_ad_tipo_elegivel', blank=True, null=True)
#     nu_serial_aplicativo = models.CharField(max_length=100, blank=True, null=True)
#     ds_fabricante_dispositivo = models.CharField(max_length=100, blank=True, null=True)
#     ds_modelo_dispositivo = models.CharField(max_length=100, blank=True, null=True)
#     co_cid10_principal = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_principal', blank=True, null=True)
#     co_cid10_secundario_1 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_secundario_1', blank=True, null=True)
#     co_cid10_secundario_2 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_secundario_2', blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=16, blank=True, null=True)
#     no_cuidador = models.CharField(max_length=255, blank=True, null=True)
#     tp_cds_cuidador = models.ForeignKey('TbCdsTipoCuidador', models.DO_NOTHING, db_column='tp_cds_cuidador', blank=True, null=True)
#     dt_nascimento_cuidador = models.DateField(blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend_prof_ad'
#
#
# class TbAtendProfAdQst(models.Model):
#     co_seq_atend_prof_ad_qst = models.BigIntegerField(primary_key=True)
#     ds_atend_prof_ad_qst = models.CharField(max_length=100, blank=True, null=True)
#     st_atend_prof_ad_qst = models.IntegerField(blank=True, null=True)
#     nu_ordem = models.IntegerField(blank=True, null=True)
#     co_atend_prof_ad = models.ForeignKey(TbAtendProfAd, models.DO_NOTHING, db_column='co_atend_prof_ad', blank=True, null=True)
#     co_situacao_presente = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend_prof_ad_qst'
#
#
# class TbAtendProfOdonto(models.Model):
#     co_atend_prof_odonto = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof_odonto', primary_key=True)
#     tp_consulta_odonto = models.ForeignKey('TbTipoConsultaOdonto', models.DO_NOTHING, db_column='tp_consulta_odonto', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend_prof_odonto'
#
#
# class TbAtendProfPreNatal(models.Model):
#     co_atend_prof_pre_natal = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof_pre_natal', primary_key=True)
#     co_unico_pre_natal = models.BigIntegerField(blank=True, null=True)
#     tp_edema = models.ForeignKey('TbTipoEdema', models.DO_NOTHING, db_column='tp_edema', blank=True, null=True)
#     st_gravidez_planejada = models.IntegerField(blank=True, null=True)
#     st_movimentacao_fetal = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend_prof_pre_natal'
#
#
# class TbAtendProfPuericultura(models.Model):
#     co_atend_prof_puericultura = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof_puericultura', primary_key=True)
#     tp_aleitamento_materno = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend_prof_puericultura'
#
#
# class TbAtendProfTipoEncamIntrn(models.Model):
#     co_seq_atend_prof_tipo_enc_int = models.BigIntegerField(primary_key=True)
#     co_agendado = models.ForeignKey(TbAgendado, models.DO_NOTHING, db_column='co_agendado', blank=True, null=True)
#     co_atend = models.ForeignKey(TbAtend, models.DO_NOTHING, db_column='co_atend', blank=True, null=True)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     tp_encam_interno = models.ForeignKey('TbTipoEncamInterno', models.DO_NOTHING, db_column='tp_encam_interno')
#     st_agendado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atend_prof_tipo_encam_intrn'
#
#
# class TbAtestado(models.Model):
#     co_seq_atestado = models.BigIntegerField(primary_key=True)
#     dt_atestado = models.DateTimeField(blank=True, null=True)
#     ds_atestado = models.TextField(blank=True, null=True)
#     st_impresso = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     im_qrcode_atestado = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atestado'
#
#
# class TbAtivColGrupo(models.Model):
#     co_seq_ativ_col_grupo = models.BigIntegerField(primary_key=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     st_ficha = models.CharField(max_length=32, blank=True, null=True)
#     co_grupo = models.ForeignKey('TbGrupoAtivCol', models.DO_NOTHING, db_column='co_grupo', blank=True, null=True)
#     dt_atualizacao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ativ_col_grupo'
#
#
# class TbAtivacaoAgendamentoOnline(models.Model):
#     co_seq_ativacao_agendamento_on = models.BigIntegerField(primary_key=True)
#     co_prof = models.ForeignKey('TbProf', models.DO_NOTHING, db_column='co_prof', blank=True, null=True)
#     dt_evento = models.DateTimeField()
#     st_ativado = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ativacao_agendamento_online'
#
#
# class TbAtor(models.Model):
#     co_seq_ator = models.BigIntegerField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ator'
#
#
# class TbAtorPapel(models.Model):
#     co_seq_ator_papel = models.BigIntegerField(primary_key=True)
#     no_tipo_ator_papel = models.CharField(max_length=100, blank=True, null=True)
#     co_prof = models.ForeignKey('TbProf', models.DO_NOTHING, db_column='co_prof', blank=True, null=True)
#     ds_modulo_inicial = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ator_papel'
#
#
# class TbAtributoComplem(models.Model):
#     co_atributo_complem = models.BigIntegerField(primary_key=True)
#     no_atributo_complem = models.CharField(max_length=255)
#     dt_competencia = models.CharField(max_length=6)
#     nu_ms = models.CharField(max_length=3)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_atributo_complem'
#
#
# class TbAuditoriaEvento(models.Model):
#     co_seq_auditoria_evento = models.BigIntegerField(primary_key=True)
#     dt_evento = models.DateTimeField(blank=True, null=True)
#     tp_evento = models.IntegerField(blank=True, null=True)
#     ds_componente_gerador = models.CharField(max_length=1000, blank=True, null=True)
#     co_usuario = models.BigIntegerField(blank=True, null=True)
#     ds_detalhes = models.TextField(blank=True, null=True)
#     tp_registro_afetado = models.IntegerField(blank=True, null=True)
#     co_registro_afetado = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_auditoria_evento'
#
#
# class TbAuditoriaProcesso(models.Model):
#     co_seq_auditoria_processo = models.BigIntegerField(primary_key=True)
#     dt_inicio = models.DateField()
#     dt_fim = models.DateField()
#     dt_solicitacao = models.DateTimeField()
#     st_processo = models.CharField(max_length=100)
#     im_impressao = models.BinaryField(blank=True, null=True)
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario')
#     st_csv = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_auditoria_processo'
#
#
# class TbBairro(models.Model):
#     co_bairro = models.BigIntegerField(primary_key=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade')
#     nu_dne = models.CharField(unique=True, max_length=8, blank=True, null=True)
#     no_bairro = models.CharField(max_length=144)
#     no_bairro_filtro = models.CharField(max_length=144)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_bairro'
#
#
# class TbCalendarioVacinal(models.Model):
#     co_calendario_vacinal = models.BigIntegerField(primary_key=True)
#     co_imunobiologico = models.ForeignKey('TbImunobiologico', models.DO_NOTHING, db_column='co_imunobiologico', blank=True, null=True)
#     co_dose_imunobiologico = models.ForeignKey('TbDoseImunobiologico', models.DO_NOTHING, db_column='co_dose_imunobiologico', blank=True, null=True)
#     nu_ordem_imunobiologico = models.IntegerField(blank=True, null=True)
#     nu_ordem_dose = models.IntegerField(blank=True, null=True)
#     ds_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_calendario_vacinal'
#
#
# class TbCategoriaAgenteCausador(models.Model):
#     co_categoria_agente_causador = models.BigIntegerField(primary_key=True)
#     no_categoria_agente_causador = models.CharField(max_length=100, blank=True, null=True)
#     no_identificador = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_categoria_agente_causador'
#
#
# class TbCbo(models.Model):
#     co_cbo = models.BigIntegerField(primary_key=True)
#     no_cbo = models.CharField(max_length=255)
#     no_cbo_filtro = models.CharField(max_length=255)
#     co_cbo_2002 = models.CharField(max_length=10)
#     st_disponivel_lotacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cbo'
#
#
# class TbCboAtend(models.Model):
#     co_cbo = models.ForeignKey(TbCbo, models.DO_NOTHING, db_column='co_cbo')
#     qt_tempo_consulta = models.IntegerField(blank=True, null=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade', blank=True, null=True)
#     co_seq_cbo_atend = models.BigIntegerField(primary_key=True)
#     st_disponivel_lotacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cbo_atend'
#
#
# class TbCdsAdmMedicamento(models.Model):
#     co_cds_adm_medicamento = models.BigIntegerField(primary_key=True)
#     no_cds_adm_medicamento = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_adm_medicamento'
#
#
# class TbCdsAleitamentoMaterno(models.Model):
#     co_cds_aleitamento_materno = models.BigIntegerField(primary_key=True)
#     no_cds_aleitamento_materno = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_aleitamento_materno'
#
#
# class TbCdsAtendDomiciliar(models.Model):
#     co_seq_cds_atend_domiciliar = models.BigIntegerField(primary_key=True)
#     co_cds_ficha_atend_domiciliar = models.ForeignKey('TbCdsFichaAtendDomiciliar', models.DO_NOTHING, db_column='co_cds_ficha_atend_domiciliar', blank=True, null=True)
#     co_cds_turno = models.ForeignKey('TbCdsTurno', models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     co_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='co_local_atend', blank=True, null=True)
#     co_ad_modalidade = models.ForeignKey(TbAdModalidade, models.DO_NOTHING, db_column='co_ad_modalidade', blank=True, null=True)
#     tp_atend_v20 = models.ForeignKey('TbTipoAtend', models.DO_NOTHING, db_column='tp_atend_v20', blank=True, null=True)
#     co_cid10 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10', blank=True, null=True)
#     co_ciap = models.ForeignKey('TbCiap', models.DO_NOTHING, db_column='co_ciap', blank=True, null=True)
#     co_ad_destino_v20 = models.ForeignKey(TbAdDestino, models.DO_NOTHING, db_column='co_ad_destino_v20', blank=True, null=True)
#     st_inicio_acompanhamento_obito = models.IntegerField(blank=True, null=True)
#     co_ad_destino = models.ForeignKey(TbAdDestino, models.DO_NOTHING, db_column='co_ad_destino', blank=True, null=True)
#     tp_atend = models.ForeignKey('TbTipoAtend', models.DO_NOTHING, db_column='tp_atend', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_atend_domiciliar'
#
#
# class TbCdsAtendIndividual(models.Model):
#     co_seq_cds_atend_individual = models.BigIntegerField(primary_key=True)
#     co_cds_ficha_atend_individual = models.ForeignKey('TbCdsFichaAtendIndividual', models.DO_NOTHING, db_column='co_cds_ficha_atend_individual')
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField()
#     co_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='co_local_atend', blank=True, null=True)
#     co_cds_aleitamento_materno = models.ForeignKey(TbCdsAleitamentoMaterno, models.DO_NOTHING, db_column='co_cds_aleitamento_materno', blank=True, null=True)
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     co_cds_pic = models.ForeignKey('TbCdsPic', models.DO_NOTHING, db_column='co_cds_pic', blank=True, null=True)
#     co_cid10 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10', blank=True, null=True)
#     st_ficou_observacao = models.IntegerField(blank=True, null=True)
#     st_vacina_em_dia = models.IntegerField(blank=True, null=True)
#     nu_idade_gestacional = models.IntegerField(blank=True, null=True)
#     co_ad_modalidade = models.ForeignKey(TbAdModalidade, models.DO_NOTHING, db_column='co_ad_modalidade', blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     tp_atend = models.ForeignKey('TbTipoAtend', models.DO_NOTHING, db_column='tp_atend', blank=True, null=True)
#     co_cds_turno = models.ForeignKey('TbCdsTurno', models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     st_gravidez_planejada = models.IntegerField(blank=True, null=True)
#     qt_gestacao_previa = models.IntegerField(blank=True, null=True)
#     qt_parto = models.IntegerField(blank=True, null=True)
#     co_racionalidade_saude = models.ForeignKey('TbRacionalidadeSaude', models.DO_NOTHING, db_column='co_racionalidade_saude', blank=True, null=True)
#     nu_perimetro_cefalico = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
#     co_cid10_2 = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_2', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_atend_individual'
#
#
# class TbCdsAtendOdonto(models.Model):
#     co_seq_cds_atend_odonto = models.BigIntegerField(primary_key=True)
#     co_cds_ficha_atend_odonto = models.ForeignKey('TbCdsFichaAtendOdonto', models.DO_NOTHING, db_column='co_cds_ficha_atend_odonto')
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField()
#     co_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='co_local_atend', blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_necessidade_especial = models.IntegerField(blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     tp_atend = models.ForeignKey('TbTipoAtend', models.DO_NOTHING, db_column='tp_atend', blank=True, null=True)
#     co_cds_turno = models.ForeignKey('TbCdsTurno', models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_atend_odonto'
#
#
# class TbCdsAtivColParticipante(models.Model):
#     co_seq_cds_ativ_col_participnt = models.BigIntegerField(primary_key=True)
#     co_cds_ficha_ativ_col = models.ForeignKey('TbCdsFichaAtivCol', models.DO_NOTHING, db_column='co_cds_ficha_ativ_col')
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     st_avaliacao_alterada = models.IntegerField(blank=True, null=True)
#     st_cessou_habito_fumar = models.IntegerField(blank=True, null=True)
#     st_abandonou_grupo = models.IntegerField(blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ativ_col_participante'
#
#
# class TbCdsAtivColPratica(models.Model):
#     no_cds_ativ_col_pratica = models.CharField(max_length=255)
#     co_cds_ativ_col_pratica = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ativ_col_pratica'
#
#
# class TbCdsAtivColPublicoAlvo(models.Model):
#     no_cds_ativ_col_publico_alvo = models.CharField(max_length=255)
#     co_cds_ativ_col_publico_alvo = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ativ_col_publico_alvo'
#
#
# class TbCdsAtivColTema(models.Model):
#     no_cds_ativ_col_tema = models.CharField(max_length=255)
#     co_cds_ativ_col_tema = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ativ_col_tema'
#
#
# class TbCdsAvalElegibilidade(models.Model):
#     co_seq_cds_aval_elegibilidade = models.BigIntegerField(primary_key=True)
#     co_cds_prof_cadastrante = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof_cadastrante', blank=True, null=True)
#     co_ad_modalidade = models.ForeignKey(TbAdModalidade, models.DO_NOTHING, db_column='co_ad_modalidade', blank=True, null=True)
#     co_ad_origem = models.ForeignKey(TbAdOrigem, models.DO_NOTHING, db_column='co_ad_origem', blank=True, null=True)
#     tp_ad_elegivel = models.ForeignKey(TbAdTipoElegivel, models.DO_NOTHING, db_column='tp_ad_elegivel', blank=True, null=True)
#     co_cid10_principal = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_principal', blank=True, null=True)
#     co_cid10_segundo = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_segundo', blank=True, null=True)
#     co_cid10_terceiro = models.ForeignKey('TbCid10', models.DO_NOTHING, db_column='co_cid10_terceiro', blank=True, null=True)
#     co_localidade_cidadao = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_cidadao', blank=True, null=True)
#     co_localidade_cidadao_nasc = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_cidadao_nasc', blank=True, null=True)
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     co_nacionalidade = models.ForeignKey('TbNacionalidade', models.DO_NOTHING, db_column='co_nacionalidade', blank=True, null=True)
#     co_raca_cor = models.ForeignKey('TbRacaCor', models.DO_NOTHING, db_column='co_raca_cor', blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     tp_logradouro = models.ForeignKey('TbTipoLogradouro', models.DO_NOTHING, db_column='tp_logradouro', blank=True, null=True)
#     co_uf = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf', blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=256, blank=True, null=True)
#     ds_email_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     dt_aval_elegibilidade = models.DateTimeField(blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=256, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_logradouro = models.CharField(max_length=256, blank=True, null=True)
#     no_mae_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_social_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     nu_cep = models.CharField(max_length=8, blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     nu_domicilio = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_referencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_residencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_nis_pis_pasep = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     st_desconhece_nome_mae = models.IntegerField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     tp_cds_cuidador = models.ForeignKey('TbCdsTipoCuidador', models.DO_NOTHING, db_column='tp_cds_cuidador', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_cds_turno = models.ForeignKey('TbCdsTurno', models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     co_pais = models.ForeignKey('TbPais', models.DO_NOTHING, db_column='co_pais', blank=True, null=True)
#     co_etnia = models.ForeignKey('TbEtnia', models.DO_NOTHING, db_column='co_etnia', blank=True, null=True)
#     no_pai_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateTimeField(blank=True, null=True)
#     ds_portaria_naturalizacao = models.CharField(max_length=60, blank=True, null=True)
#     dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=15, blank=True, null=True)
#     co_cds_prof_at_compartilhado = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof_at_compartilhado', blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
#     co_ad_procedencia = models.ForeignKey(TbAdOrigem, models.DO_NOTHING, db_column='co_ad_procedencia', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_aval_elegibilidade'
#
#
# class TbCdsCadDomiciliar(models.Model):
#     co_seq_cds_cad_domiciliar = models.BigIntegerField(primary_key=True)
#     tp_logradouro = models.ForeignKey('TbTipoLogradouro', models.DO_NOTHING, db_column='tp_logradouro', blank=True, null=True)
#     no_logradouro = models.CharField(max_length=256, blank=True, null=True)
#     nu_domicilio = models.CharField(max_length=255, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=256, blank=True, null=True)
#     no_bairro = models.CharField(max_length=256, blank=True, null=True)
#     co_municipio = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_municipio', blank=True, null=True)
#     nu_cep = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_residencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_referencia = models.CharField(max_length=255, blank=True, null=True)
#     ds_rg_recusa_cad = models.CharField(max_length=255, blank=True, null=True)
#     dt_cad_domiciliar = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     st_recusa_cad = models.IntegerField(blank=True, null=True)
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     co_uf = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf', blank=True, null=True)
#     no_logradouro_filtro = models.CharField(max_length=256, blank=True, null=True)
#     st_atualizacao = models.IntegerField(blank=True, null=True)
#     co_cds_prof_cadastrante = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof_cadastrante')
#     co_unico_domicilio = models.CharField(max_length=96, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     st_versao_atual = models.IntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
#     no_instituicao_permanencia = models.CharField(max_length=255, blank=True, null=True)
#     st_outros_prof_vinculados = models.IntegerField(blank=True, null=True)
#     no_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     nu_cns_responsavel_tecnico = models.CharField(max_length=15, blank=True, null=True)
#     no_cargo_instituicao = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     tp_cds_imovel = models.ForeignKey('TbCdsTipoImovel', models.DO_NOTHING, db_column='tp_cds_imovel', blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     ds_complemento_filtro = models.CharField(max_length=255, blank=True, null=True)
#     st_gerado_automaticamente = models.IntegerField(blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_cad_domiciliar'
#
#
# class TbCdsCadIndividual(models.Model):
#     co_pais = models.ForeignKey('TbPais', models.DO_NOTHING, db_column='co_pais', blank=True, null=True)
#     co_municipio = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_municipio', blank=True, null=True)
#     nu_pis_pasep = models.CharField(max_length=255, blank=True, null=True)
#     nu_cartao_sus_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_responsavel = models.DateTimeField(blank=True, null=True)
#     ds_rg_recusa_cad = models.CharField(max_length=255, blank=True, null=True)
#     co_unidade_saude = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude', blank=True, null=True)
#     dt_cad_individual = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_cbo = models.ForeignKey(TbCbo, models.DO_NOTHING, db_column='co_cbo', blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     st_recusa_cad = models.IntegerField(blank=True, null=True)
#     st_responsavel_familiar = models.IntegerField(blank=True, null=True)
#     co_seq_cds_cad_individual = models.BigIntegerField(primary_key=True)
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_social_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_raca_cor = models.ForeignKey('TbRacaCor', models.DO_NOTHING, db_column='co_raca_cor', blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     no_mae_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_desconhece_nome_mae = models.IntegerField(blank=True, null=True)
#     co_nacionalidade = models.ForeignKey('TbNacionalidade', models.DO_NOTHING, db_column='co_nacionalidade', blank=True, null=True)
#     nu_celular_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_atualizacao = models.IntegerField(blank=True, null=True)
#     ds_email_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     co_cds_prof_cadastrante = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof_cadastrante')
#     co_unico_ficha_origem = models.CharField(max_length=96, blank=True, null=True)
#     st_versao_atual = models.IntegerField(blank=True, null=True)
#     co_unico_grupo = models.CharField(max_length=44, blank=True, null=True)
#     no_cidadao_filtro = models.CharField(max_length=600, blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_etnia = models.ForeignKey('TbEtnia', models.DO_NOTHING, db_column='co_etnia', blank=True, null=True)
#     no_pai_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateTimeField(blank=True, null=True)
#     ds_portaria_naturalizacao = models.CharField(max_length=60, blank=True, null=True)
#     dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
#     dt_obito = models.DateTimeField(blank=True, null=True)
#     nu_declaracao_obito = models.CharField(max_length=9, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     st_ficha_inativa = models.IntegerField(blank=True, null=True)
#     st_gerado_automaticamente = models.IntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#     st_erro_inativacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_cad_individual'
#
#
# class TbCdsCidadaoResposta(models.Model):
#     co_seq_cds_cidadao_resposta = models.BigIntegerField(primary_key=True)
#     co_pergunta = models.ForeignKey('TbPergunta', models.DO_NOTHING, db_column='co_pergunta')
#     co_pergunta_detalhe = models.ForeignKey('TbPerguntaDetalhe', models.DO_NOTHING, db_column='co_pergunta_detalhe', blank=True, null=True)
#     ds_resposta = models.CharField(max_length=255, blank=True, null=True)
#     st_resposta = models.IntegerField(blank=True, null=True)
#     co_cds_cad_individual = models.ForeignKey(TbCdsCadIndividual, models.DO_NOTHING, db_column='co_cds_cad_individual', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_cidadao_resposta'
#
#
# class TbCdsDomicilio(models.Model):
#     co_seq_cds_domicilio = models.BigIntegerField(primary_key=True)
#     tp_logradouro = models.ForeignKey('TbTipoLogradouro', models.DO_NOTHING, db_column='tp_logradouro', blank=True, null=True)
#     ds_complemento = models.CharField(max_length=256, blank=True, null=True)
#     co_municipio = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_municipio', blank=True, null=True)
#     no_logradouro = models.CharField(max_length=256, blank=True, null=True)
#     no_bairro = models.CharField(max_length=256, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     nu_fone_referencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_residencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_domicilio = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_domicilio = models.CharField(max_length=96, blank=True, null=True)
#     dt_ultima_atualizacao = models.DateTimeField(blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     co_uf = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf', blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_ultima_ficha = models.CharField(max_length=96, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     tp_cds_imovel = models.ForeignKey('TbCdsTipoImovel', models.DO_NOTHING, db_column='tp_cds_imovel', blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
#     no_instituicao_permanencia = models.CharField(max_length=255, blank=True, null=True)
#     st_outros_prof_vinculados = models.IntegerField(blank=True, null=True)
#     no_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     nu_cns_responsavel_tecnico = models.CharField(max_length=15, blank=True, null=True)
#     no_cargo_instituicao = models.CharField(max_length=255, blank=True, null=True)
#     nu_contato_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_domicilio'
#
#
# class TbCdsDomicilioFamilia(models.Model):
#     co_seq_cds_domicilio_familia = models.BigIntegerField(primary_key=True)
#     co_cds_cad_domiciliar = models.ForeignKey(TbCdsCadDomiciliar, models.DO_NOTHING, db_column='co_cds_cad_domiciliar')
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_renda_familiar = models.ForeignKey('TbRendaFamiliar', models.DO_NOTHING, db_column='co_renda_familiar', blank=True, null=True)
#     dt_mudanca = models.DateTimeField(blank=True, null=True)
#     qt_membros_familia = models.IntegerField(blank=True, null=True)
#     st_mudanca = models.IntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_domicilio_familia'
#
#
# class TbCdsDomicilioResposta(models.Model):
#     co_seq_cds_domicilio_resposta = models.BigIntegerField(primary_key=True)
#     co_cds_cad_domiciliar = models.ForeignKey(TbCdsCadDomiciliar, models.DO_NOTHING, db_column='co_cds_cad_domiciliar')
#     co_pergunta = models.ForeignKey('TbPergunta', models.DO_NOTHING, db_column='co_pergunta')
#     co_pergunta_detalhe = models.ForeignKey('TbPerguntaDetalhe', models.DO_NOTHING, db_column='co_pergunta_detalhe', blank=True, null=True)
#     ds_resposta = models.CharField(max_length=255, blank=True, null=True)
#     st_resposta = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_domicilio_resposta'
#
#
# class TbCdsFichaAtendDomiciliar(models.Model):
#     co_seq_cds_ficha_atend_dom = models.BigIntegerField(primary_key=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     co_cds_prof_principal = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof_principal', blank=True, null=True)
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_cds_prof_atend_comp = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof_atend_comp', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_atend_domiciliar'
#
#
# class TbCdsFichaAtendIndividual(models.Model):
#     co_seq_cds_ficha_atend_indivdl = models.BigIntegerField(primary_key=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof')
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_atend_individual'
#
#
# class TbCdsFichaAtendOdonto(models.Model):
#     co_seq_cds_ficha_atend_odonto = models.BigIntegerField(primary_key=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof')
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_atend_odonto'
#
#
# class TbCdsFichaAtivCol(models.Model):
#     co_seq_cds_ficha_ativ_col = models.BigIntegerField(primary_key=True)
#     dt_ativ_col = models.DateTimeField(blank=True, null=True)
#     hr_inicio = models.DateTimeField(blank=True, null=True)
#     hr_fim = models.DateTimeField(blank=True, null=True)
#     co_inep_escola = models.BigIntegerField(blank=True, null=True)
#     ds_local_ativ = models.CharField(max_length=500, blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     qt_avaliacao_alterada = models.IntegerField(blank=True, null=True)
#     qt_participante_ativ = models.IntegerField(blank=True, null=True)
#     qt_participante_programado = models.IntegerField(blank=True, null=True)
#     tp_cds_ativ_col = models.ForeignKey('TbCdsTipoAtivCol', models.DO_NOTHING, db_column='tp_cds_ativ_col', blank=True, null=True)
#     co_cds_prof_responsavel = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof_responsavel')
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_cds_turno = models.ForeignKey('TbCdsTurno', models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     co_proced_sigtap = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced_sigtap', blank=True, null=True)
#     st_pse_educacao = models.IntegerField(blank=True, null=True)
#     st_pse_saude = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_ativ_col'
#
#
# class TbCdsFichaConsumoAlimentar(models.Model):
#     co_seq_cds_ficha_consumo_alim = models.BigIntegerField(primary_key=True)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof', blank=True, null=True)
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_identificacao_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_cidadao = models.DateTimeField(blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     co_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='co_local_atend', blank=True, null=True)
#     co_qst_questionario_respondido = models.ForeignKey('TbQstQuestionarioRespondido', models.DO_NOTHING, db_column='co_qst_questionario_respondido', blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_consumo_alimentar'
#
#
# class TbCdsFichaProced(models.Model):
#     co_seq_cds_ficha_proced = models.BigIntegerField(primary_key=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     qt_afericao_pressao_arterial = models.BigIntegerField(blank=True, null=True)
#     qt_glicemia = models.BigIntegerField(blank=True, null=True)
#     qt_afericao_temperatura = models.BigIntegerField(blank=True, null=True)
#     qt_medicao_altura = models.BigIntegerField(blank=True, null=True)
#     qt_curativo_simples = models.BigIntegerField(blank=True, null=True)
#     qt_medicao_peso = models.BigIntegerField(blank=True, null=True)
#     qt_coleta_material = models.BigIntegerField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof')
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_proced'
#
#
# class TbCdsFichaVacinacao(models.Model):
#     co_seq_cds_ficha_vacinacao = models.BigIntegerField(primary_key=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.ForeignKey('TbCdsTipoOrigem', models.DO_NOTHING, db_column='tp_cds_origem', blank=True, null=True)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof', blank=True, null=True)
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     st_cancelado = models.IntegerField(blank=True, null=True)
#     nu_revisao = models.IntegerField(blank=True, null=True)
#     co_unico_ficha_cancelada = models.CharField(max_length=96, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_vacinacao'
#
#
# class TbCdsFichaVisitaDomiciliar(models.Model):
#     co_seq_cds_ficha_visita_dom = models.BigIntegerField(primary_key=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof')
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_visita_domiciliar'
#
#
# class TbCdsFichaZikaMicrocefalia(models.Model):
#     co_seq_cds_ficha_zica_micrcfl = models.BigIntegerField(primary_key=True)
#     co_cds_turno = models.ForeignKey('TbCdsTurno', models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     co_cds_prof = models.ForeignKey('TbCdsProf', models.DO_NOTHING, db_column='co_cds_prof', blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_cns_responsavel_familiar = models.CharField(max_length=15, blank=True, null=True)
#     dt_ficha_complementar = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     st_enfileirado = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96)
#     co_localidade_origem = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_origem', blank=True, null=True)
#     dt_teste_olhinho = models.DateTimeField(blank=True, null=True)
#     co_teste_olhinho = models.ForeignKey('TbFichaZikaTipoExame', models.DO_NOTHING, db_column='co_teste_olhinho', blank=True, null=True)
#     dt_exame_fundo_olho = models.DateTimeField(blank=True, null=True)
#     co_exame_fundo_olho = models.ForeignKey('TbFichaZikaTipoExame', models.DO_NOTHING, db_column='co_exame_fundo_olho', blank=True, null=True)
#     dt_exame_orelhinha = models.DateTimeField(blank=True, null=True)
#     co_exame_orelhinha = models.ForeignKey('TbFichaZikaTipoExame', models.DO_NOTHING, db_column='co_exame_orelhinha', blank=True, null=True)
#     dt_us_transfontanela = models.DateTimeField(blank=True, null=True)
#     co_us_transfontanela = models.ForeignKey('TbFichaZikaTipoExame', models.DO_NOTHING, db_column='co_us_transfontanela', blank=True, null=True)
#     dt_tomografia_computadorizada = models.DateTimeField(blank=True, null=True)
#     co_tomografia_computadorizada = models.ForeignKey('TbFichaZikaTipoExame', models.DO_NOTHING, db_column='co_tomografia_computadorizada', blank=True, null=True)
#     dt_ressonancia_magnetica = models.DateTimeField(blank=True, null=True)
#     co_ressonancia_magnetica = models.ForeignKey('TbFichaZikaTipoExame', models.DO_NOTHING, db_column='co_ressonancia_magnetica', blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_ficha_zika_microcefalia'
#
#
# class TbCdsPic(models.Model):
#     co_cds_pic = models.BigIntegerField(primary_key=True)
#     no_cds_pic = models.CharField(max_length=255)
#     no_cds_pic_filtro = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_pic'
#
#
# class TbCdsProced(models.Model):
#     co_seq_cds_proced = models.BigIntegerField(primary_key=True)
#     co_cds_ficha_proced = models.ForeignKey(TbCdsFichaProced, models.DO_NOTHING, db_column='co_cds_ficha_proced')
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField()
#     co_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='co_local_atend', blank=True, null=True)
#     st_escuta_inicial = models.IntegerField(blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     co_cds_turno = models.ForeignKey('TbCdsTurno', models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_proced'
#
#
# class TbCdsProf(models.Model):
#     co_seq_cds_prof = models.BigIntegerField(primary_key=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cbo_2002 = models.CharField(max_length=10, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_cds_prof = models.CharField(unique=True, max_length=40)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_prof'
#
#
# class TbCdsTipoAtendNasf(models.Model):
#     co_cds_tipo_atend_nasf = models.BigIntegerField(primary_key=True)
#     no_cds_tipo_atend_nasf = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_atend_nasf'
#
#
# class TbCdsTipoAtivCol(models.Model):
#     no_cds_tipo_ativ_col = models.CharField(max_length=255)
#     co_cds_tipo_ativ_col = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_ativ_col'
#
#
# class TbCdsTipoConduta(models.Model):
#     co_cds_tipo_conduta = models.BigIntegerField(primary_key=True)
#     no_cds_tipo_conduta = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_conduta'
#
#
# class TbCdsTipoCuidador(models.Model):
#     co_cds_tipo_cuidador = models.BigIntegerField(primary_key=True)
#     no_cds_tipo_cuidador = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_cuidador'
#
#
# class TbCdsTipoImovel(models.Model):
#     co_cds_tipo_imovel = models.BigIntegerField(primary_key=True)
#     no_cds_tipo_imovel = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_imovel'
#
#
# class TbCdsTipoOrigem(models.Model):
#     co_cds_tipo_origem = models.BigIntegerField(primary_key=True)
#     no_cds_tipo_origem = models.CharField(max_length=225)
#     no_identificador = models.CharField(max_length=225)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_origem'
#
#
# class TbCdsTipoSituacaoPresente(models.Model):
#     co_cds_tipo_situacao_presente = models.BigIntegerField(primary_key=True)
#     no_cds_tipo_situacao_presente = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_situacao_presente'
#
#
# class TbCdsTipoVigSaudeBucal(models.Model):
#     no_cds_tipo_vig_saude_bucal = models.CharField(max_length=255)
#     co_cds_tipo_vig_saude_bucal = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_tipo_vig_saude_bucal'
#
#
# class TbCdsTurno(models.Model):
#     co_cds_turno = models.BigIntegerField(primary_key=True)
#     no_cds_turno = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_turno'
#
#
# class TbCdsVacina(models.Model):
#     co_seq_cds_vacina = models.BigIntegerField(primary_key=True)
#     co_estrategia_vacinacao = models.ForeignKey('TbEstrategiaVacinacao', models.DO_NOTHING, db_column='co_estrategia_vacinacao', blank=True, null=True)
#     co_imunobiologico = models.ForeignKey('TbImunobiologico', models.DO_NOTHING, db_column='co_imunobiologico', blank=True, null=True)
#     co_dose_imunobiologico = models.ForeignKey('TbDoseImunobiologico', models.DO_NOTHING, db_column='co_dose_imunobiologico', blank=True, null=True)
#     ds_lote = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_filtro = models.CharField(max_length=255, blank=True, null=True)
#     no_fabricante = models.CharField(max_length=255, blank=True, null=True)
#     no_fabricante_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_cds_vacinacao = models.ForeignKey('TbCdsVacinacao', models.DO_NOTHING, db_column='co_cds_vacinacao', blank=True, null=True)
#     co_grupo_atendimento = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_vacina'
#
#
# class TbCdsVacinacao(models.Model):
#     co_seq_cds_vacinacao = models.BigIntegerField(primary_key=True)
#     co_cds_turno = models.ForeignKey(TbCdsTurno, models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     co_local_atend = models.ForeignKey('TbLocalAtend', models.DO_NOTHING, db_column='co_local_atend', blank=True, null=True)
#     st_viajante = models.IntegerField(blank=True, null=True)
#     st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_puerpera = models.IntegerField(blank=True, null=True)
#     co_cds_ficha_vacinacao = models.ForeignKey(TbCdsFichaVacinacao, models.DO_NOTHING, db_column='co_cds_ficha_vacinacao', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_vacinacao'
#
#
# class TbCdsVisitaDomDesfecho(models.Model):
#     no_cds_visita_dom_desfecho = models.CharField(max_length=255)
#     co_cds_visita_dom_desfecho = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_visita_dom_desfecho'
#
#
# class TbCdsVisitaDomMotivo(models.Model):
#     no_cds_visita_dom_motivo = models.CharField(max_length=255)
#     co_cds_visita_dom_motivo = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_visita_dom_motivo'
#
#
# class TbCdsVisitaDomiciliar(models.Model):
#     co_seq_cds_visita_domiciliar = models.BigIntegerField(primary_key=True)
#     co_cds_ficha_visita_domiciliar = models.ForeignKey(TbCdsFichaVisitaDomiciliar, models.DO_NOTHING, db_column='co_cds_ficha_visita_domiciliar')
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     st_acompanhada_outro_prof = models.IntegerField(blank=True, null=True)
#     co_cds_turno = models.ForeignKey(TbCdsTurno, models.DO_NOTHING, db_column='co_cds_turno', blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     co_cds_visita_dom_desfecho = models.ForeignKey(TbCdsVisitaDomDesfecho, models.DO_NOTHING, db_column='co_cds_visita_dom_desfecho', blank=True, null=True)
#     tp_cds_imovel = models.ForeignKey(TbCdsTipoImovel, models.DO_NOTHING, db_column='tp_cds_imovel', blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     nu_peso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
#     nu_altura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     tp_glicemia = models.ForeignKey('TbTipoGlicemia', models.DO_NOTHING, db_column='tp_glicemia', blank=True, null=True)
#     nu_medicao_pressao_arterial = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_temperatura = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_glicemia = models.CharField(max_length=20, blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#     co_uuid_origem_fcd = models.CharField(max_length=44, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cds_visita_domiciliar'
#
#
# class TbCfgAgenda(models.Model):
#     co_seq_config_agenda = models.BigIntegerField(primary_key=True)
#     co_entidade_configurada = models.BigIntegerField()
#     co_tipo_cfg_agenda = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cfg_agenda'
#
#
# class TbCfgAgendaDetalhe(models.Model):
#     co_seq_config_agenda_detalhe = models.BigIntegerField(primary_key=True)
#     co_dia_semana = models.ForeignKey('TbDiaSemana', models.DO_NOTHING, db_column='co_dia_semana')
#     co_periodo = models.ForeignKey('TbPeriodo', models.DO_NOTHING, db_column='co_periodo')
#     horario_inicial = models.CharField(max_length=5)
#     horario_final = models.CharField(max_length=5)
#     co_cfg_agenda = models.ForeignKey(TbCfgAgenda, models.DO_NOTHING, db_column='co_cfg_agenda')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cfg_agenda_detalhe'
#
#
# class TbCfgAgendaMunicipal(models.Model):
#     co_seq_cfg_agenda_municipal = models.BigIntegerField(primary_key=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade')
#     nu_duracao_atendimento_padrao = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cfg_agenda_municipal'
#
#
# class TbCfgAgendaOnlineDetalhe(models.Model):
#     co_seq_cfg_agenda_online_dtlh = models.BigIntegerField(primary_key=True)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao')
#     co_dia_semana = models.ForeignKey('TbDiaSemana', models.DO_NOTHING, db_column='co_dia_semana')
#     ds_horario = models.CharField(max_length=5)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     uuid_horario_agenda_online = models.CharField(unique=True, max_length=36, blank=True, null=True)
#     st_registro_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cfg_agenda_online_detalhe'
#
#
# class TbCfgRnds(models.Model):
#     co_seq_cfg_rnds = models.BigIntegerField(primary_key=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade')
#     co_ator_papel = models.ForeignKey(TbAdmMunicipal, models.DO_NOTHING, db_column='co_ator_papel')
#     no_certificado = models.CharField(max_length=255)
#     ds_senha_certificado = models.CharField(max_length=255)
#     dt_inclusao = models.DateTimeField()
#     dt_habilitacao = models.DateTimeField()
#     dt_validade_certificado = models.DateTimeField()
#     co_identificador_solicitante = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cfg_rnds'
#
#
# class TbCiap(models.Model):
#     co_seq_ciap = models.BigIntegerField(primary_key=True)
#     co_ciap = models.CharField(max_length=6, blank=True, null=True)
#     ds_ciap = models.CharField(max_length=255, blank=True, null=True)
#     ds_ciap_filtro = models.CharField(max_length=255)
#     st_filtro_padrao = models.IntegerField(blank=True, null=True)
#     co_cid10_encaminhamento = models.BigIntegerField(blank=True, null=True)
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ciap'
#
#
# class TbCiapCapitulo(models.Model):
#     co_seq_ciap_capitulo = models.BigIntegerField(primary_key=True)
#     co_capitulo = models.CharField(max_length=255, blank=True, null=True)
#     ds_capitulo = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ciap_capitulo'
#
#
# class TbCiapComponente(models.Model):
#     co_ciap_componente = models.BigIntegerField(primary_key=True)
#     no_ciap_componente = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ciap_componente'
#
#
# class TbCiapDab(models.Model):
#     co_ciap = models.OneToOneField(TbCiap, models.DO_NOTHING, db_column='co_ciap', primary_key=True)
#     nu_ciap_ms = models.CharField(max_length=6, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ciap_dab'
#
#
# class TbCiapMs(models.Model):
#     co_ciap = models.OneToOneField(TbCiap, models.DO_NOTHING, db_column='co_ciap', primary_key=True)
#     ds_inclusao = models.CharField(max_length=400, blank=True, null=True)
#     ds_exclusao = models.CharField(max_length=400, blank=True, null=True)
#     ds_criterio = models.CharField(max_length=400, blank=True, null=True)
#     ds_nota = models.CharField(max_length=400, blank=True, null=True)
#     ds_definicao = models.CharField(max_length=400, blank=True, null=True)
#     co_ciap_componente = models.ForeignKey(TbCiapComponente, models.DO_NOTHING, db_column='co_ciap_componente', blank=True, null=True)
#     tp_ciap = models.ForeignKey('TbTipoCiap', models.DO_NOTHING, db_column='tp_ciap', blank=True, null=True)
#     co_ciap_capitulo = models.ForeignKey(TbCiapCapitulo, models.DO_NOTHING, db_column='co_ciap_capitulo', blank=True, null=True)
#     ds_inclusao_filtro = models.CharField(max_length=400, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ciap_ms'
#
#
# class TbCid10(models.Model):
#     co_cid10 = models.BigIntegerField(primary_key=True)
#     nu_cid10 = models.CharField(max_length=4)
#     tp_agravo = models.ForeignKey('TbTipoAgravo', models.DO_NOTHING, db_column='tp_agravo')
#     no_cid10 = models.CharField(max_length=400)
#     no_cid10_filtro = models.CharField(max_length=400)
#     st_ativo = models.IntegerField()
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cid10'


# class TbCidadao(models.Model):
#     co_seq_cidadao = models.BigIntegerField(primary_key=True)
#     co_unico_cidadao_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     co_unico_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     st_desconhece_nome_mae = models.IntegerField()
#     co_localidade = models.ForeignKey('esus.TbLocalidade',
#                                       on_delete=models.DO_NOTHING,
#                                       db_column='co_localidade',
#                                       blank=True, null=True)
#     nu_area = models.CharField(max_length=3, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     nu_nis_pis_pasep = models.CharField(max_length=50, blank=True, null=True)
#     dt_atualizado = models.DateTimeField(blank=True, null=True)
#     nu_cns_responsavel = models.CharField(max_length=16, blank=True, null=True)
#     no_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_responsavel = models.DateTimeField(blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=16, blank=True, null=True)
#     no_cuidador = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_cuidador = models.DateTimeField(blank=True, null=True)
#     tp_cds_cuidador = models.ForeignKey('esus.TbCdsTipoCuidador',
#                                         on_delete=models.DO_NOTHING,
#                                         db_column='tp_cds_cuidador',
#                                         blank=True, null=True)
#     co_unico_cidadao = models.CharField(max_length=96)
#     co_nacionalidade = models.ForeignKey('TbNacionalidade', models.DO_NOTHING, db_column='co_nacionalidade')
#     co_pais_nascimento = models.ForeignKey('TbPais', models.DO_NOTHING, db_column='co_pais_nascimento', blank=True, null=True)
#     co_unico_ultima_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ultima_ficha = models.DateField(blank=True, null=True)
#     st_registro_cadsus = models.IntegerField(blank=True, null=True)
#     dt_atualizado_cadsus = models.DateField(blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateTimeField(blank=True, null=True)
#     dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
#     nu_portaria_naturalizacao = models.CharField(max_length=16, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     st_infrm_orientacao_sexual = models.IntegerField(blank=True, null=True)
#     tp_orientacao_sexual = models.CharField(max_length=25, blank=True, null=True)
#     st_infrm_identidade_genero = models.IntegerField(blank=True, null=True)
#     tp_identidade_genero = models.CharField(max_length=25, blank=True, null=True)
#     st_compartilhamento_prontuario = models.IntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_nao_possui_cuidador = models.IntegerField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=500, blank=True, null=True)
#     no_cidadao_filtro = models.CharField(max_length=600, blank=True, null=True)
#     co_escolaridade = models.ForeignKey('TbEscolaridade', models.DO_NOTHING, db_column='co_escolaridade', blank=True, null=True)
#     co_raca_cor = models.ForeignKey('TbRacaCor', models.DO_NOTHING, db_column='co_raca_cor', blank=True, null=True)
#     co_etnia = models.ForeignKey('TbEtnia', models.DO_NOTHING, db_column='co_etnia', blank=True, null=True)
#     co_estado_civil = models.ForeignKey('TbEstadoCivil', models.DO_NOTHING, db_column='co_estado_civil', blank=True, null=True)
#     co_cbo = models.ForeignKey(TbCbo, models.DO_NOTHING, db_column='co_cbo', blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     dt_obito = models.DateField(blank=True, null=True)
#     no_mae = models.CharField(max_length=500, blank=True, null=True)
#     no_mae_filtro = models.CharField(max_length=600, blank=True, null=True)
#     no_pai = models.CharField(max_length=500, blank=True, null=True)
#     no_social = models.CharField(max_length=255, blank=True, null=True)
#     st_faleceu = models.IntegerField(blank=True, null=True)
#     nu_documento_obito = models.CharField(max_length=255, blank=True, null=True)
#     st_dados_obito_cadsus = models.IntegerField(blank=True, null=True)
#     no_localidade_exterior = models.CharField(max_length=255, blank=True, null=True)
#     co_pais_exterior = models.ForeignKey('TbPais', models.DO_NOTHING, db_column='co_pais_exterior', blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf', blank=True, null=True)
#     co_localidade_endereco = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade_endereco', blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.ForeignKey('TbTipoLogradouro', models.DO_NOTHING, db_column='tp_logradouro', blank=True, null=True)
#     nu_telefone_residencial = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_celular = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_contato = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo_para_exibicao = models.IntegerField(blank=True, null=True)
#     st_unificado = models.IntegerField()
#     st_territorio_utiliza_cpf = models.IntegerField(blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#     no_tipo_sanguineo = models.CharField(max_length=22, blank=True, null=True)
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'tb_cidadao'


# class TbCidadaoGrupo(models.Model):
#     co_seq_cidadao_grupo = models.BigIntegerField(primary_key=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     nu_uuid_ultima_ficha = models.CharField(max_length=96, blank=True, null=True)
#     nu_uuid_origem = models.CharField(max_length=96, blank=True, null=True)
#     co_cidadao = models.ForeignKey(TbCidadao, models.DO_NOTHING, db_column='co_cidadao')
#     co_cidadao_master = models.ForeignKey(TbCidadao, models.DO_NOTHING, db_column='co_cidadao_master')
#     co_cidadao_unificado = models.ForeignKey(TbCidadao, models.DO_NOTHING, db_column='co_cidadao_unificado')
#     dt_atualizacao = models.DateTimeField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cidadao_grupo'
#
#
# class TbCidadaoGrupoAtivCol(models.Model):
#     co_seq_cidadao_grupo = models.BigIntegerField(primary_key=True)
#     co_unico_cidadao_grupo = models.CharField(unique=True, max_length=96)
#     no_cidadao_grupo = models.CharField(max_length=255, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_sexo = models.IntegerField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cidadao_grupo_ativ_col'
#
#
# class TbCidadaoNucleoFamiliar(models.Model):
#     co_seq_cidadao_nucleo_familiar = models.BigIntegerField(primary_key=True)
#     dt_ultima_atualizacao = models.DateField()
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20)
#     nu_cpf_cns_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     st_responsavel = models.IntegerField()
#     st_mudou_se = models.IntegerField()
#     co_cidadao = models.ForeignKey(TbCidadao, models.DO_NOTHING, db_column='co_cidadao')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cidadao_nucleo_familiar'
#
#
# class TbCidadaoVinculacaoEquipe(models.Model):
#     co_seq_cidadao_vinculacao_eqp = models.BigIntegerField(primary_key=True)
#     co_cidadao = models.OneToOneField(TbCidadao, models.DO_NOTHING, db_column='co_cidadao')
#     co_unico_ficha = models.CharField(unique=True, max_length=96)
#     co_unico_cadastro_individual = models.CharField(max_length=96, blank=True, null=True)
#     st_envio = models.IntegerField()
#     ds_versao_ficha = models.CharField(max_length=30)
#     st_usar_cadastro_individual = models.IntegerField(blank=True, null=True)
#     st_saida_cadastro_obito = models.IntegerField(blank=True, null=True)
#     st_saida_cadastro_territorio = models.IntegerField(blank=True, null=True)
#     dt_atualizacao_cadastro = models.DateTimeField()
#     co_prof_cadastrante_cds = models.ForeignKey(TbCdsProf, models.DO_NOTHING, db_column='co_prof_cadastrante_cds', blank=True, null=True)
#     co_lotacao_cadastrante_pec = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao_cadastrante_pec', blank=True, null=True)
#     tp_cds_origem = models.ForeignKey(TbCdsTipoOrigem, models.DO_NOTHING, db_column='tp_cds_origem', blank=True, null=True)
#     nu_cnes = models.CharField(max_length=7, blank=True, null=True)
#     nu_ine = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cidadao_vinculacao_equipe'
#
#
# class TbClasseImunobiologico(models.Model):
#     co_classe_imunobiologico = models.BigIntegerField(primary_key=True)
#     no_classe_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_classe_imunobiologico'
#
#
# class TbClassificacaoRisco(models.Model):
#     co_classificacao_risco = models.BigIntegerField(primary_key=True)
#     no_classificacao_risco = models.CharField(max_length=50, blank=True, null=True)
#     no_identificador = models.CharField(max_length=30)
#     nu_ordem = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_classificacao_risco'
#
#
# class TbClassificacaoRiscoEncam(models.Model):
#     co_classificacao_risco_encam = models.BigIntegerField(primary_key=True)
#     no_classificacao_risco_encam = models.CharField(max_length=50)
#     no_identificador = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_classificacao_risco_encam'
#
#
# class TbComplexidade(models.Model):
#     no_complexidade = models.CharField(max_length=100)
#     sg_complexidade = models.CharField(max_length=2)
#     co_complexidade = models.BigIntegerField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_complexidade'
#
#
# class TbConfigAgendaFechamento(models.Model):
#     dt_inicio = models.DateTimeField()
#     dt_fim = models.DateTimeField()
#     ds_motivo = models.CharField(max_length=4000, blank=True, null=True)
#     co_seq_config_agenda_fechament = models.BigIntegerField(primary_key=True)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     no_ident_motivo_fechamento = models.CharField(max_length=30, blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     st_registro_ativo = models.IntegerField(blank=True, null=True)
#     uuid_fechamento = models.CharField(unique=True, max_length=36, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_config_agenda_fechamento'
#
#
# class TbConfigAtencaoDomiciliar(models.Model):
#     co_seq_config_atencao_domicilr = models.BigIntegerField(primary_key=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade', blank=True, null=True)
#     qt_tempo_duracao_consulta = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_config_atencao_domiciliar'
#
#
# class TbConfigAtendDomiciliar(models.Model):
#     co_seq_config_atend_domiciliar = models.BigIntegerField(primary_key=True)
#     co_equipe_pai = models.ForeignKey('TbEquipe', models.DO_NOTHING, db_column='co_equipe_pai')
#     co_equipe_filho = models.ForeignKey('TbEquipe', models.DO_NOTHING, db_column='co_equipe_filho')
#     co_config_atencao_domiciliar = models.ForeignKey(TbConfigAtencaoDomiciliar, models.DO_NOTHING, db_column='co_config_atencao_domiciliar', blank=True, null=True)
#     tp_config_atend_domiciliar = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_config_atend_domiciliar'
#
#
# class TbConfigSistema(models.Model):
#     co_config_sistema = models.CharField(primary_key=True, max_length=255)
#     ds_config_sistema = models.CharField(max_length=255)
#     st_disponivel_sistema = models.IntegerField()
#     ds_texto = models.CharField(max_length=255, blank=True, null=True)
#     ds_inteiro = models.IntegerField(blank=True, null=True)
#     ds_binario = models.BinaryField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_config_sistema'
#
#
# class TbConselhoClasse(models.Model):
#     co_conselho_classe = models.BigIntegerField(primary_key=True)
#     sg_conselho_classe = models.CharField(max_length=255, blank=True, null=True)
#     no_conselho_classe = models.CharField(max_length=200, blank=True, null=True)
#     no_curto_conselho = models.CharField(max_length=400, blank=True, null=True)
#     no_conselho_classe_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_conselho_classe'
#
#
# class TbContextoPergunta(models.Model):
#     co_contexto_pergunta = models.BigIntegerField(primary_key=True)
#     ds_contexto_pergunta = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_contexto_pergunta'
#
#
# class TbCriticidadeAlergia(models.Model):
#     co_criticidade_alergia = models.BigIntegerField(primary_key=True)
#     no_criticidade_alergia = models.CharField(max_length=50, blank=True, null=True)
#     no_identificador = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_criticidade_alergia'
#
#
# class TbCronicidade(models.Model):
#     co_cronicidade = models.BigIntegerField(primary_key=True)
#     no_cronicidade = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_cronicidade'
#
#
# class TbDadoRecebidoCompetencia(models.Model):
#     co_seq_dado_recebido_competenc = models.BigIntegerField(primary_key=True)
#     no_competencia = models.CharField(max_length=20, blank=True, null=True)
#     nu_mes = models.IntegerField(blank=True, null=True)
#     nu_ano = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dado_recebido_competencia'
#
#
# class TbDadoRecebidoInfoInstalac(models.Model):
#     co_seq_dado_recebido_info_inst = models.BigIntegerField(primary_key=True)
#     nu_contra_chave = models.CharField(max_length=96, blank=True, null=True)
#     co_unico_instalacao = models.CharField(max_length=96, blank=True, null=True)
#     nu_identificador_responsavel = models.CharField(max_length=20, blank=True, null=True)
#     no_responsavel_envio = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone = models.CharField(max_length=25, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     ds_versao_sistema = models.CharField(max_length=30, blank=True, null=True)
#     ds_banco_de_dados = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dado_recebido_info_instalac'
#
#
# class TbDadoRelProcessamento(models.Model):
#     co_seq_dado_rel_processamento = models.BigIntegerField(primary_key=True)
#     dt_marca_reprocessamento = models.DateTimeField(blank=True, null=True)
#     co_ator_papel = models.ForeignKey(TbAtorPapel, models.DO_NOTHING, db_column='co_ator_papel', blank=True, null=True)
#     dt_processamento_inicio = models.DateTimeField(blank=True, null=True)
#     dt_processamento_producao = models.DateTimeField(blank=True, null=True)
#     dt_processamento_consolidados = models.DateTimeField(blank=True, null=True)
#     dt_processamento_operacionais = models.DateTimeField(blank=True, null=True)
#     dt_processamento_conclusao = models.DateTimeField(blank=True, null=True)
#     dt_att_cidadao_pec_etl = models.DateTimeField(blank=True, null=True)
#     co_dim_tempo_inicio = models.ForeignKey('TbDimTempo', models.DO_NOTHING, db_column='co_dim_tempo_inicio', blank=True, null=True)
#     co_dim_tempo_final = models.ForeignKey('TbDimTempo', models.DO_NOTHING, db_column='co_dim_tempo_final', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dado_rel_processamento'
#
#
# class TbDadoTransp(models.Model):
#     co_seq_dado_transp = models.BigIntegerField(primary_key=True)
#     tp_origem_dado_transp = models.ForeignKey('TbTipoOrigemDadoTransp', models.DO_NOTHING, db_column='tp_origem_dado_transp')
#     tp_dado_transp = models.BigIntegerField()
#     co_unico_dado_serializado = models.CharField(unique=True, max_length=96)
#     co_ibge_dado_serializado = models.CharField(max_length=10, blank=True, null=True)
#     nu_versao_dado_serializado = models.CharField(max_length=10, blank=True, null=True)
#     nu_cnes_dado_serializado = models.CharField(max_length=20, blank=True, null=True)
#     nu_ine_dado_serializado = models.CharField(max_length=20, blank=True, null=True)
#     im_dado_serializado = models.BinaryField()
#     st_validado = models.IntegerField(blank=True, null=True)
#     co_dado_recebido_competencia = models.ForeignKey(TbDadoRecebidoCompetencia, models.DO_NOTHING, db_column='co_dado_recebido_competencia', blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     nu_revisao = models.IntegerField(blank=True, null=True)
#     st_cancelado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dado_transp'
#
#
# class TbDadoTranspRecebido(models.Model):
#     co_seq_dado_transp_recebido = models.BigIntegerField(primary_key=True)
#     co_dado_transp = models.ForeignKey(TbDadoTransp, models.DO_NOTHING, db_column='co_dado_transp', blank=True, null=True)
#     co_info_instal_remetente = models.ForeignKey(TbDadoRecebidoInfoInstalac, models.DO_NOTHING, db_column='co_info_instal_remetente', blank=True, null=True)
#     co_info_instal_originadora = models.ForeignKey(TbDadoRecebidoInfoInstalac, models.DO_NOTHING, db_column='co_info_instal_originadora', blank=True, null=True)
#     nu_lote_originadora = models.BigIntegerField(blank=True, null=True)
#     dt_recebimento = models.DateTimeField(blank=True, null=True)
#     dt_processamento = models.DateTimeField(blank=True, null=True)
#     st_dado_recebido = models.ForeignKey('TbSituacaoDadoRecebido', models.DO_NOTHING, db_column='st_dado_recebido', blank=True, null=True)
#     ds_processamento_mensagem = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dado_transp_recebido'
#
#
# class TbDadoTranspRecebidoOnline(models.Model):
#     co_seq_dado_transp_receb_onlin = models.BigIntegerField(primary_key=True)
#     dt_recebimento = models.DateField()
#     nu_lote_originadora = models.BigIntegerField(blank=True, null=True)
#     co_envio = models.BigIntegerField(blank=True, null=True)
#     ds_processamento_mensagem = models.TextField(blank=True, null=True)
#     co_ibge_dado_serializado = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_dado_serializado = models.CharField(max_length=255, blank=True, null=True)
#     nu_versao_dado_serializado = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes_dado_serializado = models.CharField(max_length=255, blank=True, null=True)
#     nu_ine_dado_serializado = models.CharField(max_length=255, blank=True, null=True)
#     im_dado_serializado = models.BinaryField(blank=True, null=True)
#     tp_dado_transp = models.ForeignKey('TbTipoDadoTransp', models.DO_NOTHING, db_column='tp_dado_transp')
#     tp_origem_dado_transp = models.ForeignKey('TbTipoOrigemDadoTransp', models.DO_NOTHING, db_column='tp_origem_dado_transp')
#     im_info_instalacao_originadora = models.BinaryField(blank=True, null=True)
#     im_info_instalacao_remetente = models.BinaryField(blank=True, null=True)
#     co_recebimento_item = models.ForeignKey('TbRecebimentoItem', models.DO_NOTHING, db_column='co_recebimento_item', blank=True, null=True)
#     nu_revisao = models.IntegerField(blank=True, null=True)
#     st_cancelado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dado_transp_recebido_online'
#
#
# class TbDente(models.Model):
#     co_parte_bucal = models.OneToOneField('TbParteBucal', models.DO_NOTHING, db_column='co_parte_bucal', primary_key=True)
#     co_sextante = models.ForeignKey('TbSextante', models.DO_NOTHING, db_column='co_sextante', blank=True, null=True)
#     nu_dente = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dente'
#
#
# class TbDiaSemana(models.Model):
#     co_dia_semana = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dia_semana'
#
#
# class TbDimAgrupadorFiltro(models.Model):
#     co_seq_dim_agrupador_filtro = models.BigIntegerField(primary_key=True)
#     co_dim_municipio = models.BigIntegerField(blank=True, null=True)
#     co_dim_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_dim_equipe = models.BigIntegerField(blank=True, null=True)
#     co_dim_profissional = models.BigIntegerField(blank=True, null=True)
#     co_dim_cbo = models.BigIntegerField(blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_agrupador_filtro'
#
#
# class TbDimAleitamento(models.Model):
#     co_seq_dim_aleitamento = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_aleitamento = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_aleitamento'
#
#
# class TbDimCatmat(models.Model):
#     co_seq_dim_catmat = models.BigIntegerField(primary_key=True)
#     co_catmat = models.CharField(max_length=20, blank=True, null=True)
#     no_principio_ativo = models.CharField(max_length=400, blank=True, null=True)
#     ds_concentracao = models.CharField(max_length=200, blank=True, null=True)
#     ds_unidade_fornecimento = models.CharField(max_length=200, blank=True, null=True)
#     co_dim_forma_farmaceutica = models.ForeignKey('TbDimFormaFarmaceutica', models.DO_NOTHING, db_column='co_dim_forma_farmaceutica', blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_catmat'
#
#
# class TbDimCbo(models.Model):
#     co_seq_dim_cbo = models.BigIntegerField(primary_key=True)
#     nu_cbo = models.CharField(max_length=20, blank=True, null=True)
#     no_cbo = models.CharField(max_length=500, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_cbo'
#
#
# class TbDimCiap(models.Model):
#     co_seq_dim_ciap = models.BigIntegerField(primary_key=True)
#     nu_ciap = models.CharField(max_length=10, blank=True, null=True)
#     no_ciap = models.CharField(max_length=500, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_ciap'
#
#
# class TbDimCid(models.Model):
#     co_seq_dim_cid = models.BigIntegerField(primary_key=True)
#     nu_cid = models.CharField(max_length=10, blank=True, null=True)
#     no_cid = models.CharField(max_length=500, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_cid'
#
#
# class TbDimCidadaoPecGrupo(models.Model):
#     co_seq_dim_cidadao_pec_grupo = models.BigIntegerField(primary_key=True)
#     co_identificacao = models.CharField(max_length=96, blank=True, null=True)
#     tp_identificacao = models.IntegerField(blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_cidadao_master = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_cidadao_pec_grupo'
#
#
# class TbDimClassificacaoRiscEnc(models.Model):
#     co_seq_dim_classific_risc_enc = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     co_classificacao_risco = models.BigIntegerField(blank=True, null=True)
#     no_classificacao_risco = models.CharField(max_length=255, blank=True, null=True)
#     no_classificacao_risco_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_classificacao_risc_enc'
#
#
# class TbDimCondutaAd(models.Model):
#     co_seq_dim_conduta_ad = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_conduta_ad = models.CharField(max_length=500, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_conduta_ad'
#
#
# class TbDimCuidador(models.Model):
#     co_seq_dim_cuidador = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_cuidador = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_cuidador'
#
#
# class TbDimDesfechoVisita(models.Model):
#     co_seq_dim_desfecho_visita = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_desfecho_visita = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_desfecho_visita'
#
#
# class TbDimDoseFrequencia(models.Model):
#     co_seq_dim_dose_frequencia = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     no_dose_frequencia = models.CharField(max_length=255, blank=True, null=True)
#     no_dose_frequencia_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_dose_frequencia'
#
#
# class TbDimDoseFrequenciaMedida(models.Model):
#     co_seq_dim_dose_frequencia_med = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     no_dose_frequencia_medida = models.CharField(max_length=255, blank=True, null=True)
#     no_dose_frequencia_medida_filt = models.CharField(max_length=255, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_dose_frequencia_medida'
#
#
# class TbDimDoseImunobiologico(models.Model):
#     co_seq_dim_dose_imunobiologico = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=255, blank=True, null=True)
#     sg_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     no_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#     nu_ordem = models.IntegerField(blank=True, null=True)
#     no_apresentacao_dose = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_dose_imunobiologico'
#
#
# class TbDimDuracaoTratamentoMed(models.Model):
#     co_seq_dim_duracao_trat_med = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     nu_duracao_tratamento_med = models.BigIntegerField(blank=True, null=True)
#     no_duracao_tratamento_med = models.CharField(max_length=255, blank=True, null=True)
#     no_duracao_tratamento_med_filt = models.CharField(max_length=255, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_duracao_tratamento_med'
#
#
# class TbDimEquipe(models.Model):
#     co_seq_dim_equipe = models.BigIntegerField(primary_key=True)
#     nu_ine = models.CharField(max_length=20, blank=True, null=True)
#     no_equipe = models.CharField(max_length=255, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_equipe'
#
#
# class TbDimEspecialidade(models.Model):
#     co_seq_dim_especialidade = models.BigIntegerField(primary_key=True)
#     ds_especialidade = models.CharField(max_length=100, blank=True, null=True)
#     ds_especialidade_filtro = models.CharField(max_length=100, blank=True, null=True)
#     co_especialidade = models.CharField(max_length=100, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_especialidade'
#
#
# class TbDimEstrategiaVacinacao(models.Model):
#     co_seq_dim_estrategia_vacnacao = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=10, blank=True, null=True)
#     nu_estrategia_vacinacao = models.CharField(max_length=255, blank=True, null=True)
#     no_estrategia_vacinacao = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_estrategia_vacinacao'
#
#
# class TbDimEtnia(models.Model):
#     co_seq_dim_etnia = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     no_etnia = models.CharField(max_length=500, blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_etnia'
#
#
# class TbDimFaixaEtaria(models.Model):
#     co_seq_dim_faixa_etaria = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_faixa_etaria = models.CharField(max_length=500, blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#     nu_faixa_inicial_anos = models.IntegerField(blank=True, null=True)
#     nu_faixa_final_anos = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_faixa_etaria'
#
#
# class TbDimFormaFarmaceutica(models.Model):
#     co_seq_dim_forma_farmaceutica = models.BigIntegerField(primary_key=True)
#     co_forma_farmaceutica = models.CharField(max_length=10, blank=True, null=True)
#     no_forma_farmaceutica = models.CharField(max_length=255, blank=True, null=True)
#     no_forma_farmaceutica_filtro = models.CharField(max_length=255, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_forma_farmaceutica'
#
#
# class TbDimFrequenciaAlimentacao(models.Model):
#     co_seq_dim_frequencia_aliment = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_dim_frequencia_alimentacao = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_frequencia_alimentacao'
#
#
# class TbDimGrupoAtendimento(models.Model):
#     co_seq_dim_grupo_atendimento = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=10, blank=True, null=True)
#     ds_grupo_atendimento = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_grupo_atendimento'
#
#
# class TbDimGrupoCbo(models.Model):
#     co_seq_dim_grupo_cbo = models.BigIntegerField(primary_key=True)
#     nu_grupo_cbo = models.CharField(max_length=10, blank=True, null=True)
#     ds_grupo_cbo = models.CharField(max_length=100, blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     ds_filtro = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_grupo_cbo'
#
#
# class TbDimIdentidadeGenero(models.Model):
#     co_seq_dim_identidade_genero = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_identidade_genero = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_identidade_genero'
#
#
# class TbDimImunobiologico(models.Model):
#     co_seq_dim_imunobiologico = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=255, blank=True, null=True)
#     sg_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     no_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_imunobiologico'
#
#
# class TbDimInep(models.Model):
#     co_seq_dim_inep = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=8, blank=True, null=True)
#     no_estabelecimento = models.CharField(max_length=200, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_inep'
#
#
# class TbDimLocalAtendimento(models.Model):
#     co_seq_dim_local_atendimento = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_local_atendimento = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_local_atendimento'
#
#
# class TbDimModalidadeAd(models.Model):
#     co_seq_dim_modalidade_ad = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_modalidade_ad = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_modalidade_ad'
#
#
# class TbDimMunicipio(models.Model):
#     co_seq_dim_municipio = models.BigIntegerField(primary_key=True)
#     no_municipio = models.CharField(max_length=500, blank=True, null=True)
#     co_ibge = models.CharField(max_length=10, blank=True, null=True)
#     co_dim_uf = models.ForeignKey('TbDimUf', models.DO_NOTHING, db_column='co_dim_uf', blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_municipio'
#
#
# class TbDimNacionalidade(models.Model):
#     co_seq_dim_nacionalidade = models.BigIntegerField(primary_key=True)
#     co_nacionalidade = models.CharField(max_length=2, blank=True, null=True)
#     no_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_nacionalidade = models.CharField(max_length=100, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_nacionalidade'
#
#
# class TbDimPais(models.Model):
#     co_seq_dim_pais = models.BigIntegerField(primary_key=True)
#     no_pais = models.CharField(max_length=500, blank=True, null=True)
#     co_cadsus = models.CharField(max_length=6, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_pais'
#
#
# class TbDimPic(models.Model):
#     co_seq_dim_pic = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_pic = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_pic'
#
#
# class TbDimPovoComunidadTrad(models.Model):
#     co_seq_dim_povo_comunidad_trad = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=10, blank=True, null=True)
#     ds_povo_comunidade_tradicional = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_povo_comunidad_trad'
#
#
# class TbDimProcedenciaOrigem(models.Model):
#     co_seq_dim_procedencia_origem = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_procedencia_origem = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_procedencia_origem'
#
#
# class TbDimProcedimento(models.Model):
#     co_seq_dim_procedimento = models.BigIntegerField(primary_key=True)
#     co_proced = models.CharField(max_length=100, blank=True, null=True)
#     ds_proced = models.CharField(max_length=500, blank=True, null=True)
#     co_seq_dim_proced_ref_ab = models.BigIntegerField(blank=True, null=True)
#     co_pai = models.ForeignKey('self', models.DO_NOTHING, db_column='co_pai', blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=350, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_procedimento'
#
#
# class TbDimProfissional(models.Model):
#     co_seq_dim_profissional = models.BigIntegerField(primary_key=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     no_profissional = models.CharField(max_length=255, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_profissional'
#
#
# class TbDimRacaCor(models.Model):
#     co_seq_dim_raca_cor = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=50, blank=True, null=True)
#     nu_ms = models.CharField(max_length=50, blank=True, null=True)
#     ds_raca_cor = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_raca_cor'
#
#
# class TbDimRacionalidadeSaude(models.Model):
#     co_seq_dim_racionalidade_saude = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     no_racionalidade_saude = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_racionalidade_saude'
#
#
# class TbDimSexo(models.Model):
#     co_seq_dim_sexo = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_sexo = models.CharField(max_length=100, blank=True, null=True)
#     sg_sexo = models.CharField(max_length=100, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_sexo'
#
#
# class TbDimSituacaoTrabalho(models.Model):
#     co_seq_dim_situacao_trabalho = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_dim_situacao_trabalho = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_situacao_trabalho'
#
#
# class TbDimTempo(models.Model):
#     co_seq_dim_tempo = models.BigIntegerField(primary_key=True)
#     dt_registro = models.DateField(blank=True, null=True)
#     nu_dia = models.SmallIntegerField(blank=True, null=True)
#     nu_mes = models.SmallIntegerField(blank=True, null=True)
#     nu_ano = models.IntegerField(blank=True, null=True)
#     ds_dia_semana = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tempo'
#
#
# class TbDimTempoMoradorRua(models.Model):
#     co_seq_dim_tempo_morador_rua = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_dim_tempo_morador_rua = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tempo_morador_rua'
#
#
# class TbDimTipoAbastecimentoAgua(models.Model):
#     co_seq_dim_tipo_abastec_agua = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_abastecimento_agua = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_abastecimento_agua'
#
#
# class TbDimTipoAcessoDomicilio(models.Model):
#     co_seq_dim_tipo_acesso_domicil = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_acesso_domicilio = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_acesso_domicilio'
#
#
# class TbDimTipoAtendimento(models.Model):
#     co_seq_dim_tipo_atendimento = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_atendimento = models.CharField(max_length=500, blank=True, null=True)
#     co_dim_tipo_atendimento_pai = models.ForeignKey('self', models.DO_NOTHING, db_column='co_dim_tipo_atendimento_pai', blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_atendimento'
#
#
# class TbDimTipoAtividade(models.Model):
#     co_seq_dim_tipo_atividade = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_atividade = models.CharField(max_length=500, blank=True, null=True)
#     co_categoria_tipo_atividade = models.BigIntegerField(blank=True, null=True)
#     ds_categoria_tipo_atividade = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_atividade'
#
#
# class TbDimTipoCondicaoPeso(models.Model):
#     co_seq_dim_tipo_condicao_peso = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_dim_tipo_condicao_peso = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_condicao_peso'
#
#
# class TbDimTipoConsultaOdonto(models.Model):
#     co_seq_dim_tipo_cnsulta_odonto = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_consulta_odonto = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_consulta_odonto'
#
#
# class TbDimTipoDestinoLixo(models.Model):
#     co_seq_dim_tipo_destino_lixo = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_destino_lixo = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_destino_lixo'
#
#
# class TbDimTipoDomicilio(models.Model):
#     co_seq_dim_tipo_domicilio = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_domicilio = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_domicilio'
#
#
# class TbDimTipoElegibilidade(models.Model):
#     co_seq_dim_tipo_elegibilidade = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_elegibilidade = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_elegibilidade'
#
#
# class TbDimTipoEscoamentoSanitar(models.Model):
#     co_seq_dim_tipo_escoamento_snt = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_escoamento_sanitario = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_escoamento_sanitar'
#
#
# class TbDimTipoEscolaridade(models.Model):
#     co_seq_dim_tipo_escolaridade = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_dim_tipo_escolaridade = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_escolaridade'
#
#
# class TbDimTipoFicha(models.Model):
#     co_seq_dim_tipo_ficha = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_ficha = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_ficha'
#
#
# class TbDimTipoGlicemia(models.Model):
#     co_seq_dim_tipo_glicemia = models.BigIntegerField(primary_key=True)
#     ds_tipo_glicemia = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_glicemia_filtro = models.CharField(max_length=100, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_glicemia'
#
#
# class TbDimTipoImovel(models.Model):
#     co_seq_dim_tipo_imovel = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_imovel = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_imovel'
#
#
# class TbDimTipoLocalizacao(models.Model):
#     co_seq_dim_tipo_localizacao = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_localizacao = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_localizacao'
#
#
# class TbDimTipoLogradouro(models.Model):
#     co_seq_dim_tipo_logradouro = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_logradouro = models.CharField(max_length=500, blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_logradouro'
#
#
# class TbDimTipoMaterialParede(models.Model):
#     co_seq_dim_tipo_material_pared = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_material_parede = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_material_parede'
#
#
# class TbDimTipoOrientacaoSexual(models.Model):
#     co_seq_dim_tipo_orientacao_sxl = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_dim_tipo_orientacao_sexual = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_orientacao_sexual'
#
#
# class TbDimTipoOrigem(models.Model):
#     co_seq_dim_tipo_origem = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=255, blank=True, null=True)
#     no_tipo_origem = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_origem'
#
#
# class TbDimTipoOrigemDadoTransp(models.Model):
#     co_seq_dim_tp_orgm_dado_transp = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=255, blank=True, null=True)
#     no_tipo_origem_dado_transp = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_origem_dado_transp'
#
#
# class TbDimTipoParentesco(models.Model):
#     co_seq_dim_tipo_parentesco = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_parentesco = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_parentesco'
#
#
# class TbDimTipoPosseTerra(models.Model):
#     co_seq_dim_tipo_posse_terra = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_posse_terra = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_posse_terra'
#
#
# class TbDimTipoRendaFamiliar(models.Model):
#     co_seq_dim_tipo_renda_familiar = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_renda_familiar = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_renda_familiar'
#
#
# class TbDimTipoSaidaCadastro(models.Model):
#     co_seq_dim_tipo_saida_cadastro = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_dim_tipo_saida_cadastro = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_saida_cadastro'
#
#
# class TbDimTipoSituacaoMoradia(models.Model):
#     co_seq_dim_tipo_situacao_morad = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_situacao_moradia = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_situacao_moradia'
#
#
# class TbDimTipoTratamentoAgua(models.Model):
#     co_seq_dim_tipo_tratament_agua = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_tipo_tratamento_agua = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_tipo_tratamento_agua'
#
#
# class TbDimTurno(models.Model):
#     co_seq_dim_turno = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     ds_turno = models.CharField(max_length=500, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_turno'
#
#
# class TbDimUf(models.Model):
#     co_seq_dim_uf = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=10, blank=True, null=True)
#     no_uf = models.CharField(max_length=500, blank=True, null=True)
#     sg_uf = models.CharField(max_length=10, blank=True, null=True)
#     co_dim_pais = models.ForeignKey(TbDimPais, models.DO_NOTHING, db_column='co_dim_pais', blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_uf'
#
#
# class TbDimUnidadeSaude(models.Model):
#     co_seq_dim_unidade_saude = models.BigIntegerField(primary_key=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     no_unidade_saude = models.CharField(max_length=500, blank=True, null=True)
#     no_bairro = models.CharField(max_length=500, blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     ds_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_unidade_saude'
#
#
# class TbDimViaAdministracao(models.Model):
#     co_seq_dim_via_administracao = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     no_via_administracao = models.CharField(max_length=255, blank=True, null=True)
#     no_via_administracao_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_ordem = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_via_administracao'
#
#
# class TbDimZikaTipoExame(models.Model):
#     co_seq_dim_zika_tipo_exame = models.BigIntegerField(primary_key=True)
#     nu_identificador = models.CharField(max_length=100, blank=True, null=True)
#     no_zika_tipo_exame = models.CharField(max_length=255, blank=True, null=True)
#     no_zika_tipo_exame_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dim_zika_tipo_exame'
#
#
# class TbDoseImunobiologico(models.Model):
#     co_dose_imunobiologico = models.BigIntegerField(primary_key=True)
#     sg_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     no_dose_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     nu_ordem = models.IntegerField(blank=True, null=True)
#     no_apresentacao_dose = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_dose_imunobiologico'
#
#
# class TbEncaminhamento(models.Model):
#     co_seq_encaminhamento = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     co_especialidade_sisreg = models.ForeignKey('TbEspecialidadeSisreg', models.DO_NOTHING, db_column='co_especialidade_sisreg', blank=True, null=True)
#     ds_complemento = models.CharField(max_length=200, blank=True, null=True)
#     co_cid10 = models.ForeignKey(TbCid10, models.DO_NOTHING, db_column='co_cid10', blank=True, null=True)
#     co_ciap = models.ForeignKey(TbCiap, models.DO_NOTHING, db_column='co_ciap', blank=True, null=True)
#     co_classificacao_risco_encam = models.ForeignKey(TbClassificacaoRiscoEncam, models.DO_NOTHING, db_column='co_classificacao_risco_encam', blank=True, null=True)
#     ds_motivo_encaminhamento = models.CharField(max_length=1000, blank=True, null=True)
#     ds_observacao = models.CharField(max_length=600, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_encaminhamento'
#
#
# class TbEnvioLog(models.Model):
#     co_seq_envio_log = models.BigIntegerField(primary_key=True)
#     data = models.DateTimeField(blank=True, null=True)
#     st_status_envio = models.IntegerField(blank=True, null=True)
#     mensagem = models.CharField(max_length=255, blank=True, null=True)
#     file_name = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_envio_log'
#
#
# class TbEquipe(models.Model):
#     co_seq_equipe = models.BigIntegerField(primary_key=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField()
#     co_unidade_saude = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude')
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     tp_equipe = models.ForeignKey('TbTipoEquipe', models.DO_NOTHING, db_column='tp_equipe', blank=True, null=True)
#     ds_area = models.CharField(max_length=255, blank=True, null=True)
#     no_equipe = models.CharField(max_length=255, blank=True, null=True)
#     no_equipe_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_equipe = models.CharField(unique=True, max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_equipe'
#
#
# class TbEscolaridade(models.Model):
#     co_escolaridade = models.BigIntegerField(primary_key=True)
#     no_escolaridade = models.CharField(max_length=255, blank=True, null=True)
#     no_escolaridade_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_escolaridade'
#
#
# class TbEspecialidadeSisreg(models.Model):
#     co_especialidade_sisreg = models.BigIntegerField(primary_key=True)
#     ds_especialidade_sisreg = models.CharField(max_length=100)
#     ds_especialidade_sisreg_filtro = models.CharField(max_length=100)
#     co_grupo_especialidade = models.ForeignKey('TbGrupoEspecialidade', models.DO_NOTHING, db_column='co_grupo_especialidade')
#     co_cbo = models.ForeignKey(TbCbo, models.DO_NOTHING, db_column='co_cbo', blank=True, null=True)
#     tp_encam_odonto = models.ForeignKey('TbTipoEncamOdonto', models.DO_NOTHING, db_column='tp_encam_odonto', blank=True, null=True)
#     tp_cds_conduta = models.ForeignKey(TbCdsTipoConduta, models.DO_NOTHING, db_column='tp_cds_conduta', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_especialidade_sisreg'
#
#
# class TbEstadoCivil(models.Model):
#     co_estado_civil = models.BigIntegerField(primary_key=True)
#     no_estado_civil = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_estado_civil'
#
#
# class TbEstrategiaVacinacao(models.Model):
#     co_estrategia_vacinacao = models.BigIntegerField(primary_key=True)
#     nu_estrategia_vacinacao = models.CharField(max_length=10, blank=True, null=True)
#     no_estrategia_vacinacao = models.CharField(max_length=255, blank=True, null=True)
#     no_estrategia_vacinacao_filtro = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_estrategia_vacinacao'
#
#
# class TbEtnia(models.Model):
#     co_etnia = models.BigIntegerField(primary_key=True)
#     no_etnia = models.CharField(max_length=255)
#     co_etnia_cadsus = models.CharField(max_length=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_etnia'
#
#
# class TbEvolucaoAvaliacao(models.Model):
#     co_atend_prof = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', primary_key=True)
#     ds_avaliacao = models.TextField(blank=True, null=True)
#     st_necessidade_de_protese = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_evolucao_avaliacao'
#
#
# class TbEvolucaoDente(models.Model):
#     co_seq_evolucao_dente = models.BigIntegerField(primary_key=True)
#     co_dente = models.ForeignKey(TbDente, models.DO_NOTHING, db_column='co_dente', blank=True, null=True)
#     co_odontograma = models.ForeignKey('TbOdontograma', models.DO_NOTHING, db_column='co_odontograma', blank=True, null=True)
#     st_coroa_cima = models.ForeignKey('TbSituacaoCoroa', models.DO_NOTHING, db_column='st_coroa_cima', blank=True, null=True)
#     st_coroa_baixo = models.ForeignKey('TbSituacaoCoroa', models.DO_NOTHING, db_column='st_coroa_baixo', blank=True, null=True)
#     st_coroa_direita = models.ForeignKey('TbSituacaoCoroa', models.DO_NOTHING, db_column='st_coroa_direita', blank=True, null=True)
#     st_coroa_esquerda = models.ForeignKey('TbSituacaoCoroa', models.DO_NOTHING, db_column='st_coroa_esquerda', blank=True, null=True)
#     st_coroa_centro = models.ForeignKey('TbSituacaoCoroa', models.DO_NOTHING, db_column='st_coroa_centro', blank=True, null=True)
#     st_raiz = models.ForeignKey('TbSituacaoRaiz', models.DO_NOTHING, db_column='st_raiz', blank=True, null=True)
#     st_face = models.ForeignKey('TbSituacaoFace', models.DO_NOTHING, db_column='st_face', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_evolucao_dente'
#
#
# class TbEvolucaoObjetivo(models.Model):
#     co_atend_prof = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', primary_key=True)
#     ds_objetivo = models.TextField(blank=True, null=True)
#     st_necessidade_especial = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_evolucao_objetivo'
#
#
# class TbEvolucaoOdonto(models.Model):
#     co_seq_evolucao_odonto = models.BigIntegerField(primary_key=True)
#     tp_parte_bucal = models.ForeignKey('TbTipoParteBucal', models.DO_NOTHING, db_column='tp_parte_bucal', blank=True, null=True)
#     ds_parte_bucal = models.CharField(max_length=255, blank=True, null=True)
#     ds_outro = models.CharField(max_length=400, blank=True, null=True)
#     co_atend_prof_odonto = models.ForeignKey(TbAtendProfOdonto, models.DO_NOTHING, db_column='co_atend_prof_odonto', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     ds_evolucao = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_evolucao_odonto'
#
#
# class TbEvolucaoPlano(models.Model):
#     co_atend_prof = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', primary_key=True)
#     ds_plano = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_evolucao_plano'
#
#
# class TbEvolucaoSubjetivo(models.Model):
#     co_atend_prof = models.OneToOneField(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', primary_key=True)
#     ds_subjetivo = models.TextField(blank=True, null=True)
#     ds_acompanhado_especialidade = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_evolucao_subjetivo'
#
#
# class TbExameClearanceCreatina(models.Model):
#     co_seq_exame_clearance_creatn = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     vl_clearance_creatina = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_clearance_creatina'
#
#
# class TbExameColesterolHdl(models.Model):
#     co_seq_exame_colesterol_hdl = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     vl_colesterol_hdl = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_colesterol_hdl'
#
#
# class TbExameColesterolLdl(models.Model):
#     co_seq_exame_colesterol_ldl = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     vl_colesterol_ldl = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_colesterol_ldl'
#
#
# class TbExameColesterolTotal(models.Model):
#     co_seq_exame_colesterol_total = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     vl_colesterol_total = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_colesterol_total'
#
#
# class TbExameCreatinaSerica(models.Model):
#     co_seq_exame_creatina_sericia = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     vl_creatina_serica = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_creatina_serica'
#
#
# class TbExameDetalhe(models.Model):
#     co_seq_exame_detalhe = models.BigIntegerField(primary_key=True)
#     ds_exame_detalhe = models.CharField(max_length=255, blank=True, null=True)
#     tp_opcao = models.ForeignKey('TbTipoOpcao', models.DO_NOTHING, db_column='tp_opcao', blank=True, null=True)
#     sg_unidade_medida = models.CharField(max_length=25, blank=True, null=True)
#     vl_comprimento = models.IntegerField(blank=True, null=True)
#     vl_minimo = models.FloatField(blank=True, null=True)
#     vl_maximo = models.FloatField(blank=True, null=True)
#     vl_precisao_decimal = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_detalhe'
#
#
# class TbExameDetalheResultado(models.Model):
#     co_seq_exame_detalhe_resultado = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     co_proced_exame_detalhe = models.ForeignKey(RlProcedExameDetalhe, models.DO_NOTHING, db_column='co_proced_exame_detalhe', blank=True, null=True)
#     tp_resultado = models.ForeignKey('TbTipoOpcao', models.DO_NOTHING, db_column='tp_resultado', blank=True, null=True)
#     nu_resultado = models.FloatField(blank=True, null=True)
#     ds_resultado = models.CharField(max_length=800, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_detalhe_resultado'
#
#
# class TbExameHemoglobinaGlicada(models.Model):
#     co_seq_exame_hemoglobina_glicd = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     vl_hemoglobina_glicada = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_hemoglobina_glicada'
#
#
# class TbExamePrenatal(models.Model):
#     co_seq_exame_prenatal = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     qt_semana_gestacional_eco = models.IntegerField(blank=True, null=True)
#     qt_dia_gestacional_eco = models.IntegerField(blank=True, null=True)
#     dt_provavel_parto_eco = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_prenatal'
#
#
# class TbExamePuericultura(models.Model):
#     co_seq_exame = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey('TbExameRequisitado', models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     co_exame = models.ForeignKey('TbFichaZikaTipoExame', models.DO_NOTHING, db_column='co_exame', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_puericultura'
#
#
# class TbExameRequisitado(models.Model):
#     co_seq_exame_requisitado = models.BigIntegerField(primary_key=True)
#     st_conferido = models.IntegerField(blank=True, null=True)
#     dt_resultado = models.DateTimeField(blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced', blank=True, null=True)
#     co_requisicao_exame = models.ForeignKey('TbRequisicaoExame', models.DO_NOTHING, db_column='co_requisicao_exame', blank=True, null=True)
#     co_atend_prof_resultado = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof_resultado', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     dt_realizacao = models.DateTimeField(blank=True, null=True)
#     dt_solicitacao = models.DateTimeField(blank=True, null=True)
#     co_proced_exame_especifico = models.ForeignKey('TbProcedExameEspecifico', models.DO_NOTHING, db_column='co_proced_exame_especifico', blank=True, null=True)
#     ds_resultado = models.TextField(blank=True, null=True)
#     ds_observacao = models.CharField(max_length=300, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_requisitado'
#
#
# class TbExameTriglicerideos(models.Model):
#     co_seq_exame_triglicerideos = models.BigIntegerField(primary_key=True)
#     co_exame_requisitado = models.ForeignKey(TbExameRequisitado, models.DO_NOTHING, db_column='co_exame_requisitado', blank=True, null=True)
#     vl_triglicerideos = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_exame_triglicerideos'
#
#
# class TbFaixaEtariaVacinacao(models.Model):
#     co_faixa_etaria_vacinacao = models.BigIntegerField(primary_key=True)
#     nu_inicio_ano = models.IntegerField(blank=True, null=True)
#     nu_fim_ano = models.IntegerField(blank=True, null=True)
#     nu_inicio_mes = models.IntegerField(blank=True, null=True)
#     nu_fim_mes = models.IntegerField(blank=True, null=True)
#     nu_inicio_dia = models.IntegerField(blank=True, null=True)
#     nu_fim_dia = models.IntegerField(blank=True, null=True)
#     ds_faixa_etaria = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_faixa_etaria_vacinacao'
#
#
# class TbFamilia(models.Model):
#     co_seq_familia = models.BigIntegerField(primary_key=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20)
#     nu_cpf_cns_responsavel = models.CharField(max_length=255)
#     nu_prontuario_familiar = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_responsavel = models.DateField(blank=True, null=True)
#     co_renda_familiar = models.BigIntegerField(blank=True, null=True)
#     qt_membro = models.IntegerField(blank=True, null=True)
#     co_cds_domicilio = models.ForeignKey(TbCdsDomicilio, models.DO_NOTHING, db_column='co_cds_domicilio')
#     dt_reside_desde = models.DateField(blank=True, null=True)
#     st_responsavel_cadastrado = models.IntegerField()
#     st_responsavel_declarado = models.IntegerField()
#     st_responsavel_vivo = models.IntegerField()
#     st_responsavel_unico = models.IntegerField()
#     st_responsavel_ainda_reside = models.IntegerField()
#     st_familia_ainda_reside = models.IntegerField()
#     st_informacao_suficiente = models.IntegerField()
#     st_domicilio_ativo = models.IntegerField(blank=True, null=True)
#     dt_atualizacao_fcd = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_familia'
#
#
# class TbFatAtdIndEncaminhamentos(models.Model):
#     co_seq_fat_atd_ind_encaminham = models.BigIntegerField(primary_key=True)
#     co_fat_atd_ind = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_especialidade = models.ForeignKey(TbDimEspecialidade, models.DO_NOTHING, db_column='co_dim_especialidade', blank=True, null=True)
#     co_dim_cid10 = models.BigIntegerField(blank=True, null=True)
#     co_dim_classificacao_risc_enc = models.ForeignKey(TbDimClassificacaoRiscEnc, models.DO_NOTHING, db_column='co_dim_classificacao_risc_enc', blank=True, null=True)
#     co_dim_ciap2 = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atd_ind_encaminhamentos'
#
#
# class TbFatAtdIndExames(models.Model):
#     co_seq_fat_atd_ind_exames = models.BigIntegerField(primary_key=True)
#     co_fat_atd_ind = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_procedimento = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento', blank=True, null=True)
#     dt_solicitacao = models.DateField(blank=True, null=True)
#     dt_realizacao = models.DateField(blank=True, null=True)
#     dt_resultado = models.DateField(blank=True, null=True)
#     nu_resultado_valor = models.FloatField(blank=True, null=True)
#     nu_resultado_dia = models.IntegerField(blank=True, null=True)
#     nu_resultado_semana = models.IntegerField(blank=True, null=True)
#     dt_resultado_data = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atd_ind_exames'
#
#
# class TbFatAtdIndMedicamentos(models.Model):
#     co_seq_fat_atd_ind_medicam = models.BigIntegerField(primary_key=True)
#     co_fat_atd_ind = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_catmat = models.ForeignKey(TbDimCatmat, models.DO_NOTHING, db_column='co_dim_catmat', blank=True, null=True)
#     co_dim_dose_frequencia_medida = models.ForeignKey(TbDimDoseFrequenciaMedida, models.DO_NOTHING, db_column='co_dim_dose_frequencia_medida', blank=True, null=True)
#     co_dim_duracao_tratamento_med = models.ForeignKey(TbDimDuracaoTratamentoMed, models.DO_NOTHING, db_column='co_dim_duracao_tratamento_med', blank=True, null=True)
#     co_dim_dose_frequencia = models.ForeignKey(TbDimDoseFrequencia, models.DO_NOTHING, db_column='co_dim_dose_frequencia', blank=True, null=True)
#     co_dim_via_administracao = models.ForeignKey(TbDimViaAdministracao, models.DO_NOTHING, db_column='co_dim_via_administracao', blank=True, null=True)
#     ds_dose = models.CharField(max_length=255, blank=True, null=True)
#     st_dose_unica = models.IntegerField(blank=True, null=True)
#     st_uso_continuo = models.IntegerField(blank=True, null=True)
#     ds_dose_frequencia = models.CharField(max_length=255, blank=True, null=True)
#     qt_dose_frequencia = models.IntegerField(blank=True, null=True)
#     qt_duracao_tratamento = models.IntegerField(blank=True, null=True)
#     qt_receitada = models.IntegerField(blank=True, null=True)
#     dt_inicio_tratamento = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atd_ind_medicamentos'
#
#
# class TbFatAtdIndProblemas(models.Model):
#     co_seq_fat_atend_ind_problemas = models.BigIntegerField(primary_key=True)
#     co_fat_atd_ind = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     co_dim_cid = models.ForeignKey(TbDimCid, models.DO_NOTHING, db_column='co_dim_cid', blank=True, null=True)
#     co_dim_ciap = models.ForeignKey(TbDimCiap, models.DO_NOTHING, db_column='co_dim_ciap', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atd_ind_problemas'
#
#
# class TbFatAtdIndProcedimentos(models.Model):
#     co_seq_fat_atend_ind_proced = models.BigIntegerField(primary_key=True)
#     co_fat_atd_ind = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     co_dim_procedimento_avaliado = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento_avaliado', blank=True, null=True)
#     co_dim_procedimento_solicitado = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento_solicitado', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atd_ind_procedimentos'
#
#
# class TbFatAtendDomCondicaoAval(models.Model):
#     co_seq_fat_atnd_dom_condo_aval = models.BigIntegerField(primary_key=True)
#     co_fat_atend_domiciliar = models.BigIntegerField(blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_cid = models.ForeignKey(TbDimCid, models.DO_NOTHING, db_column='co_dim_cid', blank=True, null=True)
#     co_dim_ciap = models.ForeignKey(TbDimCiap, models.DO_NOTHING, db_column='co_dim_ciap', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atend_dom_condicao_aval'
#
#
# class TbFatAtendDomProced(models.Model):
#     co_seq_fat_atend_dom_proced = models.BigIntegerField(primary_key=True)
#     co_fat_atend_domiciliar = models.BigIntegerField(blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_procedimento = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atend_dom_proced'
#
#
# class TbFatAtendOdontoEncaminham(models.Model):
#     co_seq_fat_atd_odo_encaminham = models.BigIntegerField(primary_key=True)
#     co_fat_atd_odo = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_especialidade = models.ForeignKey(TbDimEspecialidade, models.DO_NOTHING, db_column='co_dim_especialidade', blank=True, null=True)
#     co_dim_cid10 = models.BigIntegerField(blank=True, null=True)
#     co_dim_ciap2 = models.BigIntegerField(blank=True, null=True)
#     co_dim_classificacao_risc_enc = models.ForeignKey(TbDimClassificacaoRiscEnc, models.DO_NOTHING, db_column='co_dim_classificacao_risc_enc', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atend_odonto_encaminham'
#
#
# class TbFatAtendOdontoExames(models.Model):
#     co_seq_fat_atd_odo_exames = models.BigIntegerField(primary_key=True)
#     co_fat_atd_odo = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_procedimento = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento', blank=True, null=True)
#     dt_solicitacao = models.DateField(blank=True, null=True)
#     dt_realizacao = models.DateField(blank=True, null=True)
#     dt_resultado = models.DateField(blank=True, null=True)
#     nu_resultado_valor = models.FloatField(blank=True, null=True)
#     nu_resultado_dia = models.IntegerField(blank=True, null=True)
#     nu_resultado_semana = models.IntegerField(blank=True, null=True)
#     dt_resultado_data = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atend_odonto_exames'
#
#
# class TbFatAtendOdontoMedicament(models.Model):
#     co_seq_fat_atd_odo_medicam = models.BigIntegerField(primary_key=True)
#     co_fat_atd_odo = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_catmat = models.ForeignKey(TbDimCatmat, models.DO_NOTHING, db_column='co_dim_catmat', blank=True, null=True)
#     co_dim_dose_frequencia_medida = models.ForeignKey(TbDimDoseFrequenciaMedida, models.DO_NOTHING, db_column='co_dim_dose_frequencia_medida', blank=True, null=True)
#     co_dim_duracao_tratamento_med = models.ForeignKey(TbDimDuracaoTratamentoMed, models.DO_NOTHING, db_column='co_dim_duracao_tratamento_med', blank=True, null=True)
#     co_dim_dose_frequencia = models.ForeignKey(TbDimDoseFrequencia, models.DO_NOTHING, db_column='co_dim_dose_frequencia', blank=True, null=True)
#     co_dim_via_administracao = models.ForeignKey(TbDimViaAdministracao, models.DO_NOTHING, db_column='co_dim_via_administracao', blank=True, null=True)
#     ds_dose = models.CharField(max_length=255, blank=True, null=True)
#     st_dose_unica = models.IntegerField(blank=True, null=True)
#     st_uso_continuo = models.IntegerField(blank=True, null=True)
#     ds_dose_frequencia = models.CharField(max_length=255, blank=True, null=True)
#     qt_dose_frequencia = models.IntegerField(blank=True, null=True)
#     qt_duracao_tratamento = models.IntegerField(blank=True, null=True)
#     qt_receitada = models.IntegerField(blank=True, null=True)
#     dt_inicio_tratamento = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atend_odonto_medicament'
#
#
# class TbFatAtendOdontoProblemas(models.Model):
#     co_seq_fat_atnd_odonto_probl = models.BigIntegerField(primary_key=True)
#     co_fat_atd_odnt = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     co_dim_cid = models.ForeignKey(TbDimCid, models.DO_NOTHING, db_column='co_dim_cid', blank=True, null=True)
#     co_dim_ciap = models.ForeignKey(TbDimCiap, models.DO_NOTHING, db_column='co_dim_ciap', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atend_odonto_problemas'
#
#
# class TbFatAtendOdontoProced(models.Model):
#     co_seq_fat_atend_odonto_proced = models.BigIntegerField(primary_key=True)
#     co_fat_atd_odnt = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     co_dim_procedimento = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento', blank=True, null=True)
#     qt_procedimentos = models.IntegerField(blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atend_odonto_proced'
#
#
# class TbFatAtendimentoDomiciliar(models.Model):
#     co_seq_fat_atend_domiciliar = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_local_atendimento = models.ForeignKey(TbDimLocalAtendimento, models.DO_NOTHING, db_column='co_dim_local_atendimento', blank=True, null=True)
#     co_dim_tipo_atendimento = models.ForeignKey(TbDimTipoAtendimento, models.DO_NOTHING, db_column='co_dim_tipo_atendimento', blank=True, null=True)
#     co_dim_modalidade_ad = models.ForeignKey(TbDimModalidadeAd, models.DO_NOTHING, db_column='co_dim_modalidade_ad', blank=True, null=True)
#     st_condic_acamado = models.IntegerField(blank=True, null=True)
#     st_condic_domiciliado = models.IntegerField(blank=True, null=True)
#     st_condic_ulceras_feridas = models.IntegerField(blank=True, null=True)
#     st_condic_acompanham_nutricion = models.IntegerField(blank=True, null=True)
#     st_condic_uso_sonda_nasogastri = models.IntegerField(blank=True, null=True)
#     st_condic_uso_sonda_nasoentera = models.IntegerField(blank=True, null=True)
#     st_condic_uso_gastrostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_colostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_cistostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_sond_vesic_demor = models.IntegerField(blank=True, null=True)
#     st_condic_acomp_pre_operatorio = models.IntegerField(blank=True, null=True)
#     st_condic_acomp_pos_operatorio = models.IntegerField(blank=True, null=True)
#     st_condic_adapt_uso_ortes_prot = models.IntegerField(blank=True, null=True)
#     st_condic_reabilita_domiciliar = models.IntegerField(blank=True, null=True)
#     st_condic_cuidd_paliat_oncolog = models.IntegerField(blank=True, null=True)
#     st_condic_cuidd_paliat_n_oncol = models.IntegerField(blank=True, null=True)
#     st_condic_oxigenoterapia_domic = models.IntegerField(blank=True, null=True)
#     st_condic_uso_traqueostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_aspir_via_aerea = models.IntegerField(blank=True, null=True)
#     st_condic_suport_ventil_cpap = models.IntegerField(blank=True, null=True)
#     st_condic_suport_ventil_bipap = models.IntegerField(blank=True, null=True)
#     st_condic_dialise_peritonial = models.IntegerField(blank=True, null=True)
#     st_condic_paracentese = models.IntegerField(blank=True, null=True)
#     st_condic_medicacao_parenteral = models.IntegerField(blank=True, null=True)
#     ds_filtro_cids = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_ciaps = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_procedimentos = models.CharField(max_length=4000, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_dim_conduta_ad = models.ForeignKey(TbDimCondutaAd, models.DO_NOTHING, db_column='co_dim_conduta_ad', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atendimento_domiciliar'
#
#
# class TbFatAtendimentoIndividual(models.Model):
#     co_seq_fat_atd_ind = models.BigIntegerField(primary_key=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_racionalidade_saude = models.ForeignKey(TbDimRacionalidadeSaude, models.DO_NOTHING, db_column='co_dim_racionalidade_saude', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_local_atendimento = models.ForeignKey(TbDimLocalAtendimento, models.DO_NOTHING, db_column='co_dim_local_atendimento', blank=True, null=True)
#     co_dim_tipo_atendimento = models.ForeignKey(TbDimTipoAtendimento, models.DO_NOTHING, db_column='co_dim_tipo_atendimento', blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     nu_perimetro_cefalico = models.FloatField(blank=True, null=True)
#     st_vacinacao_em_dia = models.IntegerField(blank=True, null=True)
#     co_dim_aleitamento = models.ForeignKey(TbDimAleitamento, models.DO_NOTHING, db_column='co_dim_aleitamento', blank=True, null=True)
#     co_dim_tempo_dum = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_dum', blank=True, null=True)
#     st_gravidez_planejada = models.IntegerField(blank=True, null=True)
#     nu_idade_gestacional_semanas = models.IntegerField(blank=True, null=True)
#     nu_gestas_previas = models.IntegerField(blank=True, null=True)
#     nu_partos = models.IntegerField(blank=True, null=True)
#     co_dim_modalidade_ad = models.ForeignKey(TbDimModalidadeAd, models.DO_NOTHING, db_column='co_dim_modalidade_ad', blank=True, null=True)
#     st_ficou_em_observacao = models.IntegerField(blank=True, null=True)
#     st_nasf_avaliacao_diagnostico = models.IntegerField(blank=True, null=True)
#     st_nasf_proce_clin_terapeutico = models.IntegerField(blank=True, null=True)
#     st_nasf_prescricao_terapeutica = models.IntegerField(blank=True, null=True)
#     st_conduta_consulta_agendada = models.IntegerField(blank=True, null=True)
#     st_conduta_cuidd_conti_program = models.IntegerField(blank=True, null=True)
#     st_conduta_agendamento_grupos = models.IntegerField(blank=True, null=True)
#     st_conduta_agendamento_nasf = models.IntegerField(blank=True, null=True)
#     st_conduta_alta_episodio = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_interno_dia = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_serv_special = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_caps = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_intern_hospi = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_urgencia = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_servico_ad = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_intersetoria = models.IntegerField(blank=True, null=True)
#     ds_filtro_cids = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_ciaps = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_proced_avaliados = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_proced_solicitados = models.CharField(max_length=4000, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
#     dt_final_atendimento = models.DateTimeField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atendimento_individual'
#
#
# class TbFatAtendimentoOdonto(models.Model):
#     co_seq_fat_atd_odnt = models.BigIntegerField(primary_key=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_local_atendimento = models.ForeignKey(TbDimLocalAtendimento, models.DO_NOTHING, db_column='co_dim_local_atendimento', blank=True, null=True)
#     st_paciente_necessidades_espec = models.IntegerField(blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_atendimento = models.ForeignKey(TbDimTipoAtendimento, models.DO_NOTHING, db_column='co_dim_tipo_atendimento', blank=True, null=True)
#     co_dim_tipo_consulta = models.ForeignKey(TbDimTipoConsultaOdonto, models.DO_NOTHING, db_column='co_dim_tipo_consulta', blank=True, null=True)
#     st_vigil_abscesso_dentoalveola = models.IntegerField(blank=True, null=True)
#     st_vigil_alterac_tecidos_moles = models.IntegerField(blank=True, null=True)
#     st_vigil_dor_dente = models.IntegerField(blank=True, null=True)
#     st_vigil_fendas_fissuras_labio = models.IntegerField(blank=True, null=True)
#     st_vigil_fluorose_dentaria = models.IntegerField(blank=True, null=True)
#     st_vigil_traumat_dentoalveolar = models.IntegerField(blank=True, null=True)
#     st_vigil_nao_identificado = models.IntegerField(blank=True, null=True)
#     st_fornecimento_escova_dental = models.IntegerField(blank=True, null=True)
#     st_fornecimento_creme_dental = models.IntegerField(blank=True, null=True)
#     st_fornecimento_fio_dental = models.IntegerField(blank=True, null=True)
#     st_conduta_consulta_agendada = models.IntegerField(blank=True, null=True)
#     st_conduta_outros_profissio_ab = models.IntegerField(blank=True, null=True)
#     st_conduta_agendamento_nasf = models.IntegerField(blank=True, null=True)
#     st_conduta_agendamento_grupos = models.IntegerField(blank=True, null=True)
#     st_conduta_alta_episodio = models.IntegerField(blank=True, null=True)
#     st_conduta_tratamento_concluid = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_necess_espec = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_cirurgia_bmf = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_endodontia = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_estomatologi = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_implantodont = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_odontopediat = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_ortod_ortop = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_periodontia = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_protese_dent = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_radiologia = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_outros = models.IntegerField(blank=True, null=True)
#     st_encaminhamento_nao_aplica = models.IntegerField(blank=True, null=True)
#     ds_filtro_cids = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_ciaps = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_procedimentos = models.CharField(max_length=4000, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
#     dt_final_atendimento = models.DateTimeField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atendimento_odonto'
#
#
# class TbFatAtividadeColetiva(models.Model):
#     co_seq_fat_atividade_coletiva = models.BigIntegerField(primary_key=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_undd_sade_acdm_sade = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_undd_sade_acdm_sade', blank=True, null=True)
#     co_dim_procedimento = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_participantes = models.IntegerField(blank=True, null=True)
#     nu_participantes_registrados = models.IntegerField(blank=True, null=True)
#     nu_avaliacoes_alteradas = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_atividade = models.ForeignKey(TbDimTipoAtividade, models.DO_NOTHING, db_column='co_dim_tipo_atividade', blank=True, null=True)
#     ds_filtro_tema_reuniao = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_tema_para_saude = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_public_alvo = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_pratica_em_saude = models.CharField(max_length=4000, blank=True, null=True)
#     st_pse_educacao = models.IntegerField(blank=True, null=True)
#     st_pse_saude = models.IntegerField(blank=True, null=True)
#     ds_outra_localidade = models.CharField(max_length=250, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_dim_inep = models.ForeignKey(TbDimInep, models.DO_NOTHING, db_column='co_dim_inep', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atividade_coletiva'
#
#
# class TbFatAtvddColetivaExt(models.Model):
#     co_seq_fat_atvdd_cltv_ext = models.BigIntegerField(primary_key=True)
#     co_fat_atividade_coletiva = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_atividade = models.ForeignKey(TbDimTipoAtividade, models.DO_NOTHING, db_column='co_dim_tipo_atividade', blank=True, null=True)
#     st_pblc_alvo_comunidade_geral = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_crianca_0_3_anos = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_crianca_4_5_anos = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_crianca_6_11_anos = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_adolescente = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_mulher = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_gestante = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_homem = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_familiares = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_idoso = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_pessoa_doen_croni = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_usuario_tabaco = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_usuario_alcool = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_usuario_outr_drog = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_pes_sofr_trtm_men = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_profiss_educacao = models.IntegerField(blank=True, null=True)
#     st_pblc_alvo_outros = models.IntegerField(blank=True, null=True)
#     st_tema_saude_comb_aedes_aegyp = models.IntegerField(blank=True, null=True)
#     st_tema_saude_agravos_negligen = models.IntegerField(blank=True, null=True)
#     st_tema_saude_aliment_saudavel = models.IntegerField(blank=True, null=True)
#     st_tema_saude_pess_doenc_croni = models.IntegerField(blank=True, null=True)
#     st_tema_saude_cidad_dirt_human = models.IntegerField(blank=True, null=True)
#     st_tema_saude_dependen_quimica = models.IntegerField(blank=True, null=True)
#     st_tema_saude_envelhecimento = models.IntegerField(blank=True, null=True)
#     st_tema_saude_pant_medic_fitot = models.IntegerField(blank=True, null=True)
#     st_tema_saude_preven_violencia = models.IntegerField(blank=True, null=True)
#     st_tema_saude_saude_ambiental = models.IntegerField(blank=True, null=True)
#     st_tema_saude_saude_bucal = models.IntegerField(blank=True, null=True)
#     st_tema_saude_saude_trabalhad = models.IntegerField(blank=True, null=True)
#     st_tema_saude_saude_mental = models.IntegerField(blank=True, null=True)
#     st_tema_saude_saude_sex_repro = models.IntegerField(blank=True, null=True)
#     st_tema_saude_seman_saud_esco = models.IntegerField(blank=True, null=True)
#     st_tema_saude_outros = models.IntegerField(blank=True, null=True)
#     st_prat_saude_antropometria = models.IntegerField(blank=True, null=True)
#     st_prat_saude_aplic_topi_fluor = models.IntegerField(blank=True, null=True)
#     st_prat_saude_desenv_linguagem = models.IntegerField(blank=True, null=True)
#     st_prat_saude_escov_supervisio = models.IntegerField(blank=True, null=True)
#     st_prat_saude_prt_corp_atv_fis = models.IntegerField(blank=True, null=True)
#     st_prat_saude_pnct_1 = models.IntegerField(blank=True, null=True)
#     st_prat_saude_pnct_2 = models.IntegerField(blank=True, null=True)
#     st_prat_saude_pnct_3 = models.IntegerField(blank=True, null=True)
#     st_prat_saude_pnct_4 = models.IntegerField(blank=True, null=True)
#     st_prat_saude_saude_auditiva = models.IntegerField(blank=True, null=True)
#     st_prat_saude_saude_ocular = models.IntegerField(blank=True, null=True)
#     st_prat_saude_situacao_vacinal = models.IntegerField(blank=True, null=True)
#     st_prat_saude_outras = models.IntegerField(blank=True, null=True)
#     st_prat_saude_outro_procedimen = models.IntegerField(blank=True, null=True)
#     co_dim_procedimento = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atvdd_coletiva_ext'
#
#
# class TbFatAtvddColetivaInt(models.Model):
#     co_seq_fat_atvdd_cltv_int = models.BigIntegerField(primary_key=True)
#     co_fat_atividade_coletiva = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_atividade = models.ForeignKey(TbDimTipoAtividade, models.DO_NOTHING, db_column='co_dim_tipo_atividade', blank=True, null=True)
#     st_tema_reuniao_quest_adm_func = models.IntegerField(blank=True, null=True)
#     st_tema_reuniao_processo_traba = models.IntegerField(blank=True, null=True)
#     st_tema_reuniao_diag_monit_ter = models.IntegerField(blank=True, null=True)
#     st_tema_reuniao_plan_monit_equ = models.IntegerField(blank=True, null=True)
#     st_tema_reuniao_disc_proj_tera = models.IntegerField(blank=True, null=True)
#     st_tema_reuniao_educa_permanen = models.IntegerField(blank=True, null=True)
#     st_tema_reuniao_outros = models.IntegerField(blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atvdd_coletiva_int'
#
#
# class TbFatAtvddColetivaPart(models.Model):
#     co_seq_fat_atvdd_cltv_part = models.BigIntegerField(primary_key=True)
#     co_fat_atividade_coletiva = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_atividade = models.ForeignKey(TbDimTipoAtividade, models.DO_NOTHING, db_column='co_dim_tipo_atividade', blank=True, null=True)
#     nu_participante_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_participante_nascimento = models.DateField(blank=True, null=True)
#     co_dim_participante_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_participante_sexo', blank=True, null=True)
#     st_avaliacao_alterada = models.IntegerField(blank=True, null=True)
#     st_pcnt_cessou_habito_fumar = models.IntegerField(blank=True, null=True)
#     st_pcnt_abandonou_grupo = models.IntegerField(blank=True, null=True)
#     nu_participante_altura = models.FloatField(blank=True, null=True)
#     nu_participante_peso = models.FloatField(blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_participante = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atvdd_coletiva_part'
#
#
# class TbFatAtvddColetivaPropart(models.Model):
#     co_seq_fat_atvdd_cltv_propart = models.BigIntegerField(primary_key=True)
#     co_fat_atividade_coletiva = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_dim_profssinal_participante = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profssinal_participante', blank=True, null=True)
#     co_dim_cbo_participante = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_participante', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_atvdd_coletiva_propart'
#
#
# class TbFatAvaliacaoElegibilidade(models.Model):
#     co_seq_fat_avaliacao_elegibldd = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional_1 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_1', blank=True, null=True)
#     co_dim_cbo_1 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_1', blank=True, null=True)
#     co_dim_equipe_1 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_1', blank=True, null=True)
#     co_dim_unidade_saude_1 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_1', blank=True, null=True)
#     co_dim_profissional_2 = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional_2', blank=True, null=True)
#     co_dim_cbo_2 = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_2', blank=True, null=True)
#     co_dim_equipe_2 = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_2', blank=True, null=True)
#     co_dim_unidade_saude_2 = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_2', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_procedencia_origem = models.ForeignKey(TbDimProcedenciaOrigem, models.DO_NOTHING, db_column='co_dim_procedencia_origem', blank=True, null=True)
#     st_condic_acamado = models.IntegerField(blank=True, null=True)
#     st_condic_domiciliado = models.IntegerField(blank=True, null=True)
#     st_condic_ulceras_feridas = models.IntegerField(blank=True, null=True)
#     st_condic_acompanham_nutricion = models.IntegerField(blank=True, null=True)
#     st_condic_uso_sonda_nasogastri = models.IntegerField(blank=True, null=True)
#     st_condic_uso_sonda_nasoentera = models.IntegerField(blank=True, null=True)
#     st_condic_uso_gastrostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_colostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_cistostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_sond_vesic_demor = models.IntegerField(blank=True, null=True)
#     st_condic_acomp_pre_operatorio = models.IntegerField(blank=True, null=True)
#     st_condic_acomp_pos_operatorio = models.IntegerField(blank=True, null=True)
#     st_condic_adapt_uso_ortes_prot = models.IntegerField(blank=True, null=True)
#     st_condic_reabilita_domiciliar = models.IntegerField(blank=True, null=True)
#     st_condic_cuidd_paliat_oncolog = models.IntegerField(blank=True, null=True)
#     st_condic_cuidd_paliat_n_oncol = models.IntegerField(blank=True, null=True)
#     st_condic_oxigenoterapia_domic = models.IntegerField(blank=True, null=True)
#     st_condic_uso_traqueostomia = models.IntegerField(blank=True, null=True)
#     st_condic_uso_aspir_via_aerea = models.IntegerField(blank=True, null=True)
#     st_condic_suport_ventil_cpap = models.IntegerField(blank=True, null=True)
#     st_condic_suport_ventil_bipap = models.IntegerField(blank=True, null=True)
#     st_condic_dialise_peritonial = models.IntegerField(blank=True, null=True)
#     st_condic_paracentese = models.IntegerField(blank=True, null=True)
#     st_condic_medicacao_parenteral = models.IntegerField(blank=True, null=True)
#     co_dim_cid_principal = models.ForeignKey(TbDimCid, models.DO_NOTHING, db_column='co_dim_cid_principal', blank=True, null=True)
#     co_dim_cid_sec_1 = models.ForeignKey(TbDimCid, models.DO_NOTHING, db_column='co_dim_cid_sec_1', blank=True, null=True)
#     co_dim_cid_sec_2 = models.ForeignKey(TbDimCid, models.DO_NOTHING, db_column='co_dim_cid_sec_2', blank=True, null=True)
#     co_dim_conclusao_modalidade_ad = models.ForeignKey(TbDimModalidadeAd, models.DO_NOTHING, db_column='co_dim_conclusao_modalidade_ad', blank=True, null=True)
#     co_dim_tipo_elegibilidade = models.ForeignKey(TbDimTipoElegibilidade, models.DO_NOTHING, db_column='co_dim_tipo_elegibilidade', blank=True, null=True)
#     st_inelegivel_instabil_clinica = models.IntegerField(blank=True, null=True)
#     st_inelegivel_necessid_propede = models.IntegerField(blank=True, null=True)
#     st_inelegivel_outro_motivo_cli = models.IntegerField(blank=True, null=True)
#     st_inelegivel_ausencia_cuidad = models.IntegerField(blank=True, null=True)
#     st_inelegivel_outra_condi_soci = models.IntegerField(blank=True, null=True)
#     co_dim_raca_cor = models.ForeignKey(TbDimRacaCor, models.DO_NOTHING, db_column='co_dim_raca_cor', blank=True, null=True)
#     co_dim_etnia = models.ForeignKey(TbDimEtnia, models.DO_NOTHING, db_column='co_dim_etnia', blank=True, null=True)
#     st_desconhece_nome_mae = models.IntegerField(blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     co_dim_nacionalidade = models.ForeignKey(TbDimNacionalidade, models.DO_NOTHING, db_column='co_dim_nacionalidade', blank=True, null=True)
#     dt_naturalizacao = models.DateField(blank=True, null=True)
#     co_dim_pais_nascimento = models.ForeignKey(TbDimPais, models.DO_NOTHING, db_column='co_dim_pais_nascimento', blank=True, null=True)
#     dt_entrada_brasil = models.DateField(blank=True, null=True)
#     co_dim_municipio_cidadao = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio_cidadao', blank=True, null=True)
#     co_dim_tipo_logradouro = models.ForeignKey(TbDimTipoLogradouro, models.DO_NOTHING, db_column='co_dim_tipo_logradouro', blank=True, null=True)
#     co_dim_municipio_residencia = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio_residencia', blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=15, blank=True, null=True)
#     co_dim_cuidador = models.ForeignKey(TbDimCuidador, models.DO_NOTHING, db_column='co_dim_cuidador', blank=True, null=True)
#     no_nome = models.CharField(max_length=225, blank=True, null=True)
#     no_nome_social = models.CharField(max_length=225, blank=True, null=True)
#     nu_nis = models.CharField(max_length=32, blank=True, null=True)
#     no_nome_mae = models.CharField(max_length=225, blank=True, null=True)
#     no_nome_pai = models.CharField(max_length=225, blank=True, null=True)
#     nu_portaria_naturalizacao = models.CharField(max_length=65, blank=True, null=True)
#     co_dim_uf_cidadao = models.BigIntegerField(blank=True, null=True)
#     no_email = models.CharField(max_length=225, blank=True, null=True)
#     nu_cep_residencia = models.CharField(max_length=33, blank=True, null=True)
#     co_dim_uf_residencia = models.BigIntegerField(blank=True, null=True)
#     no_bairro_residencia = models.CharField(max_length=545, blank=True, null=True)
#     no_logradouro_residencia = models.CharField(max_length=161, blank=True, null=True)
#     nu_num_logradouro_residencia = models.CharField(max_length=33, blank=True, null=True)
#     no_complemento_residencia = models.CharField(max_length=545, blank=True, null=True)
#     no_referencia_residencia = models.CharField(max_length=97, blank=True, null=True)
#     nu_telefone_residencia = models.CharField(max_length=33, blank=True, null=True)
#     nu_telefone_contato = models.CharField(max_length=33, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     co_fat_cidadao_pec_cuidador = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec_cuidador', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_avaliacao_elegibilidade'
#
#
# class TbFatCadDomFamilia(models.Model):
#     co_seq_fat_cad_dom_familia = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_uuid_ficha_origem = models.CharField(max_length=92, blank=True, null=True)
#     st_recusa_cadastro = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_tempo_validade = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade', blank=True, null=True)
#     co_dim_tempo_validade_recusa = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade_recusa', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     nu_cns_responsavel = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     dt_inicio_residencia = models.DateField(blank=True, null=True)
#     st_mudou = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_renda_familiar = models.ForeignKey(TbDimTipoRendaFamiliar, models.DO_NOTHING, db_column='co_dim_tipo_renda_familiar', blank=True, null=True)
#     st_normaliza_ficha_cadastros = models.IntegerField(blank=True, null=True)
#     co_fat_cad_domiciliar = models.BigIntegerField(blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     qt_membro_familiar = models.IntegerField(blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_cad_dom_familia'
#
#
# class TbFatCadDomiciliar(models.Model):
#     co_seq_fat_cad_domiciliar = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_uuid_ficha_origem = models.CharField(max_length=92, blank=True, null=True)
#     qt_morador = models.IntegerField(blank=True, null=True)
#     nu_comodo = models.IntegerField(blank=True, null=True)
#     st_recusa_cadastro = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_tipo_imovel = models.ForeignKey(TbDimTipoImovel, models.DO_NOTHING, db_column='co_dim_tipo_imovel', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_tempo_validade = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade', blank=True, null=True)
#     co_dim_tempo_validade_recusa = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade_recusa', blank=True, null=True)
#     co_dim_tipo_logradouro = models.ForeignKey(TbDimTipoLogradouro, models.DO_NOTHING, db_column='co_dim_tipo_logradouro', blank=True, null=True)
#     co_dim_municipio_cidadao = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio_cidadao', blank=True, null=True)
#     co_dim_tipo_situacao_moradia = models.ForeignKey(TbDimTipoSituacaoMoradia, models.DO_NOTHING, db_column='co_dim_tipo_situacao_moradia', blank=True, null=True)
#     co_dim_tipo_localizacao = models.ForeignKey(TbDimTipoLocalizacao, models.DO_NOTHING, db_column='co_dim_tipo_localizacao', blank=True, null=True)
#     co_dim_tipo_domicilio = models.ForeignKey(TbDimTipoDomicilio, models.DO_NOTHING, db_column='co_dim_tipo_domicilio', blank=True, null=True)
#     co_dim_tipo_posse_terra = models.ForeignKey(TbDimTipoPosseTerra, models.DO_NOTHING, db_column='co_dim_tipo_posse_terra', blank=True, null=True)
#     co_dim_tipo_acesso_domicilio = models.ForeignKey(TbDimTipoAcessoDomicilio, models.DO_NOTHING, db_column='co_dim_tipo_acesso_domicilio', blank=True, null=True)
#     co_dim_tipo_material_parede = models.ForeignKey(TbDimTipoMaterialParede, models.DO_NOTHING, db_column='co_dim_tipo_material_parede', blank=True, null=True)
#     co_dim_tipo_abastecimento_agua = models.ForeignKey(TbDimTipoAbastecimentoAgua, models.DO_NOTHING, db_column='co_dim_tipo_abastecimento_agua', blank=True, null=True)
#     co_dim_tipo_tratamento_agua = models.ForeignKey(TbDimTipoTratamentoAgua, models.DO_NOTHING, db_column='co_dim_tipo_tratamento_agua', blank=True, null=True)
#     co_dim_tipo_escoamento_sanitar = models.ForeignKey(TbDimTipoEscoamentoSanitar, models.DO_NOTHING, db_column='co_dim_tipo_escoamento_sanitar', blank=True, null=True)
#     co_dim_tipo_destino_lixo = models.ForeignKey(TbDimTipoDestinoLixo, models.DO_NOTHING, db_column='co_dim_tipo_destino_lixo', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     st_disp_energia = models.IntegerField(blank=True, null=True)
#     st_animal_domiciliar = models.IntegerField(blank=True, null=True)
#     qt_animal_domiciliar = models.IntegerField(blank=True, null=True)
#     st_animal_gato = models.IntegerField(blank=True, null=True)
#     st_animal_cachorro = models.IntegerField(blank=True, null=True)
#     st_animal_passaro = models.IntegerField(blank=True, null=True)
#     st_animal_outros = models.IntegerField(blank=True, null=True)
#     st_outros_prof_vinclds = models.IntegerField(blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_processo_linha_tempo = models.IntegerField(blank=True, null=True)
#     st_processo_familia = models.IntegerField(blank=True, null=True)
#     st_familias = models.IntegerField(blank=True, null=True)
#     ds_filtro_tipo_renda_familiar = models.CharField(max_length=4000, blank=True, null=True)
#     nu_cep = models.CharField(max_length=33, blank=True, null=True)
#     no_logradouro = models.CharField(max_length=288, blank=True, null=True)
#     nu_num_logradouro = models.CharField(max_length=64, blank=True, null=True)
#     no_complemento = models.CharField(max_length=545, blank=True, null=True)
#     no_bairro = models.CharField(max_length=545, blank=True, null=True)
#     no_ponto_referencia = models.CharField(max_length=200, blank=True, null=True)
#     nu_telefone_residencia = models.CharField(max_length=64, blank=True, null=True)
#     nu_telefone_contato = models.CharField(max_length=64, blank=True, null=True)
#     no_instituicao_nome = models.CharField(max_length=225, blank=True, null=True)
#     no_instituicao_cargo = models.CharField(max_length=225, blank=True, null=True)
#     nu_instituicao_cns = models.CharField(max_length=33, blank=True, null=True)
#     nu_instituicao_telefone = models.CharField(max_length=33, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     st_gerado_automaticamente = models.IntegerField(blank=True, null=True)
#     st_proc_operacionais = models.IntegerField(blank=True, null=True)
#     st_processa_familita_terrtro = models.IntegerField(blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_cad_domiciliar'
#
#
# class TbFatCadIndividual(models.Model):
#     co_seq_fat_cad_individual = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_uuid_ficha_origem = models.CharField(max_length=92, blank=True, null=True)
#     st_recusa_cadastro = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     st_desconhece_mae = models.IntegerField(blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_tempo_validade = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade', blank=True, null=True)
#     co_dim_tempo_validade_recusa = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade_recusa', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_raca_cor = models.ForeignKey(TbDimRacaCor, models.DO_NOTHING, db_column='co_dim_raca_cor', blank=True, null=True)
#     co_dim_nacionalidade = models.ForeignKey(TbDimNacionalidade, models.DO_NOTHING, db_column='co_dim_nacionalidade', blank=True, null=True)
#     co_dim_pais_nascimento = models.ForeignKey(TbDimPais, models.DO_NOTHING, db_column='co_dim_pais_nascimento', blank=True, null=True)
#     co_dim_municipio_cidadao = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio_cidadao', blank=True, null=True)
#     nu_cns_responsavel = models.CharField(max_length=15, blank=True, null=True)
#     st_responsavel_familiar = models.IntegerField(blank=True, null=True)
#     st_frequenta_creche = models.IntegerField(blank=True, null=True)
#     st_frequenta_cuidador = models.IntegerField(blank=True, null=True)
#     st_participa_grupo_comunitario = models.IntegerField(blank=True, null=True)
#     st_plano_saude_privado = models.IntegerField(blank=True, null=True)
#     st_comunidade_tradicional = models.IntegerField(blank=True, null=True)
#     st_deficiencia = models.IntegerField(blank=True, null=True)
#     st_defi_auditiva = models.IntegerField(blank=True, null=True)
#     st_defi_intelectual_cognitiva = models.IntegerField(blank=True, null=True)
#     st_defi_outra = models.IntegerField(blank=True, null=True)
#     st_defi_visual = models.IntegerField(blank=True, null=True)
#     st_defi_fisica = models.IntegerField(blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_doenca_respiratoria = models.IntegerField(blank=True, null=True)
#     st_doenca_respira_asma = models.IntegerField(blank=True, null=True)
#     st_doenca_respira_dpoc_enfisem = models.IntegerField(blank=True, null=True)
#     st_doenca_respira_outra = models.IntegerField(blank=True, null=True)
#     st_doenca_respira_n_sabe = models.IntegerField(blank=True, null=True)
#     st_fumante = models.IntegerField(blank=True, null=True)
#     st_alcool = models.IntegerField(blank=True, null=True)
#     st_outra_droga = models.IntegerField(blank=True, null=True)
#     st_hipertensao_arterial = models.IntegerField(blank=True, null=True)
#     st_diabete = models.IntegerField(blank=True, null=True)
#     st_avc = models.IntegerField(blank=True, null=True)
#     st_infarto = models.IntegerField(blank=True, null=True)
#     st_hanseniase = models.IntegerField(blank=True, null=True)
#     st_tuberculose = models.IntegerField(blank=True, null=True)
#     st_cancer = models.IntegerField(blank=True, null=True)
#     st_internacao_12 = models.IntegerField(blank=True, null=True)
#     st_tratamento_psiquiatra = models.IntegerField(blank=True, null=True)
#     st_acamado = models.IntegerField(blank=True, null=True)
#     st_domiciliado = models.IntegerField(blank=True, null=True)
#     st_usa_planta_medicinal = models.IntegerField(blank=True, null=True)
#     st_doenca_cardiaca = models.IntegerField(blank=True, null=True)
#     st_doenca_card_insuficiencia = models.IntegerField(blank=True, null=True)
#     st_doenca_card_outro = models.IntegerField(blank=True, null=True)
#     st_doenca_card_n_sabe = models.IntegerField(blank=True, null=True)
#     st_problema_rins = models.IntegerField(blank=True, null=True)
#     st_problema_rins_insuficiencia = models.IntegerField(blank=True, null=True)
#     st_problema_rins_outro = models.IntegerField(blank=True, null=True)
#     st_problema_rins_nao_sabe = models.IntegerField(blank=True, null=True)
#     st_pic = models.IntegerField(blank=True, null=True)
#     st_morador_rua = models.IntegerField(blank=True, null=True)
#     st_recebe_beneficio = models.IntegerField(blank=True, null=True)
#     st_referencia_familiar = models.IntegerField(blank=True, null=True)
#     co_dim_frequencia_alimentacao = models.ForeignKey(TbDimFrequenciaAlimentacao, models.DO_NOTHING, db_column='co_dim_frequencia_alimentacao', blank=True, null=True)
#     st_orig_alimen_restaurante_pop = models.IntegerField(blank=True, null=True)
#     st_orig_alimen_doacao_reli = models.IntegerField(blank=True, null=True)
#     st_orig_alimen_doacao_rest = models.IntegerField(blank=True, null=True)
#     st_orig_alimen_doacao_popular = models.IntegerField(blank=True, null=True)
#     st_orig_alimen_outros = models.IntegerField(blank=True, null=True)
#     st_acompanhado_instituicao = models.IntegerField(blank=True, null=True)
#     st_visita_familiar_frequente = models.IntegerField(blank=True, null=True)
#     st_higiene_pessoal_acesso = models.IntegerField(blank=True, null=True)
#     st_hig_pess_banho = models.IntegerField(blank=True, null=True)
#     st_hig_pess_sanitario = models.IntegerField(blank=True, null=True)
#     st_hig_pess_higiene_bucal = models.IntegerField(blank=True, null=True)
#     st_hig_pess_outros = models.IntegerField(blank=True, null=True)
#     co_dim_tipo_parentesco = models.ForeignKey(TbDimTipoParentesco, models.DO_NOTHING, db_column='co_dim_tipo_parentesco', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tipo_escolaridade = models.ForeignKey(TbDimTipoEscolaridade, models.DO_NOTHING, db_column='co_dim_tipo_escolaridade', blank=True, null=True)
#     co_dim_situacao_trabalho = models.ForeignKey(TbDimSituacaoTrabalho, models.DO_NOTHING, db_column='co_dim_situacao_trabalho', blank=True, null=True)
#     co_dim_tipo_orientacao_sexual = models.ForeignKey(TbDimTipoOrientacaoSexual, models.DO_NOTHING, db_column='co_dim_tipo_orientacao_sexual', blank=True, null=True)
#     co_dim_tipo_saida_cadastro = models.ForeignKey(TbDimTipoSaidaCadastro, models.DO_NOTHING, db_column='co_dim_tipo_saida_cadastro', blank=True, null=True)
#     co_dim_tipo_condicao_peso = models.ForeignKey(TbDimTipoCondicaoPeso, models.DO_NOTHING, db_column='co_dim_tipo_condicao_peso', blank=True, null=True)
#     co_dim_tempo_morador_rua = models.ForeignKey(TbDimTempoMoradorRua, models.DO_NOTHING, db_column='co_dim_tempo_morador_rua', blank=True, null=True)
#     co_dim_etnia = models.ForeignKey(TbDimEtnia, models.DO_NOTHING, db_column='co_dim_etnia', blank=True, null=True)
#     co_dim_cbo_cidadao = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo_cidadao', blank=True, null=True)
#     co_dim_identidade_genero = models.ForeignKey(TbDimIdentidadeGenero, models.DO_NOTHING, db_column='co_dim_identidade_genero', blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     st_desconhece_pai = models.IntegerField(blank=True, null=True)
#     st_informar_orientacao_sexual = models.IntegerField(blank=True, null=True)
#     st_informar_identidade_genero = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateField(blank=True, null=True)
#     dt_entrada_brasil = models.DateField(blank=True, null=True)
#     dt_obito = models.DateField(blank=True, null=True)
#     st_respons_crianca_adulto_resp = models.IntegerField(blank=True, null=True)
#     st_respons_crianca_outra_crian = models.IntegerField(blank=True, null=True)
#     st_respons_crianca_adolescente = models.IntegerField(blank=True, null=True)
#     st_respons_crianca_sozinha = models.IntegerField(blank=True, null=True)
#     st_respons_crianca_creche = models.IntegerField(blank=True, null=True)
#     st_respons_crianca_outro = models.IntegerField(blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_processo_linha_tempo = models.IntegerField(blank=True, null=True)
#     st_processo_cidadao = models.IntegerField(blank=True, null=True)
#     no_nome = models.CharField(max_length=500, blank=True, null=True)
#     no_nome_social = models.CharField(max_length=500, blank=True, null=True)
#     no_nome_mae = models.CharField(max_length=500, blank=True, null=True)
#     no_nome_pai = models.CharField(max_length=500, blank=True, null=True)
#     nu_nis = models.CharField(max_length=32, blank=True, null=True)
#     nu_portaria_naturalizacao = models.CharField(max_length=65, blank=True, null=True)
#     nu_celular = models.CharField(max_length=33, blank=True, null=True)
#     no_email = models.CharField(max_length=500, blank=True, null=True)
#     nu_obito_do = models.CharField(max_length=32, blank=True, null=True)
#     no_maternidade_referencia = models.CharField(max_length=500, blank=True, null=True)
#     no_causa_internacao12 = models.CharField(max_length=500, blank=True, null=True)
#     no_plantas_medicinais = models.CharField(max_length=500, blank=True, null=True)
#     no_outra_condicao1 = models.CharField(max_length=500, blank=True, null=True)
#     no_outra_condicao2 = models.CharField(max_length=500, blank=True, null=True)
#     no_outra_condicao3 = models.CharField(max_length=500, blank=True, null=True)
#     no_acompanhado_instituicao = models.CharField(max_length=500, blank=True, null=True)
#     no_visita_familiar_parentesco = models.CharField(max_length=500, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     st_gerado_automaticamente = models.IntegerField(blank=True, null=True)
#     st_ficha_inativa = models.IntegerField(blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     co_fat_cidadao_pec_responsvl = models.ForeignKey('TbFatCidadaoPec', models.DO_NOTHING, db_column='co_fat_cidadao_pec_responsvl', blank=True, null=True)
#     st_proc_operacionais = models.IntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_povo_comunidad_trad = models.ForeignKey(TbDimPovoComunidadTrad, models.DO_NOTHING, db_column='co_dim_povo_comunidad_trad', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_cad_individual'
#
#
# class TbFatCidadao(models.Model):
#     co_seq_fat_cidadao = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_uuid_ficha_origem = models.CharField(max_length=92, blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     co_fat_cad_individual = models.BigIntegerField(blank=True, null=True)
#     co_fat_familia = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_fat_cidadao_raiz = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai1 = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai2 = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_validade = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade', blank=True, null=True)
#     co_dim_linha_tempo_validade = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_linha_tempo_validade', blank=True, null=True)
#     co_fat_cidadao_raiz_equipe = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai1_equipe = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai2_equipe = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_valdd_equipe = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_valdd_equipe', blank=True, null=True)
#     co_dim_linha_tempo_valdd_equp = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_linha_tempo_valdd_equp', blank=True, null=True)
#     co_fat_cidadao_raiz_undde_sade = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai1_undde_sade = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai2_undde_sade = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_valdd_unidd_saud = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_valdd_unidd_saud', blank=True, null=True)
#     co_dim_lnh_vldd_unidd_sad = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_lnh_vldd_unidd_sad', blank=True, null=True)
#     co_fat_cidadao_raiz_municipio = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai1_municipio = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao_pai2_municipio = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_valdd_municipio = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_valdd_municipio', blank=True, null=True)
#     co_dim_linha_valdd_municipio = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_linha_valdd_municipio', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     st_responsavel_familiar = models.IntegerField(blank=True, null=True)
#     st_mudou = models.IntegerField(blank=True, null=True)
#     st_vivo = models.IntegerField(blank=True, null=True)
#     st_ativo_territorio = models.IntegerField(blank=True, null=True)
#     st_processo_linha_tempo = models.IntegerField(blank=True, null=True)
#     st_processo_familia = models.IntegerField(blank=True, null=True)
#     st_ficha_inativa = models.IntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_cidadao'
#
#
# class TbFatCidadaoPec(models.Model):
#     co_seq_fat_cidadao_pec = models.BigIntegerField(primary_key=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=500, blank=True, null=True)
#     no_social_cidadao = models.CharField(max_length=500, blank=True, null=True)
#     co_dim_tempo_nascimento = models.BigIntegerField(blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_identidade_genero = models.ForeignKey(TbDimIdentidadeGenero, models.DO_NOTHING, db_column='co_dim_identidade_genero', blank=True, null=True)
#     nu_telefone_celular = models.CharField(max_length=100, blank=True, null=True)
#     st_faleceu = models.IntegerField(blank=True, null=True)
#     st_lookup_etl = models.IntegerField(blank=True, null=True)
#     st_deletar = models.IntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_unidade_saude_vinc = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude_vinc', blank=True, null=True)
#     co_dim_equipe_vinc = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe_vinc', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_cidadao_pec'
#
#
# class TbFatCidadaoTerritorio(models.Model):
#     co_seq_fat_cidadao_territorio = models.BigIntegerField(primary_key=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     st_responsavel = models.IntegerField(blank=True, null=True)
#     st_responsavel_informado = models.IntegerField(blank=True, null=True)
#     st_mudou_se = models.IntegerField(blank=True, null=True)
#     st_vivo = models.IntegerField(blank=True, null=True)
#     st_responsavel_com_fci = models.IntegerField(blank=True, null=True)
#     st_cns_null = models.IntegerField(blank=True, null=True)
#     st_cidadao_consistente = models.IntegerField(blank=True, null=True)
#     co_fat_familia_territorio = models.BigIntegerField(blank=True, null=True)
#     co_fat_ciddo_terrtrio_resp = models.BigIntegerField(blank=True, null=True)
#     st_processado_cidadao_respnsvl = models.IntegerField(blank=True, null=True)
#     co_fat_cad_individual = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_cidadao_territorio'
#
#
# class TbFatCnslddoCiddoFaiCid(models.Model):
#     co_seq_fat_cnsldo_cido_fai_cid = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_dim_cid = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_cnslddo_ciddo_fai_cid'
#
#
# class TbFatComplementar(models.Model):
#     co_seq_fat_complementar = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     nu_cns_responsavel = models.CharField(max_length=15, blank=True, null=True)
#     dt_teste_olhinho = models.DateField(blank=True, null=True)
#     st_teste_olhinho = models.IntegerField(blank=True, null=True)
#     dt_exame_fundo_olho = models.DateField(blank=True, null=True)
#     st_exame_fundo_olho = models.IntegerField(blank=True, null=True)
#     dt_teste_orelhinha = models.DateField(blank=True, null=True)
#     st_teste_orelhinha = models.IntegerField(blank=True, null=True)
#     dt_transfontanela = models.DateField(blank=True, null=True)
#     st_transfontanela = models.IntegerField(blank=True, null=True)
#     dt_tomografia = models.DateField(blank=True, null=True)
#     st_tomografia = models.IntegerField(blank=True, null=True)
#     dt_ressonancia = models.DateField(blank=True, null=True)
#     st_ressonancia = models.IntegerField(blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     co_fat_cidadao_pec_responsvl = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec_responsvl', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_complementar'
#
#
# class TbFatConsolidadoCidadaoFai(models.Model):
#     co_seq_fat_conslddo_ciddo_fai = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_dim_tempo_ultima_ficha = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_has = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_diabetes = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_tabagismo = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_obesidade = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_avc = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_infarto = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_doenca_cardiaca = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_problema_rins = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_rastr_rsco_crdo = models.BigIntegerField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     st_risco_cardio = models.IntegerField(blank=True, null=True)
#     co_dim_tempo_consulta_purperio = models.BigIntegerField(blank=True, null=True)
#     st_teste_pezinho = models.IntegerField(blank=True, null=True)
#     st_teste_orelhinha = models.IntegerField(blank=True, null=True)
#     st_teste_olhinho = models.IntegerField(blank=True, null=True)
#     co_dim_tempo_consulta_prcltra = models.BigIntegerField(blank=True, null=True)
#     co_dim_aleitamento_prcltra = models.BigIntegerField(blank=True, null=True)
#     nu_perimetro_cefalico_prcltra = models.FloatField(blank=True, null=True)
#     nu_altura_prcltra = models.FloatField(blank=True, null=True)
#     nu_peso_prcltra = models.FloatField(blank=True, null=True)
#     co_dim_tempo_cnslta_1_prcltra = models.BigIntegerField(blank=True, null=True)
#     st_vacinacao_em_dia_prcltra = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_consolidado_cidadao_fai'
#
#
# class TbFatConsolidadoCidadaoFao(models.Model):
#     co_seq_fat_conslddo_ciddo_fao = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_dim_tempo_ultima_ficha = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_consolidado_cidadao_fao'
#
#
# class TbFatConsolidadoCidadaoFci(models.Model):
#     co_seq_fat_conslddo_ciddo_fci = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_dim_tempo_ultima_ficha = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_has_sim = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_has_nao = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_diabete_sim = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_diabete_nao = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_fumante_sim = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_fumante_nao = models.BigIntegerField(blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_tempo_avc_sim = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_infarto_sim = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_donca_crdaca_sim = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_problema_rins_sim = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_avc_nao = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_infarto_nao = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_donca_crdaca_nao = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_problema_rins_nao = models.BigIntegerField(blank=True, null=True)
#     st_hprtnsao_artrl_ultima_ficha = models.IntegerField(blank=True, null=True)
#     st_diabete_ultima_ficha = models.IntegerField(blank=True, null=True)
#     st_fumante_ultima_ficha = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_consolidado_cidadao_fci'
#
#
# class TbFatConsolidadoCidadaoFp(models.Model):
#     co_seq_fat_conslddo_ciddo_fp = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_dim_tempo_ultima_ficha = models.BigIntegerField(blank=True, null=True)
#     st_teste_orelhinha = models.IntegerField(blank=True, null=True)
#     st_teste_olhinho = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_consolidado_cidadao_fp'
#
#
# class TbFatConsolidadoCidadaoFvd(models.Model):
#     co_seq_fat_conslddo_ciddo_fvd = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_dim_tempo_ultima_ficha = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_ult_visita_acs = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_consolidado_cidadao_fvd'
#
#
# class TbFatFamilia(models.Model):
#     co_seq_fat_familia = models.BigIntegerField(primary_key=True)
#     co_fat_cad_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_fat_cad_dom_familia = models.BigIntegerField(blank=True, null=True)
#     co_fat_cidadao = models.BigIntegerField(blank=True, null=True)
#     nu_uuid_ficha_cd = models.CharField(max_length=92, blank=True, null=True)
#     nu_uuid_ficha_cd_origem = models.CharField(max_length=92, blank=True, null=True)
#     nu_cns_responsavel = models.CharField(max_length=15, blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_tempo_validade = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_validade', blank=True, null=True)
#     st_registro_valido = models.IntegerField(blank=True, null=True)
#     st_responsavel_declarado_ci = models.IntegerField(blank=True, null=True)
#     st_responsavel_vivo = models.IntegerField(blank=True, null=True)
#     st_responsavel_unico = models.IntegerField(blank=True, null=True)
#     st_responsavel_ainda_reside = models.IntegerField(blank=True, null=True)
#     st_familia_ainda_reside = models.IntegerField(blank=True, null=True)
#     st_com_domicilio = models.IntegerField(blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_familia'
#
#
# class TbFatFamiliaTerritorio(models.Model):
#     co_seq_fat_familia_territorio = models.BigIntegerField(primary_key=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     nu_uuid_ficha_origem = models.CharField(max_length=92, blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_fat_cad_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_dim_tempo_fcd = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_fcd')
#     nu_prontuario = models.CharField(max_length=30, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_familia_fcd_mudouse = models.IntegerField(blank=True, null=True)
#     st_resp_com_fci_no_territorio = models.IntegerField(blank=True, null=True)
#     st_resp_declarado_no_fci = models.IntegerField(blank=True, null=True)
#     st_resp_outro_fcd_mais_atual = models.IntegerField(blank=True, null=True)
#     st_responsavel_ainda_reside = models.IntegerField(blank=True, null=True)
#     st_responsavel_vivo = models.IntegerField(blank=True, null=True)
#     st_familia_consistente = models.IntegerField(blank=True, null=True)
#     st_processo_att_cidadao = models.IntegerField(blank=True, null=True)
#     co_fat_cidadao_territorio = models.ForeignKey(TbFatCidadaoTerritorio, models.DO_NOTHING, db_column='co_fat_cidadao_territorio', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_familia_territorio'
#
#
# class TbFatFichas(models.Model):
#     co_seq_fat_fichas = models.BigIntegerField(primary_key=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_fichas'
#
#
# class TbFatMarcaConsumoAlimnt(models.Model):
#     co_seq_fat_marca_con_almnt = models.BigIntegerField(primary_key=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_local_atendimento = models.ForeignKey(TbDimLocalAtendimento, models.DO_NOTHING, db_column='co_dim_local_atendimento', blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     nu_resp_menor_6_meses_1 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_2 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_3 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_4 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_5 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_6 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_7 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_8 = models.IntegerField(blank=True, null=True)
#     nu_resp_menor_6_meses_9 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_1 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_2 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_3 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_4 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_5 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_6 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_7 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_8 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_9 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_10 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_11 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_12 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_13 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_14 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_15 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_16 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_17 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_18 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_19 = models.IntegerField(blank=True, null=True)
#     nu_resp_de_6_a_23_meses_20 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_1 = models.IntegerField(blank=True, null=True)
#     st_resp_2_anos_ou_mais_2_1 = models.IntegerField(blank=True, null=True)
#     st_resp_2_anos_ou_mais_2_2 = models.IntegerField(blank=True, null=True)
#     st_resp_2_anos_ou_mais_2_3 = models.IntegerField(blank=True, null=True)
#     st_resp_2_anos_ou_mais_2_4 = models.IntegerField(blank=True, null=True)
#     st_resp_2_anos_ou_mais_2_5 = models.IntegerField(blank=True, null=True)
#     st_resp_2_anos_ou_mais_2_6 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_3 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_4 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_5 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_6 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_7 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_8 = models.IntegerField(blank=True, null=True)
#     nu_resp_2_anos_ou_mais_9 = models.IntegerField(blank=True, null=True)
#     no_nome = models.CharField(max_length=225, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_marca_consumo_alimnt'
#
#
# class TbFatProcedAtend(models.Model):
#     co_seq_fat_proced_atend = models.BigIntegerField(primary_key=True)
#     co_fat_procedimento = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_local_atendimento = models.ForeignKey(TbDimLocalAtendimento, models.DO_NOTHING, db_column='co_dim_local_atendimento', blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     st_escuta_inicial = models.IntegerField(blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     ds_filtro_procedimento = models.CharField(max_length=4000, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
#     dt_final_atendimento = models.DateTimeField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_proced_atend'
#
#
# class TbFatProcedAtendProced(models.Model):
#     co_seq_fat_proced_atend_proced = models.BigIntegerField(primary_key=True)
#     co_fat_procedimento = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_local_atendimento = models.ForeignKey(TbDimLocalAtendimento, models.DO_NOTHING, db_column='co_dim_local_atendimento', blank=True, null=True)
#     st_escuta_inicial = models.IntegerField(blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_procedimento = models.ForeignKey(TbDimProcedimento, models.DO_NOTHING, db_column='co_dim_procedimento', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_proced_atend_proced'
#
#
# class TbFatProcedimento(models.Model):
#     co_seq_fat_procedimento = models.BigIntegerField(primary_key=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nr_proc_consdd_pressao_arteria = models.IntegerField(blank=True, null=True)
#     nr_proc_consdd_temperatura = models.IntegerField(blank=True, null=True)
#     nr_proc_consdd_curativo_simple = models.IntegerField(blank=True, null=True)
#     nr_proc_consdd_mate_exame_labo = models.IntegerField(blank=True, null=True)
#     nr_proc_consdd_glicemia_capila = models.IntegerField(blank=True, null=True)
#     nr_proc_consdd_medicao_altura = models.IntegerField(blank=True, null=True)
#     nr_proc_consdd_medicao_peso = models.IntegerField(blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_procedimento'
#
#
# class TbFatRelOpCrianca(models.Model):
#     co_seq_fat_rel_op_crianca = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     st_teste_pezinho = models.IntegerField(blank=True, null=True)
#     st_teste_orelhinha = models.IntegerField(blank=True, null=True)
#     st_teste_olhinho = models.IntegerField(blank=True, null=True)
#     dt_atend_odonto = models.DateField(blank=True, null=True)
#     dt_ultima_visita_domiciliar = models.DateField(blank=True, null=True)
#     dt_atend_puericultura = models.DateField(blank=True, null=True)
#     dt_1_consulta_puericultura = models.DateField(blank=True, null=True)
#     co_dim_aleitamento_materno = models.BigIntegerField(blank=True, null=True)
#     st_vacina_em_dia = models.IntegerField(blank=True, null=True)
#     nu_perimetro_cefalico = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_rel_op_crianca'
#
#
# class TbFatRelOpGestante(models.Model):
#     co_seq_fat_rel_op_gestante = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     co_gestacao = models.IntegerField(blank=True, null=True)
#     co_peso = models.IntegerField(blank=True, null=True)
#     dt_inicio_gestacao = models.DateField(blank=True, null=True)
#     dt_inicio_puerperio = models.DateField(blank=True, null=True)
#     dt_fim_puerperio = models.DateField(blank=True, null=True)
#     dt_fao_ultimo = models.DateField(blank=True, null=True)
#     dt_fvd_ultimo = models.DateField(blank=True, null=True)
#     st_ultima_vacina_em_dia = models.IntegerField(blank=True, null=True)
#     st_solicitacao_vdrl = models.IntegerField(blank=True, null=True)
#     st_avaliacao_vdrl = models.IntegerField(blank=True, null=True)
#     dt_fai_dum = models.DateField(blank=True, null=True)
#     dt_ultima_fai_pre_natal = models.DateField(blank=True, null=True)
#     dt_fai_puerperio = models.DateField(blank=True, null=True)
#     nu_idade_gestacional = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_rel_op_gestante'
#
#
# class TbFatRelOpRiscoCardio(models.Model):
#     co_seq_fat_rel_op_risco_cardio = models.BigIntegerField(primary_key=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec')
#     dt_hipertensao_arterial_fai = models.DateField(blank=True, null=True)
#     dt_hiprtnsao_arterial_fci_sim = models.DateField(blank=True, null=True)
#     dt_hiprtnsao_arterial_fci_nao = models.DateField(blank=True, null=True)
#     dt_diabetes_fai = models.DateField(blank=True, null=True)
#     dt_diabetes_fci_sim = models.DateField(blank=True, null=True)
#     dt_diabetes_fci_nao = models.DateField(blank=True, null=True)
#     dt_tabagismo_fai = models.DateField(blank=True, null=True)
#     dt_tabagismo_fci_sim = models.DateField(blank=True, null=True)
#     dt_tabagismo_fci_nao = models.DateField(blank=True, null=True)
#     dt_obesidade_fai = models.DateField(blank=True, null=True)
#     nu_imc = models.FloatField(blank=True, null=True)
#     dt_rastreamento_risco_cardio = models.DateField(blank=True, null=True)
#     dt_ultima_visita_domiciliar = models.DateField(blank=True, null=True)
#     dt_atend_odonto = models.DateField(blank=True, null=True)
#     dt_atend_individual = models.DateField(blank=True, null=True)
#     st_risco_cardio = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_rel_op_risco_cardio'
#
#
# class TbFatVacinacao(models.Model):
#     co_seq_fat_vacinacao = models.BigIntegerField(primary_key=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=30, blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     co_dim_local_atendimento = models.ForeignKey(TbDimLocalAtendimento, models.DO_NOTHING, db_column='co_dim_local_atendimento', blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     st_viajante = models.IntegerField(blank=True, null=True)
#     st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_puerpera = models.IntegerField(blank=True, null=True)
#     ds_filtro_imunobiologico = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_estrategia_vacinacao = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_dose_imunobiologico = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_lote = models.CharField(max_length=4000, blank=True, null=True)
#     ds_filtro_fabricante = models.CharField(max_length=4000, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     dt_inicial_atendimento = models.DateTimeField(blank=True, null=True)
#     dt_final_atendimento = models.DateTimeField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     ds_filtro_grupo_atendimento = models.CharField(max_length=4000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_vacinacao'
#
#
# class TbFatVacinacaoVacina(models.Model):
#     co_seq_fat_vacinacao_vacina = models.BigIntegerField(primary_key=True)
#     co_fat_vacinacao = models.BigIntegerField(blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     nu_atendimento = models.IntegerField(blank=True, null=True)
#     co_dim_imunobiologico = models.ForeignKey(TbDimImunobiologico, models.DO_NOTHING, db_column='co_dim_imunobiologico', blank=True, null=True)
#     co_dim_estrategia_vacinacao = models.ForeignKey(TbDimEstrategiaVacinacao, models.DO_NOTHING, db_column='co_dim_estrategia_vacinacao', blank=True, null=True)
#     co_dim_dose_imunobiologico = models.ForeignKey(TbDimDoseImunobiologico, models.DO_NOTHING, db_column='co_dim_dose_imunobiologico', blank=True, null=True)
#     no_lote = models.CharField(max_length=255, blank=True, null=True)
#     no_fabricante = models.CharField(max_length=255, blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_dim_grupo_atendimento = models.ForeignKey(TbDimGrupoAtendimento, models.DO_NOTHING, db_column='co_dim_grupo_atendimento', blank=True, null=True)
#     st_registro_anterior = models.IntegerField(blank=True, null=True)
#     co_dim_tempo_vacina_aplicada = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo_vacina_aplicada', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_vacinacao_vacina'
#
#
# class TbFatVisitaDomiciliar(models.Model):
#     co_seq_fat_visita_domiciliar = models.BigIntegerField(primary_key=True)
#     nu_uuid_ficha = models.CharField(max_length=92, blank=True, null=True)
#     co_dim_tipo_ficha = models.ForeignKey(TbDimTipoFicha, models.DO_NOTHING, db_column='co_dim_tipo_ficha', blank=True, null=True)
#     co_dim_municipio = models.ForeignKey(TbDimMunicipio, models.DO_NOTHING, db_column='co_dim_municipio', blank=True, null=True)
#     co_dim_profissional = models.ForeignKey(TbDimProfissional, models.DO_NOTHING, db_column='co_dim_profissional', blank=True, null=True)
#     co_dim_cbo = models.ForeignKey(TbDimCbo, models.DO_NOTHING, db_column='co_dim_cbo', blank=True, null=True)
#     co_dim_unidade_saude = models.ForeignKey(TbDimUnidadeSaude, models.DO_NOTHING, db_column='co_dim_unidade_saude', blank=True, null=True)
#     co_dim_equipe = models.ForeignKey(TbDimEquipe, models.DO_NOTHING, db_column='co_dim_equipe', blank=True, null=True)
#     co_dim_tempo = models.ForeignKey(TbDimTempo, models.DO_NOTHING, db_column='co_dim_tempo', blank=True, null=True)
#     co_dim_tipo_imovel = models.ForeignKey(TbDimTipoImovel, models.DO_NOTHING, db_column='co_dim_tipo_imovel', blank=True, null=True)
#     co_dim_turno = models.ForeignKey(TbDimTurno, models.DO_NOTHING, db_column='co_dim_turno', blank=True, null=True)
#     co_dim_sexo = models.ForeignKey(TbDimSexo, models.DO_NOTHING, db_column='co_dim_sexo', blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_dim_faixa_etaria = models.ForeignKey(TbDimFaixaEtaria, models.DO_NOTHING, db_column='co_dim_faixa_etaria', blank=True, null=True)
#     st_visita_compartilhada = models.IntegerField(blank=True, null=True)
#     st_mot_vis_cad_att = models.IntegerField(blank=True, null=True)
#     st_mot_vis_visita_periodica = models.IntegerField(blank=True, null=True)
#     st_mot_vis_busca_ativa = models.IntegerField(blank=True, null=True)
#     st_mot_vis_acompanhamento = models.IntegerField(blank=True, null=True)
#     st_mot_vis_egresso_internacao = models.IntegerField(blank=True, null=True)
#     st_mot_vis_ctrl_ambnte_vetor = models.IntegerField(blank=True, null=True)
#     st_mot_vis_convte_atvidd_cltva = models.IntegerField(blank=True, null=True)
#     st_mot_vis_orintacao_prevncao = models.IntegerField(blank=True, null=True)
#     st_mot_vis_outros = models.IntegerField(blank=True, null=True)
#     st_busca_ativa_consulta = models.IntegerField(blank=True, null=True)
#     st_busca_ativa_exame = models.IntegerField(blank=True, null=True)
#     st_busca_ativa_vacina = models.IntegerField(blank=True, null=True)
#     st_busca_ativa_bolsa_familia = models.IntegerField(blank=True, null=True)
#     st_acomp_gestante = models.IntegerField(blank=True, null=True)
#     st_acomp_puerpera = models.IntegerField(blank=True, null=True)
#     st_acomp_recem_nascido = models.IntegerField(blank=True, null=True)
#     st_acomp_crianca = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_desnutricao = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_reabil_deficie = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_hipertensao = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_diabetes = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_asma = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_dpoc_enfisema = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_cancer = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_doenca_cronica = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_hanseniase = models.IntegerField(blank=True, null=True)
#     st_acomp_pessoa_tuberculose = models.IntegerField(blank=True, null=True)
#     st_acomp_sintomaticos_respirat = models.IntegerField(blank=True, null=True)
#     st_acomp_tabagista = models.IntegerField(blank=True, null=True)
#     st_acomp_domiciliados_acamados = models.IntegerField(blank=True, null=True)
#     st_acomp_condi_vulnerab_social = models.IntegerField(blank=True, null=True)
#     st_acomp_condi_bolsa_familia = models.IntegerField(blank=True, null=True)
#     st_acomp_saude_mental = models.IntegerField(blank=True, null=True)
#     st_acomp_usuario_alcool = models.IntegerField(blank=True, null=True)
#     st_acomp_usuario_outras_drogra = models.IntegerField(blank=True, null=True)
#     st_ctrl_amb_vet_acao_educativa = models.IntegerField(blank=True, null=True)
#     st_ctrl_amb_vet_imovel_foco = models.IntegerField(blank=True, null=True)
#     st_ctrl_amb_vet_acao_mecanica = models.IntegerField(blank=True, null=True)
#     st_ctrl_amb_vet_tratamnt_focal = models.IntegerField(blank=True, null=True)
#     co_dim_desfecho_visita = models.ForeignKey(TbDimDesfechoVisita, models.DO_NOTHING, db_column='co_dim_desfecho_visita', blank=True, null=True)
#     nu_uuid_dado_transp = models.CharField(max_length=92, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=65, blank=True, null=True)
#     co_dim_tipo_origem_dado_transp = models.ForeignKey(TbDimTipoOrigemDadoTransp, models.DO_NOTHING, db_column='co_dim_tipo_origem_dado_transp', blank=True, null=True)
#     co_dim_cds_tipo_origem = models.ForeignKey(TbDimTipoOrigem, models.DO_NOTHING, db_column='co_dim_cds_tipo_origem', blank=True, null=True)
#     co_fat_cidadao_pec = models.ForeignKey(TbFatCidadaoPec, models.DO_NOTHING, db_column='co_fat_cidadao_pec', blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     co_dim_tipo_glicemia = models.ForeignKey(TbDimTipoGlicemia, models.DO_NOTHING, db_column='co_dim_tipo_glicemia', blank=True, null=True)
#     nu_medicao_pressao_arterial = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_temperatura = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_glicemia = models.CharField(max_length=20, blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#     co_uuid_origem_fcd = models.CharField(max_length=44, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_fat_visita_domiciliar'
#
#
# class TbFichaZikaTipoExame(models.Model):
#     co_ficha_zika_tipo_exame = models.BigIntegerField(primary_key=True)
#     no_ficha_zika_tipo_exame = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_ficha_zika_tipo_exame'
#
#
# class TbFormaFarmaceutica(models.Model):
#     co_forma_farmaceutica = models.BigIntegerField(primary_key=True)
#     no_forma_farmaceutica = models.CharField(max_length=255)
#     no_forma_farmaceutica_filtro = models.CharField(unique=True, max_length=255)
#     st_ativo = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_forma_farmaceutica'
#
#
# class TbGestorEstadual(models.Model):
#     co_ator_papel = models.OneToOneField(TbAtorPapel, models.DO_NOTHING, db_column='co_ator_papel', primary_key=True)
#     co_uf = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_gestor_estadual'
#
#
# class TbGestorMunicipal(models.Model):
#     co_ator_papel = models.OneToOneField(TbAtorPapel, models.DO_NOTHING, db_column='co_ator_papel', primary_key=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_gestor_municipal'
#
#
# class TbGravidade(models.Model):
#     co_gravidade = models.BigIntegerField(primary_key=True)
#     no_gravidade = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_gravidade'
#
#
# class TbGrupoAlvoVacinacao(models.Model):
#     co_grupo_alvo_vacinacao = models.BigIntegerField(primary_key=True)
#     no_grupo_alvo_vacinacao = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_grupo_alvo_vacinacao'
#
#
# class TbGrupoAtendimento(models.Model):
#     co_grupo_atendimento = models.BigIntegerField(primary_key=True)
#     no_grupo_atendimento = models.CharField(max_length=100)
#     no_grupo_atendimento_filtro = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_grupo_atendimento'
#
#
# class TbGrupoAtivCol(models.Model):
#     co_seq_grupo_ativ_col = models.BigIntegerField(primary_key=True)
#     co_unico_grupo = models.CharField(unique=True, max_length=96)
#     no_grupo = models.CharField(max_length=255, blank=True, null=True)
#     sg_grupo = models.CharField(max_length=255, blank=True, null=True)
#     tp_grupo = models.CharField(max_length=32, blank=True, null=True)
#     co_cor_grupo = models.IntegerField(blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     dt_ultima_atualizacao = models.DateTimeField(blank=True, null=True)
#     dt_ultima_atividade = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_grupo_ativ_col'
#
#
# class TbGrupoCondicaoSaude(models.Model):
#     co_seq_grupo_condicao_saude = models.BigIntegerField(primary_key=True)
#     no_grupo = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_grupo_condicao_saude'
#
#
# class TbGrupoEspecialidade(models.Model):
#     co_grupo_especialidade = models.BigIntegerField(primary_key=True)
#     no_grupo_especialidade = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_grupo_especialidade'
#
#
# class TbGrupoExame(models.Model):
#     co_seq_grupo_exame = models.BigIntegerField(primary_key=True)
#     no_grupo_exame = models.CharField(max_length=255)
#     nu_idade_minima = models.IntegerField()
#     nu_idade_maxima = models.IntegerField()
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade')
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_grupo_exame'
#
#
# class TbHistoricoCabecalho(models.Model):
#     co_seq_historico_cabecalho = models.BigIntegerField(primary_key=True)
#     co_unico_registro = models.CharField(max_length=255, blank=True, null=True)
#     nu_cpf_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     co_unico_cidadao_prontuario = models.CharField(max_length=96, blank=True, null=True)
#     nu_cns_prof = models.CharField(max_length=15, blank=True, null=True)
#     co_cbo = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes_unid = models.CharField(max_length=50, blank=True, null=True)
#     co_turno = models.BigIntegerField(blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     dt_atendimento = models.DateTimeField(blank=True, null=True)
#     co_tipo_atendimento = models.BigIntegerField(blank=True, null=True)
#     co_tipo_apresentacao = models.BigIntegerField(blank=True, null=True)
#     co_subtipo_atendimento = models.BigIntegerField(blank=True, null=True)
#     co_tipo_consulta = models.BigIntegerField(blank=True, null=True)
#     co_origem_atendimento = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_historico_cabecalho'
#
#
# class TbHistoricoUnificacao(models.Model):
#     co_seq_historico_unificacao = models.BigIntegerField(primary_key=True)
#     dt_unificacao = models.DateTimeField(blank=True, null=True)
#     co_cidadao_grupo = models.ForeignKey(TbCidadaoGrupo, models.DO_NOTHING, db_column='co_cidadao_grupo')
#     co_prof = models.ForeignKey('TbProf', models.DO_NOTHING, db_column='co_prof', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_historico_unificacao'
#
#
# class TbImportacaoCnes(models.Model):
#     co_seq_importacao_cnes = models.BigIntegerField(primary_key=True)
#     dt_relatorio = models.DateTimeField()
#     co_ator_papel_bkp = models.BigIntegerField(blank=True, null=True)
#     co_prof = models.ForeignKey('TbProf', models.DO_NOTHING, db_column='co_prof', blank=True, null=True)
#     nu_unidades_novas = models.BigIntegerField(blank=True, null=True)
#     nu_unidades_atualizadas = models.BigIntegerField(blank=True, null=True)
#     nu_equipes_novas = models.BigIntegerField(blank=True, null=True)
#     nu_equipes_atualizadas = models.BigIntegerField(blank=True, null=True)
#     nu_profissionais_novos = models.BigIntegerField(blank=True, null=True)
#     nu_profissionais_atualizados = models.BigIntegerField(blank=True, null=True)
#     nu_lotacoes_novas = models.BigIntegerField(blank=True, null=True)
#     nu_lotacoes_atualizadas = models.BigIntegerField(blank=True, null=True)
#     co_processo = models.ForeignKey('TbProcesso', models.DO_NOTHING, db_column='co_processo', blank=True, null=True)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade', blank=True, null=True)
#     ds_detalhes = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_importacao_cnes'
#
#
# class TbImunobiologico(models.Model):
#     co_imunobiologico = models.BigIntegerField(primary_key=True)
#     sg_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     no_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     no_filtro_imunobiologico = models.CharField(max_length=255, blank=True, null=True)
#     co_classe_imunobiologico = models.ForeignKey(TbClasseImunobiologico, models.DO_NOTHING, db_column='co_classe_imunobiologico', blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_imunobiologico'
#
#
# class TbImunobiologicoFabricante(models.Model):
#     co_seq_imunobiologico_fabrcnt = models.BigIntegerField(primary_key=True)
#     no_fabricante = models.CharField(max_length=255, blank=True, null=True)
#     no_fabricante_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_imunobiologico_fabricante'
#
#
# class TbImunobiologicoLote(models.Model):
#     co_seq_imunobiologico_lote = models.BigIntegerField(primary_key=True)
#     co_imunobiologico = models.ForeignKey(TbImunobiologico, models.DO_NOTHING, db_column='co_imunobiologico', blank=True, null=True)
#     ds_lote = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_filtro = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_fabricante_filtro = models.CharField(max_length=255, blank=True, null=True)
#     dt_validade = models.DateField(blank=True, null=True)
#     co_imunobiologico_fabricante = models.BigIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField()
#     co_unidade_saude = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_imunobiologico_lote'
#
#
# class TbInep(models.Model):
#     co_inep = models.BigIntegerField(primary_key=True)
#     ds_inep = models.CharField(max_length=8)
#     co_localidade = models.ForeignKey('TbLocalidade', models.DO_NOTHING, db_column='co_localidade')
#     no_estabelecimento = models.CharField(max_length=200)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_inep'
#         unique_together = (('ds_inep', 'co_localidade'),)
#
#
# class TbIntegracaoHorus(models.Model):
#     co_unidade_saude = models.OneToOneField('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude', primary_key=True)
#     dt_habilitar_integracao = models.DateTimeField(blank=True, null=True)
#     st_ativo = models.IntegerField()
#     tp_erro_teste_horus = models.CharField(max_length=50, blank=True, null=True)
#     co_unidade_saude_padrao = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude_padrao', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_integracao_horus'
#
#
# class TbJustificativaAgenda(models.Model):
#     co_seq_justificativa_agendamnt = models.BigIntegerField(primary_key=True)
#     co_agendamento = models.ForeignKey(TbAgendado, models.DO_NOTHING, db_column='co_agendamento')
#     co_lotacao_justificativa = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao_justificativa', blank=True, null=True)
#     ds_justificativa = models.CharField(max_length=2000, blank=True, null=True)
#     dt_justificativa = models.DateTimeField()
#     co_origem_justificativa = models.ForeignKey('TbOrigem', models.DO_NOTHING, db_column='co_origem_justificativa', blank=True, null=True)
#     ds_opcao_justificativa = models.CharField(max_length=44, blank=True, null=True)
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_justificativa_agenda'
#
#
# class TbJustificativaProntuario(models.Model):
#     co_seq_justificativa_prontuar = models.BigIntegerField(primary_key=True)
#     dt_acesso_prontuario = models.DateTimeField()
#     ds_justificativa = models.CharField(max_length=1000)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario')
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_justificativa_prontuario'
#
#
# class TbJustificativaStatusCiddao(models.Model):
#     co_seq_justifica_inativ_cidada = models.BigIntegerField(primary_key=True)
#     dt_justificativa = models.DateTimeField()
#     ds_justificativa = models.CharField(max_length=1000)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     co_cidadao = models.ForeignKey(TbCidadao, models.DO_NOTHING, db_column='co_cidadao')
#     st_cidadao = models.IntegerField(blank=True, null=True)
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_justificativa_status_ciddao'
#
#
# class TbLembrete(models.Model):
#     co_seq_lembrete = models.BigIntegerField(primary_key=True)
#     dt_prontuario_lembrete = models.DateTimeField(blank=True, null=True)
#     ds_lembrete = models.TextField(blank=True, null=True)
#     st_desativado = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     co_ultimo_lembrete_evolucao = models.ForeignKey('TbLembreteEvolucao', models.DO_NOTHING, db_column='co_ultimo_lembrete_evolucao', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lembrete'
#
#
# class TbLembreteEvolucao(models.Model):
#     co_seq_lembrete_evolucao = models.BigIntegerField(primary_key=True)
#     ds_lembrete = models.TextField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_lotacao = models.ForeignKey('TbLotacao', models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     dt_prontuario_lembrete = models.DateTimeField(blank=True, null=True)
#     co_visibilidade_lembrete = models.ForeignKey('TbVisibilidadeLembrete', models.DO_NOTHING, db_column='co_visibilidade_lembrete', blank=True, null=True)
#     co_lembrete = models.ForeignKey(TbLembrete, models.DO_NOTHING, db_column='co_lembrete', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lembrete_evolucao'
#
#
# class TbListaMedicamento(models.Model):
#     co_lista_medicamento = models.BigIntegerField(primary_key=True)
#     no_lista_medicamento = models.CharField(max_length=100, blank=True, null=True)
#     tp_receita = models.ForeignKey('TbTipoReceita', models.DO_NOTHING, db_column='tp_receita', blank=True, null=True)
#     nu_dias_validade = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lista_medicamento'
#
#
# class TbLocalAplVacina(models.Model):
#     co_local_apl_vacina = models.BigIntegerField(primary_key=True)
#     no_local_apl_vacina = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_local_apl_vacina'
#
#
# class TbLocalAtend(models.Model):
#     co_local_atend = models.BigIntegerField(primary_key=True)
#     no_local_atend = models.CharField(max_length=255, blank=True, null=True)
#     no_local_atend_filtro = models.CharField(max_length=100, blank=True, null=True)
#     st_local_cds = models.IntegerField(blank=True, null=True)
#     st_local_ad = models.IntegerField(blank=True, null=True)
#     ds_local_atend_exibicao = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_local_atend'


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


# class TbLogradouro(models.Model):
#     co_logradouro = models.BigIntegerField(primary_key=True)
#     nu_dne = models.CharField(max_length=8)
#     no_preposicao = models.CharField(max_length=6, blank=True, null=True)
#     no_logradouro = models.CharField(max_length=72)
#     nu_cep = models.CharField(max_length=8)
#     nu_inicial_trecho = models.CharField(max_length=22, blank=True, null=True)
#     nu_final_trecho = models.CharField(max_length=22, blank=True, null=True)
#     tp_logradouro = models.ForeignKey('TbTipoLogradouro', models.DO_NOTHING, db_column='tp_logradouro', blank=True, null=True)
#     co_titulo_patente = models.ForeignKey('TbTituloPatente', models.DO_NOTHING, db_column='co_titulo_patente', blank=True, null=True)
#     tp_paridade = models.ForeignKey('TbTipoParidade', models.DO_NOTHING, db_column='tp_paridade', blank=True, null=True)
#     sg_tipo_registro = models.CharField(max_length=1)
#     no_logradouro_filtro = models.CharField(max_length=150)
#     no_logradouro_exibicao = models.CharField(max_length=150)
#     nu_lote = models.CharField(max_length=22, blank=True, null=True)
#     no_complemento = models.CharField(max_length=72, blank=True, null=True)
#     ds_letra_numero_complemento = models.CharField(max_length=22, blank=True, null=True)
#     co_bairro_dne = models.ForeignKey(TbBairro, models.DO_NOTHING, db_column='co_bairro_dne')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_logradouro'
#
#
# class TbLotacao(models.Model):
#     dt_desativacao_lotacao = models.DateTimeField(blank=True, null=True)
#     co_cbo = models.ForeignKey(TbCbo, models.DO_NOTHING, db_column='co_cbo')
#     co_prof = models.ForeignKey('TbProf', models.DO_NOTHING, db_column='co_prof')
#     co_unidade_saude = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude')
#     co_equipe = models.ForeignKey(TbEquipe, models.DO_NOTHING, db_column='co_equipe', blank=True, null=True)
#     co_ator_papel = models.BigIntegerField(primary_key=True)
#     st_atualiza_perfil = models.IntegerField(blank=True, null=True)
#     st_importada = models.IntegerField(blank=True, null=True)
#     st_agenda_alterada_manual = models.IntegerField(blank=True, null=True)
#     dt_ultima_tentativa_envio = models.DateTimeField(blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     st_ativo_agenda_online = models.IntegerField(blank=True, null=True)
#     ds_ultima_tentativa = models.TextField(blank=True, null=True)
#     co_unico_lotacao = models.CharField(unique=True, max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lotacao'
#
#
# class TbLoteTransp(models.Model):
#     co_seq_lote_transp = models.BigIntegerField(primary_key=True)
#     dt_criacao = models.DateTimeField()
#     co_ibge = models.CharField(max_length=10, blank=True, null=True)
#     st_lote_retransmissao = models.IntegerField(blank=True, null=True)
#     ds_filtro_cnes_ficha = models.CharField(max_length=7, blank=True, null=True)
#     dt_filtro_competencia = models.DateTimeField(blank=True, null=True)
#     dt_filtro_inicio = models.DateTimeField(blank=True, null=True)
#     dt_filtro_fim = models.DateTimeField(blank=True, null=True)
#     dt_ultima_tentativa = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lote_transp'
#
#
# class TbLoteTranspHistoricoExprt(models.Model):
#     co_seq_lote_transp_historc_exp = models.BigIntegerField(primary_key=True)
#     co_lote_transp = models.ForeignKey(TbLoteTransp, models.DO_NOTHING, db_column='co_lote_transp', blank=True, null=True)
#     no_profissional = models.CharField(max_length=250, blank=True, null=True)
#     no_cbo = models.CharField(max_length=255, blank=True, null=True)
#     dt_exportacao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lote_transp_historico_exprt'
#
#
# class TbLoteTranspItem(models.Model):
#     co_seq_lote_transp_item = models.BigIntegerField(primary_key=True)
#     co_lote_transp = models.ForeignKey(TbLoteTransp, models.DO_NOTHING, db_column='co_lote_transp')
#     co_dado_transp = models.ForeignKey(TbDadoTransp, models.DO_NOTHING, db_column='co_dado_transp')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lote_transp_item'
#
#
# class TbLoteTranspItemNodo(models.Model):
#     co_seq_lote_transp_item_nodo = models.BigIntegerField(primary_key=True)
#     co_lote_transp_item = models.ForeignKey(TbLoteTranspItem, models.DO_NOTHING, db_column='co_lote_transp_item')
#     co_nodo = models.ForeignKey('TbNodo', models.DO_NOTHING, db_column='co_nodo')
#     ds_ultima_tentativa = models.TextField(blank=True, null=True)
#     dt_ultima_tentativa = models.DateTimeField(blank=True, null=True)
#     st_enviado = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lote_transp_item_nodo'
#         unique_together = (('co_lote_transp_item', 'co_nodo'),)
#
#
# class TbLoteTranspNodo(models.Model):
#     co_seq_lote_transp_nodo = models.BigIntegerField(primary_key=True)
#     co_lote_transp = models.ForeignKey(TbLoteTransp, models.DO_NOTHING, db_column='co_lote_transp')
#     co_nodo = models.ForeignKey('TbNodo', models.DO_NOTHING, db_column='co_nodo')
#     tp_situacao_lote_transp_nodo = models.ForeignKey('TbSituacaoLoteTranspNodo', models.DO_NOTHING, db_column='tp_situacao_lote_transp_nodo', blank=True, null=True)
#     dt_ultima_tentativa = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_lote_transp_nodo'
#         unique_together = (('co_lote_transp', 'co_nodo'),)
#
#
# class TbMedicamento(models.Model):
#     co_seq_medicamento = models.BigIntegerField(primary_key=True)
#     no_principio_ativo = models.CharField(max_length=400)
#     ds_concentracao = models.CharField(max_length=200, blank=True, null=True)
#     co_forma_farmaceutica = models.ForeignKey(TbFormaFarmaceutica, models.DO_NOTHING, db_column='co_forma_farmaceutica', blank=True, null=True)
#     ds_unidade_fornecimento = models.CharField(max_length=200)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_medicamento'
#
#
# class TbMedicamentoCatmat(models.Model):
#     co_medicamento_catmat = models.BigIntegerField(primary_key=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_principio_ativo = models.ForeignKey('TbPrincipioAtivo', models.DO_NOTHING, db_column='co_principio_ativo')
#     co_unidade_fornecimento = models.ForeignKey('TbUnidadeMedida', models.DO_NOTHING, db_column='co_unidade_fornecimento')
#     co_catmat = models.CharField(max_length=20)
#     ds_volume = models.CharField(max_length=100, blank=True, null=True)
#     co_medicamento = models.OneToOneField(TbMedicamento, models.DO_NOTHING, db_column='co_medicamento')
#     nu_frequencia_instalacao = models.IntegerField(blank=True, null=True)
#     co_rename = models.CharField(max_length=28, blank=True, null=True)
#     no_medicamento_filtro = models.CharField(max_length=600, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_medicamento_catmat'
#
#
# class TbMedicamentoUsoContinuo(models.Model):
#     co_seq_medicament_uso_continuo = models.BigIntegerField(primary_key=True)
#     co_medicamento = models.ForeignKey(TbMedicamento, models.DO_NOTHING, db_column='co_medicamento', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     co_ultima_receita_medicamento = models.ForeignKey('TbReceitaMedicamento', models.DO_NOTHING, db_column='co_ultima_receita_medicamento', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_medicamento_uso_continuo'
#         unique_together = (('co_medicamento', 'co_prontuario'),)
#
#
# class TbMedicao(models.Model):
#     co_seq_medicao = models.BigIntegerField(primary_key=True)
#     dt_medicao = models.DateTimeField()
#     tp_glicemia = models.ForeignKey('TbTipoGlicemia', models.DO_NOTHING, db_column='tp_glicemia', blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof')
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     nu_medicao_peso = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_altura = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_frequencia_cardiaca = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_pressao_arterial = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_perimetro_cefalico = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_frequnca_resprtria = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_temperatura = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_saturacao_o2 = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_glicemia = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_imc = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_altura_uterina = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_batimnto_cardco_ftl = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_vacinacao_em_dia = models.CharField(max_length=20, blank=True, null=True)
#     nu_perimetro_panturrilha = models.CharField(max_length=20, blank=True, null=True)
#     st_medicao_anterior = models.IntegerField(blank=True, null=True)
#     nu_medicao_circunf_abdominal = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_apgar_um = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_apgar_cinco = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_apgar_dez = models.CharField(max_length=20, blank=True, null=True)
#     tp_gravidez = models.ForeignKey('TbTipoGravidez', models.DO_NOTHING, db_column='tp_gravidez', blank=True, null=True)
#     tp_parto = models.ForeignKey('TbTipoParto', models.DO_NOTHING, db_column='tp_parto', blank=True, null=True)
#     nu_medicao_ig_semanas = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_ig_dias = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_medicao'
#
#
# class TbMemoria(models.Model):
#     co_memoria = models.CharField(primary_key=True, max_length=50)
#     ds_memoria = models.BinaryField()
#     dt_expiracao = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_memoria'
#
#
# class TbMes(models.Model):
#     co_mes = models.BigIntegerField(primary_key=True)
#     no_mes = models.CharField(max_length=25)
#     no_identificador = models.CharField(max_length=25)
#     sg_mes = models.CharField(max_length=5)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_mes'
#
#
# class TbMigracao(models.Model):
#     id = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     filename = models.CharField(max_length=255)
#     dateexecuted = models.DateTimeField()
#     orderexecuted = models.IntegerField()
#     exectype = models.CharField(max_length=10)
#     md5sum = models.CharField(max_length=35, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     comments = models.CharField(max_length=255, blank=True, null=True)
#     tag = models.CharField(max_length=255, blank=True, null=True)
#     liquibase = models.CharField(max_length=20, blank=True, null=True)
#     contexts = models.CharField(max_length=255, blank=True, null=True)
#     labels = models.CharField(max_length=255, blank=True, null=True)
#     deployment_id = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_migracao'
#
#
# class TbMigracaoEstrutura(models.Model):
#     co_migracao_estrutura = models.CharField(max_length=255)
#     no_autor_migracao = models.CharField(max_length=255)
#     no_arquivo_migracao = models.CharField(max_length=255)
#     dt_execucao = models.DateTimeField()
#     nu_ordem_execucao = models.DecimalField(max_digits=38, decimal_places=0)
#     no_tipo_execucao = models.CharField(max_length=10)
#     no_md5_soma_verificacao = models.CharField(max_length=35, blank=True, null=True)
#     no_descricao = models.CharField(max_length=255, blank=True, null=True)
#     ds_comentario = models.CharField(max_length=255, blank=True, null=True)
#     no_etiqueta = models.CharField(max_length=255, blank=True, null=True)
#     no_versao_liquibase = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_migracao_estrutura'
#
#
# class TbMigracaoTrava(models.Model):
#     id = models.IntegerField(primary_key=True)
#     locked = models.BooleanField()
#     lockgranted = models.DateTimeField(blank=True, null=True)
#     lockedby = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_migracao_trava'
#
#
# class TbMotivoReserva(models.Model):
#     co_motivo_reserva = models.BigIntegerField(primary_key=True)
#     no_motivo_reserva = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_motivo_reserva'
#
#
# class TbNacionalidade(models.Model):
#     co_nacionalidade = models.BigIntegerField(primary_key=True)
#     no_nacionalidade = models.CharField(max_length=15)
#     no_identificador = models.CharField(max_length=15)
#     co_nacionalidade_cadsus = models.CharField(max_length=1, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_nacionalidade'
#
#
# class TbNeuroAlterFenot(models.Model):
#     co_seq_neuro_alter_fenot = models.BigIntegerField(primary_key=True)
#     co_alter_fenot_detalhe = models.ForeignKey('TbNeuroAlterFenotDetalhe', models.DO_NOTHING, db_column='co_alter_fenot_detalhe')
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario')
#     co_ultimo_alter_fenot_evolucao = models.ForeignKey('TbNeuroAlterFenotEvolucao', models.DO_NOTHING, db_column='co_ultimo_alter_fenot_evolucao')
#     co_unico_alter_fenot = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_alter_fenot'
#         unique_together = (('co_prontuario', 'co_alter_fenot_detalhe'),)
#
#
# class TbNeuroAlterFenotDetalhe(models.Model):
#     co_neuro_alter_fenot_detalhe = models.BigIntegerField(primary_key=True)
#     ds_alter_fenot = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_alter_fenot_detalhe'
#
#
# class TbNeuroAlterFenotEvolucao(models.Model):
#     co_seq_neuro_alter_fenot_evol = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof')
#     co_alter_fenot_detalhe = models.ForeignKey(TbNeuroAlterFenotDetalhe, models.DO_NOTHING, db_column='co_alter_fenot_detalhe')
#     st_avaliado = models.CharField(max_length=32)
#     co_unico_neuro_alter_fenot = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_alter_fenot_evolucao'
#         unique_together = (('co_atend_prof', 'co_alter_fenot_detalhe'),)
#
#
# class TbNeuroFaixaEtaria(models.Model):
#     co_neuro_faixa_etaria = models.BigIntegerField(primary_key=True)
#     nu_dias_inicio = models.IntegerField(blank=True, null=True)
#     nu_dias_fim = models.IntegerField(blank=True, null=True)
#     ds_faixa_etaria = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_faixa_etaria'
#
#
# class TbNeuroFatorRisco(models.Model):
#     co_seq_neuro_fator_risco = models.BigIntegerField(primary_key=True)
#     co_fator_risco_detalhe = models.ForeignKey('TbNeuroFatorRiscoDetalhe', models.DO_NOTHING, db_column='co_fator_risco_detalhe')
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario')
#     co_ultimo_fator_risco_evolucao = models.ForeignKey('TbNeuroFatorRiscoEvolucao', models.DO_NOTHING, db_column='co_ultimo_fator_risco_evolucao')
#     co_unico_fator_risco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_fator_risco'
#         unique_together = (('co_prontuario', 'co_fator_risco_detalhe'),)
#
#
# class TbNeuroFatorRiscoDetalhe(models.Model):
#     co_neuro_fator_risco_detalhe = models.BigIntegerField(primary_key=True)
#     ds_fator_risco = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_fator_risco_detalhe'
#
#
# class TbNeuroFatorRiscoEvolucao(models.Model):
#     co_seq_neuro_fator_risco_evol = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof')
#     co_fator_risco_detalhe = models.ForeignKey(TbNeuroFatorRiscoDetalhe, models.DO_NOTHING, db_column='co_fator_risco_detalhe')
#     st_avaliado = models.CharField(max_length=32)
#     co_unico_neuro_fator_risco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_fator_risco_evolucao'
#         unique_together = (('co_atend_prof', 'co_fator_risco_detalhe'),)
#
#
# class TbNeuroMarco(models.Model):
#     co_seq_neuro_marco = models.BigIntegerField(primary_key=True)
#     co_marco_detalhe = models.ForeignKey('TbNeuroMarcoDetalhe', models.DO_NOTHING, db_column='co_marco_detalhe')
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario')
#     co_ultimo_marco_evolucao = models.ForeignKey('TbNeuroMarcoEvolucao', models.DO_NOTHING, db_column='co_ultimo_marco_evolucao')
#     co_unico_marco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_marco'
#         unique_together = (('co_prontuario', 'co_marco_detalhe'),)
#
#
# class TbNeuroMarcoDetalhe(models.Model):
#     co_neuro_marco_detalhe = models.BigIntegerField(primary_key=True)
#     ds_titulo = models.CharField(max_length=255, blank=True, null=True)
#     ds_marco = models.CharField(max_length=1100, blank=True, null=True)
#     co_faixa_etaria = models.ForeignKey(TbNeuroFaixaEtaria, models.DO_NOTHING, db_column='co_faixa_etaria', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_marco_detalhe'
#
#
# class TbNeuroMarcoEvolucao(models.Model):
#     co_seq_neuro_marco_evolucao = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof')
#     co_marco_detalhe = models.ForeignKey(TbNeuroMarcoDetalhe, models.DO_NOTHING, db_column='co_marco_detalhe')
#     st_avaliado = models.CharField(max_length=32)
#     nu_anos_idade_registro = models.IntegerField(blank=True, null=True)
#     nu_meses_idade_registro = models.IntegerField(blank=True, null=True)
#     co_unico_neuro_marco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_neuro_marco_evolucao'
#         unique_together = (('co_atend_prof', 'co_marco_detalhe'),)
#
#
# class TbNodo(models.Model):
#     co_nodo = models.BigIntegerField(primary_key=True)
#     no_servidor = models.CharField(max_length=60, blank=True, null=True)
#     ds_nome = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_conexao = models.IntegerField(blank=True, null=True)
#     dt_testeconexao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_nodo'
#
#
# class TbOdontograma(models.Model):
#     co_seq_odontograma = models.BigIntegerField(primary_key=True)
#     co_atend_prof_odonto = models.ForeignKey(TbAtendProfOdonto, models.DO_NOTHING, db_column='co_atend_prof_odonto', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     st_protese_total_superior = models.IntegerField(blank=True, null=True)
#     st_protese_total_inferior = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_odontograma'
#
#
# class TbOrientacao(models.Model):
#     co_seq_orientacao = models.BigIntegerField(primary_key=True)
#     ds_orientacao = models.TextField()
#     st_orientacao_finalizada = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof')
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_orientacao'
#
#
# class TbOrigem(models.Model):
#     co_origem = models.BigIntegerField(primary_key=True)
#     ds_origem = models.CharField(max_length=30)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_origem'


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


# class TbParteBucal(models.Model):
#     co_parte_bucal = models.BigIntegerField(primary_key=True)
#     tp_parte_bucal = models.CharField(max_length=60, blank=True, null=True)
#     ds_parte_bucal = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_parte_bucal'
#
#
# class TbParteBucalProced(models.Model):
#     co_parte_bucal_proced = models.BigIntegerField(primary_key=True)
#     co_proced = models.ForeignKey('TbProced', models.DO_NOTHING, db_column='co_proced', blank=True, null=True)
#     tp_parte_bucal = models.ForeignKey('TbTipoParteBucal', models.DO_NOTHING, db_column='tp_parte_bucal', blank=True, null=True)
#     nu_dente = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_parte_bucal_proced'
#
#
# class TbPerfil(models.Model):
#     co_seq_perfil = models.BigIntegerField(primary_key=True)
#     no_perfil = models.CharField(max_length=100)
#     no_perfil_filtro = models.CharField(max_length=50)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.ForeignKey(TbLocalidade, models.DO_NOTHING, db_column='co_localidade', blank=True, null=True)
#     no_perfil_padrao = models.CharField(max_length=100, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     no_tipo_perfil = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_perfil'
#
#
# class TbPerfilRecurso(models.Model):
#     co_seq_perfil_recurso = models.BigIntegerField(primary_key=True)
#     co_perfil = models.ForeignKey(TbPerfil, models.DO_NOTHING, db_column='co_perfil')
#     no_recurso = models.CharField(max_length=400)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_perfil_recurso'
#
#
# class TbPergunta(models.Model):
#     co_seq_pergunta = models.BigIntegerField(primary_key=True)
#     ds_local = models.CharField(max_length=10, blank=True, null=True)
#     ds_pergunta = models.CharField(max_length=255)
#     co_pergunta_pai = models.ForeignKey('self', models.DO_NOTHING, db_column='co_pergunta_pai', blank=True, null=True)
#     co_contexto_pergunta = models.ForeignKey(TbContextoPergunta, models.DO_NOTHING, db_column='co_contexto_pergunta')
#     tp_pergunta = models.ForeignKey('TbTipoPergunta', models.DO_NOTHING, db_column='tp_pergunta')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_pergunta'
#
#
# class TbPerguntaDetalhe(models.Model):
#     co_pergunta_detalhe = models.BigIntegerField(primary_key=True)
#     co_pergunta = models.ForeignKey(TbPergunta, models.DO_NOTHING, db_column='co_pergunta')
#     ds_local = models.CharField(max_length=10, blank=True, null=True)
#     ds_pergunta_detalhe = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_pergunta_detalhe'
#
#
# class TbPeriodo(models.Model):
#     co_periodo = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_periodo'
#
#
# class TbPessoaFisicaImagem(models.Model):
#     co_seq_pessoa_fisica_imagem = models.BigIntegerField(primary_key=True)
#     im_icone = models.BinaryField(blank=True, null=True)
#     im_conteudo = models.BinaryField(blank=True, null=True)
#     co_cidadao = models.ForeignKey(TbCidadao, models.DO_NOTHING, db_column='co_cidadao', blank=True, null=True)
#     no_tipo_imagem = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_pessoa_fisica_imagem'
#
#
# class TbPovoComunidadeTradicional(models.Model):
#     co_povo_comunidade_tradicional = models.BigIntegerField(primary_key=True)
#     no_povo_comunidade_tradicional = models.CharField(max_length=255)
#     no_povo_comunidade_trad_filtro = models.CharField(unique=True, max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_povo_comunidade_tradicional'
#
#
# class TbPreNatal(models.Model):
#     co_seq_pre_natal = models.BigIntegerField(primary_key=True)
#     co_problema = models.ForeignKey('TbProblema', models.DO_NOTHING, db_column='co_problema', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     tp_gravidez = models.ForeignKey('TbTipoGravidez', models.DO_NOTHING, db_column='tp_gravidez', blank=True, null=True)
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     dt_desfecho = models.DateTimeField(blank=True, null=True)
#     st_gravidez_planejada = models.IntegerField(blank=True, null=True)
#     st_alto_risco = models.IntegerField(blank=True, null=True)
#     co_unico_pre_natal = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_pre_natal'
#
#
# class TbPrincipioAtivo(models.Model):
#     co_principio_ativo = models.BigIntegerField(primary_key=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     no_principio_ativo_filtro = models.CharField(max_length=200)
#     no_principio_ativo = models.CharField(max_length=200)
#     co_lista_medicamento = models.ForeignKey(TbListaMedicamento, models.DO_NOTHING, db_column='co_lista_medicamento', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_principio_ativo'
#
#
# class TbProblema(models.Model):
#     co_seq_problema = models.BigIntegerField(primary_key=True)
#     dt_registro = models.DateTimeField(blank=True, null=True)
#     ds_outro = models.CharField(max_length=255, blank=True, null=True)
#     ds_problema_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_ciap = models.ForeignKey(TbCiap, models.DO_NOTHING, db_column='co_ciap', blank=True, null=True)
#     co_cid10 = models.ForeignKey(TbCid10, models.DO_NOTHING, db_column='co_cid10', blank=True, null=True)
#     co_ultimo_problema_evolucao = models.ForeignKey('TbProblemaEvolucao', models.DO_NOTHING, db_column='co_ultimo_problema_evolucao', blank=True, null=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     co_unico_problema = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_problema'
#
#
# class TbProblemaEvolucao(models.Model):
#     co_seq_problema_evolucao = models.BigIntegerField(primary_key=True)
#     ds_observacao = models.CharField(max_length=255, blank=True, null=True)
#     co_situacao_problema = models.ForeignKey('TbSituacaoProblema', models.DO_NOTHING, db_column='co_situacao_problema')
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     co_unico_problema = models.BigIntegerField(blank=True, null=True)
#     co_mes_inicio = models.ForeignKey(TbMes, models.DO_NOTHING, db_column='co_mes_inicio', blank=True, null=True)
#     co_mes_fim = models.ForeignKey(TbMes, models.DO_NOTHING, db_column='co_mes_fim', blank=True, null=True)
#     qt_mes_inicio = models.IntegerField(blank=True, null=True)
#     qt_mes_fim = models.IntegerField(blank=True, null=True)
#     qt_ano_inicio = models.IntegerField(blank=True, null=True)
#     qt_ano_fim = models.IntegerField(blank=True, null=True)
#     nu_dia_inicio = models.IntegerField(blank=True, null=True)
#     nu_dia_fim = models.IntegerField(blank=True, null=True)
#     nu_ano_inicio = models.IntegerField(blank=True, null=True)
#     nu_ano_fim = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_problema_evolucao'
#
#
# class TbProced(models.Model):
#     co_seq_proced = models.BigIntegerField(primary_key=True)
#     no_proced = models.CharField(max_length=260)
#     no_proced_filtro = models.CharField(max_length=260)
#     nu_idade_minima = models.IntegerField()
#     nu_idade_maxima = models.IntegerField()
#     co_proced = models.CharField(max_length=255)
#     dt_competencia = models.CharField(max_length=6)
#     st_ativo = models.IntegerField()
#     st_masculino = models.IntegerField(blank=True, null=True)
#     st_feminino = models.IntegerField(blank=True, null=True)
#     co_complexidade = models.BigIntegerField(blank=True, null=True)
#     co_proced_grupo = models.BigIntegerField(blank=True, null=True)
#     co_proced_subgrupo = models.BigIntegerField(blank=True, null=True)
#     co_proced_forma_organizacional = models.BigIntegerField(blank=True, null=True)
#     st_filtro_padrao = models.IntegerField(blank=True, null=True)
#     st_proced_padrao_dab = models.IntegerField(blank=True, null=True)
#     st_proced_dab = models.IntegerField(blank=True, null=True)
#     co_proced_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_proced_ref_sigtap = models.BigIntegerField(blank=True, null=True)
#     st_idade_aplicavel = models.IntegerField()
#     tp_proced = models.CharField(max_length=30, blank=True, null=True)
#     st_plano = models.IntegerField(blank=True, null=True)
#     st_exame = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced'
#
#
# class TbProcedAutomatico(models.Model):
#     co_seq_proced_automatico = models.BigIntegerField(primary_key=True)
#     co_proced = models.ForeignKey(RlProcedCbo, models.DO_NOTHING, db_column='co_proced')
#     co_cbo = models.BigIntegerField()
#     st_consulta_agendada = models.IntegerField(blank=True, null=True)
#     st_atend_odonto = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_automatico'
#
#
# class TbProcedExameEspecifico(models.Model):
#     co_proced_exame_especifico = models.BigIntegerField(primary_key=True)
#     no_proced_exame_especifico = models.CharField(max_length=50)
#     no_identificador = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_exame_especifico'
#
#
# class TbProcedFiltro(models.Model):
#     co_proced = models.OneToOneField(TbProced, models.DO_NOTHING, db_column='co_proced', primary_key=True)
#     st_proced = models.IntegerField()
#     st_proced_exame = models.IntegerField()
#     st_proced_bucal = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_filtro'
#
#
# class TbProcedFormaOrganizacional(models.Model):
#     co_proced_forma_organizacional = models.BigIntegerField(primary_key=True)
#     co_proced_grupo = models.ForeignKey('TbProcedGrupo', models.DO_NOTHING, db_column='co_proced_grupo')
#     co_proced_subgrupo = models.ForeignKey('TbProcedSubgrupo', models.DO_NOTHING, db_column='co_proced_subgrupo')
#     no_proced_forma_organizacional = models.CharField(max_length=255)
#     dt_competencia = models.CharField(max_length=6)
#     nu_ms = models.CharField(max_length=2)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_forma_organizacional'
#
#
# class TbProcedGrupo(models.Model):
#     co_proced_grupo = models.BigIntegerField(primary_key=True)
#     no_proced_grupo = models.CharField(max_length=100)
#     dt_competencia = models.CharField(max_length=6)
#     nu_ms = models.CharField(max_length=2)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_grupo'
#
#
# class TbProcedNomePopular(models.Model):
#     co_seq_proced_nome_popular = models.BigIntegerField(primary_key=True)
#     co_proced = models.ForeignKey(TbProced, models.DO_NOTHING, db_column='co_proced', blank=True, null=True)
#     no_popular = models.CharField(max_length=255, blank=True, null=True)
#     no_sinonimos = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_nome_popular'
#
#
# class TbProcedSolicitado(models.Model):
#     co_seq_proced_solicitado = models.BigIntegerField(primary_key=True)
#     co_prontuario = models.ForeignKey('TbProntuario', models.DO_NOTHING, db_column='co_prontuario')
#     co_proced = models.ForeignKey(TbProced, models.DO_NOTHING, db_column='co_proced')
#     ds_orientacao = models.CharField(max_length=4000, blank=True, null=True)
#     co_lotacao_solicitante = models.ForeignKey(TbLotacao, models.DO_NOTHING, db_column='co_lotacao_solicitante')
#     dt_solicitacao = models.DateTimeField()
#     co_lotacao_executante = models.ForeignKey(TbLotacao, models.DO_NOTHING, db_column='co_lotacao_executante', blank=True, null=True)
#     dt_execucao = models.DateTimeField(blank=True, null=True)
#     ds_observacao_execucao = models.CharField(max_length=4000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_solicitado'
#
#
# class TbProcedSubgrupo(models.Model):
#     co_proced_subgrupo = models.BigIntegerField(primary_key=True)
#     co_proced_grupo = models.ForeignKey(TbProcedGrupo, models.DO_NOTHING, db_column='co_proced_grupo')
#     no_proced_subgrupo = models.CharField(max_length=100)
#     dt_competencia = models.CharField(max_length=6)
#     nu_ms = models.CharField(max_length=2)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_proced_subgrupo'
#
#
# class TbProcessamentoDomCid(models.Model):
#     co_seq_processamento_dom_cid = models.BigIntegerField(primary_key=True)
#     co_dado_transp = models.ForeignKey(TbDadoTransp, models.DO_NOTHING, db_column='co_dado_transp')
#     dt_processamento = models.DateField(blank=True, null=True)
#     ds_mensagem = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_processamento_dom_cid'
#
#
# class TbProcessamentoHistCds(models.Model):
#     co_seq_processamento_hist_cds = models.BigIntegerField(primary_key=True)
#     co_dado_transp = models.ForeignKey(TbDadoTransp, models.DO_NOTHING, db_column='co_dado_transp')
#     dt_processamento = models.DateField(blank=True, null=True)
#     ds_mensagem = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_processamento_hist_cds'
#
#
# class TbProcesso(models.Model):
#     co_seq_processo = models.BigIntegerField(primary_key=True)
#     st_processo = models.CharField(max_length=100)
#     dt_inicio = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'tb_processo'
#
#
# class TbProf(models.Model):
#     co_seq_prof = models.BigIntegerField(primary_key=True)
#     nu_conselho_classe = models.CharField(max_length=100, blank=True, null=True)
#     co_uf_emissora_conselho_classe = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf_emissora_conselho_classe', blank=True, null=True)
#     co_conselho_classe = models.ForeignKey(TbConselhoClasse, models.DO_NOTHING, db_column='co_conselho_classe', blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     no_profissional = models.CharField(max_length=500, blank=True, null=True)
#     no_profissional_filtro = models.CharField(max_length=600, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     nu_telefone = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.ForeignKey('TbUf', models.DO_NOTHING, db_column='co_uf', blank=True, null=True)
#     co_localidade_endereco = models.ForeignKey(TbLocalidade, models.DO_NOTHING, db_column='co_localidade_endereco', blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.ForeignKey('TbTipoLogradouro', models.DO_NOTHING, db_column='tp_logradouro', blank=True, null=True)
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario', blank=True, null=True)
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_prof'
#
#
# class TbProfGrupoAtivCol(models.Model):
#     co_seq_prof_grupo = models.BigIntegerField(primary_key=True)
#     no_prof_grupo = models.CharField(max_length=255, blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     co_cbo_2002 = models.CharField(max_length=10, blank=True, null=True)
#     co_unico_prof = models.CharField(unique=True, max_length=40, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_prof_grupo_ativ_col'
#
#
# class TbProntuario(models.Model):
#     co_seq_prontuario = models.BigIntegerField(primary_key=True)
#     co_unico_prontuario = models.CharField(max_length=36)
#     co_unico_cidadao_prontuario = models.CharField(max_length=36)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     co_prontuario_grupo = models.BigIntegerField(blank=True, null=True)
#     co_cidadao = models.OneToOneField(TbCidadao, models.DO_NOTHING, db_column='co_cidadao', blank=True, null=True)
#     st_cidadao_processado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_prontuario'
#
#
# class TbProntuarioGrupoHistorico(models.Model):
#     co_seq_prontuario_grpo_hstrco = models.BigIntegerField(primary_key=True)
#     co_prontuario_grupo = models.ForeignKey(TbProntuario, models.DO_NOTHING, db_column='co_prontuario_grupo', blank=True, null=True)
#     co_prontuario = models.ForeignKey(TbProntuario, models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     dt_unificacao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_prontuario_grupo_historico'
#
#
# class TbProntuarioUnidadeSaude(models.Model):
#     co_seq_prontuario_unidade_saud = models.BigIntegerField(primary_key=True)
#     co_unidade_saude = models.ForeignKey('TbUnidadeSaude', models.DO_NOTHING, db_column='co_unidade_saude')
#     co_cidadao = models.BigIntegerField()
#     nu_prontuario = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_prontuario_unidade_saude'
#
#
# class TbQstAssociacaoPergunta(models.Model):
#     co_qst_associacao_pergunta = models.BigIntegerField(primary_key=True)
#     co_qst_questionario_pergunta = models.ForeignKey('TbQstQuestionarioPergunta', models.DO_NOTHING, db_column='co_qst_questionario_pergunta', blank=True, null=True)
#     co_qst_qst_pergunta_associacao = models.ForeignKey('TbQstQuestionarioPergunta', models.DO_NOTHING, db_column='co_qst_qst_pergunta_associacao', blank=True, null=True)
#     co_opcao_pergunta = models.ForeignKey('TbQstOpcaoPergunta', models.DO_NOTHING, db_column='co_opcao_pergunta', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_associacao_pergunta'
#
#
# class TbQstOpcaoPergunta(models.Model):
#     co_qst_opcao_pergunta = models.BigIntegerField(primary_key=True)
#     co_qst_pergunta = models.ForeignKey('TbQstPergunta', models.DO_NOTHING, db_column='co_qst_pergunta', blank=True, null=True)
#     co_qst_opcao_tipo_pergunta = models.ForeignKey('TbQstOpcaoTipoPergunta', models.DO_NOTHING, db_column='co_qst_opcao_tipo_pergunta', blank=True, null=True)
#     co_qst_orientacao_prof = models.ForeignKey('TbQstOrientacaoProf', models.DO_NOTHING, db_column='co_qst_orientacao_prof', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_opcao_pergunta'
#
#
# class TbQstOpcaoTipoPergunta(models.Model):
#     co_qst_opcao_tipo_pergunta = models.BigIntegerField(primary_key=True)
#     no_qst_opcao_tipo_pergunta = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_opcao_tipo_pergunta'
#
#
# class TbQstOrientacaoProf(models.Model):
#     co_qst_orientacao_prof = models.BigIntegerField(primary_key=True)
#     ds_orientacao_prof = models.CharField(max_length=1000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_orientacao_prof'
#
#
# class TbQstPergunta(models.Model):
#     co_qst_pergunta = models.BigIntegerField(primary_key=True)
#     no_qst_pergunta = models.CharField(max_length=800, blank=True, null=True)
#     tp_opcao_pergunta = models.ForeignKey('TbTipoOpcao', models.DO_NOTHING, db_column='tp_opcao_pergunta', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_pergunta'
#
#
# class TbQstQuestionario(models.Model):
#     co_qst_questionario = models.BigIntegerField(primary_key=True)
#     ds_questionario = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     tp_qst_questionario = models.ForeignKey('TbQstTipoQuestionario', models.DO_NOTHING, db_column='tp_qst_questionario', blank=True, null=True)
#     nu_idade_meses_limite_inferior = models.IntegerField(blank=True, null=True)
#     nu_idade_meses_limite_superior = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_questionario'
#
#
# class TbQstQuestionarioPergunta(models.Model):
#     co_qst_questionario_pergunta = models.BigIntegerField(primary_key=True)
#     ds_ordenacao = models.CharField(max_length=15, blank=True, null=True)
#     co_qst_questionario = models.ForeignKey(TbQstQuestionario, models.DO_NOTHING, db_column='co_qst_questionario', blank=True, null=True)
#     co_qst_pergunta = models.ForeignKey(TbQstPergunta, models.DO_NOTHING, db_column='co_qst_pergunta', blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_questionario_pergunta'
#
#
# class TbQstQuestionarioRespondido(models.Model):
#     co_seq_qst_qst_respondido = models.BigIntegerField(primary_key=True)
#     co_qst_questionario = models.ForeignKey(TbQstQuestionario, models.DO_NOTHING, db_column='co_qst_questionario', blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     dt_respondido = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_questionario_respondido'
#
#
# class TbQstResposta(models.Model):
#     co_seq_qst_resposta = models.BigIntegerField(primary_key=True)
#     co_qst_questionario_respondido = models.ForeignKey(TbQstQuestionarioRespondido, models.DO_NOTHING, db_column='co_qst_questionario_respondido', blank=True, null=True)
#     co_qst_questionario_pergunta = models.ForeignKey(TbQstQuestionarioPergunta, models.DO_NOTHING, db_column='co_qst_questionario_pergunta', blank=True, null=True)
#     tp_qst_resposta = models.ForeignKey('TbQstTipoResposta', models.DO_NOTHING, db_column='tp_qst_resposta', blank=True, null=True)
#     nu_resposta = models.IntegerField(blank=True, null=True)
#     ds_resposta = models.CharField(max_length=800, blank=True, null=True)
#     co_qst_opcao_pergunta = models.ForeignKey(TbQstOpcaoPergunta, models.DO_NOTHING, db_column='co_qst_opcao_pergunta', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_resposta'
#
#
# class TbQstTipoQuestionario(models.Model):
#     co_qst_tipo_questionario = models.IntegerField(primary_key=True)
#     no_qst_tipo_questionario = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_tipo_questionario'
#
#
# class TbQstTipoResposta(models.Model):
#     co_qst_tipo_resposta = models.IntegerField(primary_key=True)
#     no_qst_tipo_resposta = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_qst_tipo_resposta'
#
#
# class TbRacaCor(models.Model):
#     co_raca_cor = models.BigIntegerField(primary_key=True)
#     no_raca_cor = models.CharField(max_length=50)
#     nu_ms = models.CharField(max_length=100, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255)
#     co_raca_cor_cadsus = models.CharField(max_length=3, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_raca_cor'
#
#
# class TbRacionalidadeSaude(models.Model):
#     co_racionalidade_saude = models.BigIntegerField(primary_key=True)
#     no_racionalidade_saude = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_racionalidade_saude'
#
#
# class TbRecebimentoItem(models.Model):
#     co_seq_receb_item = models.BigIntegerField(primary_key=True)
#     co_receb_lote = models.ForeignKey('TbRecebimentoLote', models.DO_NOTHING, db_column='co_receb_lote')
#     st_dado_recebido = models.BigIntegerField(blank=True, null=True)
#     tp_dado_transp = models.BigIntegerField(blank=True, null=True)
#     co_unico_dado_serializado = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes_dado_serializado = models.CharField(max_length=255, blank=True, null=True)
#     nu_versao_dado_serializado = models.CharField(max_length=10, blank=True, null=True)
#     no_arquivo = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_recebimento_item'
#
#
# class TbRecebimentoLote(models.Model):
#     co_seq_receb_lote = models.BigIntegerField(primary_key=True)
#     dt_recebimento = models.DateTimeField(blank=True, null=True)
#     nu_lote_originadora = models.BigIntegerField(blank=True, null=True)
#     no_responsavel_envio = models.CharField(max_length=256, blank=True, null=True)
#     no_responsavel_envio_filtro = models.CharField(max_length=256, blank=True, null=True)
#     nu_identificador_responsavel = models.CharField(max_length=20, blank=True, null=True)
#     tp_origem_dado_recebido = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_recebimento_lote'
#
#
# class TbRecebimentoValidacaoErros(models.Model):
#     co_receb_item = models.BigIntegerField()
#     ds_erro = models.TextField(blank=True, null=True)
#     ds_erro_campo_nao_preenchido = models.TextField(blank=True, null=True)
#     ds_erro_campo_invalido = models.TextField(blank=True, null=True)
#     nu_registro_da_ficha = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
#     co_seq_receb_valid_erro = models.BigIntegerField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_recebimento_validacao_erros'
#
#
# class TbReceitaMedicamento(models.Model):
#     co_seq_receita_medicamento = models.BigIntegerField(primary_key=True)
#     no_posologia = models.CharField(max_length=200, blank=True, null=True)
#     qt_receitada = models.IntegerField(blank=True, null=True)
#     co_aplicacao_medicamento = models.ForeignKey(TbAplicacaoMedicamento, models.DO_NOTHING, db_column='co_aplicacao_medicamento', blank=True, null=True)
#     st_uso_continuo = models.IntegerField()
#     co_medicamento = models.ForeignKey(TbMedicamento, models.DO_NOTHING, db_column='co_medicamento')
#     dt_inicio_tratamento = models.DateField(blank=True, null=True)
#     dt_fim_tratamento = models.DateField(blank=True, null=True)
#     qt_duracao_tratamento = models.IntegerField(blank=True, null=True)
#     ds_dose = models.CharField(max_length=100, blank=True, null=True)
#     tp_frequencia_dose = models.ForeignKey('TbReceitaTipoFrequencia', models.DO_NOTHING, db_column='tp_frequencia_dose', blank=True, null=True)
#     ds_frequencia_dose = models.CharField(max_length=25, blank=True, null=True)
#     st_registro_manual = models.IntegerField(blank=True, null=True)
#     st_dose_unica = models.IntegerField(blank=True, null=True)
#     ds_recomendacao = models.TextField(blank=True, null=True)
#     qt_periodo_frequencia = models.IntegerField(blank=True, null=True)
#     tp_un_medida_tempo_frequencia = models.BigIntegerField(blank=True, null=True)
#     tp_un_medida_tempo_tratamento = models.ForeignKey('TbUnidadeMedidaTempo', models.DO_NOTHING, db_column='tp_un_medida_tempo_tratamento', blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     tp_receita = models.ForeignKey('TbTipoReceita', models.DO_NOTHING, db_column='tp_receita', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_receita_medicamento'
#
#
# class TbReceitaTipoFrequencia(models.Model):
#     co_receita_tipo_frequencia = models.BigIntegerField(primary_key=True)
#     no_tipo_frequencia = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_receita_tipo_frequencia'
#
#
# class TbRecurso(models.Model):
#     co_seq_recurso = models.BigIntegerField(primary_key=True)
#     ds_caminho = models.CharField(max_length=1000)
#     no_recurso = models.CharField(max_length=1000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_recurso'
#
#
# class TbRefreshToken(models.Model):
#     co_token = models.CharField(primary_key=True, max_length=36)
#     no_principal = models.CharField(max_length=100)
#     dt_criacao = models.DateTimeField()
#     dt_expiracao = models.DateTimeField()
#     ds_api_consumer = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_refresh_token'
#
#
# class TbRegistroVacinacao(models.Model):
#     co_seq_registro_vacinacao = models.BigIntegerField(primary_key=True)
#     co_estrategia_vacinacao = models.ForeignKey(TbEstrategiaVacinacao, models.DO_NOTHING, db_column='co_estrategia_vacinacao', blank=True, null=True)
#     co_imunobiologico = models.ForeignKey(TbImunobiologico, models.DO_NOTHING, db_column='co_imunobiologico', blank=True, null=True)
#     co_dose_imunobiologico = models.ForeignKey(TbDoseImunobiologico, models.DO_NOTHING, db_column='co_dose_imunobiologico', blank=True, null=True)
#     co_via_adm_vacina = models.ForeignKey('TbViaAdmVacina', models.DO_NOTHING, db_column='co_via_adm_vacina', blank=True, null=True)
#     co_local_apl_vacina = models.ForeignKey(TbLocalAplVacina, models.DO_NOTHING, db_column='co_local_apl_vacina', blank=True, null=True)
#     co_vacinacao = models.ForeignKey('TbVacinacao', models.DO_NOTHING, db_column='co_vacinacao', blank=True, null=True)
#     co_tipo_registro_vacinacao = models.ForeignKey('TbTipoRegistroVacinacao', models.DO_NOTHING, db_column='co_tipo_registro_vacinacao', blank=True, null=True)
#     st_registro_anterior = models.IntegerField(blank=True, null=True)
#     dt_aprazamento = models.DateField(blank=True, null=True)
#     dt_aplicacao = models.DateTimeField(blank=True, null=True)
#     co_imunobiologico_lote = models.ForeignKey(TbImunobiologicoLote, models.DO_NOTHING, db_column='co_imunobiologico_lote', blank=True, null=True)
#     ds_observacoes = models.CharField(max_length=300, blank=True, null=True)
#     co_grupo_atendimento = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_registro_vacinacao'
#
#
# class TbRegraVacinalDose(models.Model):
#     co_regra_vacinal_dose = models.BigIntegerField(primary_key=True)
#     co_imunobiologico = models.ForeignKey(TbImunobiologico, models.DO_NOTHING, db_column='co_imunobiologico', blank=True, null=True)
#     co_dose_imunobiologico = models.ForeignKey(TbDoseImunobiologico, models.DO_NOTHING, db_column='co_dose_imunobiologico', blank=True, null=True)
#     co_sexo = models.ForeignKey('TbSexo', models.DO_NOTHING, db_column='co_sexo', blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_regra_vacinal_dose'
#
#
# class TbRegraVacinalEstrategia(models.Model):
#     co_regra_vacinal_estrategia = models.BigIntegerField(primary_key=True)
#     co_imunobiologico = models.ForeignKey(TbImunobiologico, models.DO_NOTHING, db_column='co_imunobiologico', blank=True, null=True)
#     co_dose_imunobiologico = models.ForeignKey(TbDoseImunobiologico, models.DO_NOTHING, db_column='co_dose_imunobiologico', blank=True, null=True)
#     co_faixa_etaria_vacinacao = models.ForeignKey(TbFaixaEtariaVacinacao, models.DO_NOTHING, db_column='co_faixa_etaria_vacinacao', blank=True, null=True)
#     co_estrategia_vacinacao = models.ForeignKey(TbEstrategiaVacinacao, models.DO_NOTHING, db_column='co_estrategia_vacinacao', blank=True, null=True)
#     st_registro_anterior = models.IntegerField(blank=True, null=True)
#     nu_dias_aprazamento = models.IntegerField(blank=True, null=True)
#     co_proxima_regra_vacinal = models.ForeignKey('self', models.DO_NOTHING, db_column='co_proxima_regra_vacinal', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_regra_vacinal_estrategia'
#
#
# class TbRelFichasConfig(models.Model):
#     co_relatorio_ficha = models.IntegerField(primary_key=True)
#     nu_quadros = models.IntegerField(blank=True, null=True)
#     nu_meses = models.IntegerField(blank=True, null=True)
#     nu_fator = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_rel_fichas_config'
#
#
# class TbRelatorioProcessamento(models.Model):
#     co_seq_relatorio_processamento = models.BigIntegerField(primary_key=True)
#     co_dado_transp = models.ForeignKey(TbDadoTransp, models.DO_NOTHING, db_column='co_dado_transp', blank=True, null=True)
#     dt_processamento = models.DateTimeField(blank=True, null=True)
#     ds_mensagem_erro = models.CharField(max_length=2000, blank=True, null=True)
#     st_processamento = models.IntegerField()
#     tp_dado_transp = models.BigIntegerField(blank=True, null=True)
#     st_reprocessar = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_relatorio_processamento'
#
#
# class TbRendaFamiliar(models.Model):
#     co_renda_familiar = models.BigIntegerField(primary_key=True)
#     no_renda_familiar = models.CharField(max_length=255)
#     co_ordem = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_renda_familiar'
#
#
# class TbReportEtlConfigs(models.Model):
#     co_chave = models.CharField(primary_key=True, max_length=500)
#     ds_valor = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_report_etl_configs'
#
#
# class TbRequisicaoExame(models.Model):
#     co_seq_requisicao_exame = models.BigIntegerField(primary_key=True)
#     dt_requisicao = models.DateTimeField(blank=True, null=True)
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     ds_justificativa_procedimento = models.CharField(max_length=2000, blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     co_cid10 = models.ForeignKey(TbCid10, models.DO_NOTHING, db_column='co_cid10', blank=True, null=True)
#     tp_exame = models.IntegerField(blank=True, null=True)
#     ds_observacao = models.CharField(max_length=500, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_requisicao_exame'
#
#
# class TbResEnvio(models.Model):
#     co_seq_res_envio = models.BigIntegerField(primary_key=True)
#     nu_submission_set_id = models.CharField(max_length=255, blank=True, null=True)
#     nu_document_id = models.CharField(max_length=255, blank=True, null=True)
#     co_res_envio_estado = models.ForeignKey('TbResEnvioEstado', models.DO_NOTHING, db_column='co_res_envio_estado')
#     dt_envio = models.DateTimeField(blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_res_envio'
#
#
# class TbResEnvioErros(models.Model):
#     co_res_envio = models.OneToOneField(TbResEnvio, models.DO_NOTHING, db_column='co_res_envio', primary_key=True)
#     ds_erro = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_res_envio_erros'
#
#
# class TbResEnvioEstado(models.Model):
#     co_res_envio_estado = models.BigIntegerField(primary_key=True)
#     ds_estado = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_res_envio_estado'
#
#
# class TbRetificacaoAtend(models.Model):
#     co_seq_retificacao_atend = models.BigIntegerField(primary_key=True)
#     bl_conteudo_atendimento = models.BinaryField(blank=True, null=True)
#     co_unico_atend_prof = models.CharField(max_length=96, blank=True, null=True)
#     co_lotacao = models.ForeignKey(TbLotacao, models.DO_NOTHING, db_column='co_lotacao', blank=True, null=True)
#     co_prontuario = models.ForeignKey(TbProntuario, models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#     dt_exclusao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_retificacao_atend'
#
#
# class TbRevisao(models.Model):
#     co_seq_revisao = models.BigIntegerField(primary_key=True)
#     dt_revisao = models.DateTimeField(blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     co_usuario = models.BigIntegerField(blank=True, null=True)
#     ds_componente_gerador = models.TextField(blank=True, null=True)
#     ds_entidades = models.TextField(blank=True, null=True)
#     tp_registro_afetado = models.IntegerField(blank=True, null=True)
#     co_registro_afetado = models.TextField(blank=True, null=True)
#     st_processo_auditoria_eventos = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_revisao'
#
#
# class TbServidorSmtp(models.Model):
#     co_seq_servidor_smtp = models.BigIntegerField(primary_key=True)
#     no_host = models.CharField(max_length=255, blank=True, null=True)
#     nu_porta = models.CharField(max_length=5, blank=True, null=True)
#     ds_usuario = models.CharField(max_length=255, blank=True, null=True)
#     ds_senha = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     st_usuario_email = models.IntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     dt_registro = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_servidor_smtp'
#
#
# class TbSessaoSincronizacao(models.Model):
#     co_unico_sessao = models.CharField(primary_key=True, max_length=36)
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario')
#     dt_inicio = models.DateField(blank=True, null=True)
#     dt_fim = models.DateField(blank=True, null=True)
#     dt_ultima_sincronizacao = models.DateField(blank=True, null=True)
#     co_unico_servidor = models.CharField(max_length=36)
#     co_unico_aplicativo = models.CharField(max_length=36)
#     co_origem = models.ForeignKey(TbCdsTipoOrigem, models.DO_NOTHING, db_column='co_origem')
#     co_recebimento_lote = models.BigIntegerField(blank=True, null=True)
#     nu_versao_cliente = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_sessao_sincronizacao'
#
#
# class TbSexo(models.Model):
#     co_sexo = models.BigIntegerField(primary_key=True)
#     no_sexo = models.CharField(max_length=15)
#     sg_sexo = models.CharField(max_length=1)
#     no_identificador = models.CharField(max_length=30)
#     co_sexo_cadsus = models.CharField(max_length=1, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_sexo'
#
#
# class TbSextante(models.Model):
#     co_parte_bucal = models.OneToOneField(TbParteBucal, models.DO_NOTHING, db_column='co_parte_bucal', primary_key=True)
#     co_arcada = models.ForeignKey(TbArcada, models.DO_NOTHING, db_column='co_arcada', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_sextante'
#
#
# class TbSinanNotificacao(models.Model):
#     co_sinan_notificacao = models.BigIntegerField(primary_key=True)
#     no_notificacao = models.CharField(max_length=255, blank=True, null=True)
#     no_notificacao_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_cid10_principal = models.ForeignKey(TbCid10, models.DO_NOTHING, db_column='co_cid10_principal', blank=True, null=True)
#     no_grupo = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_sinan_notificacao'
#
#
# class TbSinanNotificacaoEvolucao(models.Model):
#     co_seq_sinan_notificacao_evol = models.BigIntegerField(primary_key=True)
#     co_sinan_notificacao = models.ForeignKey(TbSinanNotificacao, models.DO_NOTHING, db_column='co_sinan_notificacao')
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof')
#     co_prontuario = models.ForeignKey(TbProntuario, models.DO_NOTHING, db_column='co_prontuario')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_sinan_notificacao_evolucao'
#
#
# class TbSituacaoAgendado(models.Model):
#     co_situacao_agendado = models.BigIntegerField(primary_key=True)
#     no_situacao_agendado = models.CharField(max_length=50, blank=True, null=True)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_situacao_agendado'
#
#
# class TbSituacaoCoroa(models.Model):
#     co_situacao_coroa = models.BigIntegerField(primary_key=True)
#     no_situacao_coroa = models.CharField(max_length=50)
#     no_identificador = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_situacao_coroa'
#
#
# class TbSituacaoDadoRecebido(models.Model):
#     co_situacao_dado_recebido = models.BigIntegerField(primary_key=True)
#     no_situacao_dado_recebido = models.CharField(max_length=80, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_situacao_dado_recebido'
#
#
# class TbSituacaoFace(models.Model):
#     co_situacao_face = models.BigIntegerField(primary_key=True)
#     no_situacao_face = models.CharField(max_length=50)
#     no_identificador = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_situacao_face'


class TbSituacaoLocalidade(models.Model):
    co_situacao_localidade = models.BigIntegerField(primary_key=True)
    no_situacao_localidade = models.CharField(max_length=100)
    sg_situacao_localidade = models.CharField(max_length=1)

    def __str__(self):
        return self.no_situacao_localidade

    class Meta:
        managed = False
        db_table = 'tb_situacao_localidade'

#
# class TbSituacaoLoteTranspNodo(models.Model):
#     co_situacao_lote_transp_nodo = models.BigIntegerField(primary_key=True)
#     no_situacao_lote_transp_nodo = models.CharField(max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_situacao_lote_transp_nodo'
#
#
# class TbSituacaoProblema(models.Model):
#     co_situacao_problema = models.BigIntegerField(primary_key=True)
#     no_situacao_problema = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_situacao_problema'
#
#
# class TbSituacaoRaiz(models.Model):
#     co_situacao_raiz = models.BigIntegerField(primary_key=True)
#     no_situacao_raiz = models.CharField(max_length=50)
#     no_identificador = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_situacao_raiz'
#
#
# class TbStatusAtend(models.Model):
#     co_status_atend = models.BigIntegerField(primary_key=True)
#     no_status_atend = models.CharField(max_length=30)
#     no_status_atend_filtro = models.CharField(max_length=30)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_status_atend'
#
#
# class TbStatusAtendProf(models.Model):
#     co_status_atend_prof = models.BigIntegerField(primary_key=True)
#     no_status_atend_prof = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_status_atend_prof'
#
#
# class TbSubtipoUnidadeSaude(models.Model):
#     co_seq_subtp_unidade_saude = models.BigIntegerField(primary_key=True)
#     co_tp_unidade_saude = models.ForeignKey('TbTipoUnidadeSaude', models.DO_NOTHING, db_column='co_tp_unidade_saude')
#     co_subtp_unidade_saude = models.CharField(max_length=3)
#     ds_subtp_unidade_saude = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_subtipo_unidade_saude'
#         unique_together = (('co_tp_unidade_saude', 'co_subtp_unidade_saude'),)
#
#
# class TbTipoAgendamento(models.Model):
#     co_tipo_agendamento = models.BigIntegerField(primary_key=True)
#     no_tipo_agendamento = models.CharField(max_length=50)
#     no_identificador = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_agendamento'
#
#
# class TbTipoAgravo(models.Model):
#     co_tipo_agravo = models.BigIntegerField(primary_key=True)
#     no_tipo_agravo = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_agravo'
#
#
# class TbTipoAtend(models.Model):
#     co_tipo_atend = models.BigIntegerField(primary_key=True)
#     no_tipo_atend = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_atend'
#
#
# class TbTipoAtendProf(models.Model):
#     co_tipo_atend_prof = models.BigIntegerField(primary_key=True)
#     no_tipo_atend_prof = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_atend_prof'
#
#
# class TbTipoCfgAgenda(models.Model):
#     co_tipo_cfg_agenda = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=32)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_cfg_agenda'
#
#
# class TbTipoCiap(models.Model):
#     co_tipo_ciap = models.BigIntegerField(primary_key=True)
#     no_tipo_ciap = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_ciap'
#
#
# class TbTipoConfigAtendDomicilir(models.Model):
#     co_tipo_config_atend_dom = models.BigIntegerField(primary_key=True)
#     no_tipo_config_atend_dom = models.CharField(max_length=30)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_config_atend_domicilir'
#
#
# class TbTipoConsultaOdonto(models.Model):
#     co_tipo_consulta_odonto = models.BigIntegerField(primary_key=True)
#     no_tipo_consulta_odonto = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_consulta_odonto'
#
#
# class TbTipoDadoTransp(models.Model):
#     co_tipo_dado_transp = models.BigIntegerField(primary_key=True)
#     no_tipo_dado_transp = models.CharField(max_length=80, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_dado_transp'
#
#
# class TbTipoEdema(models.Model):
#     co_tipo_edema = models.BigIntegerField(primary_key=True)
#     no_tipo_edema = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_edema'
#
#
# class TbTipoEncamInterno(models.Model):
#     co_tipo_encam_interno = models.BigIntegerField(primary_key=True)
#     no_tipo_encam_interno = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_encam_interno'
#
#
# class TbTipoEncamOdonto(models.Model):
#     no_tipo_encam_odonto = models.CharField(max_length=255)
#     co_tipo_encam_odonto = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_encam_odonto'
#
#
# class TbTipoEquipe(models.Model):
#     co_seq_tipo_equipe = models.BigIntegerField(primary_key=True)
#     sg_tipo_equipe = models.CharField(max_length=30)
#     no_tipo_equipe = models.CharField(max_length=200)
#     sg_tipo_equipe_filtro = models.CharField(max_length=30, blank=True, null=True)
#     no_tipo_equipe_filtro = models.CharField(max_length=200, blank=True, null=True)
#     nu_ms = models.CharField(max_length=4)
#     ds_tp_equipe = models.CharField(max_length=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_equipe'
#
#
# class TbTipoExame(models.Model):
#     co_tipo_exame = models.BigIntegerField(primary_key=True)
#     no_tipo_exame = models.CharField(max_length=50)
#     co_sexo = models.ForeignKey(TbSexo, models.DO_NOTHING, db_column='co_sexo')
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_exame'
#
#
# class TbTipoFornecOdonto(models.Model):
#     no_tipo_fornec_odonto = models.CharField(max_length=255)
#     co_tipo_fornec_odonto = models.BigIntegerField(primary_key=True)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_fornec_odonto'
#
#
# class TbTipoGlicemia(models.Model):
#     co_tipo_glicemia = models.BigIntegerField(primary_key=True)
#     no_tipo_glicemia = models.CharField(max_length=15)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_glicemia'
#
#
# class TbTipoGravidez(models.Model):
#     co_tipo_gravidez = models.BigIntegerField(primary_key=True)
#     no_tipo_gravidez = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_gravidez'


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


# class TbTipoLogradouro(models.Model):
#     co_tipo_logradouro = models.BigIntegerField(primary_key=True)
#     nu_dne = models.CharField(unique=True, max_length=3)
#     no_tipo_logradouro = models.CharField(max_length=144)
#     no_tipo_logradouro_filtro = models.CharField(max_length=144)
#     co_tp_logradouro_cadsus = models.CharField(max_length=3, blank=True, null=True)
#     nu_frequencia = models.BigIntegerField()
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_logradouro'
#
#
# class TbTipoOpcao(models.Model):
#     co_tipo_opcao = models.BigIntegerField(primary_key=True)
#     no_tipo_opcao = models.CharField(max_length=25)
#     no_identificador = models.CharField(max_length=25)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_opcao'
#
#
# class TbTipoOrigemDadoTransp(models.Model):
#     co_seq_tipo_origem_dado_transp = models.BigIntegerField(primary_key=True)
#     no_tipo_origem_dado_transp = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_origem_dado_transp'
#
#
# class TbTipoParidade(models.Model):
#     co_tipo_paridade = models.BigIntegerField(primary_key=True)
#     no_tipo_paridade = models.CharField(max_length=100)
#     sg_tipo_paridade = models.CharField(max_length=1)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_paridade'
#
#
# class TbTipoParteBucal(models.Model):
#     co_tipo_parte_bucal = models.BigIntegerField(primary_key=True)
#     no_tipo_parte_bucal = models.CharField(max_length=100)
#     no_identificador = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_parte_bucal'
#
#
# class TbTipoParto(models.Model):
#     co_tipo_parto = models.BigIntegerField(primary_key=True)
#     no_tipo_parto = models.CharField(max_length=15)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_parto'
#
#
# class TbTipoPergunta(models.Model):
#     co_tipo_pergunta = models.BigIntegerField(primary_key=True)
#     ds_tipo_pergunta = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_pergunta'
#
#
# class TbTipoReceita(models.Model):
#     co_tipo_receita = models.BigIntegerField(primary_key=True)
#     no_tipo_receita = models.CharField(max_length=100)
#     no_identificador = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_receita'
#
#
# class TbTipoRegistro(models.Model):
#     co_tipo_registro = models.BigIntegerField(primary_key=True)
#     no_tipo_registro = models.CharField(max_length=50)
#     dt_competencia = models.CharField(max_length=6)
#     nu_ms = models.CharField(max_length=2)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_registro'
#
#
# class TbTipoRegistroVacinacao(models.Model):
#     co_tipo_registro_vacinacao = models.BigIntegerField(primary_key=True)
#     no_tipo_registro_vacinacao = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_registro_vacinacao'
#
#
# class TbTipoServico(models.Model):
#     co_seq_tipo_servico = models.BigIntegerField(primary_key=True)
#     no_tipo_servico = models.CharField(max_length=50)
#     no_tipo_servico_filtro = models.CharField(max_length=50, blank=True, null=True)
#     st_interno = models.IntegerField()
#     co_localidade = models.ForeignKey(TbLocalidade, models.DO_NOTHING, db_column='co_localidade', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_servico'
#         unique_together = (('co_localidade', 'no_tipo_servico'),)
#
#
# class TbTipoUnidadeSaude(models.Model):
#     co_seq_tipo_unidade_saude = models.BigIntegerField(primary_key=True)
#     no_tipo_unidade_saude = models.CharField(max_length=120)
#     co_tipo_unidade_cnes = models.BigIntegerField(unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_tipo_unidade_saude'
#
#
# class TbTituloPatente(models.Model):
#     co_titulo_patente = models.BigIntegerField(primary_key=True)
#     nu_dne = models.CharField(unique=True, max_length=4)
#     no_titulo_patente = models.CharField(max_length=72)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_titulo_patente'
#
#
# class TbTokenRedefinicaoSenha(models.Model):
#     co_seq_token_redefinicao_senha = models.BigIntegerField(primary_key=True)
#     ds_token = models.CharField(max_length=32, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     dt_registro = models.DateTimeField(blank=True, null=True)
#     dt_validade = models.DateTimeField(blank=True, null=True)
#     co_usuario = models.ForeignKey('TbUsuario', models.DO_NOTHING, db_column='co_usuario')
#
#     class Meta:
#         managed = False
#         db_table = 'tb_token_redefinicao_senha'


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


# class TbUnidadeMedida(models.Model):
#     co_unidade_medida = models.BigIntegerField(primary_key=True)
#     sg_unidade_medida = models.CharField(max_length=25)
#     no_unidade_medida_filtro = models.CharField(max_length=100, blank=True, null=True)
#     no_unidade_medida = models.CharField(max_length=100)
#     no_unidade_medida_plural = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_unidade_medida'
#
#
# class TbUnidadeMedidaTempo(models.Model):
#     co_unidade_medida_tempo = models.BigIntegerField(primary_key=True)
#     no_unidade_medida_tempo = models.CharField(max_length=255)
#     no_identificador = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_unidade_medida_tempo'
#
#
# class TbUnidadeSaude(models.Model):
#     nu_licenca_funcionamento = models.CharField(max_length=20, blank=True, null=True)
#     tp_unidade_saude = models.ForeignKey(TbTipoUnidadeSaude, models.DO_NOTHING, db_column='tp_unidade_saude', blank=True, null=True)
#     co_seq_unidade_saude = models.BigIntegerField(primary_key=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     nu_cnpj = models.CharField(max_length=14, blank=True, null=True)
#     no_unidade_saude = models.CharField(max_length=255, blank=True, null=True)
#     no_unidade_saude_filtro = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_comercial = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_comercial2 = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_fax = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.ForeignKey(TbUf, models.DO_NOTHING, db_column='co_uf', blank=True, null=True)
#     co_localidade_endereco = models.ForeignKey(TbLocalidade, models.DO_NOTHING, db_column='co_localidade_endereco', blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.ForeignKey(TbTipoLogradouro, models.DO_NOTHING, db_column='tp_logradouro', blank=True, null=True)
#     co_subtp_unidade_saude = models.ForeignKey(TbSubtipoUnidadeSaude, models.DO_NOTHING, db_column='co_subtp_unidade_saude', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_unidade_saude'
#
#
# class TbUsuario(models.Model):
#     co_seq_usuario = models.BigIntegerField(primary_key=True)
#     st_bloqueado = models.IntegerField()
#     ds_senha = models.CharField(max_length=255, blank=True, null=True)
#     st_trocar_senha = models.IntegerField()
#     co_ator = models.ForeignKey(TbAtor, models.DO_NOTHING, db_column='co_ator', blank=True, null=True)
#     dt_ultima_atualizacao_senha = models.DateField(blank=True, null=True)
#     st_termo_uso = models.IntegerField(blank=True, null=True)
#     st_forcar_troca_senha = models.IntegerField()
#     nr_tentativas_acesso = models.IntegerField()
#     ds_login = models.CharField(unique=True, max_length=255, blank=True, null=True)
#     dt_envio_email_recuperar_senha = models.DateTimeField(blank=True, null=True)
#     st_visualizou_novidades = models.IntegerField(blank=True, null=True)
#     st_pesquisa_respondida = models.IntegerField(blank=True, null=True)
#     dt_primeiro_login_versao = models.DateTimeField(blank=True, null=True)
#     dt_pesquisa_respondida = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_usuario'
#
#
# class TbVacinacao(models.Model):
#     co_seq_vacinacao = models.BigIntegerField(primary_key=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_puerpera = models.IntegerField(blank=True, null=True)
#     st_viajante = models.IntegerField(blank=True, null=True)
#     st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.ForeignKey(TbAtendProf, models.DO_NOTHING, db_column='co_atend_prof', blank=True, null=True)
#     co_prontuario = models.ForeignKey(TbProntuario, models.DO_NOTHING, db_column='co_prontuario', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_vacinacao'
#
#
# class TbViaAdmVacina(models.Model):
#     co_via_adm_vacina = models.BigIntegerField(primary_key=True)
#     no_via_adm_vacina = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_via_adm_vacina'
#
#
# class TbVisibilidadeLembrete(models.Model):
#     co_visibilidade_lembrete = models.BigIntegerField(primary_key=True)
#     no_visibilidade_lembrete = models.CharField(max_length=30)
#     no_identificador = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         db_table = 'tb_visibilidade_lembrete'
#
#
# class TlAcesso(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_perfil = models.BigIntegerField(blank=True, null=True)
#     nu_obrigacao = models.IntegerField(blank=True, null=True)
#     co_recurso = models.BigIntegerField(blank=True, null=True)
#     nu_acao = models.IntegerField(blank=True, null=True)
#     co_seq_acesso = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_acesso'
#         unique_together = (('co_revisao', 'co_seq_acesso'),)
#
#
# class TlAdCidadao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_ad_cidadao = models.BigIntegerField()
#     co_equipe = models.BigIntegerField(blank=True, null=True)
#     dt_admissao = models.DateTimeField(blank=True, null=True)
#     co_ad_modalidade = models.BigIntegerField(blank=True, null=True)
#     co_ad_origem = models.BigIntegerField(blank=True, null=True)
#     co_cid10_principal = models.BigIntegerField(blank=True, null=True)
#     co_cid10_causa_associada = models.BigIntegerField(blank=True, null=True)
#     co_ad_destino = models.BigIntegerField(blank=True, null=True)
#     dt_saida = models.DateTimeField(blank=True, null=True)
#     dt_ultima_visita = models.DateTimeField(blank=True, null=True)
#     dt_proxima_visita = models.DateTimeField(blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     no_especificacao_origem = models.CharField(max_length=255, blank=True, null=True)
#     co_cid10_secundario_2 = models.BigIntegerField(blank=True, null=True)
#     dt_reg_obito = models.DateTimeField(blank=True, null=True)
#     st_cidadao_sincronizado = models.IntegerField(blank=True, null=True)
#     st_dt_saida_restaurada = models.IntegerField(blank=True, null=True)
#     st_dt_saida_futura = models.IntegerField(blank=True, null=True)
#     nu_documento_obito = models.CharField(max_length=16, blank=True, null=True)
#     co_unico_ad_cidadao_obito = models.BigIntegerField(blank=True, null=True)
#     co_unico_ad_cidadao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ad_cidadao'
#         unique_together = (('co_revisao', 'co_seq_ad_cidadao'),)
#
#
# class TlAdCidadaoHistorico(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_seq_ad_cidadao_historico = models.BigIntegerField()
#     co_unico_ad_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_ad_modalidade = models.BigIntegerField(blank=True, null=True)
#     co_prof = models.BigIntegerField(blank=True, null=True)
#     dt_registro = models.DateTimeField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ad_cidadao_historico'
#         unique_together = (('co_revisao', 'co_seq_ad_cidadao_historico'),)
#
#
# class TlAdQuestao(models.Model):
#     co_seq_ad_questao = models.BigIntegerField()
#     ds_ad_questao = models.CharField(max_length=255, blank=True, null=True)
#     co_ad_cidadao = models.BigIntegerField(blank=True, null=True)
#     st_ad_questao = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     nu_ordem = models.IntegerField(blank=True, null=True)
#     co_situacao_presente = models.BigIntegerField(blank=True, null=True)
#     co_unico_ad_questao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ad_questao'
#         unique_together = (('co_revisao', 'co_seq_ad_questao'),)
#
#
# class TlAdResposta(models.Model):
#     co_seq_ad_resposta = models.BigIntegerField()
#     co_unico_ad_questao = models.BigIntegerField(blank=True, null=True)
#     st_ad_resposta = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_ad = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ad_resposta'
#         unique_together = (('co_revisao', 'co_seq_ad_resposta'),)
#
#
# class TlAdTipoElegivel(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ad_tipo_elegivel = models.BigIntegerField()
#     no_ad_tipo_elegivel = models.CharField(max_length=100, blank=True, null=True)
#     no_identificador = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ad_tipo_elegivel'
#         unique_together = (('co_revisao', 'co_ad_tipo_elegivel'),)
#
#
# class TlAdTipoInelegivel(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ad_tipo_inelegivel = models.BigIntegerField()
#     no_ad_tipo_inelegivel = models.CharField(max_length=150, blank=True, null=True)
#     no_identificador = models.CharField(max_length=150, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ad_tipo_inelegivel'
#         unique_together = (('co_revisao', 'co_ad_tipo_inelegivel'),)
#
#
# class TlAdmGeral(models.Model):
#     co_ator_papel = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_instalacao_terminada = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_adm_geral'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlAdmMunicipal(models.Model):
#     co_ator_papel = models.BigIntegerField()
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     ds_autorizacao = models.CharField(max_length=225, blank=True, null=True)
#     st_instalacao_terminada = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_adm_municipal'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlAdmMunicipalCentralizador(models.Model):
#     co_ator_papel = models.BigIntegerField()
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_adm_municipal_centralizador'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlAgendado(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_agendado = models.BigIntegerField()
#     dt_agendado = models.DateTimeField(blank=True, null=True)
#     hr_inicial_agendado = models.DateTimeField(blank=True, null=True)
#     ds_observacao = models.CharField(max_length=400, blank=True, null=True)
#     st_agendado = models.BigIntegerField(blank=True, null=True)
#     tp_agendamento = models.BigIntegerField(blank=True, null=True)
#     co_lotacao_agendada = models.BigIntegerField(blank=True, null=True)
#     co_motivo_reserva = models.BigIntegerField(blank=True, null=True)
#     ds_outro_motivo_reserva = models.CharField(max_length=600, blank=True, null=True)
#     co_origem = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_lotacao_criadora = models.BigIntegerField(blank=True, null=True)
#     dt_criacao = models.DateTimeField(blank=True, null=True)
#     uuid_agendamento = models.CharField(max_length=36, blank=True, null=True)
#     dt_ultima_tentativa_envio = models.DateTimeField(blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     ds_ultima_tentativa = models.TextField(blank=True, null=True)
#     st_cidadao_agendamento_online = models.CharField(max_length=48, blank=True, null=True)
#     st_fora_ubs = models.IntegerField(blank=True, null=True)
#     co_local_atend = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_agendado'
#         unique_together = (('co_revisao', 'co_seq_agendado'),)
#
#
# class TlAlergia(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_alergia = models.BigIntegerField()
#     co_categoria_agente_causador = models.BigIntegerField(blank=True, null=True)
#     no_substancia_especifica = models.CharField(max_length=300, blank=True, null=True)
#     no_substancia_especifica_filtr = models.CharField(max_length=300, blank=True, null=True)
#     co_ultima_alergia_evolucao = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_unico_alergia = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_alergia'
#         unique_together = (('co_revisao', 'co_seq_alergia'),)
#
#
# class TlAlergiaEvolucao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_alergia_evolucao = models.BigIntegerField()
#     co_unico_alergia = models.BigIntegerField(blank=True, null=True)
#     no_manifestacoes = models.CharField(max_length=800, blank=True, null=True)
#     dt_instalacao = models.DateField(blank=True, null=True)
#     st_alergia_avaliada = models.IntegerField(blank=True, null=True)
#     co_criticidade_alergia = models.BigIntegerField(blank=True, null=True)
#     no_evolucao = models.CharField(max_length=800, blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_alergia_evolucao'
#         unique_together = (('co_revisao', 'co_seq_alergia_evolucao'),)
#
#
# class TlAntecedente(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField()
#     ds_cirurgia = models.CharField(max_length=400, blank=True, null=True)
#     ds_internacao = models.CharField(max_length=400, blank=True, null=True)
#     ds_alergia_medicamento = models.CharField(max_length=400, blank=True, null=True)
#     ds_observacao = models.CharField(max_length=400, blank=True, null=True)
#     ds_aborto = models.CharField(max_length=255, blank=True, null=True)
#     ds_parto = models.CharField(max_length=255, blank=True, null=True)
#     qt_aborto = models.CharField(max_length=255, blank=True, null=True)
#     ds_natimorto = models.CharField(max_length=255, blank=True, null=True)
#     ds_recem_nascido = models.CharField(max_length=255, blank=True, null=True)
#     ds_cesaria = models.CharField(max_length=255, blank=True, null=True)
#     ds_parto_domiciliar = models.CharField(max_length=255, blank=True, null=True)
#     ds_filho_vivo = models.CharField(max_length=255, blank=True, null=True)
#     ds_obito_antes_primeira_semana = models.CharField(max_length=255, blank=True, null=True)
#     ds_gestacao = models.CharField(max_length=255, blank=True, null=True)
#     ds_parto_vaginal = models.CharField(max_length=255, blank=True, null=True)
#     ds_obito_apos_primeira_semana = models.CharField(max_length=255, blank=True, null=True)
#     dt_ultimo_parto = models.DateTimeField(blank=True, null=True)
#     qt_recem_nascido_acima = models.CharField(max_length=255, blank=True, null=True)
#     qt_nascidos_vivos = models.CharField(max_length=255, blank=True, null=True)
#     st_parto_menos_de_um_ano = models.IntegerField(blank=True, null=True)
#     dt_ultima_atualizacao_pessoal = models.DateTimeField(blank=True, null=True)
#     dt_ultima_atualizacao_gestacnl = models.DateTimeField(blank=True, null=True)
#     nu_peso = models.CharField(max_length=255, blank=True, null=True)
#     nu_altura = models.CharField(max_length=255, blank=True, null=True)
#     nu_perimetro_cefalico = models.CharField(max_length=255, blank=True, null=True)
#     nu_apgar_um = models.CharField(max_length=255, blank=True, null=True)
#     nu_apgar_cinco = models.CharField(max_length=255, blank=True, null=True)
#     nu_apgar_dez = models.CharField(max_length=255, blank=True, null=True)
#     tp_gravidez = models.CharField(max_length=255, blank=True, null=True)
#     tp_parto = models.CharField(max_length=255, blank=True, null=True)
#     nu_ig_semanas = models.CharField(max_length=255, blank=True, null=True)
#     nu_ig_dias = models.CharField(max_length=255, blank=True, null=True)
#     dt_ultima_atualizacao_puericu = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_antecedente'
#         unique_together = (('co_revisao', 'co_prontuario'),)
#
#
# class TlAntecedenteCiap(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField()
#     co_ciap = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_antecedente_ciap'
#         unique_together = (('co_revisao', 'co_prontuario', 'co_ciap'),)
#
#
# class TlAntecedenteHistorico(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_antecedente_historico = models.BigIntegerField()
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_antecedente_historico'
#         unique_together = (('co_revisao', 'co_seq_antecedente_historico'),)
#
#
# class TlAntecedenteItem(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_antecedente_item = models.BigIntegerField()
#     co_antecedente_historico = models.BigIntegerField(blank=True, null=True)
#     ds_valor_item = models.CharField(max_length=255, blank=True, null=True)
#     st_valor_item = models.IntegerField(blank=True, null=True)
#     tp_antecedente_item = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_antecedente_item'
#         unique_together = (('co_revisao', 'co_seq_antecedente_item'),)
#
#
# class TlAntecedenteTipoItem(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_antecedente_tipo_item = models.BigIntegerField()
#     no_antecedente_tipo_item = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_antecedente_tipo_item'
#         unique_together = (('co_revisao', 'co_antecedente_tipo_item'),)
#
#
# class TlAplicacaoMedicamento(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_aplicacao_medicamento = models.BigIntegerField()
#     no_aplicacao_medicamento = models.CharField(max_length=100, blank=True, null=True)
#     no_aplicacao_med_filtro = models.CharField(max_length=100, blank=True, null=True)
#     nu_frequencia_instalacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_aplicacao_medicamento'
#         unique_together = (('co_revisao', 'co_aplicacao_medicamento'),)
#
#
# class TlArcada(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_parte_bucal = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_arcada'
#         unique_together = (('co_revisao', 'co_parte_bucal'),)
#
#
# class TlAtend(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_atend = models.BigIntegerField()
#     dt_fim = models.DateTimeField(blank=True, null=True)
#     dt_inicio = models.DateTimeField(blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     st_atend = models.BigIntegerField(blank=True, null=True)
#     co_agendado = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_classificacao_risco = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     no_tipo_atend = models.CharField(max_length=255, blank=True, null=True)
#     dt_encaminhamento = models.DateTimeField(blank=True, null=True)
#     st_fechado_automaticamente = models.IntegerField(blank=True, null=True)
#     nu_lotacao_anterior = models.BigIntegerField(blank=True, null=True)
#     co_unico_atend = models.CharField(max_length=96, blank=True, null=True)
#     tp_local_atend = models.BigIntegerField(blank=True, null=True)
#     st_registro_tardio = models.IntegerField(blank=True, null=True)
#     no_justificativa_reg_tardio = models.CharField(max_length=50, blank=True, null=True)
#     dt_criacao_registro = models.DateTimeField(blank=True, null=True)
#     dt_ultima_alteracao_status = models.DateTimeField(blank=True, null=True)
#     co_equipe = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend'
#         unique_together = (('co_revisao', 'co_seq_atend'),)
#
#
# class TlAtendProced(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_atend_proced = models.BigIntegerField()
#     st_obrigatorio = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField(blank=True, null=True)
#     co_cid10_principal = models.BigIntegerField(blank=True, null=True)
#     st_automatico = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_proced'
#         unique_together = (('co_revisao', 'co_seq_atend_proced'),)
#
#
# class TlAtendProf(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_atend_prof = models.BigIntegerField()
#     dt_fim = models.DateTimeField(blank=True, null=True)
#     dt_inicio = models.DateTimeField(blank=True, null=True)
#     co_atend = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof_tipo_encam_intrn = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     tp_atend_prof = models.BigIntegerField(blank=True, null=True)
#     st_atend_prof = models.BigIntegerField(blank=True, null=True)
#     st_atend_enviado = models.IntegerField(blank=True, null=True)
#     co_unico_ad_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_classificacao_risco = models.BigIntegerField(blank=True, null=True)
#     co_unico_atend_prof = models.CharField(max_length=96, blank=True, null=True)
#     tp_atend = models.BigIntegerField(blank=True, null=True)
#     nu_conselho_classe = models.CharField(max_length=100, blank=True, null=True)
#     co_uf_emissora_conselho_classe = models.BigIntegerField(blank=True, null=True)
#     co_conselho_classe = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_racionalidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_lotacao_atend_compartilhado = models.BigIntegerField(blank=True, null=True)
#     st_registro_historico = models.IntegerField(blank=True, null=True)
#     nu_revisao = models.IntegerField(blank=True, null=True)
#     st_cancelado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof'
#         unique_together = (('co_revisao', 'co_seq_atend_prof'),)
#
#
# class TlAtendProfAd(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_ad = models.BigIntegerField()
#     st_elegivel = models.IntegerField(blank=True, null=True)
#     co_ad_origem = models.BigIntegerField(blank=True, null=True)
#     co_ad_modalidade = models.BigIntegerField(blank=True, null=True)
#     co_ad_destino = models.BigIntegerField(blank=True, null=True)
#     co_ad_tipo_elegivel = models.BigIntegerField(blank=True, null=True)
#     nu_serial_aplicativo = models.CharField(max_length=100, blank=True, null=True)
#     ds_fabricante_dispositivo = models.CharField(max_length=100, blank=True, null=True)
#     ds_modelo_dispositivo = models.CharField(max_length=100, blank=True, null=True)
#     co_cid10_principal = models.BigIntegerField(blank=True, null=True)
#     co_cid10_secundario_1 = models.BigIntegerField(blank=True, null=True)
#     co_cid10_secundario_2 = models.BigIntegerField(blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=16, blank=True, null=True)
#     no_cuidador = models.CharField(max_length=255, blank=True, null=True)
#     tp_cds_cuidador = models.BigIntegerField(blank=True, null=True)
#     dt_nascimento_cuidador = models.DateField(blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_ad'
#         unique_together = (('co_revisao', 'co_atend_prof_ad'),)
#
#
# class TlAtendProfAdQst(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_atend_prof_ad_qst = models.BigIntegerField()
#     ds_atend_prof_ad_qst = models.CharField(max_length=100, blank=True, null=True)
#     st_atend_prof_ad_qst = models.IntegerField(blank=True, null=True)
#     nu_ordem = models.IntegerField(blank=True, null=True)
#     co_atend_prof_ad = models.BigIntegerField(blank=True, null=True)
#     co_situacao_presente = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_ad_qst'
#         unique_together = (('co_revisao', 'co_seq_atend_prof_ad_qst'),)
#
#
# class TlAtendProfAdTipoInelegvl(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_ad = models.BigIntegerField()
#     tp_ad_inelegivel = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_ad_tipo_inelegvl'
#         unique_together = (('co_revisao', 'co_atend_prof_ad', 'tp_ad_inelegivel'),)
#
#
# class TlAtendProfConduta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField()
#     tp_cds_conduta = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_conduta'
#         unique_together = (('co_revisao', 'co_atend_prof', 'tp_cds_conduta'),)
#
#
# class TlAtendProfOdonto(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_odonto = models.BigIntegerField()
#     tp_consulta_odonto = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_odonto'
#         unique_together = (('co_revisao', 'co_atend_prof_odonto'),)
#
#
# class TlAtendProfOdontoTipoEncm(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_odonto = models.BigIntegerField()
#     tp_encam_odonto = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_odonto_tipo_encm'
#         unique_together = (('co_revisao', 'co_atend_prof_odonto', 'tp_encam_odonto'),)
#
#
# class TlAtendProfOdontoTipoFrnc(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_odonto = models.BigIntegerField()
#     tp_fornecimento_odonto = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_odonto_tipo_frnc'
#         unique_together = (('co_revisao', 'co_atend_prof_odonto', 'tp_fornecimento_odonto'),)
#
#
# class TlAtendProfPic(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_pic = models.BigIntegerField()
#     co_atend_prof = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_pic'
#         unique_together = (('co_revisao', 'co_atend_prof', 'co_cds_pic'),)
#
#
# class TlAtendProfPreNatal(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_pre_natal = models.BigIntegerField()
#     co_unico_pre_natal = models.BigIntegerField(blank=True, null=True)
#     tp_edema = models.BigIntegerField(blank=True, null=True)
#     st_gravidez_planejada = models.IntegerField(blank=True, null=True)
#     st_movimentacao_fetal = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_pre_natal'
#         unique_together = (('co_revisao', 'co_atend_prof_pre_natal'),)
#
#
# class TlAtendProfPuericultura(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof_puericultura = models.BigIntegerField()
#     tp_aleitamento_materno = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_puericultura'
#         unique_together = (('co_revisao', 'co_atend_prof_puericultura'),)
#
#
# class TlAtendProfTipoEncamIntrn(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_atend_prof_tipo_enc_int = models.BigIntegerField()
#     co_agendado = models.BigIntegerField(blank=True, null=True)
#     co_atend = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     tp_encam_interno = models.BigIntegerField(blank=True, null=True)
#     st_agendado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_prof_tipo_encam_intrn'
#         unique_together = (('co_revisao', 'co_seq_atend_prof_tipo_enc_int'),)
#
#
# class TlAtendTipoServico(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     tp_servico = models.BigIntegerField()
#     co_atend = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atend_tipo_servico'
#         unique_together = (('co_revisao', 'co_atend', 'tp_servico'),)
#
#
# class TlAtestado(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_atestado = models.BigIntegerField()
#     dt_atestado = models.DateTimeField(blank=True, null=True)
#     ds_atestado = models.TextField(blank=True, null=True)
#     st_impresso = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     im_qrcode_atestado = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atestado'
#         unique_together = (('co_revisao', 'co_seq_atestado'),)
#
#
# class TlAtivColGrupo(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_ativ_col_grupo = models.BigIntegerField(primary_key=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     st_ficha = models.CharField(max_length=32, blank=True, null=True)
#     co_grupo = models.BigIntegerField(blank=True, null=True)
#     dt_atualizacao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ativ_col_grupo'
#         unique_together = (('co_seq_ativ_col_grupo', 'co_revisao'),)
#
#
# class TlAtor(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_ator = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ator'
#         unique_together = (('co_revisao', 'co_seq_ator'),)
#
#
# class TlAtorPapel(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_ator_papel = models.BigIntegerField()
#     co_ator = models.BigIntegerField(blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     no_tipo_ator_papel = models.CharField(max_length=100, blank=True, null=True)
#     tp_perfil = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ator_papel'
#         unique_together = (('co_revisao', 'co_seq_ator_papel'),)
#
#
# class TlAtorPapelPerfil(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField()
#     co_perfil = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ator_papel_perfil'
#         unique_together = (('co_revisao', 'co_ator_papel', 'co_perfil'),)
#
#
# class TlAtributoComplem(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atributo_complem = models.BigIntegerField()
#     no_atributo_complem = models.CharField(max_length=255, blank=True, null=True)
#     dt_competencia = models.CharField(max_length=6, blank=True, null=True)
#     nu_ms = models.CharField(max_length=3, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_atributo_complem'
#         unique_together = (('co_revisao', 'co_atributo_complem'),)
#
#
# class TlBairro(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_bairro = models.BigIntegerField()
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     nu_dne = models.CharField(max_length=8, blank=True, null=True)
#     no_bairro = models.CharField(max_length=144, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=144, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_bairro'
#         unique_together = (('co_revisao', 'co_bairro'),)
#
#
# class TlCboAtend(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     qt_tempo_consulta = models.IntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_seq_cbo_atend = models.BigIntegerField()
#     st_disponivel_lotacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cbo_atend'
#         unique_together = (('co_revisao', 'co_seq_cbo_atend'),)
#
#
# class TlCdsAleitamentoMaterno(models.Model):
#     co_cds_aleitamento_materno = models.BigIntegerField()
#     no_cds_aleitamento_materno = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_aleitamento_materno'
#         unique_together = (('co_revisao', 'co_cds_aleitamento_materno'),)
#
#
# class TlCdsAtendDomProced(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_atend_domiciliar = models.BigIntegerField()
#     co_proced = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_dom_proced'
#         unique_together = (('co_revisao', 'co_cds_atend_domiciliar', 'co_proced'),)
#
#
# class TlCdsAtendDomSituacaoPres(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_atend_domiciliar = models.BigIntegerField()
#     co_cds_situacao_presente = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_dom_situacao_pres'
#         unique_together = (('co_revisao', 'co_cds_atend_domiciliar', 'co_cds_situacao_presente'),)
#
#
# class TlCdsAtendDomiciliar(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_atend_domiciliar = models.BigIntegerField()
#     co_cds_ficha_atend_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     co_local_atend = models.BigIntegerField(blank=True, null=True)
#     co_ad_modalidade = models.BigIntegerField(blank=True, null=True)
#     tp_atend_v20 = models.BigIntegerField(blank=True, null=True)
#     co_cid10 = models.BigIntegerField(blank=True, null=True)
#     co_ciap = models.BigIntegerField(blank=True, null=True)
#     co_ad_destino_v20 = models.BigIntegerField(blank=True, null=True)
#     st_inicio_acompanhamento_obito = models.IntegerField(blank=True, null=True)
#     co_ad_destino = models.BigIntegerField(blank=True, null=True)
#     tp_atend = models.BigIntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_domiciliar'
#         unique_together = (('co_revisao', 'co_seq_cds_atend_domiciliar'),)
#
#
# class TlCdsAtendIndividual(models.Model):
#     co_seq_cds_atend_individual = models.BigIntegerField()
#     co_cds_ficha_atend_individual = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_local_atend = models.BigIntegerField(blank=True, null=True)
#     co_cds_aleitamento_materno = models.BigIntegerField(blank=True, null=True)
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     co_cds_pic = models.BigIntegerField(blank=True, null=True)
#     co_cid10 = models.BigIntegerField(blank=True, null=True)
#     st_ficou_observacao = models.IntegerField(blank=True, null=True)
#     st_vacina_em_dia = models.IntegerField(blank=True, null=True)
#     nu_idade_gestacional = models.IntegerField(blank=True, null=True)
#     co_ad_modalidade = models.BigIntegerField(blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     tp_atend = models.BigIntegerField(blank=True, null=True)
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     st_gravidez_planejada = models.IntegerField(blank=True, null=True)
#     qt_gestacao_previa = models.IntegerField(blank=True, null=True)
#     qt_parto = models.IntegerField(blank=True, null=True)
#     co_racionalidade_saude = models.BigIntegerField(blank=True, null=True)
#     nu_perimetro_cefalico = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
#     co_cid10_2 = models.BigIntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_individual'
#         unique_together = (('co_revisao', 'co_seq_cds_atend_individual'),)
#
#
# class TlCdsAtendIndividualCiap(models.Model):
#     co_cds_atend_individual = models.BigIntegerField()
#     co_ciap = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_individual_ciap'
#         unique_together = (('co_revisao', 'co_cds_atend_individual', 'co_ciap'),)
#
#
# class TlCdsAtendIndividualCondut(models.Model):
#     co_cds_atend_individual = models.BigIntegerField()
#     tp_cds_conduta = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_individual_condut'
#         unique_together = (('co_revisao', 'co_cds_atend_individual', 'tp_cds_conduta'),)
#
#
# class TlCdsAtendIndividualNasf(models.Model):
#     co_cds_atend_individual = models.BigIntegerField()
#     tp_cds_atend_nasf = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_individual_nasf'
#         unique_together = (('co_revisao', 'co_cds_atend_individual', 'tp_cds_atend_nasf'),)
#
#
# class TlCdsAtendOdontTipVigBuc(models.Model):
#     co_cds_atend_odonto = models.BigIntegerField()
#     tp_cds_vig_saude_bucal = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_odont_tip_vig_buc'
#         unique_together = (('co_revisao', 'co_cds_atend_odonto', 'tp_cds_vig_saude_bucal'),)
#
#
# class TlCdsAtendOdonto(models.Model):
#     co_seq_cds_atend_odonto = models.BigIntegerField()
#     co_local_atend = models.BigIntegerField(blank=True, null=True)
#     co_cds_ficha_atend_odonto = models.BigIntegerField(blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     st_necessidade_especial = models.IntegerField(blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     tp_atend = models.BigIntegerField(blank=True, null=True)
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_odonto'
#         unique_together = (('co_revisao', 'co_seq_cds_atend_odonto'),)
#
#
# class TlCdsAtendOdontoTipoCnslt(models.Model):
#     co_cds_atend_odonto = models.BigIntegerField()
#     tp_consulta_odonto = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_odonto_tipo_cnslt'
#         unique_together = (('co_revisao', 'co_cds_atend_odonto', 'tp_consulta_odonto'),)
#
#
# class TlCdsAtendOdontoTipoEncam(models.Model):
#     co_cds_atend_odonto = models.BigIntegerField()
#     tp_encam_odonto = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_odonto_tipo_encam'
#         unique_together = (('co_revisao', 'co_cds_atend_odonto', 'tp_encam_odonto'),)
#
#
# class TlCdsAtendOdontoTipoFornc(models.Model):
#     co_cds_atend_odonto = models.BigIntegerField()
#     tp_fornecimento_odonto = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_atend_odonto_tipo_fornc'
#         unique_together = (('co_revisao', 'co_cds_atend_odonto', 'tp_fornecimento_odonto'),)
#
#
# class TlCdsAtivColParticipante(models.Model):
#     co_seq_cds_ativ_col_participnt = models.BigIntegerField()
#     co_cds_ficha_ativ_col = models.BigIntegerField(blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=225, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     st_avaliacao_alterada = models.IntegerField(blank=True, null=True)
#     nu_peso = models.FloatField(blank=True, null=True)
#     nu_altura = models.FloatField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     st_cessou_habito_fumar = models.IntegerField(blank=True, null=True)
#     st_abandonou_grupo = models.IntegerField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ativ_col_participante'
#         unique_together = (('co_revisao', 'co_seq_cds_ativ_col_participnt'),)
#
#
# class TlCdsAtivColPratica(models.Model):
#     co_cds_ativ_col_pratica = models.BigIntegerField()
#     no_cds_ativ_col_pratica = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ativ_col_pratica'
#         unique_together = (('co_revisao', 'co_cds_ativ_col_pratica'),)
#
#
# class TlCdsAtivColPublicoAlvo(models.Model):
#     co_cds_ativ_col_publico_alvo = models.BigIntegerField()
#     no_cds_ativ_col_publico_alvo = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ativ_col_publico_alvo'
#         unique_together = (('co_revisao', 'co_cds_ativ_col_publico_alvo'),)
#
#
# class TlCdsAtivColTema(models.Model):
#     co_cds_ativ_col_tema = models.BigIntegerField()
#     no_cds_ativ_col_tema = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ativ_col_tema'
#         unique_together = (('co_revisao', 'co_cds_ativ_col_tema'),)
#
#
# class TlCdsAvalElegAdTipoInelg(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_aval_elegibilidade = models.BigIntegerField(blank=True, null=True)
#     tp_ad_inelegivel = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_aval_eleg_ad_tipo_inelg'
#
#
# class TlCdsAvalElegCdsSitucPrs(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_aval_elegibilidade = models.BigIntegerField(blank=True, null=True)
#     tp_cds_situacao_presente = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_aval_eleg_cds_situc_prs'
#
#
# class TlCdsAvalElegibilidade(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_aval_elegibilidade = models.BigIntegerField()
#     co_cds_prof_cadastrante = models.BigIntegerField(blank=True, null=True)
#     co_ad_modalidade = models.BigIntegerField(blank=True, null=True)
#     co_ad_origem = models.BigIntegerField(blank=True, null=True)
#     tp_ad_elegivel = models.BigIntegerField(blank=True, null=True)
#     co_cid10_principal = models.BigIntegerField(blank=True, null=True)
#     co_cid10_segundo = models.BigIntegerField(blank=True, null=True)
#     co_cid10_terceiro = models.BigIntegerField(blank=True, null=True)
#     co_localidade_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_localidade_cidadao_nasc = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     co_nacionalidade = models.BigIntegerField(blank=True, null=True)
#     co_raca_cor = models.BigIntegerField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=256, blank=True, null=True)
#     ds_email_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     dt_aval_elegibilidade = models.DateTimeField(blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=256, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_logradouro = models.CharField(max_length=256, blank=True, null=True)
#     no_mae_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_social_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     nu_cep = models.CharField(max_length=8, blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     nu_domicilio = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_referencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_residencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_nis_pis_pasep = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     st_desconhece_nome_mae = models.IntegerField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     tp_cds_cuidador = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     co_pais = models.BigIntegerField(blank=True, null=True)
#     co_etnia = models.BigIntegerField(blank=True, null=True)
#     no_pai_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateTimeField(blank=True, null=True)
#     ds_portaria_naturalizacao = models.CharField(max_length=60, blank=True, null=True)
#     dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=15, blank=True, null=True)
#     co_cds_prof_at_compartilhado = models.BigIntegerField(blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
#     co_ad_procedencia = models.BigIntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_aval_elegibilidade'
#         unique_together = (('co_revisao', 'co_seq_cds_aval_elegibilidade'),)
#
#
# class TlCdsCadDomiciliar(models.Model):
#     co_cds_prof_cadastrante = models.BigIntegerField(blank=True, null=True)
#     co_seq_cds_cad_domiciliar = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     ds_rg_recusa_cad = models.CharField(max_length=255, blank=True, null=True)
#     dt_cad_domiciliar = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     st_recusa_cad = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=256, blank=True, null=True)
#     nu_cep = models.CharField(max_length=255, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=256, blank=True, null=True)
#     nu_fone_referencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_residencia = models.CharField(max_length=255, blank=True, null=True)
#     no_logradouro = models.CharField(max_length=256, blank=True, null=True)
#     nu_domicilio = models.CharField(max_length=255, blank=True, null=True)
#     co_municipio = models.BigIntegerField(blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     no_logradouro_filtro = models.CharField(max_length=256, blank=True, null=True)
#     st_atualizacao = models.IntegerField(blank=True, null=True)
#     co_unico_domicilio = models.CharField(max_length=96, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     st_versao_atual = models.IntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
#     no_instituicao_permanencia = models.CharField(max_length=255, blank=True, null=True)
#     st_outros_prof_vinculados = models.IntegerField(blank=True, null=True)
#     no_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     nu_cns_responsavel_tecnico = models.CharField(max_length=15, blank=True, null=True)
#     no_cargo_instituicao = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     tp_cds_imovel = models.BigIntegerField(blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     ds_complemento_filtro = models.CharField(max_length=255, blank=True, null=True)
#     st_gerado_automaticamente = models.IntegerField(blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_cad_domiciliar'
#         unique_together = (('co_revisao', 'co_seq_cds_cad_domiciliar'),)
#
#
# class TlCdsCadIndividual(models.Model):
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     co_municipio = models.BigIntegerField(blank=True, null=True)
#     co_pais = models.BigIntegerField(blank=True, null=True)
#     co_cds_prof_cadastrante = models.BigIntegerField(blank=True, null=True)
#     co_seq_cds_cad_individual = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     ds_rg_recusa_cad = models.CharField(max_length=255, blank=True, null=True)
#     dt_cad_individual = models.DateTimeField(blank=True, null=True)
#     dt_nascimento_responsavel = models.DateTimeField(blank=True, null=True)
#     nu_cartao_sus_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     nu_pis_pasep = models.CharField(max_length=255, blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     st_recusa_cad = models.IntegerField(blank=True, null=True)
#     st_responsavel_familiar = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_social_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_raca_cor = models.BigIntegerField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     no_mae_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_desconhece_nome_mae = models.IntegerField(blank=True, null=True)
#     co_nacionalidade = models.BigIntegerField(blank=True, null=True)
#     nu_celular_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     ds_email_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_atualizacao = models.IntegerField(blank=True, null=True)
#     co_unico_ficha_origem = models.CharField(max_length=96, blank=True, null=True)
#     st_versao_atual = models.IntegerField(blank=True, null=True)
#     co_unico_grupo = models.CharField(max_length=44, blank=True, null=True)
#     no_cidadao_filtro = models.CharField(max_length=600, blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_etnia = models.BigIntegerField(blank=True, null=True)
#     no_pai_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateTimeField(blank=True, null=True)
#     ds_portaria_naturalizacao = models.CharField(max_length=60, blank=True, null=True)
#     dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
#     dt_obito = models.DateTimeField(blank=True, null=True)
#     nu_declaracao_obito = models.CharField(max_length=9, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     st_ficha_inativa = models.IntegerField(blank=True, null=True)
#     st_gerado_automaticamente = models.IntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#     st_erro_inativacao = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_cad_individual'
#         unique_together = (('co_revisao', 'co_seq_cds_cad_individual'),)
#
#
# class TlCdsCidadaoResposta(models.Model):
#     co_cds_cad_individual = models.BigIntegerField(blank=True, null=True)
#     co_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_pergunta_detalhe = models.BigIntegerField(blank=True, null=True)
#     st_resposta = models.IntegerField(blank=True, null=True)
#     co_seq_cds_cidadao_resposta = models.BigIntegerField()
#     ds_resposta = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_cidadao_resposta'
#         unique_together = (('co_revisao', 'co_seq_cds_cidadao_resposta'),)
#
#
# class TlCdsDomicilio(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_domicilio = models.BigIntegerField()
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     ds_complemento = models.CharField(max_length=256, blank=True, null=True)
#     co_municipio = models.BigIntegerField(blank=True, null=True)
#     no_logradouro = models.CharField(max_length=256, blank=True, null=True)
#     no_bairro = models.CharField(max_length=256, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     nu_fone_referencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_fone_residencia = models.CharField(max_length=255, blank=True, null=True)
#     nu_domicilio = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_domicilio = models.CharField(max_length=96, blank=True, null=True)
#     dt_ultima_atualizacao = models.DateTimeField(blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_ultima_ficha = models.CharField(max_length=96, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     tp_cds_imovel = models.BigIntegerField(blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
#     no_instituicao_permanencia = models.CharField(max_length=255, blank=True, null=True)
#     st_outros_prof_vinculados = models.IntegerField(blank=True, null=True)
#     no_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     nu_cns_responsavel_tecnico = models.CharField(max_length=15, blank=True, null=True)
#     no_cargo_instituicao = models.CharField(max_length=255, blank=True, null=True)
#     nu_contato_responsavel_tecnico = models.CharField(max_length=255, blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_domicilio'
#         unique_together = (('co_revisao', 'co_seq_cds_domicilio'),)
#
#
# class TlCdsDomicilioFamilia(models.Model):
#     co_seq_cds_domicilio_familia = models.BigIntegerField()
#     co_cds_cad_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_renda_familiar = models.BigIntegerField(blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     dt_mudanca = models.DateTimeField(blank=True, null=True)
#     qt_membros_familia = models.IntegerField(blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     st_mudanca = models.IntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_domicilio_familia'
#         unique_together = (('co_revisao', 'co_seq_cds_domicilio_familia'),)
#
#
# class TlCdsDomicilioResposta(models.Model):
#     co_seq_cds_domicilio_resposta = models.BigIntegerField()
#     co_cds_cad_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_pergunta_detalhe = models.BigIntegerField(blank=True, null=True)
#     st_resposta = models.IntegerField(blank=True, null=True)
#     ds_resposta = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_domicilio_resposta'
#         unique_together = (('co_revisao', 'co_seq_cds_domicilio_resposta'),)
#
#
# class TlCdsFichaAtendDomiciliar(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_ficha_atend_dom = models.BigIntegerField()
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     co_cds_prof_principal = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_cds_prof_atend_comp = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_atend_domiciliar'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_atend_dom'),)
#
#
# class TlCdsFichaAtendIndivdlPrf(models.Model):
#     co_cds_ficha_atend_individual = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_atend_indivdl_prf'
#         unique_together = (('co_revisao', 'co_cds_ficha_atend_individual', 'co_cds_prof'),)
#
#
# class TlCdsFichaAtendIndividual(models.Model):
#     co_seq_cds_ficha_atend_indivdl = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_atend_individual'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_atend_indivdl'),)
#
#
# class TlCdsFichaAtendOdonto(models.Model):
#     co_seq_cds_ficha_atend_odonto = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_atend_odonto'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_atend_odonto'),)
#
#
# class TlCdsFichaAtendOdontoProf(models.Model):
#     co_cds_ficha_atend_odonto = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_atend_odonto_prof'
#         unique_together = (('co_revisao', 'co_cds_ficha_atend_odonto', 'co_cds_prof'),)
#
#
# class TlCdsFichaAtivCol(models.Model):
#     co_inep_escola = models.BigIntegerField(blank=True, null=True)
#     co_seq_cds_ficha_ativ_col = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     ds_local_ativ = models.CharField(max_length=500, blank=True, null=True)
#     dt_ativ_col = models.DateTimeField(blank=True, null=True)
#     hr_fim = models.DateTimeField(blank=True, null=True)
#     hr_inicio = models.DateTimeField(blank=True, null=True)
#     qt_avaliacao_alterada = models.IntegerField(blank=True, null=True)
#     qt_participante_ativ = models.IntegerField(blank=True, null=True)
#     qt_participante_programado = models.IntegerField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_ativ_col = models.BigIntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof_responsavel = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     co_proced_sigtap = models.BigIntegerField(blank=True, null=True)
#     st_pse_educacao = models.IntegerField(blank=True, null=True)
#     st_pse_saude = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_ativ_col'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_ativ_col'),)
#
#
# class TlCdsFichaAtivColPratica(models.Model):
#     co_cds_ficha_ativ_col = models.BigIntegerField()
#     co_cds_ativ_col_pratica = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_ativ_col_pratica'
#         unique_together = (('co_revisao', 'co_cds_ficha_ativ_col', 'co_cds_ativ_col_pratica'),)
#
#
# class TlCdsFichaAtivColProf(models.Model):
#     co_cds_ficha_ativ_col = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_ativ_col_prof'
#         unique_together = (('co_revisao', 'co_cds_ficha_ativ_col', 'co_cds_prof'),)
#
#
# class TlCdsFichaAtivColPubAlvo(models.Model):
#     co_cds_ficha_ativ_col = models.BigIntegerField()
#     co_cds_ativ_col_publico_alvo = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_ativ_col_pub_alvo'
#         unique_together = (('co_revisao', 'co_cds_ativ_col_publico_alvo', 'co_cds_ficha_ativ_col'),)
#
#
# class TlCdsFichaAtivColTema(models.Model):
#     co_cds_ficha_ativ_col = models.BigIntegerField()
#     co_cds_ativ_col_tema = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_ativ_col_tema'
#         unique_together = (('co_revisao', 'co_cds_ativ_col_tema', 'co_cds_ficha_ativ_col'),)
#
#
# class TlCdsFichaConsumoAlimentar(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_ficha_consumo_alim = models.BigIntegerField()
#     co_cds_prof = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     no_identificacao_cidadao = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_cidadao = models.DateTimeField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     co_local_atend = models.BigIntegerField(blank=True, null=True)
#     co_qst_questionario_respondido = models.BigIntegerField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_consumo_alimentar'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_consumo_alim'),)
#
#
# class TlCdsFichaProced(models.Model):
#     co_seq_cds_ficha_proced = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     qt_afericao_pressao_arterial = models.BigIntegerField(blank=True, null=True)
#     qt_afericao_temperatura = models.BigIntegerField(blank=True, null=True)
#     qt_coleta_material = models.BigIntegerField(blank=True, null=True)
#     qt_curativo_simples = models.BigIntegerField(blank=True, null=True)
#     qt_glicemia = models.BigIntegerField(blank=True, null=True)
#     qt_medicao_altura = models.BigIntegerField(blank=True, null=True)
#     qt_medicao_peso = models.BigIntegerField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_proced'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_proced'),)
#
#
# class TlCdsFichaVacinacao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_ficha_vacinacao = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     st_cancelado = models.IntegerField(blank=True, null=True)
#     nu_revisao = models.IntegerField(blank=True, null=True)
#     co_unico_ficha_cancelada = models.CharField(max_length=96, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_vacinacao'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_vacinacao'),)
#
#
# class TlCdsFichaVisitaDomiciliar(models.Model):
#     co_seq_cds_ficha_visita_dom = models.BigIntegerField()
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ficha = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField(blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_visita_domiciliar'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_visita_dom'),)
#
#
# class TlCdsFichaZikaMicrocefalia(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_ficha_zica_micrcfl = models.BigIntegerField()
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     co_cds_prof = models.BigIntegerField(blank=True, null=True)
#     nu_cns_cidadao = models.CharField(max_length=15, blank=True, null=True)
#     nu_cns_responsavel_familiar = models.CharField(max_length=15, blank=True, null=True)
#     dt_ficha_complementar = models.DateTimeField(blank=True, null=True)
#     st_ficha = models.IntegerField(blank=True, null=True)
#     st_enfileirado = models.IntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     co_localidade_origem = models.BigIntegerField(blank=True, null=True)
#     dt_teste_olhinho = models.DateTimeField(blank=True, null=True)
#     co_teste_olhinho = models.BigIntegerField(blank=True, null=True)
#     dt_exame_fundo_olho = models.DateTimeField(blank=True, null=True)
#     co_exame_fundo_olho = models.BigIntegerField(blank=True, null=True)
#     dt_exame_orelhinha = models.DateTimeField(blank=True, null=True)
#     co_exame_orelhinha = models.BigIntegerField(blank=True, null=True)
#     dt_us_transfontanela = models.DateTimeField(blank=True, null=True)
#     co_us_transfontanela = models.BigIntegerField(blank=True, null=True)
#     dt_tomografia_computadorizada = models.DateTimeField(blank=True, null=True)
#     co_tomografia_computadorizada = models.BigIntegerField(blank=True, null=True)
#     dt_ressonancia_magnetica = models.DateTimeField(blank=True, null=True)
#     co_ressonancia_magnetica = models.BigIntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_ficha_zika_microcefalia'
#         unique_together = (('co_revisao', 'co_seq_cds_ficha_zica_micrcfl'),)
#
#
# class TlCdsPic(models.Model):
#     co_cds_pic = models.BigIntegerField()
#     no_cds_pic = models.CharField(max_length=255, blank=True, null=True)
#     no_cds_pic_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_pic'
#         unique_together = (('co_revisao', 'co_cds_pic'),)
#
#
# class TlCdsProced(models.Model):
#     co_cds_ficha_proced = models.BigIntegerField(blank=True, null=True)
#     co_local_atend = models.BigIntegerField(blank=True, null=True)
#     co_seq_cds_proced = models.BigIntegerField()
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     st_escuta_inicial = models.IntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_proced'
#         unique_together = (('co_revisao', 'co_seq_cds_proced'),)
#
#
# class TlCdsProf(models.Model):
#     co_seq_cds_prof = models.BigIntegerField()
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cbo_2002 = models.CharField(max_length=10, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=255, blank=True, null=True)
#     co_unico_cds_prof = models.CharField(max_length=40, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_prof'
#         unique_together = (('co_revisao', 'co_seq_cds_prof'),)
#
#
# class TlCdsTipoAtendNasf(models.Model):
#     co_cds_tipo_atend_nasf = models.BigIntegerField()
#     no_cds_tipo_atend_nasf = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_tipo_atend_nasf'
#         unique_together = (('co_revisao', 'co_cds_tipo_atend_nasf'),)
#
#
# class TlCdsTipoAtivCol(models.Model):
#     co_cds_tipo_ativ_col = models.BigIntegerField()
#     no_cds_tipo_ativ_col = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_tipo_ativ_col'
#         unique_together = (('co_revisao', 'co_cds_tipo_ativ_col'),)
#
#
# class TlCdsTipoConduta(models.Model):
#     co_cds_tipo_conduta = models.BigIntegerField()
#     no_cds_tipo_conduta = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_tipo_conduta'
#         unique_together = (('co_revisao', 'co_cds_tipo_conduta'),)
#
#
# class TlCdsTipoCuidador(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_tipo_cuidador = models.BigIntegerField()
#     no_cds_tipo_cuidador = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_tipo_cuidador'
#         unique_together = (('co_revisao', 'co_cds_tipo_cuidador'),)
#
#
# class TlCdsTipoImovel(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_tipo_imovel = models.BigIntegerField()
#     no_cds_tipo_imovel = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_tipo_imovel'
#         unique_together = (('co_revisao', 'co_cds_tipo_imovel'),)
#
#
# class TlCdsTipoSituacaoPresente(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_tipo_situacao_presente = models.BigIntegerField()
#     no_cds_tipo_situacao_presente = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_tipo_situacao_presente'
#         unique_together = (('co_revisao', 'co_cds_tipo_situacao_presente'),)
#
#
# class TlCdsTipoVigSaudeBucal(models.Model):
#     co_cds_tipo_vig_saude_bucal = models.BigIntegerField()
#     no_cds_tipo_vig_saude_bucal = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_tipo_vig_saude_bucal'
#         unique_together = (('co_revisao', 'co_cds_tipo_vig_saude_bucal'),)
#
#
# class TlCdsVacina(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_vacina = models.BigIntegerField()
#     co_estrategia_vacinacao = models.BigIntegerField(blank=True, null=True)
#     co_imunobiologico = models.BigIntegerField(blank=True, null=True)
#     co_dose_imunobiologico = models.BigIntegerField(blank=True, null=True)
#     ds_lote = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_filtro = models.CharField(max_length=255, blank=True, null=True)
#     no_fabricante = models.CharField(max_length=255, blank=True, null=True)
#     no_fabricante_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_cds_vacinacao = models.BigIntegerField(blank=True, null=True)
#     co_grupo_atendimento = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_vacina'
#         unique_together = (('co_revisao', 'co_seq_cds_vacina'),)
#
#
# class TlCdsVacinacao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cds_vacinacao = models.BigIntegerField()
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     co_local_atend = models.BigIntegerField(blank=True, null=True)
#     st_viajante = models.IntegerField(blank=True, null=True)
#     st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_puerpera = models.IntegerField(blank=True, null=True)
#     co_cds_ficha_vacinacao = models.BigIntegerField(blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_vacinacao'
#         unique_together = (('co_revisao', 'co_seq_cds_vacinacao'),)
#
#
# class TlCdsVisitaDomDesfecho(models.Model):
#     co_cds_visita_dom_desfecho = models.BigIntegerField()
#     no_cds_visita_dom_desfecho = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_visita_dom_desfecho'
#         unique_together = (('co_revisao', 'co_cds_visita_dom_desfecho'),)
#
#
# class TlCdsVisitaDomMotivo(models.Model):
#     co_cds_visita_dom_motivo = models.BigIntegerField()
#     no_cds_visita_dom_motivo = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_visita_dom_motivo'
#         unique_together = (('co_revisao', 'co_cds_visita_dom_motivo'),)
#
#
# class TlCdsVisitaDomiciliar(models.Model):
#     co_cds_ficha_visita_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_seq_cds_visita_domiciliar = models.BigIntegerField()
#     dt_nascimento = models.DateTimeField(blank=True, null=True)
#     nu_cartao_sus = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=255, blank=True, null=True)
#     st_acompanhada_outro_prof = models.IntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cds_turno = models.BigIntegerField(blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     co_cds_visita_dom_desfecho = models.BigIntegerField(blank=True, null=True)
#     tp_cds_imovel = models.BigIntegerField(blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     nu_peso = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
#     nu_altura = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
#     nu_cpf_cidadao = models.CharField(max_length=11, blank=True, null=True)
#     tp_glicemia = models.IntegerField(blank=True, null=True)
#     nu_medicao_pressao_arterial = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_temperatura = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_glicemia = models.CharField(max_length=20, blank=True, null=True)
#     nu_latitude = models.FloatField(blank=True, null=True)
#     nu_longitude = models.FloatField(blank=True, null=True)
#     co_uuid_origem_fcd = models.CharField(max_length=44, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cds_visita_domiciliar'
#         unique_together = (('co_revisao', 'co_seq_cds_visita_domiciliar'),)
#
#
# class TlCfgAgendaOnlineDetalhe(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cfg_agenda_online_dtlh = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_dia_semana = models.BigIntegerField(blank=True, null=True)
#     ds_horario = models.CharField(max_length=5, blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     uuid_horario_agenda_online = models.CharField(max_length=36, blank=True, null=True)
#     st_registro_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cfg_agenda_online_detalhe'
#
#
# class TlCiapCid10(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ciap = models.BigIntegerField()
#     co_cid10 = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ciap_cid10'
#         unique_together = (('co_revisao', 'co_ciap', 'co_cid10'),)
#
#
# class TlCidadao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_unico_cidadao_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     co_unico_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     co_seq_cidadao = models.BigIntegerField()
#     st_desconhece_nome_mae = models.IntegerField(blank=True, null=True)
#     st_nao_possui_cns = models.IntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     tp_sanguineo = models.BigIntegerField(blank=True, null=True)
#     nu_area = models.CharField(max_length=3, blank=True, null=True)
#     nu_micro_area = models.CharField(max_length=3, blank=True, null=True)
#     nu_nis_pis_pasep = models.CharField(max_length=50, blank=True, null=True)
#     dt_atualizado = models.DateTimeField(blank=True, null=True)
#     nu_cns_responsavel = models.CharField(max_length=16, blank=True, null=True)
#     no_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_responsavel = models.DateTimeField(blank=True, null=True)
#     nu_cns_cuidador = models.CharField(max_length=16, blank=True, null=True)
#     no_cuidador = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_cuidador = models.DateTimeField(blank=True, null=True)
#     tp_cds_cuidador = models.BigIntegerField(blank=True, null=True)
#     co_unico_cidadao = models.CharField(max_length=96, blank=True, null=True)
#     co_nacionalidade = models.BigIntegerField(blank=True, null=True)
#     co_pais_nascimento = models.BigIntegerField(blank=True, null=True)
#     co_unico_ultima_ficha = models.CharField(max_length=96, blank=True, null=True)
#     dt_ultima_ficha = models.DateField(blank=True, null=True)
#     st_registro_cadsus = models.IntegerField(blank=True, null=True)
#     dt_atualizado_cadsus = models.DateField(blank=True, null=True)
#     st_desconhece_nome_pai = models.IntegerField(blank=True, null=True)
#     dt_naturalizacao = models.DateTimeField(blank=True, null=True)
#     dt_entrada_brasil = models.DateTimeField(blank=True, null=True)
#     nu_portaria_naturalizacao = models.CharField(max_length=16, blank=True, null=True)
#     st_fora_area = models.IntegerField(blank=True, null=True)
#     st_infrm_orientacao_sexual = models.IntegerField(blank=True, null=True)
#     tp_orientacao_sexual = models.CharField(max_length=25, blank=True, null=True)
#     st_infrm_identidade_genero = models.IntegerField(blank=True, null=True)
#     tp_identidade_genero = models.CharField(max_length=25, blank=True, null=True)
#     st_compartilhamento_prontuario = models.IntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_nao_possui_cuidador = models.IntegerField(blank=True, null=True)
#     dt_ultima_alteracao_cns = models.DateTimeField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     no_cidadao = models.CharField(max_length=500, blank=True, null=True)
#     no_cidadao_filtro = models.CharField(max_length=600, blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     co_escolaridade = models.BigIntegerField(blank=True, null=True)
#     co_raca_cor = models.BigIntegerField(blank=True, null=True)
#     co_etnia = models.BigIntegerField(blank=True, null=True)
#     co_estado_civil = models.BigIntegerField(blank=True, null=True)
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     dt_obito = models.DateField(blank=True, null=True)
#     no_mae = models.CharField(max_length=500, blank=True, null=True)
#     no_mae_filtro = models.CharField(max_length=600, blank=True, null=True)
#     no_pai = models.CharField(max_length=500, blank=True, null=True)
#     no_pai_filtro = models.CharField(max_length=600, blank=True, null=True)
#     no_social = models.CharField(max_length=255, blank=True, null=True)
#     st_faleceu = models.IntegerField(blank=True, null=True)
#     nu_documento_obito = models.CharField(max_length=255, blank=True, null=True)
#     st_dados_obito_cadsus = models.IntegerField(blank=True, null=True)
#     no_localidade_exterior = models.CharField(max_length=255, blank=True, null=True)
#     co_pais_exterior = models.BigIntegerField(blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_localidade_endereco = models.BigIntegerField(blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     nu_telefone_residencial = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_celular = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_contato = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo_para_exibicao = models.IntegerField(blank=True, null=True)
#     st_unificado = models.IntegerField(blank=True, null=True)
#     st_territorio_utiliza_cpf = models.IntegerField(blank=True, null=True)
#     nu_cpf_cuidador = models.CharField(max_length=11, blank=True, null=True)
#     nu_cpf_responsavel = models.CharField(max_length=11, blank=True, null=True)
#     no_tipo_sanguineo = models.CharField(max_length=22, blank=True, null=True)
#     no_sexo = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cidadao'
#         unique_together = (('co_revisao', 'co_seq_cidadao'),)
#
#
# class TlCidadaoGrupo(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cidadao_grupo = models.BigIntegerField(primary_key=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     nu_uuid_ultima_ficha = models.CharField(max_length=96, blank=True, null=True)
#     nu_uuid_origem = models.CharField(max_length=96, blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_cidadao_master = models.BigIntegerField(blank=True, null=True)
#     co_cidadao_unificado = models.BigIntegerField(blank=True, null=True)
#     dt_atualizacao = models.DateTimeField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cidadao_grupo'
#         unique_together = (('co_seq_cidadao_grupo', 'co_revisao'),)
#
#
# class TlCidadaoGrupoAtivCol(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cidadao_grupo = models.BigIntegerField(primary_key=True)
#     co_unico_cidadao_grupo = models.CharField(max_length=96, blank=True, null=True)
#     no_cidadao_grupo = models.CharField(max_length=255, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     co_sexo = models.IntegerField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cidadao_grupo_ativ_col'
#         unique_together = (('co_seq_cidadao_grupo', 'co_revisao'),)
#
#
# class TlCidadaoNucleoFamiliar(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cidadao_nucleo_familiar = models.BigIntegerField()
#     dt_ultima_atualizacao = models.DateField(blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     nu_cpf_cns_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     st_responsavel = models.IntegerField(blank=True, null=True)
#     st_mudou_se = models.IntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cidadao_nucleo_familiar'
#         unique_together = (('co_revisao', 'co_seq_cidadao_nucleo_familiar'),)
#
#
# class TlCidadaoVinculacaoEquipe(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cidadao_vinculacao_eqp = models.BigIntegerField(primary_key=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     co_unico_ficha = models.CharField(max_length=96, blank=True, null=True)
#     co_unico_cadastro_individual = models.CharField(max_length=96, blank=True, null=True)
#     st_envio = models.IntegerField(blank=True, null=True)
#     ds_versao_ficha = models.CharField(max_length=30, blank=True, null=True)
#     st_usar_cadastro_individual = models.IntegerField(blank=True, null=True)
#     st_saida_cadastro_obito = models.IntegerField(blank=True, null=True)
#     st_saida_cadastro_territorio = models.IntegerField(blank=True, null=True)
#     dt_atualizacao_cadastro = models.DateTimeField(blank=True, null=True)
#     co_prof_cadastrante_cds = models.BigIntegerField(blank=True, null=True)
#     co_lotacao_cadastrante_pec = models.BigIntegerField(blank=True, null=True)
#     tp_cds_origem = models.BigIntegerField(blank=True, null=True)
#     nu_cnes = models.CharField(max_length=7, blank=True, null=True)
#     nu_ine = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cidadao_vinculacao_equipe'
#         unique_together = (('co_seq_cidadao_vinculacao_eqp', 'co_revisao'),)
#
#
# class TlCns(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_cns = models.BigIntegerField()
#     nu_cns = models.CharField(max_length=15, blank=True, null=True)
#     st_definitivo = models.IntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_cns'
#         unique_together = (('co_revisao', 'co_seq_cns'),)
#
#
# class TlCompartilhamentoProntuario(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_compartilha_prontuario = models.BigIntegerField()
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_usuario = models.BigIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     dt_ultima_alteracao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_compartilhamento_prontuario'
#         unique_together = (('co_revisao', 'co_seq_compartilha_prontuario'),)
#
#
# class TlComplexidade(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_complexidade = models.CharField(max_length=100, blank=True, null=True)
#     sg_complexidade = models.CharField(max_length=2, blank=True, null=True)
#     co_complexidade = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_complexidade'
#         unique_together = (('co_revisao', 'co_complexidade'),)
#
#
# class TlConfigAgendaDetalhe(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_config_agenda_detalhe = models.BigIntegerField()
#     co_dia_semana = models.BigIntegerField(blank=True, null=True)
#     co_periodo = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     horario_inicial = models.CharField(max_length=5, blank=True, null=True)
#     horario_final = models.CharField(max_length=5, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_config_agenda_detalhe'
#         unique_together = (('co_revisao', 'co_seq_config_agenda_detalhe'),)
#
#
# class TlConfigAgendaFechamento(models.Model):
#     dt_inicio = models.DateTimeField(blank=True, null=True)
#     dt_fim = models.DateTimeField(blank=True, null=True)
#     ds_motivo = models.CharField(max_length=4000, blank=True, null=True)
#     co_seq_config_agenda_fechament = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     no_ident_motivo_fechamento = models.CharField(max_length=30, blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     st_registro_ativo = models.IntegerField(blank=True, null=True)
#     uuid_fechamento = models.CharField(max_length=36, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_config_agenda_fechamento'
#         unique_together = (('co_revisao', 'co_seq_config_agenda_fechament'),)
#
#
# class TlConfigAtencaoDomiciliar(models.Model):
#     co_seq_config_atencao_domicilr = models.BigIntegerField()
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     qt_tempo_duracao_consulta = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_config_atencao_domiciliar'
#         unique_together = (('co_revisao', 'co_seq_config_atencao_domicilr'),)
#
#
# class TlConfigAtendDomiciliar(models.Model):
#     co_seq_config_atend_domiciliar = models.BigIntegerField()
#     co_equipe_pai = models.BigIntegerField(blank=True, null=True)
#     co_equipe_filho = models.BigIntegerField(blank=True, null=True)
#     tp_config_atend_domiciliar = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_config_atencao_domiciliar = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_config_atend_domiciliar'
#         unique_together = (('co_revisao', 'co_seq_config_atend_domiciliar'),)
#
#
# class TlConfigperiodoDiasemana(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_config_periodo = models.BigIntegerField(blank=True, null=True)
#     co_dia_semana = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_configperiodo_diasemana'
#
#
# class TlConfiguracaoHorario(models.Model):
#     co_seq_config_periodo = models.BigIntegerField()
#     hora_inicial_primeiro_periodo = models.CharField(max_length=10, blank=True, null=True)
#     hora_final_primeiro_periodo = models.CharField(max_length=10, blank=True, null=True)
#     hora_inicial_segundo_periodo = models.CharField(max_length=10, blank=True, null=True)
#     hora_final_segundo_periodo = models.CharField(max_length=10, blank=True, null=True)
#     hora_inicial_terceiro_periodo = models.CharField(max_length=10, blank=True, null=True)
#     hora_final_terceiro_periodo = models.CharField(max_length=10, blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     tempo_duracao_consulta = models.IntegerField(blank=True, null=True)
#     hora_inicial_quarto_periodo = models.CharField(max_length=10, blank=True, null=True)
#     hora_final_quarto_periodo = models.CharField(max_length=10, blank=True, null=True)
#     hora_inicial_atend_unidade = models.CharField(max_length=10, blank=True, null=True)
#     hora_final_atend_unidade = models.CharField(max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_configuracao_horario'
#         unique_together = (('co_revisao', 'co_seq_config_periodo'),)
#
#
# class TlContextoPergunta(models.Model):
#     co_contexto_pergunta = models.BigIntegerField()
#     ds_contexto_pergunta = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_contexto_pergunta'
#         unique_together = (('co_revisao', 'co_contexto_pergunta'),)
#
#
# class TlDente(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_parte_bucal = models.BigIntegerField()
#     co_sextante = models.BigIntegerField(blank=True, null=True)
#     nu_dente = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_dente'
#         unique_together = (('co_revisao', 'co_parte_bucal'),)
#
#
# class TlEncaminhamento(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_encaminhamento = models.BigIntegerField()
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_especialidade_sisreg = models.BigIntegerField(blank=True, null=True)
#     ds_complemento = models.CharField(max_length=200, blank=True, null=True)
#     co_cid10 = models.BigIntegerField(blank=True, null=True)
#     co_ciap = models.BigIntegerField(blank=True, null=True)
#     co_classificacao_risco_encam = models.BigIntegerField(blank=True, null=True)
#     ds_motivo_encaminhamento = models.CharField(max_length=1000, blank=True, null=True)
#     ds_observacao = models.CharField(max_length=600, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_encaminhamento'
#         unique_together = (('co_revisao', 'co_seq_encaminhamento'),)
#
#
# class TlEquipe(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_equipe = models.BigIntegerField()
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     tp_equipe = models.BigIntegerField(blank=True, null=True)
#     ds_area = models.CharField(max_length=255, blank=True, null=True)
#     no_equipe = models.CharField(max_length=255, blank=True, null=True)
#     no_equipe_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_equipe'
#         unique_together = (('co_revisao', 'co_seq_equipe'),)
#
#
# class TlEvolAvalTpVigSaudeBucl(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_evolucao_avaliacao = models.BigIntegerField()
#     co_tipo_vig_saude_bucal = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evol_aval_tp_vig_saude_bucl'
#         unique_together = (('co_revisao', 'co_evolucao_avaliacao', 'co_tipo_vig_saude_bucal'),)
#
#
# class TlEvolucaoAvaliacao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField()
#     ds_avaliacao = models.TextField(blank=True, null=True)
#     st_necessidade_de_protese = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_avaliacao'
#         unique_together = (('co_revisao', 'co_atend_prof'),)
#
#
# class TlEvolucaoAvaliacaoCiapCid(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_evolucao_aval_ciap_cid = models.BigIntegerField()
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_ciap = models.BigIntegerField(blank=True, null=True)
#     co_cid10 = models.BigIntegerField(blank=True, null=True)
#     ds_nota = models.CharField(max_length=400, blank=True, null=True)
#     co_unico_problema = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_avaliacao_ciap_cid'
#         unique_together = (('co_revisao', 'co_seq_evolucao_aval_ciap_cid'),)
#
#
# class TlEvolucaoDente(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_evolucao_dente = models.BigIntegerField()
#     co_dente = models.BigIntegerField(blank=True, null=True)
#     co_odontograma = models.BigIntegerField(blank=True, null=True)
#     st_coroa_cima = models.BigIntegerField(blank=True, null=True)
#     st_coroa_baixo = models.BigIntegerField(blank=True, null=True)
#     st_coroa_direita = models.BigIntegerField(blank=True, null=True)
#     st_coroa_esquerda = models.BigIntegerField(blank=True, null=True)
#     st_coroa_centro = models.BigIntegerField(blank=True, null=True)
#     st_raiz = models.BigIntegerField(blank=True, null=True)
#     st_face = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_dente'
#         unique_together = (('co_revisao', 'co_seq_evolucao_dente'),)
#
#
# class TlEvolucaoObjetivo(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField()
#     ds_objetivo = models.TextField(blank=True, null=True)
#     st_necessidade_especial = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_objetivo'
#         unique_together = (('co_revisao', 'co_atend_prof'),)
#
#
# class TlEvolucaoOdonto(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_evolucao_odonto = models.BigIntegerField()
#     tp_parte_bucal = models.BigIntegerField(blank=True, null=True)
#     ds_parte_bucal = models.CharField(max_length=255, blank=True, null=True)
#     ds_outro = models.CharField(max_length=400, blank=True, null=True)
#     co_atend_prof_odonto = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     ds_evolucao = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_odonto'
#         unique_together = (('co_revisao', 'co_seq_evolucao_odonto'),)
#
#
# class TlEvolucaoOdontoParteBucal(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_evolucao_odonto = models.BigIntegerField()
#     co_parte_bucal = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_odonto_parte_bucal'
#         unique_together = (('co_revisao', 'co_evolucao_odonto', 'co_parte_bucal'),)
#
#
# class TlEvolucaoOdontoProced(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_evolucao_odonto = models.BigIntegerField()
#     co_proced = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_odonto_proced'
#         unique_together = (('co_revisao', 'co_evolucao_odonto', 'co_proced'),)
#
#
# class TlEvolucaoPlano(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField()
#     ds_plano = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_plano'
#         unique_together = (('co_revisao', 'co_atend_prof'),)
#
#
# class TlEvolucaoPlanoCiap(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_evolucao_plano_ciap = models.BigIntegerField()
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_ciap = models.BigIntegerField(blank=True, null=True)
#     ds_nota = models.CharField(max_length=400, blank=True, null=True)
#     co_proced = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_plano_ciap'
#         unique_together = (('co_revisao', 'co_seq_evolucao_plano_ciap'),)
#
#
# class TlEvolucaoSubjetivo(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField()
#     ds_subjetivo = models.TextField(blank=True, null=True)
#     ds_acompanhado_especialidade = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_subjetivo'
#         unique_together = (('co_revisao', 'co_atend_prof'),)
#
#
# class TlEvolucaoSubjetivoCiap(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_evolucao_subjetivo_ciap = models.BigIntegerField()
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_ciap = models.BigIntegerField(blank=True, null=True)
#     ds_nota = models.CharField(max_length=400, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_evolucao_subjetivo_ciap'
#         unique_together = (('co_revisao', 'co_seq_evolucao_subjetivo_ciap'),)
#
#
# class TlExameClearanceCreatina(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_clearance_creatn = models.BigIntegerField(blank=True, null=True)
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     vl_clearance_creatina = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_clearance_creatina'
#
#
# class TlExameColesterolHdl(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_colesterol_hdl = models.BigIntegerField(blank=True, null=True)
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     vl_colesterol_hdl = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_colesterol_hdl'
#
#
# class TlExameColesterolLdl(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_colesterol_ldl = models.BigIntegerField(blank=True, null=True)
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     vl_colesterol_ldl = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_colesterol_ldl'
#
#
# class TlExameColesterolTotal(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_colesterol_total = models.BigIntegerField(blank=True, null=True)
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     vl_colesterol_total = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_colesterol_total'
#
#
# class TlExameCreatinaSerica(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_creatina_sericia = models.BigIntegerField(blank=True, null=True)
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     vl_creatina_serica = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_creatina_serica'
#
#
# class TlExameDetalhe(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_detalhe = models.BigIntegerField()
#     ds_exame_detalhe = models.CharField(max_length=255, blank=True, null=True)
#     tp_opcao = models.BigIntegerField(blank=True, null=True)
#     sg_unidade_medida = models.CharField(max_length=25, blank=True, null=True)
#     vl_comprimento = models.IntegerField(blank=True, null=True)
#     vl_minimo = models.FloatField(blank=True, null=True)
#     vl_maximo = models.FloatField(blank=True, null=True)
#     vl_precisao_decimal = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_detalhe'
#         unique_together = (('co_revisao', 'co_seq_exame_detalhe'),)
#
#
# class TlExameDetalheResultado(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_detalhe_resultado = models.BigIntegerField()
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     co_proced_exame_detalhe = models.BigIntegerField(blank=True, null=True)
#     tp_resultado = models.BigIntegerField(blank=True, null=True)
#     nu_resultado = models.FloatField(blank=True, null=True)
#     ds_resultado = models.CharField(max_length=800, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_detalhe_resultado'
#         unique_together = (('co_revisao', 'co_seq_exame_detalhe_resultado'),)
#
#
# class TlExameHemoglobinaGlicada(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_hemoglobina_glicd = models.BigIntegerField()
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     vl_hemoglobina_glicada = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_hemoglobina_glicada'
#         unique_together = (('co_revisao', 'co_seq_exame_hemoglobina_glicd'),)
#
#
# class TlExamePrenatal(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_prenatal = models.BigIntegerField()
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     qt_semana_gestacional_eco = models.IntegerField(blank=True, null=True)
#     qt_dia_gestacional_eco = models.IntegerField(blank=True, null=True)
#     dt_provavel_parto_eco = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_prenatal'
#         unique_together = (('co_revisao', 'co_seq_exame_prenatal'),)
#
#
# class TlExamePuericultura(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame = models.BigIntegerField()
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     co_exame = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_puericultura'
#         unique_together = (('co_revisao', 'co_seq_exame'),)
#
#
# class TlExameRequisitado(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_requisitado = models.BigIntegerField()
#     dt_resultado = models.DateTimeField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField(blank=True, null=True)
#     co_requisicao_exame = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof_resultado = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     st_conferido = models.IntegerField(blank=True, null=True)
#     dt_realizacao = models.DateTimeField(blank=True, null=True)
#     dt_solicitacao = models.DateTimeField(blank=True, null=True)
#     co_proced_exame_especifico = models.BigIntegerField(blank=True, null=True)
#     ds_resultado = models.TextField(blank=True, null=True)
#     ds_observacao = models.CharField(max_length=300, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_requisitado'
#         unique_together = (('co_revisao', 'co_seq_exame_requisitado'),)
#
#
# class TlExameTriglicerideos(models.Model):
#     co_revisao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_exame_triglicerideos = models.BigIntegerField(blank=True, null=True)
#     co_exame_requisitado = models.BigIntegerField(blank=True, null=True)
#     vl_triglicerideos = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_exame_triglicerideos'
#
#
# class TlFamilia(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_familia = models.BigIntegerField()
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     nu_cpf_cns_responsavel = models.CharField(max_length=255, blank=True, null=True)
#     nu_prontuario_familiar = models.CharField(max_length=255, blank=True, null=True)
#     dt_nascimento_responsavel = models.DateField(blank=True, null=True)
#     co_renda_familiar = models.BigIntegerField(blank=True, null=True)
#     qt_membro = models.IntegerField(blank=True, null=True)
#     co_cds_domicilio = models.BigIntegerField(blank=True, null=True)
#     dt_reside_desde = models.DateField(blank=True, null=True)
#     st_responsavel_cadastrado = models.IntegerField(blank=True, null=True)
#     st_responsavel_declarado = models.IntegerField(blank=True, null=True)
#     st_responsavel_vivo = models.IntegerField(blank=True, null=True)
#     st_responsavel_unico = models.IntegerField(blank=True, null=True)
#     st_responsavel_ainda_reside = models.IntegerField(blank=True, null=True)
#     st_familia_ainda_reside = models.IntegerField(blank=True, null=True)
#     st_informacao_suficiente = models.IntegerField(blank=True, null=True)
#     st_domicilio_ativo = models.IntegerField(blank=True, null=True)
#     dt_atualizacao_fcd = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_familia'
#         unique_together = (('co_revisao', 'co_seq_familia'),)
#
#
# class TlFichaZikaTipoExame(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ficha_zika_tipo_exame = models.BigIntegerField()
#     no_ficha_zika_tipo_exame = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_ficha_zika_tipo_exame'
#         unique_together = (('co_revisao', 'co_ficha_zika_tipo_exame'),)
#
#
# class TlFormaFarmaceutica(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_forma_farmaceutica = models.BigIntegerField()
#     no_forma_farmaceutica = models.CharField(max_length=255, blank=True, null=True)
#     no_forma_farmaceutica_filtro = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_forma_farmaceutica'
#         unique_together = (('co_revisao', 'co_forma_farmaceutica'),)
#
#
# class TlGestorEstadual(models.Model):
#     co_ator_papel = models.BigIntegerField()
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_gestor_estadual'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlGestorMunicipal(models.Model):
#     co_ator_papel = models.BigIntegerField()
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_gestor_municipal'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlGrupoAtivCol(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_grupo_ativ_col = models.BigIntegerField(primary_key=True)
#     co_unico_grupo = models.CharField(max_length=96, blank=True, null=True)
#     no_grupo = models.CharField(max_length=255, blank=True, null=True)
#     sg_grupo = models.CharField(max_length=255, blank=True, null=True)
#     tp_grupo = models.CharField(max_length=32, blank=True, null=True)
#     co_cor_grupo = models.IntegerField(blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     dt_ultima_atualizacao = models.DateTimeField(blank=True, null=True)
#     dt_ultima_atividade = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_grupo_ativ_col'
#         unique_together = (('co_seq_grupo_ativ_col', 'co_revisao'),)
#
#
# class TlGrupoAtivColCidadao(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_grp_ativ_col_cidadao = models.BigIntegerField(primary_key=True)
#     co_grupo = models.BigIntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     st_cidadao = models.CharField(max_length=32, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_grupo_ativ_col_cidadao'
#         unique_together = (('co_seq_grp_ativ_col_cidadao', 'co_revisao'),)
#
#
# class TlGrupoAtivColProf(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_grp_ativ_col_prof = models.BigIntegerField(primary_key=True)
#     co_grupo = models.BigIntegerField(blank=True, null=True)
#     co_prof = models.BigIntegerField(blank=True, null=True)
#     st_prof = models.CharField(max_length=32, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_grupo_ativ_col_prof'
#         unique_together = (('co_seq_grp_ativ_col_prof', 'co_revisao'),)
#
#
# class TlGrupoEspecialidade(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_grupo_especialidade = models.BigIntegerField()
#     no_grupo_especialidade = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_grupo_especialidade'
#         unique_together = (('co_revisao', 'co_grupo_especialidade'),)
#
#
# class TlImunobiologicoLote(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_imunobiologico_lote = models.BigIntegerField(primary_key=True)
#     co_imunobiologico = models.BigIntegerField(blank=True, null=True)
#     ds_lote = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_filtro = models.CharField(max_length=255, blank=True, null=True)
#     ds_lote_fabricante_filtro = models.CharField(max_length=255, blank=True, null=True)
#     dt_validade = models.DateField(blank=True, null=True)
#     co_imunobiologico_fabricante = models.BigIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_imunobiologico_lote'
#         unique_together = (('co_seq_imunobiologico_lote', 'co_revisao'),)
#
#
# class TlIntegracaoHorus(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField()
#     dt_habilitar_integracao = models.DateTimeField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     tp_erro_teste_horus = models.CharField(max_length=50, blank=True, null=True)
#     co_unidade_saude_padrao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_integracao_horus'
#         unique_together = (('co_revisao', 'co_unidade_saude'),)
#
#
# class TlJustificativaAgenda(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_justificativa_agendamnt = models.BigIntegerField()
#     co_agendamento = models.BigIntegerField(blank=True, null=True)
#     co_lotacao_justificativa = models.BigIntegerField(blank=True, null=True)
#     ds_justificativa = models.CharField(max_length=2000, blank=True, null=True)
#     dt_justificativa = models.DateTimeField(blank=True, null=True)
#     co_origem_justificativa = models.BigIntegerField(blank=True, null=True)
#     ds_opcao_justificativa = models.CharField(max_length=44, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_justificativa_agenda'
#         unique_together = (('co_revisao', 'co_seq_justificativa_agendamnt'),)
#
#
# class TlJustificativaProntuario(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_justificativa_prontuar = models.BigIntegerField()
#     dt_acesso_prontuario = models.DateTimeField(blank=True, null=True)
#     ds_justificativa = models.CharField(max_length=1000, blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_usuario = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_justificativa_prontuario'
#         unique_together = (('co_revisao', 'co_seq_justificativa_prontuar'),)
#
#
# class TlJustificativaStatusCiddao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_justifica_inativ_cidada = models.BigIntegerField()
#     dt_justificativa = models.DateTimeField(blank=True, null=True)
#     ds_justificativa = models.CharField(max_length=1000, blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     st_cidadao = models.IntegerField(blank=True, null=True)
#     co_usuario = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_justificativa_status_ciddao'
#         unique_together = (('co_revisao', 'co_seq_justifica_inativ_cidada'),)
#
#
# class TlLembrete(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_lembrete = models.BigIntegerField()
#     dt_prontuario_lembrete = models.DateTimeField(blank=True, null=True)
#     ds_lembrete = models.TextField(blank=True, null=True)
#     st_desativado = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_ultimo_lembrete_evolucao = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_lembrete'
#         unique_together = (('co_revisao', 'co_seq_lembrete'),)
#
#
# class TlLembreteEvolucao(models.Model):
#     co_seq_lembrete_evolucao = models.BigIntegerField()
#     ds_lembrete = models.TextField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     dt_prontuario_lembrete = models.DateTimeField(blank=True, null=True)
#     co_visibilidade_lembrete = models.BigIntegerField(blank=True, null=True)
#     co_lembrete = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_lembrete_evolucao'
#         unique_together = (('co_revisao', 'co_seq_lembrete_evolucao'),)
#
#
# class TlListaMedicamento(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_lista_medicamento = models.BigIntegerField()
#     no_lista_medicamento = models.CharField(max_length=100, blank=True, null=True)
#     tp_receita = models.BigIntegerField(blank=True, null=True)
#     nu_dias_validade = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_lista_medicamento'
#         unique_together = (('co_revisao', 'co_lista_medicamento'),)
#
#
# class TlLogradouro(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_logradouro = models.BigIntegerField()
#     nu_dne = models.CharField(max_length=8, blank=True, null=True)
#     no_preposicao = models.CharField(max_length=6, blank=True, null=True)
#     no_logradouro = models.CharField(max_length=72, blank=True, null=True)
#     nu_cep = models.CharField(max_length=8, blank=True, null=True)
#     nu_inicial_trecho = models.CharField(max_length=22, blank=True, null=True)
#     nu_final_trecho = models.CharField(max_length=22, blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#     co_titulo_patente = models.BigIntegerField(blank=True, null=True)
#     tp_paridade = models.BigIntegerField(blank=True, null=True)
#     sg_tipo_registro = models.CharField(max_length=1, blank=True, null=True)
#     no_logradouro_filtro = models.CharField(max_length=150, blank=True, null=True)
#     no_logradouro_exibicao = models.CharField(max_length=150, blank=True, null=True)
#     nu_lote = models.CharField(max_length=22, blank=True, null=True)
#     no_complemento = models.CharField(max_length=72, blank=True, null=True)
#     ds_letra_numero_complemento = models.CharField(max_length=22, blank=True, null=True)
#     co_bairro_dne = models.CharField(max_length=8, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_logradouro'
#         unique_together = (('co_revisao', 'co_logradouro'),)
#
#
# class TlLotacao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     dt_desativacao_lotacao = models.DateTimeField(blank=True, null=True)
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     co_prof = models.BigIntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_equipe = models.BigIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField()
#     st_alterada_manual = models.IntegerField(blank=True, null=True)
#     st_importada = models.IntegerField(blank=True, null=True)
#     st_agenda_alterada_manual = models.IntegerField(blank=True, null=True)
#     dt_ultima_tentativa_envio = models.DateTimeField(blank=True, null=True)
#     st_sincronizacao = models.CharField(max_length=48, blank=True, null=True)
#     st_ativo_agenda_online = models.IntegerField(blank=True, null=True)
#     ds_ultima_tentativa = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_lotacao'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlMedicamento(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_medicamento = models.BigIntegerField()
#     no_principio_ativo = models.CharField(max_length=400, blank=True, null=True)
#     ds_concentracao = models.CharField(max_length=200, blank=True, null=True)
#     co_forma_farmaceutica = models.BigIntegerField(blank=True, null=True)
#     ds_unidade_fornecimento = models.CharField(max_length=200, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_medicamento'
#         unique_together = (('co_revisao', 'co_seq_medicamento'),)
#
#
# class TlMedicamentoCatmat(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_medicamento_catmat = models.BigIntegerField()
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_principio_ativo = models.BigIntegerField(blank=True, null=True)
#     co_unidade_fornecimento = models.BigIntegerField(blank=True, null=True)
#     co_catmat = models.CharField(max_length=20, blank=True, null=True)
#     ds_volume = models.CharField(max_length=100, blank=True, null=True)
#     co_medicamento = models.BigIntegerField(blank=True, null=True)
#     nu_frequencia_instalacao = models.IntegerField(blank=True, null=True)
#     co_rename = models.CharField(max_length=28, blank=True, null=True)
#     no_medicamento_filtro = models.CharField(max_length=600, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_medicamento_catmat'
#         unique_together = (('co_revisao', 'co_medicamento_catmat'),)
#
#
# class TlMedicamentoUsoContinuo(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_medicament_uso_continuo = models.BigIntegerField()
#     co_medicamento = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_ultima_receita_medicamento = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_medicamento_uso_continuo'
#         unique_together = (('co_revisao', 'co_seq_medicament_uso_continuo'),)
#
#
# class TlMedicao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_medicao = models.BigIntegerField()
#     dt_medicao = models.DateTimeField(blank=True, null=True)
#     tp_glicemia = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     nu_medicao_peso = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_altura = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_frequencia_cardiaca = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_pressao_arterial = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_perimetro_cefalico = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_frequnca_resprtria = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_temperatura = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_saturacao_o2 = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_glicemia = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_imc = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_altura_uterina = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_batimnto_cardco_ftl = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_vacinacao_em_dia = models.CharField(max_length=20, blank=True, null=True)
#     nu_perimetro_panturrilha = models.CharField(max_length=20, blank=True, null=True)
#     st_medicao_anterior = models.IntegerField(blank=True, null=True)
#     nu_medicao_circunf_abdominal = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_apgar_um = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_apgar_cinco = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_apgar_dez = models.CharField(max_length=20, blank=True, null=True)
#     tp_gravidez = models.IntegerField(blank=True, null=True)
#     tp_parto = models.IntegerField(blank=True, null=True)
#     nu_medicao_ig_semanas = models.CharField(max_length=20, blank=True, null=True)
#     nu_medicao_ig_dias = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_medicao'
#         unique_together = (('co_revisao', 'co_seq_medicao'),)
#
#
# class TlMotivoReserva(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_motivo_reserva = models.BigIntegerField()
#     no_motivo_reserva = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_motivo_reserva'
#         unique_together = (('co_revisao', 'co_motivo_reserva'),)
#
#
# class TlNeuroAlterFenot(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_neuro_alter_fenot = models.BigIntegerField(primary_key=True)
#     co_alter_fenot_detalhe = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_ultimo_alter_fenot_evolucao = models.BigIntegerField(blank=True, null=True)
#     co_unico_alter_fenot = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_neuro_alter_fenot'
#         unique_together = (('co_seq_neuro_alter_fenot', 'co_revisao'),)
#
#
# class TlNeuroAlterFenotEvolucao(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_neuro_alter_fenot_evol = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_alter_fenot_detalhe = models.BigIntegerField(blank=True, null=True)
#     st_avaliado = models.CharField(max_length=32, blank=True, null=True)
#     co_unico_neuro_alter_fenot = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_neuro_alter_fenot_evolucao'
#         unique_together = (('co_seq_neuro_alter_fenot_evol', 'co_revisao'),)
#
#
# class TlNeuroFatorRisco(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_neuro_fator_risco = models.BigIntegerField(primary_key=True)
#     co_fator_risco_detalhe = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_ultimo_fator_risco_evolucao = models.BigIntegerField(blank=True, null=True)
#     co_unico_fator_risco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_neuro_fator_risco'
#         unique_together = (('co_seq_neuro_fator_risco', 'co_revisao'),)
#
#
# class TlNeuroFatorRiscoEvolucao(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_neuro_fator_risco_evol = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_fator_risco_detalhe = models.BigIntegerField(blank=True, null=True)
#     st_avaliado = models.CharField(max_length=32, blank=True, null=True)
#     co_unico_neuro_fator_risco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_neuro_fator_risco_evolucao'
#         unique_together = (('co_seq_neuro_fator_risco_evol', 'co_revisao'),)
#
#
# class TlNeuroMarco(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_neuro_marco = models.BigIntegerField(primary_key=True)
#     co_marco_detalhe = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_ultimo_marco_evolucao = models.BigIntegerField(blank=True, null=True)
#     co_unico_marco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_neuro_marco'
#         unique_together = (('co_seq_neuro_marco', 'co_revisao'),)
#
#
# class TlNeuroMarcoEvolucao(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_neuro_marco_evolucao = models.BigIntegerField(primary_key=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_marco_detalhe = models.BigIntegerField(blank=True, null=True)
#     st_avaliado = models.CharField(max_length=32, blank=True, null=True)
#     nu_anos_idade_registro = models.IntegerField(blank=True, null=True)
#     nu_meses_idade_registro = models.IntegerField(blank=True, null=True)
#     co_unico_neuro_marco = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_neuro_marco_evolucao'
#         unique_together = (('co_seq_neuro_marco_evolucao', 'co_revisao'),)
#
#
# class TlOdontograma(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_odontograma = models.BigIntegerField()
#     co_atend_prof_odonto = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     st_protese_total_superior = models.IntegerField(blank=True, null=True)
#     st_protese_total_inferior = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_odontograma'
#         unique_together = (('co_revisao', 'co_seq_odontograma'),)
#
#
# class TlOpcaoRapidaExame(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_opcao_rapida_exame = models.BigIntegerField(primary_key=True)
#     no_opcao_rapida_exame = models.CharField(max_length=255, blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     nu_idade_minima = models.IntegerField(blank=True, null=True)
#     nu_idade_maxima = models.IntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_opcao_rapida_exame'
#         unique_together = (('co_seq_opcao_rapida_exame', 'co_revisao'),)
#
#
# class TlOrientacao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_orientacao = models.BigIntegerField()
#     ds_orientacao = models.TextField(blank=True, null=True)
#     st_orientacao_finalizada = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_orientacao'
#         unique_together = (('co_revisao', 'co_seq_orientacao'),)
#
#
# class TlPapel(models.Model):
#     co_ator_papel = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     co_lotacao = models.BigIntegerField(blank=True, null=True)
#     co_seq_papel = models.BigIntegerField()
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     no_descricao = models.CharField(max_length=270, blank=True, null=True)
#     no_descricao_grupo = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_papel'
#         unique_together = (('co_revisao', 'co_seq_papel'),)
#
#
# class TlParteBucal(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_parte_bucal = models.BigIntegerField()
#     tp_parte_bucal = models.CharField(max_length=60, blank=True, null=True)
#     ds_parte_bucal = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_parte_bucal'
#         unique_together = (('co_revisao', 'co_parte_bucal'),)
#
#
# class TlParteBucalProced(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_parte_bucal_proced = models.BigIntegerField()
#     co_proced = models.BigIntegerField(blank=True, null=True)
#     tp_parte_bucal = models.BigIntegerField(blank=True, null=True)
#     nu_dente = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_parte_bucal_proced'
#         unique_together = (('co_revisao', 'co_parte_bucal_proced'),)
#
#
# class TlPerfil(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_perfil = models.BigIntegerField()
#     no_perfil = models.CharField(max_length=100, blank=True, null=True)
#     no_perfil_filtro = models.CharField(max_length=50, blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     no_perfil_padrao = models.CharField(max_length=100, blank=True, null=True)
#     tp_perfil = models.BigIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_perfil'
#         unique_together = (('co_revisao', 'co_seq_perfil'),)
#
#
# class TlPergunta(models.Model):
#     co_contexto_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_pergunta_pai = models.BigIntegerField(blank=True, null=True)
#     co_seq_pergunta = models.BigIntegerField()
#     ds_local = models.CharField(max_length=10, blank=True, null=True)
#     ds_pergunta = models.CharField(max_length=255, blank=True, null=True)
#     tp_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_pergunta'
#         unique_together = (('co_revisao', 'co_seq_pergunta'),)
#
#
# class TlPerguntaDetalhe(models.Model):
#     co_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_pergunta_detalhe = models.BigIntegerField()
#     ds_local = models.CharField(max_length=10, blank=True, null=True)
#     ds_pergunta_detalhe = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_pergunta_detalhe'
#         unique_together = (('co_revisao', 'co_pergunta_detalhe'),)
#
#
# class TlPessoaFisicaImagem(models.Model):
#     co_seq_pessoa_fisica_imagem = models.BigIntegerField()
#     im_icone = models.BinaryField(blank=True, null=True)
#     im_conteudo = models.BinaryField(blank=True, null=True)
#     tp_imagem = models.BigIntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     no_tipo_imagem = models.CharField(max_length=24, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_pessoa_fisica_imagem'
#         unique_together = (('co_revisao', 'co_seq_pessoa_fisica_imagem'),)
#
#
# class TlPovoComunidadeTradicional(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_povo_comunidade_tradicional = models.BigIntegerField()
#     no_povo_comunidade_tradicional = models.CharField(max_length=255, blank=True, null=True)
#     no_povo_comunidade_trad_filtro = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_povo_comunidade_tradicional'
#         unique_together = (('co_revisao', 'co_povo_comunidade_tradicional'),)
#
#
# class TlPreNatal(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_pre_natal = models.BigIntegerField()
#     co_problema = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     tp_gravidez = models.BigIntegerField(blank=True, null=True)
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     dt_desfecho = models.DateTimeField(blank=True, null=True)
#     st_gravidez_planejada = models.IntegerField(blank=True, null=True)
#     st_alto_risco = models.IntegerField(blank=True, null=True)
#     co_unico_pre_natal = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_pre_natal'
#         unique_together = (('co_revisao', 'co_seq_pre_natal'),)
#
#
# class TlPrincipioAtivo(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_principio_ativo = models.BigIntegerField()
#     st_ativo = models.IntegerField(blank=True, null=True)
#     no_principio_ativo_filtro = models.CharField(max_length=200, blank=True, null=True)
#     no_principio_ativo = models.CharField(max_length=200, blank=True, null=True)
#     co_lista_medicamento = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_principio_ativo'
#         unique_together = (('co_revisao', 'co_principio_ativo'),)
#
#
# class TlProblema(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_problema = models.BigIntegerField()
#     dt_registro = models.DateTimeField(blank=True, null=True)
#     ds_outro = models.CharField(max_length=255, blank=True, null=True)
#     ds_problema_filtro = models.CharField(max_length=255, blank=True, null=True)
#     co_ciap = models.BigIntegerField(blank=True, null=True)
#     co_cid10 = models.BigIntegerField(blank=True, null=True)
#     co_ultimo_problema_evolucao = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_unico_problema = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_problema'
#         unique_together = (('co_revisao', 'co_seq_problema'),)
#
#
# class TlProblemaEvolucao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_problema_evolucao = models.BigIntegerField()
#     ds_observacao = models.CharField(max_length=255, blank=True, null=True)
#     co_situacao_problema = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_unico_problema = models.BigIntegerField(blank=True, null=True)
#     co_mes_inicio = models.BigIntegerField(blank=True, null=True)
#     co_mes_fim = models.BigIntegerField(blank=True, null=True)
#     qt_mes_inicio = models.IntegerField(blank=True, null=True)
#     qt_mes_fim = models.IntegerField(blank=True, null=True)
#     qt_ano_inicio = models.IntegerField(blank=True, null=True)
#     qt_ano_fim = models.IntegerField(blank=True, null=True)
#     nu_dia_inicio = models.IntegerField(blank=True, null=True)
#     nu_dia_fim = models.IntegerField(blank=True, null=True)
#     nu_ano_inicio = models.IntegerField(blank=True, null=True)
#     nu_ano_fim = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_problema_evolucao'
#         unique_together = (('co_revisao', 'co_seq_problema_evolucao'),)
#
#
# class TlProcedAtributoComplem(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField()
#     co_atributo_complem = models.BigIntegerField()
#     dt_competencia = models.CharField(max_length=60, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_atributo_complem'
#         unique_together = (('co_revisao', 'co_proced', 'co_atributo_complem'),)
#
#
# class TlProcedAutomatico(models.Model):
#     co_seq_proced_automatico = models.BigIntegerField()
#     co_proced = models.BigIntegerField(blank=True, null=True)
#     co_cbo = models.BigIntegerField(blank=True, null=True)
#     st_consulta_agendada = models.IntegerField(blank=True, null=True)
#     st_atend_odonto = models.IntegerField(blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_automatico'
#         unique_together = (('co_revisao', 'co_seq_proced_automatico'),)
#
#
# class TlProcedCbo(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField()
#     co_cbo = models.BigIntegerField()
#     dt_competencia = models.CharField(max_length=6, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_cbo'
#         unique_together = (('co_revisao', 'co_cbo', 'co_proced'),)
#
#
# class TlProcedCdsProced(models.Model):
#     co_cds_proced = models.BigIntegerField()
#     co_proced = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_cds_proced'
#         unique_together = (('co_revisao', 'co_cds_proced', 'co_proced'),)
#
#
# class TlProcedCid10(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_cid10 = models.BigIntegerField()
#     co_proced = models.BigIntegerField()
#     dt_competencia = models.CharField(max_length=6, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     st_cid_principal = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_cid10'
#         unique_together = (('co_revisao', 'co_cid10', 'co_proced'),)
#
#
# class TlProcedExameDetalhe(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_proced_exame_detalhe = models.BigIntegerField()
#     co_proced = models.BigIntegerField(blank=True, null=True)
#     co_exame_detalhe = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_exame_detalhe'
#         unique_together = (('co_revisao', 'co_seq_proced_exame_detalhe'),)
#
#
# class TlProcedExameEspecifico(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_proced_exame_especifico = models.BigIntegerField()
#     no_proced_exame_especifico = models.CharField(max_length=50, blank=True, null=True)
#     no_identificador = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_exame_especifico'
#         unique_together = (('co_revisao', 'co_proced_exame_especifico'),)
#
#
# class TlProcedNomePopular(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_proced_nome_popular = models.BigIntegerField()
#     co_proced = models.BigIntegerField(blank=True, null=True)
#     no_popular = models.CharField(max_length=255, blank=True, null=True)
#     no_sinonimos = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_nome_popular'
#         unique_together = (('co_revisao', 'co_seq_proced_nome_popular'),)
#
#
# class TlProcedOpcaoRapidaExame(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_proced_opcao_rapida_exm = models.BigIntegerField(primary_key=True)
#     co_opcao_rapida_exame = models.BigIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_opcao_rapida_exame'
#         unique_together = (('co_seq_proced_opcao_rapida_exm', 'co_revisao'),)
#
#
# class TlProcedSolicitado(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_proced_solicitado = models.BigIntegerField()
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField(blank=True, null=True)
#     ds_orientacao = models.CharField(max_length=4000, blank=True, null=True)
#     co_lotacao_solicitante = models.BigIntegerField(blank=True, null=True)
#     dt_solicitacao = models.DateTimeField(blank=True, null=True)
#     co_lotacao_executante = models.BigIntegerField(blank=True, null=True)
#     dt_execucao = models.DateTimeField(blank=True, null=True)
#     ds_observacao_execucao = models.CharField(max_length=4000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_solicitado'
#         unique_together = (('co_revisao', 'co_seq_proced_solicitado'),)
#
#
# class TlProcedTipoRegistro(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_proced = models.BigIntegerField()
#     tp_registro = models.BigIntegerField()
#     dt_competencia = models.CharField(max_length=6, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_proced_tipo_registro'
#         unique_together = (('co_revisao', 'co_proced', 'tp_registro'),)
#
#
# class TlProf(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField()
#     nu_conselho_classe = models.CharField(max_length=100, blank=True, null=True)
#     co_uf_emissora_conselho_classe = models.BigIntegerField(blank=True, null=True)
#     co_conselho_classe = models.BigIntegerField(blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     no_profissional = models.CharField(max_length=500, blank=True, null=True)
#     no_profissional_filtro = models.CharField(max_length=600, blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     dt_nascimento = models.DateField(blank=True, null=True)
#     nu_telefone = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_localidade_endereco = models.BigIntegerField(blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_prof'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlProfGrupoAtivCol(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_prof_grupo = models.BigIntegerField(primary_key=True)
#     no_prof_grupo = models.CharField(max_length=255, blank=True, null=True)
#     nu_cpf = models.CharField(max_length=11, blank=True, null=True)
#     nu_cns = models.CharField(max_length=16, blank=True, null=True)
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     nu_ine = models.CharField(max_length=255, blank=True, null=True)
#     co_cbo_2002 = models.CharField(max_length=10, blank=True, null=True)
#     co_unico_prof = models.CharField(max_length=40, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_prof_grupo_ativ_col'
#         unique_together = (('co_seq_prof_grupo', 'co_revisao'),)
#
#
# class TlProfMunicipio(models.Model):
#     co_localidade = models.BigIntegerField()
#     co_ator_papel = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_prof_municipio'
#         unique_together = (('co_revisao', 'co_ator_papel', 'co_localidade'),)
#
#
# class TlProntuario(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_prontuario = models.BigIntegerField()
#     co_unico_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     co_unico_cidadao_prontuario = models.CharField(max_length=36, blank=True, null=True)
#     qt_referencia = models.BigIntegerField(blank=True, null=True)
#     co_prontuario_grupo = models.BigIntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     st_cidadao_processado = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_prontuario'
#         unique_together = (('co_revisao', 'co_seq_prontuario'),)
#
#
# class TlProntuarioGrupoHistorico(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_prontuario_grpo_hstrco = models.BigIntegerField(primary_key=True)
#     co_prontuario_grupo = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#     dt_unificacao = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_prontuario_grupo_historico'
#         unique_together = (('co_seq_prontuario_grpo_hstrco', 'co_revisao'),)
#
#
# class TlProntuarioUnidadeSaude(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_prontuario_unidade_saud = models.BigIntegerField()
#     co_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_cidadao = models.BigIntegerField(blank=True, null=True)
#     nu_prontuario = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_prontuario_unidade_saude'
#         unique_together = (('co_revisao', 'co_seq_prontuario_unidade_saud'),)
#
#
# class TlQstAssociacaoOpcaoPergnt(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_associacao_pergunta = models.BigIntegerField()
#     co_qst_opcao_pergunta = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_associacao_opcao_pergnt'
#         unique_together = (('co_revisao', 'co_qst_associacao_pergunta', 'co_qst_opcao_pergunta'),)
#
#
# class TlQstAssociacaoPergunta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_associacao_pergunta = models.BigIntegerField()
#     co_qst_questionario_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_qst_qst_pergunta_associacao = models.BigIntegerField(blank=True, null=True)
#     co_opcao_pergunta = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_associacao_pergunta'
#         unique_together = (('co_revisao', 'co_qst_associacao_pergunta'),)
#
#
# class TlQstOpcaoPergunta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_opcao_pergunta = models.BigIntegerField()
#     co_qst_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_qst_opcao_tipo_pergunta = models.BigIntegerField(blank=True, null=True)
#     co_qst_orientacao_prof = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_opcao_pergunta'
#         unique_together = (('co_revisao', 'co_qst_opcao_pergunta'),)
#
#
# class TlQstOpcaoTipoPergunta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_opcao_tipo_pergunta = models.BigIntegerField()
#     no_qst_opcao_tipo_pergunta = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_opcao_tipo_pergunta'
#         unique_together = (('co_revisao', 'co_qst_opcao_tipo_pergunta'),)
#
#
# class TlQstOrientacaoProf(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_orientacao_prof = models.BigIntegerField()
#     ds_orientacao_prof = models.CharField(max_length=1000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_orientacao_prof'
#         unique_together = (('co_revisao', 'co_qst_orientacao_prof'),)
#
#
# class TlQstPergunta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_pergunta = models.BigIntegerField()
#     no_qst_pergunta = models.CharField(max_length=800, blank=True, null=True)
#     tp_opcao_pergunta = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_pergunta'
#         unique_together = (('co_revisao', 'co_qst_pergunta'),)
#
#
# class TlQstQuestionario(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_questionario = models.BigIntegerField()
#     ds_questionario = models.CharField(max_length=255, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     tp_qst_questionario = models.IntegerField(blank=True, null=True)
#     nu_idade_meses_limite_inferior = models.IntegerField(blank=True, null=True)
#     nu_idade_meses_limite_superior = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_questionario'
#         unique_together = (('co_revisao', 'co_qst_questionario'),)
#
#
# class TlQstQuestionarioPergunta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_questionario_pergunta = models.BigIntegerField()
#     ds_ordenacao = models.CharField(max_length=15, blank=True, null=True)
#     co_qst_questionario = models.BigIntegerField(blank=True, null=True)
#     co_qst_pergunta = models.BigIntegerField(blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_questionario_pergunta'
#         unique_together = (('co_revisao', 'co_qst_questionario_pergunta'),)
#
#
# class TlQstQuestionarioRespondido(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_qst_qst_respondido = models.BigIntegerField()
#     co_qst_questionario = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     dt_respondido = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_questionario_respondido'
#         unique_together = (('co_revisao', 'co_seq_qst_qst_respondido'),)
#
#
# class TlQstResposta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_qst_resposta = models.BigIntegerField()
#     co_qst_questionario_respondido = models.BigIntegerField(blank=True, null=True)
#     co_qst_questionario_pergunta = models.BigIntegerField(blank=True, null=True)
#     tp_qst_resposta = models.IntegerField(blank=True, null=True)
#     nu_resposta = models.IntegerField(blank=True, null=True)
#     ds_resposta = models.CharField(max_length=800, blank=True, null=True)
#     co_qst_opcao_pergunta = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_resposta'
#         unique_together = (('co_revisao', 'co_seq_qst_resposta'),)
#
#
# class TlQstRespostaOpcaoPergunta(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_qst_resposta = models.BigIntegerField()
#     co_qst_opcao_pergunta = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_qst_resposta_opcao_pergunta'
#         unique_together = (('co_revisao', 'co_qst_resposta', 'co_qst_opcao_pergunta'),)
#
#
# class TlReceita(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_receita = models.BigIntegerField()
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     tp_receita = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_receita'
#         unique_together = (('co_revisao', 'co_seq_receita'),)
#
#
# class TlReceitaMedicamento(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_receita_medicamento = models.BigIntegerField()
#     no_posologia = models.CharField(max_length=200, blank=True, null=True)
#     qt_receitada = models.IntegerField(blank=True, null=True)
#     co_aplicacao_medicamento = models.BigIntegerField(blank=True, null=True)
#     st_uso_continuo = models.IntegerField(blank=True, null=True)
#     co_medicamento = models.BigIntegerField(blank=True, null=True)
#     dt_inicio_tratamento = models.DateField(blank=True, null=True)
#     dt_fim_tratamento = models.DateField(blank=True, null=True)
#     qt_duracao_tratamento = models.IntegerField(blank=True, null=True)
#     ds_dose = models.CharField(max_length=100, blank=True, null=True)
#     tp_frequencia_dose = models.BigIntegerField(blank=True, null=True)
#     ds_frequencia_dose = models.CharField(max_length=25, blank=True, null=True)
#     st_registro_manual = models.IntegerField(blank=True, null=True)
#     st_dose_unica = models.IntegerField(blank=True, null=True)
#     ds_recomendacao = models.TextField(blank=True, null=True)
#     qt_periodo_frequencia = models.IntegerField(blank=True, null=True)
#     tp_un_medida_tempo_frequencia = models.BigIntegerField(blank=True, null=True)
#     tp_un_medida_tempo_tratamento = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     tp_receita = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_receita_medicamento'
#         unique_together = (('co_revisao', 'co_seq_receita_medicamento'),)
#
#
# class TlReceitaTipoFrequencia(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_receita_tipo_frequencia = models.BigIntegerField()
#     no_tipo_frequencia = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_receita_tipo_frequencia'
#         unique_together = (('co_revisao', 'co_receita_tipo_frequencia'),)
#
#
# class TlRecurso(models.Model):
#     co_seq_recurso = models.BigIntegerField()
#     ds_caminho = models.CharField(max_length=1000, blank=True, null=True)
#     no_recurso = models.CharField(max_length=1000, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_recurso'
#         unique_together = (('co_revisao', 'co_seq_recurso'),)
#
#
# class TlRegistroVacinacao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_registro_vacinacao = models.BigIntegerField()
#     co_estrategia_vacinacao = models.BigIntegerField(blank=True, null=True)
#     co_imunobiologico = models.BigIntegerField(blank=True, null=True)
#     co_dose_imunobiologico = models.BigIntegerField(blank=True, null=True)
#     co_via_adm_vacina = models.BigIntegerField(blank=True, null=True)
#     co_local_apl_vacina = models.BigIntegerField(blank=True, null=True)
#     co_vacinacao = models.BigIntegerField(blank=True, null=True)
#     co_tipo_registro_vacinacao = models.BigIntegerField(blank=True, null=True)
#     st_registro_anterior = models.IntegerField(blank=True, null=True)
#     dt_aprazamento = models.DateField(blank=True, null=True)
#     dt_aplicacao = models.DateTimeField(blank=True, null=True)
#     co_imunobiologico_lote = models.BigIntegerField(blank=True, null=True)
#     ds_observacoes = models.CharField(max_length=300, blank=True, null=True)
#     co_grupo_atendimento = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_registro_vacinacao'
#         unique_together = (('co_revisao', 'co_seq_registro_vacinacao'),)
#
#
# class TlRendaFamiliar(models.Model):
#     co_renda_familiar = models.BigIntegerField()
#     no_renda_familiar = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ordem = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_renda_familiar'
#         unique_together = (('co_revisao', 'co_renda_familiar'),)
#
#
# class TlRequisicaoExame(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_requisicao_exame = models.BigIntegerField()
#     dt_requisicao = models.DateTimeField(blank=True, null=True)
#     dt_ultima_menstruacao = models.DateTimeField(blank=True, null=True)
#     ds_justificativa_procedimento = models.CharField(max_length=500, blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_cid10 = models.BigIntegerField(blank=True, null=True)
#     tp_exame = models.IntegerField(blank=True, null=True)
#     ds_observacao = models.CharField(max_length=500, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_requisicao_exame'
#         unique_together = (('co_revisao', 'co_seq_requisicao_exame'),)
#
#
# class TlRlCdsVisitaDomMotivo(models.Model):
#     co_cds_visita_domiciliar = models.BigIntegerField()
#     co_cds_visita_dom_motivo = models.BigIntegerField()
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_rl_cds_visita_dom_motivo'
#         unique_together = (('co_revisao', 'co_cds_visita_domiciliar', 'co_cds_visita_dom_motivo'),)
#
#
# class TlSextante(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_parte_bucal = models.BigIntegerField()
#     co_arcada = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_sextante'
#         unique_together = (('co_revisao', 'co_parte_bucal'),)
#
#
# class TlSinanNotificacaoEvolucao(models.Model):
#     co_revisao = models.BigIntegerField()
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_sinan_notificacao_evol = models.BigIntegerField(primary_key=True)
#     co_sinan_notificacao = models.BigIntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_sinan_notificacao_evolucao'
#         unique_together = (('co_seq_sinan_notificacao_evol', 'co_revisao'),)
#
#
# class TlSituacaoCoroa(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_situacao_coroa = models.BigIntegerField()
#     no_situacao_coroa = models.CharField(max_length=50, blank=True, null=True)
#     no_identificador = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_situacao_coroa'
#         unique_together = (('co_revisao', 'co_situacao_coroa'),)
#
#
# class TlSituacaoFace(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_situacao_face = models.BigIntegerField()
#     no_situacao_face = models.CharField(max_length=50, blank=True, null=True)
#     no_identificador = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_situacao_face'
#         unique_together = (('co_revisao', 'co_situacao_face'),)
#
#
# class TlSituacaoRaiz(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_situacao_raiz = models.BigIntegerField()
#     no_situacao_raiz = models.CharField(max_length=50, blank=True, null=True)
#     no_identificador = models.CharField(max_length=50, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_situacao_raiz'
#         unique_together = (('co_revisao', 'co_situacao_raiz'),)
#
#
# class TlTipoAtendProcedAutomatic(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_proced_automatico = models.BigIntegerField()
#     tp_atend = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_atend_proced_automatic'
#         unique_together = (('co_revisao', 'co_proced_automatico', 'tp_atend'),)
#
#
# class TlTipoConsultaOdntPrcAuto(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_proced_automatico = models.BigIntegerField()
#     tp_consulta_odonto = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_consulta_odnt_prc_auto'
#         unique_together = (('co_revisao', 'co_proced_automatico', 'tp_consulta_odonto'),)
#
#
# class TlTipoConsultaOdonto(models.Model):
#     co_tipo_consulta_odonto = models.BigIntegerField()
#     no_tipo_consulta_odonto = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_consulta_odonto'
#         unique_together = (('co_revisao', 'co_tipo_consulta_odonto'),)
#
#
# class TlTipoEdema(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_tipo_edema = models.BigIntegerField()
#     no_tipo_edema = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_edema'
#         unique_together = (('co_revisao', 'co_tipo_edema'),)
#
#
# class TlTipoEncamOdonto(models.Model):
#     co_tipo_encam_odonto = models.BigIntegerField()
#     no_tipo_encam_odonto = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_encam_odonto'
#         unique_together = (('co_revisao', 'co_tipo_encam_odonto'),)
#
#
# class TlTipoEncamOdontoProcdAut(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_proced_automatico = models.BigIntegerField()
#     tp_encam_odonto = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_encam_odonto_procd_aut'
#         unique_together = (('co_revisao', 'co_proced_automatico', 'tp_encam_odonto'),)
#
#
# class TlTipoExame(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_tipo_exame = models.BigIntegerField()
#     no_tipo_exame = models.CharField(max_length=50, blank=True, null=True)
#     co_sexo = models.BigIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_exame'
#         unique_together = (('co_revisao', 'co_tipo_exame'),)
#
#
# class TlTipoFornecOdonto(models.Model):
#     co_tipo_fornec_odonto = models.BigIntegerField()
#     no_tipo_fornec_odonto = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_fornec_odonto'
#         unique_together = (('co_revisao', 'co_tipo_fornec_odonto'),)
#
#
# class TlTipoGravidez(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_tipo_gravidez = models.BigIntegerField()
#     no_tipo_gravidez = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_gravidez'
#         unique_together = (('co_revisao', 'co_tipo_gravidez'),)
#
#
# class TlTipoLocalidade(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_tipo_localidade = models.BigIntegerField()
#     no_tipo_localidade = models.CharField(max_length=100, blank=True, null=True)
#     sg_tipo_localidade = models.CharField(max_length=1, blank=True, null=True)
#     no_identificador = models.CharField(max_length=30, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_localidade'
#         unique_together = (('co_revisao', 'co_tipo_localidade'),)
#
#
# class TlTipoParteBucal(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_tipo_parte_bucal = models.BigIntegerField()
#     no_tipo_parte_bucal = models.CharField(max_length=100, blank=True, null=True)
#     no_identificador = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_parte_bucal'
#         unique_together = (('co_revisao', 'co_tipo_parte_bucal'),)
#
#
# class TlTipoPerfil(models.Model):
#     co_tipo_perfil = models.BigIntegerField()
#     no_tipo_perfil = models.CharField(max_length=100, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_perfil'
#         unique_together = (('co_revisao', 'co_tipo_perfil'),)
#
#
# class TlTipoPergunta(models.Model):
#     co_tipo_pergunta = models.BigIntegerField()
#     ds_tipo_pergunta = models.CharField(max_length=255, blank=True, null=True)
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_pergunta'
#         unique_together = (('co_revisao', 'co_tipo_pergunta'),)
#
#
# class TlTipoRegistro(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_tipo_registro = models.BigIntegerField()
#     no_tipo_registro = models.CharField(max_length=50, blank=True, null=True)
#     dt_competencia = models.CharField(max_length=6, blank=True, null=True)
#     nu_ms = models.CharField(max_length=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_registro'
#         unique_together = (('co_revisao', 'co_tipo_registro'),)
#
#
# class TlTipoServico(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_tipo_servico = models.BigIntegerField()
#     no_tipo_servico = models.CharField(max_length=50, blank=True, null=True)
#     no_tipo_servico_filtro = models.CharField(max_length=50, blank=True, null=True)
#     st_interno = models.IntegerField(blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_tipo_servico'
#         unique_together = (('co_revisao', 'co_tipo_servico'),)
#
#
# class TlTituloPatente(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_titulo_patente = models.BigIntegerField()
#     nu_dne = models.CharField(max_length=4, blank=True, null=True)
#     no_titulo_patente = models.CharField(max_length=72, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_titulo_patente'
#         unique_together = (('co_revisao', 'co_titulo_patente'),)
#
#
# class TlUnidadeMedida(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_unidade_medida = models.BigIntegerField()
#     sg_unidade_medida = models.CharField(max_length=25, blank=True, null=True)
#     no_unidade_medida_filtro = models.CharField(max_length=100, blank=True, null=True)
#     no_unidade_medida = models.CharField(max_length=100, blank=True, null=True)
#     no_unidade_medida_plural = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_unidade_medida'
#         unique_together = (('co_revisao', 'co_unidade_medida'),)
#
#
# class TlUnidadeMedidaTempo(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_unidade_medida_tempo = models.BigIntegerField()
#     no_unidade_medida_tempo = models.CharField(max_length=255, blank=True, null=True)
#     no_identificador = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_unidade_medida_tempo'
#         unique_together = (('co_revisao', 'co_unidade_medida_tempo'),)
#
#
# class TlUnidadeSaude(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     nu_licenca_funcionamento = models.CharField(max_length=20, blank=True, null=True)
#     tp_unidade_saude = models.BigIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField()
#     nu_cnes = models.CharField(max_length=20, blank=True, null=True)
#     st_ativo = models.IntegerField(blank=True, null=True)
#     nu_cnpj = models.CharField(max_length=14, blank=True, null=True)
#     no_unidade_saude = models.CharField(max_length=255, blank=True, null=True)
#     no_unidade_saude_filtro = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_comercial = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_comercial2 = models.CharField(max_length=255, blank=True, null=True)
#     nu_telefone_fax = models.CharField(max_length=255, blank=True, null=True)
#     ds_email = models.CharField(max_length=255, blank=True, null=True)
#     ds_cep = models.CharField(max_length=8, blank=True, null=True)
#     ds_complemento = models.CharField(max_length=50, blank=True, null=True)
#     ds_ponto_referencia = models.CharField(max_length=100, blank=True, null=True)
#     ds_logradouro = models.CharField(max_length=150, blank=True, null=True)
#     co_uf = models.BigIntegerField(blank=True, null=True)
#     co_localidade = models.BigIntegerField(blank=True, null=True)
#     nu_numero = models.CharField(max_length=20, blank=True, null=True)
#     st_sem_numero = models.IntegerField(blank=True, null=True)
#     no_bairro = models.CharField(max_length=255, blank=True, null=True)
#     no_bairro_filtro = models.CharField(max_length=255, blank=True, null=True)
#     tp_logradouro = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_unidade_saude'
#         unique_together = (('co_revisao', 'co_ator_papel'),)
#
#
# class TlUnidadeSaudeComplexidade(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_ator_papel = models.BigIntegerField()
#     co_complexidade = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_unidade_saude_complexidade'
#         unique_together = (('co_revisao', 'co_complexidade', 'co_ator_papel'),)
#
#
# class TlUnidadeSaudeHorus(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_unidade_saude = models.BigIntegerField()
#     co_unidade_saude_horus = models.BigIntegerField()
#     co_seq_unidade_saude_horus = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_unidade_saude_horus'
#         unique_together = (('co_revisao', 'co_unidade_saude', 'co_unidade_saude_horus'),)
#
#
# class TlUnidadeSaudeTipoServico(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     tp_servico = models.BigIntegerField()
#     co_ator_papel = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tl_unidade_saude_tipo_servico'
#         unique_together = (('co_revisao', 'co_ator_papel', 'tp_servico'),)
#
#
# class TlUsuario(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_usuario = models.BigIntegerField()
#     st_bloqueado = models.IntegerField(blank=True, null=True)
#     ds_senha = models.CharField(max_length=255, blank=True, null=True)
#     st_trocar_senha = models.IntegerField(blank=True, null=True)
#     co_ator = models.BigIntegerField(blank=True, null=True)
#     dt_ultima_atualizacao_senha = models.DateField(blank=True, null=True)
#     st_termo_uso = models.IntegerField(blank=True, null=True)
#     st_forcar_troca_senha = models.IntegerField(blank=True, null=True)
#     nr_tentativas_acesso = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_usuario'
#         unique_together = (('co_revisao', 'co_seq_usuario'),)
#
#
# class TlVacinacao(models.Model):
#     co_revisao = models.BigIntegerField(primary_key=True)
#     co_tipo_revisao = models.SmallIntegerField(blank=True, null=True)
#     co_seq_vacinacao = models.BigIntegerField()
#     st_gestante = models.IntegerField(blank=True, null=True)
#     st_puerpera = models.IntegerField(blank=True, null=True)
#     st_viajante = models.IntegerField(blank=True, null=True)
#     st_comunicante_hanseniase = models.IntegerField(blank=True, null=True)
#     co_atend_prof = models.BigIntegerField(blank=True, null=True)
#     co_prontuario = models.BigIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tl_vacinacao'
#         unique_together = (('co_revisao', 'co_seq_vacinacao'),)
