# Generated by Django 3.0.8 on 2020-07-03 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_Category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
    ]