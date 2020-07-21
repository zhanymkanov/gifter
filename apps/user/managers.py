from django.contrib.auth.base_user import BaseUserManager

from .constants import ErrorMessage


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(ErrorMessage.SUPERUSER_MUST_HAVE_IS_STAFF_TRUE)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(ErrorMessage.SUPERUSER_MUST_HAVE_IS_SUPERUSER_TRUE)

        return self.create_user(email, password, **extra_fields)
