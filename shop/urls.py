from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("<int:pk>/<slug:slug>/", views.detail, name="detail"),
    path("new/", views.new, name="new"),
    path("my_products/", views.my_products_list, name="dashboard"),
    path("<int:pk>/<slug:slug>/delete/", views.delete, name="delete"),
    path("<int:pk>/<slug:slug>/edit/", views.edit, name="edit"),
    path("search/", views.search_products, name="search"),
]
