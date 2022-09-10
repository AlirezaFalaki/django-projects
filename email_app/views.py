from django.shortcuts import render
from rest_framework import viewsets, generics, renderers
from rest_framework.response import Response
from .serializers import EmailSerilizer
from .models import Email
# Create your views here.


class Home(viewsets.ModelViewSet):

    queryset = Email.objects.all()
    serializer_class = EmailSerilizer
    renderer_classes = [renderers.StaticHTMLRenderer]





