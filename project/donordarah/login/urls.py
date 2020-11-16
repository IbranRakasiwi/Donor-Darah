from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views

urlpatterns = [
    path('',views.base),
    # path('login/', views.login),

]