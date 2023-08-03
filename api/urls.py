from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import UserViewSet, ProductViewSet

# url объединили в один. Теперь вместо 4х здесь 2 маршрута
router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", ProductViewSet, basename="products")

urlpatterns = router.urls

# from .views import ProductListCreateView, ProductDetailView


# urlpatterns = [
#     path("products/", ProductListCreateView.as_view(), name="product_list"),
#     path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),

# ]
