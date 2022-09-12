from django.contrib.auth.models import User
from rest_framework import viewsets, generics, renderers, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import EmailSerializer, RegisterSerializer, UserSerializer
from .models import Email
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.response import Response
# Create your views here.


class AuthorEmailViewset(viewsets.ModelViewSet):

    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def filter_queryset(self, queryset):
        queryset = Email.objects.filter(author=self.request.user.id)
        return super().filter_queryset(queryset)

    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': str(request.auth),  # None
    #     }
    #     return Response(content)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# class Logout(generics.GenericAPIView):




