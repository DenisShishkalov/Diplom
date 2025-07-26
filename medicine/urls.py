from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from medicine.apps import MedicineConfig
from medicine.views import TemplateView, DoctorCreateView, DoctorListView, DoctorDetailView, DoctorUpdateView, DoctorDeleteView
from . import views

app_name = MedicineConfig.name

urlpatterns = [
    path("", views.CompanyView.as_view(), name="company"),
    path('medicine/doctor/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('medicine/doctor/', DoctorListView.as_view(), name='doctor_list'),
    path('medicine/doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('medicine/doctor/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('medicine/doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
