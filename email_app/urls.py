from django.urls import path, include
from . import views
# from knox import views as knoxviews
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register(r'emails', views.AuthorEmailViewset)

app_name = 'email_app'

urlpatterns = [
    path('', include(router.urls), name='emials'),
    path('register/', views.RegisterAPI.as_view(), name='register'),
    # path('login/', views.LoginAPI.as_view(), name='login'),
    # path('logout/', knoxviews.LogoutView.as_view(), name='logout'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),



]


