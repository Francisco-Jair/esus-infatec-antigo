# Generated by Django 3.2.13 on 2022-11-19 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_patientindicator'),
    ]

    operations = [
        migrations.CreateModel(
            name='PregnantWoman',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.role')),
                ('dum', models.DateField(blank=True, null=True)),
                ('dpp', models.DateField(blank=True, null=True)),
                ('is_pregnant', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='left_city',
            field=models.BooleanField(default=False),
        ),
    ]