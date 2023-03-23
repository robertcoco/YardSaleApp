# python build in libraries
import json

# django
from .forms import NewUserForm
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth


# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = "/shop/login/"
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
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        return redirect("shop:login")

    return render(request, "shop/register.html")

def user_login(request):
    if request.method == "POST":
        products = Product.objects.all()
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            name = user.first_name
            login(request, user)
            return redirect("shop:index")

        else:
            messages.error(request, "Bad credentials")
            return redirect("shop:login")  
  
    return render(request, "shop/login.html")


def user_logout(request):
    logout_then_login(request,login_url='shop/login')
    return redirect ("shop:login")
  # Redirect to a success page.
