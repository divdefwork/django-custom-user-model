from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Свій/настроюваний менеджер, який розширює BaseUserManager,
    надаючи йому два додаткові методи: create_user і create_superuser.
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Створіть та збережіть користувача з вказаною
        електронною адресою та паролем.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"  # змусити користувача увійти за допомогою email
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()
