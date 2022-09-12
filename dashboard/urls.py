from django.urls import path
from . import views


app_name = "dashboard"
urlpatterns = [
    path('', views.IndexView.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    # path('detail/<int:pk>/', views.detailmail, name='detail'),
]

# path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
# path('logout/', auth_views.LogoutView.as_view(template_name='user/landing.html'), name="logout"),
# path('register/', register, name="register"),

