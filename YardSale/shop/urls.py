from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.home, name = "index"),
    path("<int:product_id>/detail", views.product, name = "detail"),
    path("<int:product_id>/addCart", views.add_to_cart, name = "addCart"),
    path("clothes/", views.ClotheView.as_view(), name = "clothes"),
    path("electronics/", views.ElectronicView.as_view(), name = "electronics"),
    path("furnitures/", views.ElectronicView.as_view(), name = "furnitures"),
    path("toys/", views.ElectronicView.as_view(), name = "toys"),
    path("register/", views.register_request, name = "register"),
    path("login/", views.user_login, name = "login"),
    path('logout/', views.user_logout, name= "logout"),
    path('eliminar_item/', views.eliminar_item, name='eliminar_item'),
    path('login/google/', views.google_auth, name='google_auth'),
]