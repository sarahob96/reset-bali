from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from programmes.views import rewindbooking, renewbooking, restartbooking, my_bookings, update_booking, update_renew_booking, update_restart_booking, delete_booking, delete_renew_booking, delete_restart_booking, ubud, seminyak
from programmes.models import Restart, Rewind, Renew
from programmes.forms import Rewind_form, Restart_form, Renew_form


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


class TestModels(TestCase):
    

    def test_rewind_empty_form(self):
        form = Rewind_form()
        self.assertIn("phone", form.fields)
        self.assertIn("email", form.fields)
    
    def test_renew_empty_form(self):
        form = Renew_form()
        self.assertIn("phone", form.fields)
        self.assertIn("email", form.fields)

    def test_restart_empty_form(self):
        form = Restart_form()
        self.assertIn("phone", form.fields)
        self.assertIn("email", form.fields)   
    
    def test_rewind_form_no_data(self):
        form = Rewind_form(data={})

        self.assertFalse(form.is_valid())
    
    def test_renew_form_no_data(self):
        form = Renew_form(data={})

        self.assertFalse(form.is_valid())
       
    def test_restart_form_no_data(self):
        form = Restart_form(data={})

        self.assertFalse(form.is_valid())


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.rewindbooking_url = reverse('rewindbooking')
        self.renewbooking_url = reverse('renewbooking')
        self.restartbooking_url = reverse('restartbooking')
        self.update_booking_url = reverse('update_booking', args=['1'])
        self.update_renew_booking_url = reverse('update_renew_booking', args=['1'])

    def test_rewindbooking_GET(self):
        client = Client()
        response = client.get(self.rewindbooking_url)
        self.assertTemplateUsed(response, 'programmes/rewind.html')

    def test_renewbooking_GET(self):
        client = Client()
        response = client.get(self.renewbooking_url)
        self.assertTemplateUsed(response, 'programmes/renew.html')

    def test_restartbooking_GET(self):
        client = Client()
        response = client.get(self.restartbooking_url)
        self.assertTemplateUsed(response, 'programmes/restart.html')

