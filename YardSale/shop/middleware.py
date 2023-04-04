from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.decorators import login_required

class LoginRequiredMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response    

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        allowed_urls = [reverse('shop:login'), reverse('shop:register')]  # lista de URLs permitidas
        if not request.user.is_authenticated and request.path not in allowed_urls:
            return redirect(reverse('shop:login'))
        return None