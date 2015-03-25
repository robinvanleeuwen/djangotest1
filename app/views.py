from time import timezone
from django.core import serializers
from django.core.context_processors import csrf
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render, get_object_or_404
from django.views.generic import ListView
from app.forms import ClientForm, CountryForm
from app.models import Client, Country


class ClientView(ListView):
    template_name = "client_list.html"
    model = Client


def manage_client(request, id_client=None):
    """
    Add/Edit client database entries
    :param request:
    :param id_client:
    :return: rendered form
    """
    if request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/client")
    else:
        form = ClientForm()

    args = {}
    args['form'] = form
    return render_to_response('recipient.html', args)


