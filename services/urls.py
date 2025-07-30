from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from services.apps import ServicesConfig
from services.views import ServiceDetailView, ServiceListView

app_name = ServicesConfig.name

urlpatterns = [
    path("service/", ServiceListView.as_view(), name="service_list"),
    path("service/<int:pk>/", ServiceDetailView.as_view(), name="service_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
