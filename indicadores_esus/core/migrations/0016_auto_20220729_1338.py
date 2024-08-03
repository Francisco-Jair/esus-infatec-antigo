# Generated by Django 3.2.13 on 2022-07-29 16:38
import json

from django.db import migrations


def populate_cities(apps, schema_editor):
    f = open('indicadores_esus/core/fixtures/cities.json')
    cities = json.load(f)
    City = apps.get_model(
        app_label='core',
        model_name='City'
    )

    for c in cities:
        try:
            city = City.objects.get(ibge_code=c['municipio-id'])
            city.state = c['UF-sigla']
            city.name = c['municipio-nome']
            city.save()
        except City.DoesNotExist:
            City.objects.create(
                state=c['UF-sigla'],
                name=c['municipio-nome'],
                ibge_code=c['municipio-id']
            )
            print(f"Criada cidade: {c['municipio-id']}-{c['municipio-nome']}-{c['UF-sigla']}")            


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_city_ibge_code'),
    ]

    operations = [
        migrations.RunPython(populate_cities),
    ]