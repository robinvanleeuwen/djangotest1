from django.contrib import admin

# Register your models here.
from app.models import Customer, Recipient, CountryCodes

admin.site.register(Customer)
admin.site.register(Recipient)
admin.site.register(CountryCodes)