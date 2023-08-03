from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model


# from shop.models import Product


# CustomUser чтобы изменять пользователя если потребуется
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)


AUTH_USER_MODEL = "accounts.CustomUser"


# class Conversation(models.Model):
#     product = models.ForeignKey(
#         Product, related_name="conversations", on_delete=models.CASCADE
#     )
#     members = models.ManyToManyField(get_user_model(), related_name="conversations")
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["-modified_at"]


# class ConversationMessage(models.Model):
#     conversation = models.ForeignKey(
#         Conversation, related_name="messages", on_delete=models.CASCADE
#     )
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.ForeignKey(
#         get_user_model(), related_name="created_messages", on_delete=models.CASCADE
#     )
