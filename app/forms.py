from django import forms
from .models import Client, Country
from django.forms.models import inlineformset_factory, ModelChoiceField

MAX_INGREDIENTS = 20

ClientFormSet = inlineformset_factory(Country,
    Client,
    can_delete=False,
    extra=3)

class UserSubmittedClientForm(forms.ModelForm):

    class Meta:
        model = Client

    country = forms.ModelChoiceField(queryset=Country.objects.all(), initial=Country.objects.all().filter(country="NL"))