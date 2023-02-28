from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("clothes/", views.ClotheView.as_view(), name = "clothes"),
    path("electronics/", views.ElectronicView.as_view(), name = "electronics"),
    path("furnitures/", views.ElectronicView.as_view(), name = "furnitures"),
    path("toys/", views.ElectronicView.as_view(), name = "toys"),
]