from django.contrib import admin
from django.urls import path

from . import views

# Указываем url страниц
urlpatterns = [
    path('', views.index, name='home'),
    path("create", views.create, name='create'),
    path("admin/", views.admin, name='admin'),
    path("user_active", views.user_is_active, name='user'),
    path("orders", views.orders, name='user')
]
