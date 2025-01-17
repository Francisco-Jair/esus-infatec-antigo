# Generated by Django 3.2.13 on 2022-05-27 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220527_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=250)),
                ('denominador', models.IntegerField()),
                ('quadrimestre', models.CharField(blank=True, max_length=7)),
                ('dt_avaliacao_ini', models.DateField(blank=True, null=True)),
                ('dt_avaliacao_fim', models.DateField(blank=True, null=True)),
                ('gerado_em', models.DateTimeField(auto_now_add=True)),
                ('alterado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='alterado_em',
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='denominador',
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='dt_avaliacao_fim',
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='dt_avaliacao_ini',
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='gerado_em',
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='id',
        ),
        migrations.RemoveField(
            model_name='indicador1',
            name='quadrimestre',
        ),
        migrations.AddField(
            model_name='indicador1',
            name='indicador_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.indicador'),
            preserve_default=False,
        ),
    ]
