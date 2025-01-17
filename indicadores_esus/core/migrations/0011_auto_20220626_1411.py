# Generated by Django 3.2.13 on 2022-06-26 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220626_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicador1dadosconsultas',
            name='consulta_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indicador1dadosconsultas',
            name='gestante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gestante_consultas_set', to='core.indicador1dados'),
        ),
    ]
