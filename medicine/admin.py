from django.contrib import admin
from medicine.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'resume', 'specialization',)
    list_filter = ('specialization',)
    search_fields = ('full_name', 'specialization',)

