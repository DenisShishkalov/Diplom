from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from config import settings
from services.models import Service


class Doctor(models.Model):
    """Модель доктора"""

    doctor_specialization = [
        ("doctor of functional diagnostics", "Врач функциональной диагностики"),
        ("Radiation diagnostics", "Лучевой диагност"),
        ("A doctor of ultrasound diagnostics", "Врач ультразвуковой диагностики"),
        (
            "Doctor of clinical laboratory diagnostics",
            "Врач клинической лабораторной диагностики",
        ),
    ]

    full_name = models.CharField(max_length=100, verbose_name="Имя и фамилия доктора")
    work_experience = models.PositiveIntegerField(
        verbose_name="стаж работы", blank=True, null=True, default=0
    )
    resume = models.TextField(verbose_name="Резюме доктора")
    avatar = models.ImageField(
        upload_to="medicine/avatars/", verbose_name="Аватарка", null=True, blank=True
    )
    specialization = models.CharField(
        max_length=150,
        choices=doctor_specialization,
        verbose_name="специализация",
        db_index=True,
    )

    class Meta:
        verbose_name = "доктор"
        verbose_name_plural = "доктора"

    def __str__(self):
        return self.full_name


class Company(models.Model):
    """Модель компании"""

    name = models.CharField(max_length=100, verbose_name="Название компании")
    history = models.TextField(verbose_name="История компании")
    mission = models.CharField(max_length=500, verbose_name="Миссия компания")
    values = models.TextField(verbose_name="ценность компании")
    phone = PhoneNumberField(blank=True, null=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, verbose_name="Врач", blank=True, null=True
    )
    services = models.ForeignKey(
        to=Service,
        on_delete=models.CASCADE,
        verbose_name="Услуги",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компаний"

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """Модель записи на прием"""

    STATUS_CHOICES = [
        ("You have an appointment", "Вы записаны на прием"),
        ("You haven't made an appointment", "Вы не записаны на прием"),
    ]

    status = models.CharField(
        choices=STATUS_CHOICES,
        default="Вы записаны на прием",
        verbose_name="Статус",
        db_index=True,
    )
    appointment_time = models.DateTimeField(
        verbose_name="время", help_text="укажите время записи на прием",
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        verbose_name="доктор",
        help_text="укажите доктора к которому хотите записаться",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
        null=True,
    )
    response = models.TextField(verbose_name="Результаты диагностики", blank=True, null=True)

    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"

    def __str__(self):
        return f"{self.doctor} : {self.appointment_time}"
