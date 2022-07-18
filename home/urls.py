from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  
    path('form_review/', views.form_review, name="form_review"),
    path('homepage', views.homepage, name="home")
]