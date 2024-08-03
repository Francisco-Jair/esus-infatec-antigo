# Generated by Django 3.2.13 on 2022-07-28 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20220727_1948'),
        ('indicator', '0002_indicatorpattern_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatedIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Indicador 1 - Proporção de gestantes com pelo menos 6 (seis) consultas pré-natal realizadas, sendo a 1ª até a 12ª semana de gestação'), ('2', 'Indicador 2 - Proporção de gestantes com realização de exames para sífilis e HIV'), ('3', 'Indicador 3 - Proporção de gestantes com atendimento odontológico realizado'), ('4', 'Indicador 4 - Proporção de mulheres com coleta de citopatológico na APS'), ('5', 'Indicador 5 - Proporção de crianças de 1(um) ano de idade vacinadas na APS contra Difeteria, Tétano, Coqueluche, Hepatite B, Infecções causadas por Haemophilus Influenzae tipo b e Poliomielite Inativada'), ('6', 'Indicador 6 - Proporção de pessoas com hipertensão, com consulta e pressão arterial aferida no semestre'), ('7', 'Indicador 7 - Proporção de pessoas com diabetes, com consulta e hemoglobina glicada solicitada no semestre')], max_length=1, verbose_name='tipo')),
                ('denominator', models.IntegerField(verbose_name='denominador')),
                ('numerator', models.IntegerField(verbose_name='numerador')),
                ('indicator_index', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='indicador')),
                ('status', models.CharField(choices=[('1', 'Gerado'), ('2', 'Calculando'), ('3', 'Removido')], max_length=1)),
                ('calculated_at', models.DateTimeField(auto_now_add=True, verbose_name='calculada em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='atualizada em')),
            ],
            options={
                'verbose_name': 'Indicador calculado',
                'verbose_name_plural': 'Indicadores calculados',
            },
        ),
        migrations.AlterField(
            model_name='indicator',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.city'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='isf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='indicador sintético final'),
        ),
        migrations.AlterField(
            model_name='indicatorpattern',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.DeleteModel(
            name='Calculated_Indicator',
        ),
        migrations.AddField(
            model_name='calculatedindicator',
            name='indicator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.indicator', verbose_name='indicador'),
        ),
        migrations.AddField(
            model_name='calculatedindicator',
            name='pattern',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='indicator.indicatorpattern'),
        ),
    ]