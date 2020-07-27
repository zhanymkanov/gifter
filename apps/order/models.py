import random
import string
import uuid

from django.conf import settings
from django.db import models

from apps.gift.models import Gift
from apps.models import ContactsModel


class Order(ContactsModel):
    class DeliveryStatus(models.TextChoices):
        NO_DELIVERY = 0, "NO_DELIVERY"
        DELIVERY_NEW = 1, "DELIVERY_NEW"
        DELIVERY_IN_PROGRESS = 10, "DELIVERY_IN_PROGRESS"
        DELIVERY_DONE = 20, "DELIVERY_DONE"
        DELIVERY_FAILED = 40, "DELIVERY_FAILED"

    class EmailDeliveryStatus(models.TextChoices):
        EMAIL_DELIVERY_NEW = 1, "EMAIL_DELIVERY_NEW"
        EMAIL_DELIVERY_DONE = 20, "EMAIL_DELIVERY_DONE"
        EMAIL_DELIVERY_FAILED = 40, "EMAIL_DELIVERY_FAILED"

    class PaymentStatus(models.TextChoices):
        PENDING = 0, "PENDING"
        PAID = 20, "PAID"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=16, unique=True, editable=False, blank=True)
    delivery_status = models.CharField(
        max_length=64,
        choices=DeliveryStatus.choices,
        default=DeliveryStatus.NO_DELIVERY,
        editable=False,
    )
    email_delivery_status = models.CharField(
        max_length=64,
        choices=EmailDeliveryStatus.choices,
        default=EmailDeliveryStatus.EMAIL_DELIVERY_NEW,
        editable=False,
    )
    payment_status = models.PositiveSmallIntegerField(
        choices=PaymentStatus.choices, default=PaymentStatus.PENDING, editable=False,
    )
    total = models.PositiveIntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        editable=False,
        related_name="orders",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    products = models.ManyToManyField(Gift, related_name="+")

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    expires_at = models.DateTimeField(blank=True, null=True)

    @classmethod
    def generate_number(cls) -> str:
        sku_chars = string.ascii_uppercase + string.digits

        def generate() -> str:
            return "".join(random.choices(sku_chars, k=7))

        while number := generate():
            if not cls.objects.filter(number=number).exists():
                break

        return number

    def __str__(self):
        return f"Order: {self.number}"
