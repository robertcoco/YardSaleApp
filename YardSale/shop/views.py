# python build in libraries
import json
import requests

# django
from .forms import NewUserForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login
from .models import Product

# Create your views here.

class IndexView(generic.ListView):
    template_name = "shop/index.html"
    context_object_name = "product_list"

    def get_queryset(self):
        """Return all the products"""
        return Product.objects.all()

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


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, "shop/productDetail.html", {
        "product" : product
    })

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registation successful" )
            login(request, user)
            return redirect("shop:index")
        messages.error(request, "Unsuccessful resgistration. Invalid information")
    form = NewUserForm()
    return render(request, "shop/register.html", {"register_form" : form})