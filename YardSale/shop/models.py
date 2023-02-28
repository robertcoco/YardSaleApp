import requests
import json

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = 'uploads/')
    price = models.IntegerField(default = 0)
    category = models.CharField(max_length = 250, default= "category")

    def __str__(self):
          return self.name

    
# Saving the products into the database

def create_product(name, img, price, category):
        """create a product and save it into the database
        
        parameters:
            - name: CharField/string
            - img: ImageField/img
            - price: IntegerField/int

        returns the created product
        """
        return Product.objects.create(name = name, img = img, price = price, category = category)

response = requests.get("https://fakestoreapi.com/products")
products = response.json()

for key, value in enumerate(products):
      create_product(value["title"], value['image'], value['price'], value['category'])
      