from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_attempt, name='login'),
    path('register/', views.register, name='register'),
    path('otp/', views.otp, name='otp'),
    path('login-otp/', views.login_otp, name='login_otp'),
]
