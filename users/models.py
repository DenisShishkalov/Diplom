import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватарка", null=True, blank=True
    )
    is_active = models.BooleanField(default=True, blank=True, null=True)

    token = models.CharField(
        max_length=100, verbose_name="Token", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def generate_verification_token(self):
        "Генерация и сохранение токена верификации"
        self.token = secrets.token_urlsafe(32)
        self.save()
        return self.token

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ["email"]
