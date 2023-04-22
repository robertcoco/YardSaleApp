from django.apps import AppConfig
from django.contrib import admin

class ShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'

    def ready(self):
        from .models import Carrito, ItemCarrito

        admin.site.register(Carrito)
        admin.site.register(ItemCarrito)