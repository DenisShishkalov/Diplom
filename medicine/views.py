from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)
from rest_framework.reverse import reverse, reverse_lazy
from medicine.forms import DoctorForm
from medicine.models import Doctor
from django.contrib.auth.mixins import LoginRequiredMixin


class CompanyView(TemplateView):
    """Контроллер отображения информации о компании"""

    template_name = "medicine/home.html"


class DoctorCreateView(LoginRequiredMixin, CreateView):
    """КОнтроллер создания доктора"""

    model = Doctor
    form_class = DoctorForm  # используем форму для создания доктора
    success_url = reverse_lazy("clients:client_list")


class DoctorListView(ListView):
    """Контроллер вывода списка врачей"""
    model = Doctor
    template_name = "medicine/doctor_list.html"
    context_object_name = "doctors"


class DoctorDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для детального просмотра"""
    model = Doctor
    context_object_name = "medicine/doctor_detail.html"


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для изменения доктора"""

    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("medicine:doctor_list")

    def get_success_url(self):
        return reverse("medicine:doctor_detail", args=[self.kwargs.get("pk")])


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления доктора"""

    model = Doctor
    success_url = reverse_lazy("medicine:doctor_list")
