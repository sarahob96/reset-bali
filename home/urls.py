from django.contrib import admin
from django.urls import path
from . import views
from . import models


urlpatterns = [
    path('', views.form_review, name='home'),
    path('home/', views.form_review, name="form_review"),
    path('home/', views.delete_comment, name="delete"),

]