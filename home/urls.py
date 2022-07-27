from django.contrib import admin
from django.urls import path, include
from . import views
from . import models


urlpatterns = [
    path('', views.form_review, name='home'),
    path('home/', views.form_review, name="form_review"),
    path('my_reviews/', views.my_reviews, name="myreviews"),
    path('update_review/<review_id>', views.update_review, name="update_review"),
    path('delete_review/<review_id>', views.delete_review, name="delete_review")
    

]