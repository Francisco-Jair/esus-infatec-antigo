# Generated by Django 3.2.13 on 2022-10-28 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0005_auto_20220728_2143'),
        ('core', '0023_role_indicator'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientIndicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerator', models.BooleanField(default=False)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.calculatedindicator')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role')),
            ],
        ),
    ]