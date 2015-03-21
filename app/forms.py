from django import forms
from .models import Client, Country
from django.forms.models import inlineformset_factory, ModelForm


class CountryForm(ModelForm):
    class Meta:
        model = Country
        exclude = [()]


class ClientForm(ModelForm):

    class Meta:
        model = Client
        exclude = [()]

    country = forms.ModelChoiceField(queryset=Country.objects.all(),
                                     initial=Country.objects.all().filter(country="NL"))


