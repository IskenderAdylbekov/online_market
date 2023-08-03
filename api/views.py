from django.shortcuts import render
from rest_framework import generics


from shop.models import Product, Category
from .serializers import ProductsSerializer
from .permissions import IsAuthorOrReadOnly


class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductsSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
