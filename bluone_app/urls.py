from django.contrib import admin
from django.urls import path
from bluone_app.views import create_employee,get_employee

urlpatterns = [
    path('api/v1/user/create/',create_employee),
    path('api/v1/user/get/',get_employee),
]