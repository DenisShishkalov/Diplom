from django.contrib import admin
from medicine.models import Doctor, Company


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'resume', 'specialization',)
    list_filter = ('specialization',)
    search_fields = ('full_name', 'specialization',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'history', 'mission', 'values')
    list_filter = ('name',)


