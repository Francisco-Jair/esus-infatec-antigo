# Generated by Django 3.2.13 on 2023-01-02 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20221219_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.role')),
            ],
        ),
        migrations.CreateModel(
            name='Diabetic',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.role')),
            ],
        ),
        migrations.CreateModel(
            name='Hypertensive',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.role')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esus_code', models.BigIntegerField(blank=True, null=True, verbose_name='Código ESUS')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nome')),
                ('procedure_code', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.role')),
            ],
        ),
        migrations.CreateModel(
            name='PatientProcedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esus_code', models.BigIntegerField(blank=True, null=True, verbose_name='Código ESUS')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_procedures', to='core.role')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.procedure')),
            ],
        ),
    ]
