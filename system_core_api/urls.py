from django.urls import path
from . import views

urlpatterns = [

    # API Endpoints for Auth-System

    path('login/', views.LoginAPIView.as_view(), name='login_api'),
    path('register/', views.RegisterAPIView.as_view(), name='register_api'),
    path('password_reset/', views.PasswordResetRequestAPIView.as_view(), name='password_reset'),
    path('password_reset_confirm/', views.PasswordResetConfirmAPIView.as_view(), name='password_reset_confirm'),



    # API Endpoints for Dispatch-System

    path('student_register/', views.StudentRegAPIView.as_view(), name='student_register_api')
]
