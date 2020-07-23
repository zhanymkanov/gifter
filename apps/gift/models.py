import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from rest_framework.exceptions import NotFound
from versatileimagefield.fields import PPOIField, VersatileImageField

from apps.models import ActiveBaseQueryset, SeoModel
from apps.vendor.models import Vendor

from .constants import ErrorMessage


class CategoryQueryset(ActiveBaseQueryset):
    def get_by_slug(self, slug):
        try:
            category = self.get(slug=slug)
        except Category.DoesNotExist:
            raise NotFound(detail=ErrorMessage.CATEGORY_DOES_NOT_EXIST)

        return category


class Category(SeoModel):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)

    objects = CategoryQueryset.as_manager()

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


class GiftQueryset(ActiveBaseQueryset):
    def get_by_slug(self, slug):
        try:
            gift = self.get(slug=slug)
        except Gift.DoesNotExist:
            raise NotFound(detail=ErrorMessage.GIFT_DOES_NOT_EXIST)

        return gift


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

    objects = GiftQueryset.as_manager()

    def __str__(self) -> str:
        return self.name
