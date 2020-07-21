# Generated by Django 3.0.8 on 2020-07-14 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gift", "0001_Gifts"),
        ("order", "0002_NumberBlank"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                related_name="_order_products_+", to="gift.Gift"
            ),
        ),
    ]
