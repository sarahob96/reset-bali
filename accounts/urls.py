from django.urls import path
from . import views

urlpatterns = [
   path('account_login/', views.account_login, name="login"),
   path('accountRegister/', views.accountRegister, name="register")
]
