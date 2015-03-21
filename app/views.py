from django.core.context_processors import csrf
from django.forms import inlineformset_factory
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from app.forms import ClientForm, CountryForm
from app.models import Client, Country


def manage_client(request, id_client=None):
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/client")
    else:
        form = ClientForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('recipient.html', args)

