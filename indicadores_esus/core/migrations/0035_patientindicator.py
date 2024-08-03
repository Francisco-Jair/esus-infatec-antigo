# Generated by Django 3.2.13 on 2023-01-05 13:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0005_auto_20220728_2143'),
        ('core', '0034_delete_patientindicator'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientIndicator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('numerator', models.BooleanField(default=False)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicator.calculatedindicator')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.role')),
            ],
        ),
    ]