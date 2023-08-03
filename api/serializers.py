from rest_framework import serializers


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
