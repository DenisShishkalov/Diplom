from django.views.generic import DetailView, ListView

from medicine.models import Doctor, Company
from services.models import Service


class HomeView(ListView):
    """Контроллер отображения главной информации"""
    model = Company
    template_name = "medicine/home.html"
    context_object_name = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor'] = Doctor.objects.all()  # или фильтруй как нужно
        context['service'] = Service.objects.all()
        context['Leading_specialist'] = Doctor.objects.get(pk=1)
        return context


class CompanyView(ListView):
    """Контроллер отображения информации о компании"""
    model = Company
    template_name = "medicine/company.html"
    context_object_name = "company"


class DoctorListView(ListView):
    """Контроллер вывода списка врачей"""
    model = Doctor
    template_name = "medicine/doctor_list.html"
    context_object_name = "doctors"


class DoctorDetailView(DetailView):
    """Контроллер для детального просмотра"""
    model = Doctor
    context_object_name = "doctor"
