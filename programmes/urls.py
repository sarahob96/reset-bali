from django.urls import path
from . import views


urlpatterns = [

    path('locations', views.locations, name="locations"),
    path('rewind', views.rewindbooking, name="rewindbooking"),
    path('restart', views.restartbooking, name="restartbooking"),
    path('renew', views.renewbooking, name="renewbooking"),
    path('ubud', views.ubud, name="ubud"),
    path('seminyak', views.seminyak, name="seminyak"),
    path('my_bookings/', views.my_bookings, name="mybookings"),
    path('update_booking/<booking_id>', views.update_booking, name="update_booking"),
    path('delete_booking/<booking_id>', views.delete_booking, name="delete_booking")
    
]