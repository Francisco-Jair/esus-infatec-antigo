# Generated by Django 3.2.13 on 2022-12-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20221218_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='ciaps',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='cids',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
