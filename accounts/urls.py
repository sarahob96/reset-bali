from django.urls import path
from . import views


urlpatterns = [
   path('new_account', views.new_account, name="register"),
   path('login_form', views.login_form, name="login"),
   path('logout_page', views.logout_page, name="logout")

]