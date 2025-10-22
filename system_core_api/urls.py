from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login_api'),
    path('register/', views.RegisterAPIView.as_view(), name='register_api'),
    path('password_reset/', views.PasswordResetRequestAPIView.as_view(), name='password_reset'),
    path('student_register/', views.StudentRegAPIView.as_view(), name='student_register_api')
]
