from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import changePassword

urlpatterns = [
   path('new_account/', views.new_account, name="register"),
   path('login_form/', views.login_form, name="login"),
   path('logout_page/', views.logout_page, name="logout"),
   path('password/', changePassword.as_view
        (template_name="accounts/change-password.html"),
        name="changepassword"),
   path('password_changed/', views.password_changed, name="password-changed"),

]
