from django.db import models


class Doctor(models.Model):
    """Модель доктора"""
    choice_specialization = [
        ("doctor of functional diagnostics", "Врач функциональной диагностики"),
        ("Radiation diagnostics", "Лучевой диагност"),
        ("A doctor of ultrasound diagnostics", "Врач ультразвуковой диагностики"),
        ("Doctor of clinical laboratory diagnostics", "Врач клинической лабораторной диагностики"),
        ("Doctor of the Centers of Hygiene and Epidemiology", "Врач центров гигиены и эпидемиологии")
    ]

    full_name = models.CharField(max_length=100, verbose_name='Имя и фамилия доктора')
    work_experience = models.PositiveIntegerField(verbose_name="стаж работы", blank=True, null=True)
    resume = models.TextField(verbose_name='Резюме доктора')
    specialization = models.CharField(max_length=150, choices=choice_specialization, verbose_name='специализация', db_index=True)


class Company(models.Model):
    """Модель компании"""
    name = models.CharField(max_length=100, verbose_name='название компании', help_text='укажите название компании')
    history = models.TextField(verbose_name='история компании', blank=True, null=True)
    mission = models.CharField(verbose_name='миссия компании', blank=True, null=True)
    value = models.CharField(verbose_name='ценность компании', blank=True, null=True)
