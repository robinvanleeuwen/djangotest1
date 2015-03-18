from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dynamic_models1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^admin/", include(admin.site.urls)),
    url(r"^recipient/", "app.forms.get_recipient", name="get_recipient")

)
