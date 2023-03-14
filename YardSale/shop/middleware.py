from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.shortcuts import render


class AuthanticatedUserMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        if user.is_authenticated:
            return render(request, "shop/login.html")
        else:
            return HttpResponse('Unauthorised', status=401)