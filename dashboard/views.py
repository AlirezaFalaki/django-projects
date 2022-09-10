from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from email_app.models import Email
# Create your views here.
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        in_emails = self.request.user.ReceiveEmails.all()
        return render(request, 'main.html', context={'mails': in_emails})


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
            user = User.objects.create(username=username, email=email, password=password)
            login(request, user)
            return redirect('dashboard:main')
        return HttpResponse('invalid input data !!!.')


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


def detailmail(request, pk):
    mail = Email.objects.get(id=pk)
    if not mail.is_read:
        mail.is_read = True
        mail.save()
        return render(request, 'MailDetail.html', context={'mail': mail})
    return render(request, 'MailDetail.html', context={'mail': mail})
