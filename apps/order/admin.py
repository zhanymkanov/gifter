from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "delivery_status",
        "email_delivery_status",
        "payment_status",
        "created_at",
        "expires_at",
    )
    list_filter = (
        "delivery_status",
        "email_delivery_status",
        "payment_status",
    )
    search_fields = ("email", "contact_phone", "contact_name")
    ordering = ("-created_at",)

    readonly_fields = (
        "uuid",
        "delivery_status",
        "email_delivery_status",
        "payment_status",
        "number",
        "total",
    )


admin.site.register(Order, OrderAdmin)
