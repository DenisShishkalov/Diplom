import secrets
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from config.settings import EMAIL_HOST_USER
from users.forms import LoginForm, UserRegisterForm
from users.models import User


class UserListView(LoginRequiredMixin, ListView):
    """Контроллер списка пользователей сервиса"""

    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"


class UserRegisterView(CreateView):
    """Регистрация пользователя через верификацию отправки на почту подтверждения"""

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("medicine:home")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет перейди по ссылке, для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """подтверждение почты по токену"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class LoginView(FormView):
    """Аутентификация пользователя"""

    form_class = LoginForm
    template_name = "users/login.html"

    def get_success_url(self):
        return self.request.POST.get("next", reverse_lazy("medicine:home"))

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active:
            messages.error(self.request, "Подтвердите ваш адрес электронной почты")
            return redirect("login")

        login(self.request, user)

        return super().form_valid(form)


class LogoutView(LogoutView):
    """Выход из аккаунта"""

    next_page = reverse_lazy("users:login")
