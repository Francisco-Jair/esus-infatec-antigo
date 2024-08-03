# Generated by Django 3.2.13 on 2023-01-19 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_patientprocedure_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='sus_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patientprocedure',
            name='evaluate_appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evaluated_procedures', to='core.appointment'),
        ),
        migrations.AddField(
            model_name='patientprocedure',
            name='request_appointment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requested_procedures', to='core.appointment'),
        ),
        migrations.AddField(
            model_name='pregnantwoman',
            name='sus_registered',
            field=models.BooleanField(default=False),
        ),
    ]
