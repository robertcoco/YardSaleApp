# python build in libraries

# 
from django.contrib.auth.views import logout_then_login
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Product, ItemCarrito, Carrito
from social_django.utils import load_strategy
from social_django.views import _do_login
from social_django.utils import load_strategy, load_backend
from social_core.exceptions import AuthCanceled

# Create your views here.

def google_auth(request):
    strategy = load_strategy(request)
    backend = 'google-oauth2'
    return _do_login(request, strategy, backend)

def home(request):
    product_list = Product.objects.all()
    itemCarrito = ItemCarrito.objects.all()
    if request.user.is_authenticated:
        username = request.user.username
        usuario = User.objects.get(username = username)
        carrito = Carrito.objects.filter(usuario = usuario)
        total_de_productos = itemCarrito.count()

    return render(request, "shop/index.html", {
        'product_list': product_list,
        'ItemsCarrito': itemCarrito,
        'total': total_de_productos
        })

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
    itemCarrito = ItemCarrito.objects.all()
    return render(request, "shop/productDetail.html", {
        "product" : product,
        "ItemsCarrito": itemCarrito
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

    else:
        # Mostrar el formulario de registro y el botón de inicio de sesión de Google
        context = {}
        context['google_login_url'] = (
            "{% url 'social:begin' 'google-oauth2' %}?next={% url 'shop:register' %}"
        )
        return render(request, "shop/register.html", context)

    # Comprobar si el usuario se autenticó con Google
    strategy = load_strategy(request)
    backend = load_backend(strategy, 'google-oauth2', redirect_uri=None)

    try:
        social = request.session['partial_pipeline']['kwargs']['social']
        user = backend.do_auth(social)

        # Si el usuario se autenticó con Google, redirigir a una página de confirmación
        return redirect('shop:login')

    except (KeyError, AuthCanceled):
        pass

    return render(request, "shop/register.html")


def user_login(request):
    if request.method == "POST":
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
    return logout_then_login(request, login_url="http://localhost:8000/shop/login")
  # Redirect to a success page.

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        username = request.POST['username']

    usuario = User.objects.get(username=username)
    carrito = Carrito.objects.create(usuario=usuario)
    producto = Product.objects.get(name=product.name)
    item = ItemCarrito.objects.create(producto=producto, carrito=carrito, cantidad=1, precio_unitario=producto.price)
    return HttpResponseRedirect(reverse("shop:detail", args = (product.id,)))

def eliminar_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = ItemCarrito.objects.get(id=item_id)
        item.delete()
    return redirect('shop:index')
