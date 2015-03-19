from django import forms
from .models import Recipe, RecipeIngredient
from django.forms.models import inlineformset_factory, ModelChoiceField

MAX_INGREDIENTS = 20

IngredientFormSet = inlineformset_factory(Recipe,
    RecipeIngredient,
    can_delete=False,
    extra=MAX_INGREDIENTS)

class UserSubmittedRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('pub_date', )