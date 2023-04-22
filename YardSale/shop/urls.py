from django.urls import path, include
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.home, name = "index"),
    path("<int:product_id>/detail", views.product, name = "detail"),
    path("<int:product_id>/addCart", views.add_to_cart, name = "addCart"),
    path("clothes/", views.clothing, name = "clothes"),
    path("electronics/", views.electronic, name = "electronics"),
    path("register/", views.register_request, name = "register"),
    path("login/", views.user_login, name = "login"),
    path('logout/', views.user_logout, name= "logout"),
    path('eliminar_item/', views.eliminar_item, name='eliminar_item'),
    path("shoppingCart", views.shopping_page, name = "shopping")
]