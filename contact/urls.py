from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.form_contact, name="form_contact"),
    path('thanks_for_contacting/', views.thanks_for_contacting, name="thanks_for_contacting"),
]