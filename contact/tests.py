from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from contact.views import form_contact
from contact.forms import contact_form


# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_form_contact_url_is_resolved(self):
        url = reverse('form_contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, form_contact)


class TestModels(TestCase):
    

    def test__form(self):
        form = contact_form()
        self.assertIn("name", form.fields)
        self.assertIn("your_message", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("phone", form.fields)
    
  
    def test_contact_form_no_data(self):
        form = contact_form(data={})
        self.assertFalse(form.is_valid())
    

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.contact_form_url = reverse('form_contact')
       

    def test_form_contact_GET(self):
        client = Client()
        response = client.get(self.contact_form_url)
        self.assertTemplateUsed(response, "contact/contact.html")
