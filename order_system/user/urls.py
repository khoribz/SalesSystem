from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(r'^login/$', views.LoginUser.as_view(), name='login'),
    path(r'^logout/$', views.LogoutUser.as_view(), name='logout'),
]
