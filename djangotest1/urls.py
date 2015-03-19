from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangotest1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^admin/", include(admin.site.urls)),
    url(r"^recipe/", "app.views.submit_client", name="get_client")


)
