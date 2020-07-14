import random
import string
import uuid

from django.conf import settings
from django.db import models

from apps.gift.models import Gift
from apps.models import ContactsModel


class Order(ContactsModel):
    class Status(models.TextChoices):
        NEW = "NEW"

        PROCESS_IN_PROGRESS = "PROCESS_IN_PROGRESS"
        PROCESS_OK = "PROCESS_OK", "Process OK"
        PROCESS_ERROR = "PROCESS_ERROR"

        CANCEL_IN_PROGRESS = "CANCEL_IN_PROGRESS"
        CANCEL_OK = "CANCEL_OK", "Cancel OK"
        CANCEL_ERROR = "CANCEL_ERROR"

    class PaymentStatus(models.TextChoices):
        PENDING = 0, "PENDING"
        PAID = 10, "PAID"

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    number = models.CharField(max_length=16, unique=True, editable=False,)
    status = models.CharField(
        max_length=64, choices=Status.choices, default=Status.NEW, editable=False,
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
    products = models.ManyToManyField(Gift)

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
