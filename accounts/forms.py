from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model
from django import forms


CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("phone", "age", "country")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите имя", "class": "w-full py-4 px-6 rounded-xl"}
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Введите электронную почту",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Придумайте пароль",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Подтвердите пароль",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите имя", "class": "w-full py-4 px-6 rounded-xl"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )


class ChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )
    new_password_conf = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                "class": "w-full py-4 px-6 rounded-xl",
            }
        )
    )
