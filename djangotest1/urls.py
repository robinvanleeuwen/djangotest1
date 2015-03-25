from django.conf.urls import patterns, include, url
from django.contrib import admin
from ajax_select import urls as ajax_select_urls
from app.views import ClientView

urlpatterns = patterns('',
    url(r"^admin/", include(admin.site.urls)),
    url(r'^client/get/(?P<client_number>\w+)', "app.ajax.get_client", name="ajax_get_client"),
    url(r"^client/search/(?P<method>\w+)", "app.ajax.search_client", name="ajax_search_client"),
    url(r"^clients/", ClientView.as_view(), name="list_client"),
    url(r"^client/", "app.views.manage_client", name="manage_client"),

)
