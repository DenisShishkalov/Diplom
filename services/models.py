from django.db import models


class Service(models.Model):
    """Модель медицинских услуг"""
    name = models.CharField(max_length=200, verbose_name='название услуги', help_text='укажите название услуги')
    description = models.TextField(verbose_name='описание услуги', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='цена', help_text='укажите цену на услугу', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
