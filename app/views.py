from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from .models import Recipe, RecipeIngredient
from .forms import UserSubmittedRecipeForm, IngredientFormSet

def submit_recipe(request):
    if request.POST:

        form = UserSubmittedRecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            ingredient_formset = IngredientFormSet(request.POST, instance=recipe)
            if ingredient_formset.is_valid():
                recipe.save()
                ingredient_formset.save()
                return HttpResponseRedirect("recipient.html")
    else:
        form = UserSubmittedRecipeForm()
        ingredient_formset = IngredientFormSet(instance=Recipe())
    return render_to_response("recipient.html", {
        "form": form,
        "ingredient_formset": ingredient_formset,
    }, context_instance=RequestContext(request))