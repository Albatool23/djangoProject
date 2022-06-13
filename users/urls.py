from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('register', views.index),
    path('new', views.index),
    path('login', views.login),





]