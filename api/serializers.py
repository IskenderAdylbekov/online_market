from rest_framework import serializers
from django.contrib.auth import get_user_model


from shop.models import Product, Category, Subcategory


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "created_by",
            "category",
            "subcategory",
            "is_sold",
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )
