from django import forms
from django.forms import ModelForm
from dsfr.forms import DsfrBaseForm

from gain.models import Indicator


class IndicatorForm(
    ModelForm,
    DsfrBaseForm
):
    detailed_entry = forms.ChoiceField(
        label="Saisie détaillée",
        required=False,
        choices=[(True, "Saisie détaillée"), ],
        widget=forms.CheckboxInput, )

    class Meta:
        model = Indicator
        fields = '__all__'
        labels = {
            'domain':         'Domaine',
            'sector':         'Secteur',
            'function':       'Fonction',
            'label':          'Libellé',
            'indicator_type': 'Type d\'indicateur',
            'period':         'Périodicité',
            'description':    'Description',
            'detailed_entry': 'Entrée détaillée',
            'formula':        'Formule'
        }
