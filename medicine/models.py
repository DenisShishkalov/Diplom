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
    work_experience = models.PositiveIntegerField(verbose_name="стаж работы", blank=True, null=True, default=0)
    resume = models.TextField(verbose_name='Резюме доктора')
    specialization = models.CharField(max_length=150, choices=choice_specialization, verbose_name='специализация', db_index=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'доктор'
        verbose_name_plural = 'доктора'
