from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')


class LoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print('salam')
            return redirect('/')
        return HttpResponse('Your entered information is not correct !!!')


class RegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('Cpassword')

        if password == cpassword:
            User.objects.create(username=username, email=email, password=password)
            return redirect('dashboard:main')
        return HttpResponse('invalid input data !!!.')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')
