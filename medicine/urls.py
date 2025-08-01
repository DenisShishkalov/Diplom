from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from medicine.apps import MedicineConfig

from .views import (AppointmentCreateView, AppointmentListView, CompanyView,
                    DoctorDetailView, DoctorListView, HomeView, ContactsListView)

app_name = MedicineConfig.name

urlpatterns = [
    # Главная страница, о компании, контакты
    path("", HomeView.as_view(), name="home"),
    path("company/", CompanyView.as_view(), name="company"),
    path("contacts/", ContactsListView.as_view(), name="contacts"),
    # Список и создание докторов
    path("medicine/doctor/", DoctorListView.as_view(), name="doctor_list"),
    path("medicine/doctor/<int:pk>/", DoctorDetailView.as_view(), name="doctor_detail"),
    # создание и список записей на прием
    path(
        "medicine/appointment/", AppointmentListView.as_view(), name="appointment_list"
    ),
    path(
        "medicine/appointment/create/",
        AppointmentCreateView.as_view(),
        name="appointment_form",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
