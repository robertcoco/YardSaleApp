import requests
import json

from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = 'uploads/')
    price = models.IntegerField(default = 0)
    category = models.CharField(max_length = 250, default= "category")

    def __str__(self):
          return self.name

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
