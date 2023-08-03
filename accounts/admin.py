from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "phone", "is_staff"]
    list_filter = ["is_staff", "is_active"]
    list_display_links = ["username", "email"]
    fieldsets = (
        (
            None,
            {"fields": ("username", "email", "password", "phone", "age", "country")},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "phone",
                    "age",
                    "country",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
