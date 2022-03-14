from django.contrib import admin
from django.urls import path, include
from .views import register,home,userview
from django.contrib.auth import views

urlpatterns = [
    path('home/', home, name='home'),
    path('userview/', userview),
    path('register/', register, name='register'),
    path('', views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
