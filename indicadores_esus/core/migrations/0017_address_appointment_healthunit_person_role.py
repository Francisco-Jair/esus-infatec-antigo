# Generated by Django 3.2.13 on 2022-10-20 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20220729_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_cpf', models.CharField(blank=True, max_length=11)),
                ('_cns', models.CharField(blank=True, max_length=16)),
                ('name', models.CharField(max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type', models.PositiveSmallIntegerField(choices=[(1, 'Paciente'), (2, 'Médico')])),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
        ),
        migrations.CreateModel(
            name='HealthUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnes', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('street', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=25)),
                ('complement', models.CharField(blank=True, max_length=25)),
                ('neighborhood', models.CharField(blank=True, max_length=50)),
                ('cep', models.CharField(blank=True, max_length=8)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.city')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=25)),
                ('complement', models.CharField(blank=True, max_length=25)),
                ('cep', models.CharField(blank=True, max_length=8)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.city')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
        ),
    ]
