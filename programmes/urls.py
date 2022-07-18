from django.urls import path
from . import views


urlpatterns = [
  
    path('locations', views.locations, name="locations"),
    path('rewind', views.locations, name="rewind"),
    path('restart', views.locations, name="restart"),
    path('renew', views.locations, name="renew"),

]