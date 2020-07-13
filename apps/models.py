from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactsModel(models.Model):
    class Meta:
        abstract = True

    contact_name = models.CharField(max_length=64)
    contact_phone = PhoneNumberField(db_index=True)
    city = models.CharField()
    shipping_address = models.CharField(blank=True)
    email = models.EmailField(db_index=True)


class SeoModel(models.Model):
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        abstract = True
