from django.urls import path
from . import views


urlpatterns = [
    

    path('locations', views.locations, name="locations"),
    path('rewind', views.rewindbooking, name="rewindbooking"),
    path('restart', views.restart, name="restart"),
    path('renew', views.renew, name="renew"),
    path('ubud', views.ubud, name="ubud"),
    path('seminyak', views.seminyak, name="seminyak"),
    
]