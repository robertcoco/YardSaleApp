import json

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = 'uploads/')
    price = models.IntegerField(default = 0)
    category = models.CharField(max_length = 250, default= "category")

    def __str__(self):
          return self.name


class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Product, through='ItemCarrito')

    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    
    @property
    def total(self):
        return sum(item.total for item in self.items.all())

    def get_total(self):
        return self.total

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad}x {self.producto.name} en {self.carrito}"
    @property
    def total(self):
        return self.cantidad * self.precio_unitario



# Saving the products into the database
def create_product(id, name, img, price, category):
        """create a product and save it into the database
        
        parameters:
            - id: AutoField/primary_key
            - name: CharField/string
            - img: ImageField/img
            - price: IntegerField/int

        returns the created product
        """
        return Product.objects.create(
        id = id, 
        name = name,
        img = img, 
        price = price, 
        category = category)

# Save the products in the database from external api

# response = requests.get("https://fakestoreapi.com/products")
# products = response.json()

# for key, value in enumerate(products):
#       create_product(value['id'], value["title"], value['image'], value['price'], value['category'])
