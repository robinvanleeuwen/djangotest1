from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=255)
    language = models.CharField(max_length=3)

    def __unicode__(self):
        return u'{0}'.format(self.country)


class AddressInformation(models.Model):

    class Meta:
        abstract = True

    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country)


class ContactInformation(models.Model):

    class Meta:
        abstract = True

    email = models.EmailField(max_length=255, default="")
    phone1 = models.CharField(max_length=255, default="")
    phone2 = models.CharField(max_length=255, default="")


class Client(AddressInformation, ContactInformation):

    client_number = models.IntegerField()
