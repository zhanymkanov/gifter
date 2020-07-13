import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from versatileimagefield.fields import PPOIField, VersatileImageField

from apps.models import SeoModel
from apps.vendor.models import Vendor


class Category(SeoModel):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    image = VersatileImageField(upload_to="gifts", ppoi_field="ppoi")
    ppoi = PPOIField()
    name = models.CharField(max_length=128, unique=True)
    alt = models.CharField(max_length=128, blank=True)

    def __str__(self) -> str:
        return self.name


class Gift(SeoModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    in_stock = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    specification = JSONField()
    categories = models.ManyToManyField(Category)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True, related_name="gifts"
    )
    images = models.ManyToManyField(Image, related_name="gifts")

    def __str__(self) -> str:
        return self.name
