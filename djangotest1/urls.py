from django.conf.urls import patterns, include, url
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

urlpatterns = patterns('',
    url(r"^admin/", include(admin.site.urls)),
    url(r"^client/", "app.views.manage_client", name="get_client"),
    url(r"^search/", "app.views.search_client", name="search_client"),
    url(r'^test/', "app.views.test_ajax", name="test_ajax"),
)
