from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from rest_framework.reverse import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from services.forms import ServiceForm
from services.models import Service


class ServiceCreateView(LoginRequiredMixin, CreateView):
    """Кoнтроллер создания услуги"""

    model = Service
    form_class = ServiceForm  # используем форму для создания услуги
    success_url = reverse_lazy("services:service_list")


class ServiceListView(ListView):
    """Контроллер вывода списка услуг"""
    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"


class ServiceDetailView(DetailView):
    """Контроллер для детального просмотра услуги"""
    model = Service
    context_object_name = "services/service_detail.html"


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения услуги"""

    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("services:service_list")

    def get_success_url(self):
        return reverse("services:service_detail", args=[self.kwargs.get("pk")])


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления услуги"""

    model = Service
    success_url = reverse_lazy("services:service_list")
