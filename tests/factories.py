import factory

from apps.product.models import Category, Image, Product
from apps.vendor.models import Vendor


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    slug = factory.Faker("slug")


class ImageFactory(factory.DjangoModelFactory):
    class Meta:
        model = Image

    image = factory.django.ImageField(color="blue")
    name = "Image"


class VendorFactory(factory.DjangoModelFactory):
    class Meta:
        model = Vendor

    name = factory.Faker("word")
    slug = factory.Faker("slug")


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)

    @factory.post_generation
    def images(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for image in extracted:
                self.images.add(image)

    name = factory.Faker("word")
    slug = factory.Faker("slug")
    price = 15_000
    description = factory.Faker("text")
    specification = {"location": "Secret"}
    vendor = factory.SubFactory(VendorFactory)
