# Generated by Django 3.2.13 on 2022-10-28 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20221028_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='_cns',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='_cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
