# Generated by Django 3.2.13 on 2022-06-26 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_indicador_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador1DadosConsultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('gestante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.indicador1')),
            ],
        ),
        migrations.CreateModel(
            name='Indicador1Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=500)),
                ('cns', models.CharField(blank=True, max_length=15)),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('dum', models.DateField(blank=True, null=True)),
                ('dpp', models.DateField(blank=True, null=True)),
                ('indicador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.indicador1')),
            ],
            options={
                'verbose_name': 'Dado do Indicador 1',
                'verbose_name_plural': 'Dados do Indicador 1',
            },
        ),
    ]
