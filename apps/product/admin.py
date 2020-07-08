from django.contrib import admin

from .models import Category, Image, Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
