import uuid
from django.db import models
from django.contrib.postgres.fields import JSONField

from apps.seo.models import SeoModel
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


class Product(SeoModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    in_stock = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField()
    specification = JSONField()
    categories = models.ManyToManyField(Category)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name
