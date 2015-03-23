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
    client_number = forms.CharField(widget=forms.TextInput(attrs={"size": 40}))
    name1 = forms.CharField(widget=forms.TextInput(attrs={"size":40}))
    name2 = forms.CharField(widget=forms.TextInput(attrs={"size":40}))
    street = forms.CharField(widget=forms.TextInput(attrs={"size":40}))
    zip = forms.CharField(widget=forms.TextInput(attrs={"size":10}))
    city = forms.CharField(widget=forms.TextInput(attrs={"size":28}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(),
                                     initial=Country.objects.all().filter(country="NL"))


