from django.urls import path
from . import views


urlpatterns = [
   path('account_login/', views.account_login, name="login"),
   path('account_register/', views.account_register, name="register"),

]
