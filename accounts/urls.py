from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm, ChangeForm

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(authentication_form=LoginForm),
        name="login",
    ),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(form_class=ChangeForm),
        name="password_change",
    ),
    path("", include("django.contrib.auth.urls")),
]
