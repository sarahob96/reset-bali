from django.contrib import admin
from django.urls import path
from . import views
from . import models


urlpatterns = [
    path('', views.homepage, name='home'),
    path('form_review/', views.form_review, name="form_review"),
    path('homepage/', views.homepage, name="home"),
    path('reviews/', models.Review, name="reviews"),

]