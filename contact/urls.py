from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.form_contact, name="form_contact"),
 
]