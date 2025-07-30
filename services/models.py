from django.db import models


class Service(models.Model):
    """Модель медицинских услуг"""
    service_specialization = [
        ("Functional diagnostics", "Функциональная диагностика"),
        ("Radiation diagnostics", "Лучевая диагностика"),
        ("Ultrasound diagnostics", "Ультразвуковая диагностика"),
        ("Clinical laboratory diagnostics", "Клиническая лабораторная диагностика"),
    ]

    name = models.CharField(max_length=200, verbose_name='название услуги', help_text='укажите название услуги')
    description = models.TextField(verbose_name='описание услуги', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='цена', help_text='укажите цену на услугу', blank=True, null=True)
    photo = models.ImageField(
        upload_to="services/photo/", verbose_name="Фото услуг", null=True, blank=True
    )
    service_specialization = models.CharField(max_length=250, choices=service_specialization, verbose_name='вид диагностической услуги', default='Функциональная диагностика')

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return self.name
