from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    """Модель контактов компании"""
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="Email")
