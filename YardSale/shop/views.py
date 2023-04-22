# python build in libraries
from functools import reduce
from operator import or_
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
from django.db.models import Q
from django.contrib.postgres.search import SearchQuery, SearchVector
# Create your views here.
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import OAuth2CallbackView

class GoogleLoginCallbackView(OAuth2CallbackView, generic.View):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

def home(request):
    query = request.GET.get('q')
    if query:
        # Dividir la cadena de consulta en palabras individuales
        keywords = query.split()

        # Lista de campos en los que se buscará
        fields = ['name__icontains', 'category__icontains']

        # Lista de consultas de búsqueda que se combinarán con OR
        queries = [Q(**{field: keyword}) for keyword in keywords for field in fields]

        # Combinar todas las consultas usando el operador OR
        product_list = Product.objects.filter(reduce(or_, queries))

    else:
        product_list = Product.objects.all()

    # Resto del código de la vista

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

def clothing(request):
    itemCarrito = ItemCarrito.objects.all()
    total_de_productos = itemCarrito.count()
    product_clothing_list = Product.objects.filter(category__endswith = "clothing")

    return render(request, "shop/clothes.html", {
        'product_clothing_list': product_clothing_list,
        'ItemsCarrito': itemCarrito,
        'total': total_de_productos
        })
    
def electronic(request):
    itemCarrito = ItemCarrito.objects.all()
    total_de_productos = itemCarrito.count()
    product_electronics_list = Product.objects.filter(category = "electronics")

    return render(request, "shop/electronics.html", {
        'product_electronics_list': product_electronics_list,
        'ItemsCarrito': itemCarrito,
        'total': total_de_productos
        })
    
def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    itemCarrito = ItemCarrito.objects.all()
    total = itemCarrito.count()
    return render(request, "shop/productDetail.html", {
        "product" : product,
        "ItemsCarrito": itemCarrito,
        "total": total 
    })

def register_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # Verificar que las contraseñas coincidan
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('shop:register')
        
        # Iniciar sesión y redirigir al usuario a la página de inicio
        user = authenticate(request, username=username, password=password1)
        login(request, user)
        messages.success(request, '¡Registro exitoso!')
        return redirect('shop:index')
    
    return render(request, 'shop/register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión con éxito
            login(request, user)
            return redirect("shop:index")
        
        else:
            # Si el usuario no existe y no ha iniciado sesión con Facebook o Google, mostrar mensaje de error
            messages.error(request, "Credenciales incorrectas")
            return redirect("shop:login")
            
    return render(request, "shop/login.html")

def user_logout(request):
    return logout_then_login(request, login_url="http://localhost:8000/accounts/login")
  # Redirect to a success page.

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        username = request.POST['username']

    usuario = User.objects.get(username=username)
    carrito = Carrito.objects.get(usuario=usuario)
    producto = Product.objects.get(name=product.name)
    item = ItemCarrito.objects.create(producto=producto, carrito=carrito, cantidad=1, precio_unitario=producto.price)
    return HttpResponseRedirect(reverse("shop:detail", args = (product.id,)))

def eliminar_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = ItemCarrito.objects.get(id=item_id)
        item.delete()
    return redirect('shop:index')

def shopping_page(request):
    item_carrito = ItemCarrito.objects.all()

    if request.user.is_authenticated:
        username = request.user.username
        usuario = User.objects.get(username = username)

    carrito = Carrito.objects.get(usuario=usuario)
    total_price = carrito.get_total()
    total_de_productos = item_carrito.count()

    return render(request, "shop/shoppingPage.html", {
        'ItemsCarrito': item_carrito,
        'total': total_de_productos,
        'total_price': total_price
        })
    

    