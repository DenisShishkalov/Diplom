from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from services.apps import ServicesConfig
from services.views import ServiceCreateView, ServiceListView, ServiceDetailView, ServiceDeleteView, ServiceUpdateView

app_name = ServicesConfig.name

urlpatterns = [
    path('service/create/', ServiceCreateView.as_view(), name='service_create'),
    path('service/', ServiceListView.as_view(), name='service_list'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('service/<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('service/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
