from django.urls import path, include

from .views import ProductListCreateView, ProductDetailView

urlpatterns = [
    path("products/", ProductListCreateView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("auth/", include("rest_framework.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path(
        "dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")  # new
    ),
]
