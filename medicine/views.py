from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from rest_framework.reverse import reverse_lazy

from medicine.forms import AppointmentForm
from medicine.models import Appointment, Company, Doctor
from services.models import Service


class HomeView(ListView):
    """Контроллер отображения главной информации"""

    model = Company
    template_name = "medicine/home.html"
    context_object_name = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["home"] = Company.objects.first()
        context["doctor"] = Doctor.objects.all()  # или фильтруй как нужно
        context["service"] = Service.objects.all()

        return context


class CompanyView(ListView):
    """Контроллер отображения информации о компании"""

    model = Company
    template_name = "medicine/company.html"
    context_object_name = "company"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctor"] = Doctor.objects.all()  # или фильтруй как нужно
        context["service"] = Service.objects.all()

        return context


class DoctorListView(ListView):
    """Контроллер вывода списка врачей"""

    model = Doctor
    template_name = "medicine/doctor_list.html"
    context_object_name = "doctors"


class DoctorDetailView(DetailView):
    """Контроллер для детального просмотра"""

    model = Doctor
    context_object_name = "doctor"


class AppointmentListView(ListView):
    """Список записей на прием"""

    model = Appointment
    template_name = "medicine/appointment_list.html"
    context_object_name = "appointments"


# LoginRequiredMixin не позволяет неавторизованным пользователям использовать указанные
class AppointmentCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания записи"""

    model = Appointment
    form_class = AppointmentForm  # используем форму для создания записи
    success_url = reverse_lazy("medicine:appointment_list")

    # автоматическое присваивание владельца при создании

    def form_valid(self, form):
        appointment = form.save()
        user = self.request.user
        appointment.owner = user
        appointment.save()
        return super().form_valid(form)


class ContactsListView(ListView):
    model = Company
    template_name = "medicine/contacts.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["company"] = Company.objects.all()  # или фильтруй как нужно

        return context
