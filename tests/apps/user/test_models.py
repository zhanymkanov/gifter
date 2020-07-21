import pytest

from apps.user.constants import ErrorMessage
from apps.user.models import User


@pytest.mark.django_db
def test_user_str():
    email = "test@test.com"
    user = User.objects.create(email=email, password="password")
    user.save()

    assert str(user) == email


@pytest.mark.django_db
def test_createsuperuser():
    user = User.objects.create_superuser(
        email="test@test.com", password="password", is_staff=True, is_superuser=True,
    )
    user.save()

    assert user.is_superuser


@pytest.mark.django_db
def test_createsuperuser_fail_is_staff():
    with pytest.raises(ValueError) as exc:
        User.objects.create_superuser(
            email="test@test.com",
            password="password",
            is_staff=False,
            is_superuser=True,
        )

    assert str(exc.value) == ErrorMessage.SUPERUSER_MUST_HAVE_IS_STAFF_TRUE


@pytest.mark.django_db
def test_createsuperuser_fail_is_superuser():
    with pytest.raises(ValueError) as exc:
        User.objects.create_superuser(
            email="test@test.com",
            password="password",
            is_staff=True,
            is_superuser=False,
        )

    assert str(exc.value) == ErrorMessage.SUPERUSER_MUST_HAVE_IS_SUPERUSER_TRUE
