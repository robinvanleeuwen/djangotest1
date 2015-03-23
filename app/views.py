from django.core import serializers
from django.core.context_processors import csrf
import json
from django.http import HttpResponseRedirect, HttpResponse
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


def search_client(request):

    if request.method == "POST":
        search_text = request.POST["search_text"]
    else:
        search_text = ""

    clients = Client.objects.filter(client_number__contains=search_text)
    args = {}
    args.update(csrf(request))
    args["clients"] = clients
    return render_to_response("ajax_search.html", args)


def test_ajax(request):
    data = []
    if request.is_ajax():
        q = request.GET.get('term','')
        clients = Client.objects.filter(client_number__contains = q)[:20]
        for c in clients:

            data.append(unicode(c.client_number))


    data = json.dumps(data)
    print data
    return HttpResponse(data, content_type="application/json")

