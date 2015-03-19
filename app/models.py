from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=255)
    langauge = models.CharField(max_length=3)

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
    country = models.ForeignKey(Country, unique=True)



class Client(AddressInformation):

    client_number = models.IntegerField()
