from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, ButtonHolder, Column, Field, Fieldset,
                                 Layout, Row)
from django import forms
from django.urls import reverse

from indicadores_esus.core import models


class HomeForm(forms.Form):
    quadrimester_choices = (
        ('Q3/2022', 'Q3/2022'),
        ('Q1/2023', 'Q1/2023'),
        ('Q2/2023', 'Q2/2023'),
        ('Q3/2023', 'Q3/2023')
    )
    health_unit = forms.ModelChoiceField(
        queryset=models.HealthUnit.objects.all().order_by('name')
    )
    health_team = forms.ModelChoiceField(
        queryset=models.HealthTeam.objects.all().order_by('name')
    )
    quadrimester = forms.ChoiceField(choices=quadrimester_choices)