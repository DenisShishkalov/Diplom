from django.views.generic import DetailView, ListView

from services.models import Service


class ServiceListView(ListView):
    """Контроллер вывода списка услуг"""

    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    """Контроллер для детального просмотра услуги"""

    model = Service
    template_name = "services/service_detail.html"
    context_object_name = "service"
