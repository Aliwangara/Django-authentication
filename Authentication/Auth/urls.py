from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
     path('Log', views.Log, name='Log'),
]
