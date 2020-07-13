# Generated by Django 3.0.8 on 2020-07-13 16:32

import uuid

import django.db.models.deletion
import djmoney.models.fields
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("gift", "0001_Gifts"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contact_name", models.CharField(max_length=64)),
                (
                    "contact_phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        db_index=True, max_length=64, region=None
                    ),
                ),
                ("city", models.CharField(max_length=64)),
                ("shipping_address", models.CharField(blank=True, max_length=256)),
                ("email", models.EmailField(db_index=True, max_length=254)),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "number",
                    models.CharField(editable=False, max_length=16, unique=True,),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("NEW", "New"),
                            ("PROCESS_IN_PROGRESS", "Process In Progress"),
                            ("PROCESS_OK", "Process OK"),
                            ("PROCESS_ERROR", "Process Error"),
                            ("CANCEL_IN_PROGRESS", "Cancel In Progress"),
                            ("CANCEL_OK", "Cancel Ok"),
                            ("CANCEL_ERROR", "Cancel Error"),
                        ],
                        default="NEW",
                        editable=False,
                        max_length=64,
                    ),
                ),
                (
                    "payment_status",
                    models.PositiveSmallIntegerField(
                        choices=[("0", "PENDING"), ("10", "PAID")],
                        default="0",
                        editable=False,
                    ),
                ),
                (
                    "total_currency",
                    djmoney.models.fields.CurrencyField(
                        choices=[
                            ("KZT", "Tenge"),
                            ("RUB", "Russian Ruble"),
                            ("USD", "US Dollar"),
                        ],
                        default="KZT",
                        editable=False,
                        max_length=3,
                    ),
                ),
                (
                    "total",
                    djmoney.models.fields.MoneyField(decimal_places=2, max_digits=12),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("expires_at", models.DateTimeField(blank=True, null=True)),
                ("products", models.ManyToManyField(to="gift.Gift")),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
