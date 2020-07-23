from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactsModel(models.Model):
    class Meta:
        abstract = True

    contact_name = models.CharField(max_length=64)
    contact_phone = PhoneNumberField(max_length=64, db_index=True)
    city = models.CharField(max_length=64)
    shipping_address = models.CharField(max_length=256, blank=True)
    email = models.EmailField(db_index=True)


class SeoModel(models.Model):
    class Meta:
        abstract = True

    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_description = models.CharField(max_length=300, blank=True, null=True)


class ActiveBaseQueryset(models.QuerySet):
    class Meta:
        abstract = True

    def active(self):
        return self.filter(is_active=True)
