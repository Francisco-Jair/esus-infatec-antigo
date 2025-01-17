# Generated by Django 3.2.13 on 2023-02-15 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_vaccination_vaccine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esus_id', models.CharField(max_length=255)),
                ('acronym', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='vaccination',
            name='dose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.dose'),
        ),
    ]
