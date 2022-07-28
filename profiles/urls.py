from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
       path('profiles', views.profiles, name="profiles"),
       path('password/', auth_views.PasswordChangeView.as_view
            (template_name="profiles/change-password.html")),

]
