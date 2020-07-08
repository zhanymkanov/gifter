# Generated by Django 3.0.8 on 2020-07-08 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendor", "0001_Vendor"),
        ("product", "0003_Product"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="in_stock",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="vendor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="vendor.Vendor",
            ),
        ),
    ]