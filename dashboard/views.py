from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')


class RegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')
