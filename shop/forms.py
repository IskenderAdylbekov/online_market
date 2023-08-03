from django import forms
from django.utils.text import slugify

from .models import Product, Conversation, ConversationMessage


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "category",
            "subcategory",
            "name",
            "description",
            "price",
            "image",
        )

        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASSES}),
            "subcategory": forms.Select(attrs={"class": INPUT_CLASSES}),
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }


class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "image",
            "is_sold",
        )

        widgets = {
            "name": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "description": forms.Textarea(attrs={"class": INPUT_CLASSES}),
            "price": forms.TextInput(attrs={"class": INPUT_CLASSES}),
            "image": forms.FileInput(attrs={"class": INPUT_CLASSES}),
        }


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "w-full py-4 px-6 rounded-xl border"}
            )
        }
