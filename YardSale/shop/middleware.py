from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from allauth.account.views import (
    login, signup, password_reset, password_reset_done, 
)

class LoginRequiredMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response    

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        key = view_kwargs.get('key')  
        allowed_urls = [reverse(login),
        reverse('shop:register'),
        reverse('shop:logout'), 
        reverse(signup), 
        reverse(password_reset), 
        reverse(password_reset_done),]  # lista de URLs permitidas
      # lista de URLs permitidas

         # Obtener la key de la URL si se está accediendo a la página de restauración de contraseña
        if 'key' in view_kwargs:
            key = view_kwargs['key']
            uidb36 = view_kwargs['uidb36']
            reset_url = reverse('account_reset_password_from_key', kwargs={'uidb36': uidb36, 'key': key})
            allowed_urls.append(reset_url)

        if not request.user.is_authenticated and request.path not in allowed_urls and not request.path.startswith(reverse(login)):
            return redirect(login)

        return None