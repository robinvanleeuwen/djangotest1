from django.db import models


class CountryCodes(models.Model):

    iso_3116_1_alpha2 = models.CharField(max_length=2, null=True, default="", unique=True)
    iso_3116_1_alpha3 = models.CharField(max_length=3, null=True, default="")
    iso_3116_1_num = models.IntegerField(null=True, default=0)
    eu_country = models.BooleanField(default=False)
    country_desc = models.IntegerField(default=0, null=True)
    language_code = models.CharField(max_length=3, null=True, default="")


class AddressInformation(models.Model):

    class Meta:
        abstract = True
        index_together = [["name1", "name2"]]
        ordering = ['name1']
        managed = True

    name1 = models.CharField(max_length=255, null=True, default="")
    name2 = models.CharField(max_length=255, null=True, default="")
    street = models.CharField(max_length=255, null=True, default="")
    zip = models.CharField(max_length=255, null=True, default="")
    country = models.ForeignKey(CountryCodes, unique=True)
    email = models.CharField(max_length=255, null=True, default="")
    phone1 = models.CharField(max_length=40, null=True, default="")
    phone2 = models.CharField(max_length=40, null=True, default="")

class Recipient(AddressInformation):

    recipientNumber = models.IntegerField(db_index=True, unique=True)


class Customer(AddressInformation):

    customerNumber = models.IntegerField(db_index=True, unique=True)

