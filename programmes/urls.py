from django.urls import path
from . import views


urlpatterns = [
  
    path('locations', views.locations, name="locations"),
    path('rewind', views.rewind, name="rewind"),
    path('restart', views.restart, name="restart"),
    path('renew', views.renew, name="renew"),
    path('ubud', views.ubud, name="ubud"),
    path('seminyak', views.seminyak, name="seminyak"),
    path('programmes', views.rewind_booking, name="rewind_booking")
]