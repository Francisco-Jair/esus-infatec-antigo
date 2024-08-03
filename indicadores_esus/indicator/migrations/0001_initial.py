# Generated by Django 3.2.13 on 2022-07-27 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0014_auto_20220727_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndicatorPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Indicador 1 - Proporção de gestantes com pelo menos 6 (seis) consultas pré-natal realizadas, sendo a 1ª até a 12ª semana de gestação'), ('2', 'Indicador 2 - Proporção de gestantes com realização de exames para sífilis e HIV'), ('3', 'Indicador 3 - Proporção de gestantes com atendimento odontológico realizado'), ('4', 'Indicador 4 - Proporção de mulheres com coleta de citopatológico na APS'), ('5', 'Indicador 5 - Proporção de crianças de 1(um) ano de idade vacinadas na APS contra Difeteria, Tétano, Coqueluche, Hepatite B, Infecções causadas por Haemophilus Influenzae tipo b e Poliomielite Inativada'), ('6', 'Indicador 6 - Proporção de pessoas com hipertensão, com consulta e pressão arterial aferida no semestre'), ('7', 'Indicador 7 - Proporção de pessoas com diabetes, com consulta e hemoglobina glicada solicitada no semestre')], max_length=1, verbose_name='tipo')),
                ('parameter', models.PositiveSmallIntegerField(verbose_name='parâmetro')),
                ('goal', models.PositiveSmallIntegerField(verbose_name='meta')),
                ('weight', models.PositiveSmallIntegerField(verbose_name='peso')),
                ('year', models.PositiveSmallIntegerField(verbose_name='ano')),
                ('estimated_denominator', models.IntegerField(blank=True, null=True, verbose_name='denominador estimado')),
            ],
            options={
                'verbose_name': 'Padrões para indicador',
                'verbose_name_plural': 'Padrões para indicadores',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='descrição')),
                ('isf', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='indicador sintético final')),
                ('quadrimester', models.CharField(blank=True, max_length=7, verbose_name='quadrimestre')),
                ('dt_init_evaluation', models.DateField(blank=True, null=True, verbose_name='data inicial da avaliação')),
                ('dt_end_evaluation', models.DateField(blank=True, null=True, verbose_name='data final da avaliação')),
                ('is_active', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.city')),
            ],
            options={
                'verbose_name': 'Indicador',
                'verbose_name_plural': 'Indicadores',
            },
        ),
        migrations.CreateModel(
            name='Calculated_Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Indicador 1 - Proporção de gestantes com pelo menos 6 (seis) consultas pré-natal realizadas, sendo a 1ª até a 12ª semana de gestação'), ('2', 'Indicador 2 - Proporção de gestantes com realização de exames para sífilis e HIV'), ('3', 'Indicador 3 - Proporção de gestantes com atendimento odontológico realizado'), ('4', 'Indicador 4 - Proporção de mulheres com coleta de citopatológico na APS'), ('5', 'Indicador 5 - Proporção de crianças de 1(um) ano de idade vacinadas na APS contra Difeteria, Tétano, Coqueluche, Hepatite B, Infecções causadas por Haemophilus Influenzae tipo b e Poliomielite Inativada'), ('6', 'Indicador 6 - Proporção de pessoas com hipertensão, com consulta e pressão arterial aferida no semestre'), ('7', 'Indicador 7 - Proporção de pessoas com diabetes, com consulta e hemoglobina glicada solicitada no semestre')], max_length=1, verbose_name='tipo')),
                ('denominator', models.IntegerField(verbose_name='denominador')),
                ('numerator', models.IntegerField(verbose_name='numerador')),
                ('indicator_index', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='indicador')),
                ('quadrimester', models.CharField(blank=True, max_length=7, verbose_name='quadrimestre')),
                ('dt_init_evaluation', models.DateField(blank=True, null=True, verbose_name='data inicial da avaliação')),
                ('dt_end_evaluation', models.DateField(blank=True, null=True, verbose_name='data final da avaliação')),
                ('status', models.CharField(choices=[('1', 'Gerado'), ('2', 'Calculando'), ('3', 'Removido')], max_length=1)),
                ('calculated_at', models.DateTimeField(auto_now_add=True, verbose_name='calculada em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizada em')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.indicator', verbose_name='indicador')),
                ('pattern', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='indicator.indicatorpattern')),
            ],
            options={
                'verbose_name': 'Indicador calculado',
                'verbose_name_plural': 'Indicadores calculados',
            },
        ),
    ]