from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from users.apps import UsersConfig
from users.views import LoginView, LogoutView, UserRegisterView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    # Регистрация/авторизация
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    # выход из системы
    path("logout/", LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
