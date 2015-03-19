from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from app.models import Client
from .forms import UserSubmittedClientForm, ClientFormSet


def submit_client(request):
    if request.POST:

        form = UserSubmittedClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client_formset = ClientFormSet(request.POST, instance=client)
            if client_formset.is_valid():
                client.save()
                client_formset.save()
                return HttpResponseRedirect("recipient.html")
    else:
        form = UserSubmittedClientForm()
        client_formset = ClientFormSet(instance=Client())
    return render_to_response("recipient.html", {
        "form": form,
        "client_formset": client_formset,
    }, context_instance=RequestContext(request))