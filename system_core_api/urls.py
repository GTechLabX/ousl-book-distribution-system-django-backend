from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login_api'),
    path('register/', views.RegisterAPIView.as_view(), name='register_api'),
]
