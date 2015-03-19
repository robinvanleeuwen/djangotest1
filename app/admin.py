from django.contrib import admin

# Register your models here.
from app.models import Country, Client

admin.site.register(Country)
admin.site.register(Client)
