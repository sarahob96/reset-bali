from django.test import SimpleTestCase
from django.urls import reverse, resolve
from programmes.views import rewindbooking, renewbooking, restartbooking, my_bookings, update_booking, update_renew_booking, update_restart_booking, delete_booking, delete_renew_booking, delete_restart_booking, ubud, seminyak
# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_rewind_booking_url_is_resolved(self):
        url = reverse('rewindbooking')
        print(resolve(url))
        self.assertEquals(resolve(url).func, rewindbooking)

    def test_restart_booking_url_is_resolved(self):
        url = reverse('restartbooking')
        print(resolve(url))
        self.assertEquals(resolve(url).func, restartbooking)

    def test_renew_booking_url_is_resolved(self):
        url = reverse('renewbooking')
        print(resolve(url))
        self.assertEquals(resolve(url).func, renewbooking)

    def test_my_bookings_url_is_resolved(self):
        url = reverse('mybookings')
        print(resolve(url))
        self.assertEquals(resolve(url).func, my_bookings)  
    
    def test_update_booking_url_is_resolved(self):
        url = reverse('update_booking', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_booking)

    def test_update_renew_booking_url_is_resolved(self):
        url = reverse('update_renew_booking', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_renew_booking)

    def test_update_restart_booking_url_is_resolved(self):
        url = reverse('update_restart_booking', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_restart_booking )  

    def test_delete_booking_url_is_resolved(self):
        url = reverse('delete_booking', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_booking )  

    def test_delete_restart_booking_url_is_resolved(self):
        url = reverse('delete_restart_booking', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_restart_booking )  

    def test_delete_renew_booking_url_is_resolved(self):
        url = reverse('delete_renew_booking', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_renew_booking )  

    def test_seminyak_is_resolved(self):
        url = reverse('seminyak')
        print(resolve(url))
        self.assertEquals(resolve(url).func, seminyak)
    
    def test_ubud_url_is_resolved(self):
        url = reverse('ubud')
        print(resolve(url))
        self.assertEquals(resolve(url).func, ubud)