from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField


# CustomUser чтобы изменять пользователя если потребуется
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)


AUTH_USER_MODEL = "accounts.CustomUser"
