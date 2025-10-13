from django.urls import path
from . import views

app_name = 'authSys'

urlpatterns = [
    path('', views.login, name="login"),
    path('', views.registration, name="registration")
]

