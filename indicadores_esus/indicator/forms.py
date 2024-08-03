from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Field, ButtonHolder, HTML
from django import forms
from django.urls import reverse

from indicadores_esus.indicator.models import INDICATOR_TYPE_CHOICES, Indicator


class CalculateIndicatorForm(forms.Form):
    type_choices = list(INDICATOR_TYPE_CHOICES)
    type_choices.insert(0, ('T', 'Todos'))
    
    quadrimester = forms.ChoiceField(
        choices=(
            ('1', 'Q1'),
            ('2', 'Q2'),
            ('3', 'Q3')
        ),
        label='Quadrimestre'
    )
    year = forms.IntegerField(label='Ano')
    type = forms.ChoiceField(choices=type_choices, label='Tipo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-calculateindicator'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Row(
                    Column(
                        Field('type', css_class='form-select'),
                        css_class='col-6'
                    ),
                    Column(
                        Field('quadrimester', css_class='form-select'),
                        css_class='col-3'
                    ),
                    Column(
                        Field('year'),
                        css_class='col-3'
                    ),
                    css_class='row'
                ),
            ),
            ButtonHolder(
                Column(
                    HTML('<input type="submit" name="submit" value="Calcular" class="btn btn-outline-primary">'),
                    css_class='col-3'
                ),
                Column(
                    HTML('<div class="spinner-border text-primary" role="status" hidden > <span class="visually-hidden"></span> </div>')
                ),
                css_class='row p-2'
            )
        )


class IndicatorTeamForm(forms.Form):
    indicator = forms.ModelChoiceField(
        queryset=Indicator.objects.filter(is_active=True).order_by('quadrimester'),
        label='Indicador'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-indicatorteam'
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Row(
                    Column(
                        Field('indicator', css_class='form-select'),
                        css_class='col-6'
                    ),
                    css_class='row'
                ),
            ),
            ButtonHolder(
                Column(
                    HTML('<input type="submit" name="submit" value="Filtrar" class="btn btn-outline-primary">'),
                    css_class='col-3'
                ),
                Column(
                    HTML('<div class="spinner-border text-primary" role="status" hidden > <span class="visually-hidden"></span> </div>')
                ),
                css_class='row p-2'
            )
        )