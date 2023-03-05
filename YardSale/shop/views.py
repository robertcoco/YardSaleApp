# python build in libraries
import json
import requests

# django
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Product
# Create your views here.

class IndexView(generic.ListView):
    template_name = "shop/index.html"
    context_object_name = "lasted_question_list"

    def get_queryset(self):
        """Return all the products"""
        return Product

class ClotheView(generic.ListView):
    template_name = "shop/clothes.html"
    context_object_name = "product_clothing_list"

    def get_queryset(self):
        """Return all the clothing products."""
        return Product.objects.filter(category__endswith = "clothing")
    
class ElectronicView(generic.ListView):
    template_name = "shop/electronics.html"
    context_object_name = "product_electronics_list"

    def get_queryset(self):
        """Return all the electronics products"""
        return Product.objects.filter(category = "electronics")
    
class FurnitureView(generic.ListView):
    template_name = "shop/furnitures.html"
    context_object_name = "lasted_question_list"

    def get_queryset(self):
        """Return the five last questions of the list"""
        return Product
    
class ToyView(generic.ListView):
    template_name = "shop/toys.html"
    context_object_name = "lasted_question_list"

    def get_queryset(self):
        """Return the five last questions of the list"""
        return Product


