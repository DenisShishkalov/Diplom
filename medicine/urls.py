from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from medicine.apps import MedicineConfig
from . import views
from .views import DoctorListView, DoctorDetailView

app_name = MedicineConfig.name

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("company/", views.CompanyView.as_view(), name="company"),
    path('medicine/doctor/', DoctorListView.as_view(), name='doctor_list'),
    path('medicine/doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
