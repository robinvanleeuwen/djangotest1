import json
from django.core import serializers
from django.http import HttpResponse
from app.models import Client


def search_client(request, method):
    """
    Search client database for clients containing client_number
    :param request:
    :return: HTTPResponse conaining JSON object with list of matching clients
    """
    data = []
    if request.is_ajax():
        q = request.GET.get('term','')
        kwargs = {"{0}__contains".format(method): q,}
        print kwargs
        clients = Client.objects.filter(**kwargs)[:20]
        for c in clients:
            data.append(unicode(c.client_number))
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_client(request, client_number):
    """
    Retrieve specific client object from database model, return it
    through HTTP/JSON
    :param request:
    :param client_number:
    :return: JSON object with 1 client instance or empty object
    """
    try:
        client = Client.objects.get(client_number=client_number)
    except Client.DoesNotExist:
        client = None
        return HttpResponse({}, content_type="application/json")

    return HttpResponse(serializers.serialize("json", [client]).strip("[]"),
                        content_type="application/json")
