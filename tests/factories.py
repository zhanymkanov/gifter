import factory
from django.conf import settings

from apps.gift.models import Category, Gift, Image
from apps.order.models import Order
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

    name = factory.Faker("name")
    slug = factory.Faker("slug")


class GiftFactory(factory.DjangoModelFactory):
    class Meta:
        model = Gift

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

    name = factory.Faker("name")
    slug = factory.Faker("slug")
    price = 15_000
    description = factory.Faker("text")
    specification = {"location": "Secret"}
    vendor = factory.SubFactory(VendorFactory)


class OrderFactory(factory.DjangoModelFactory):
    class Meta:
        model = Order

    contact_name = factory.Faker("name")
    contact_phone = factory.Faker("phone_number")
    email = factory.Faker("email")
    city = "Нур-Султан"
    total = 0


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    email = factory.Faker("email")
    password = factory.Faker("word")
