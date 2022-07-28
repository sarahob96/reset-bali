from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from accounts.views import new_account, login_form, logout_page, password_changed 
from accounts.forms import UserCreateForm

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEquals(resolve(url).func, new_account)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEquals(resolve(url).func, login_form)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, logout_page)

    def test_password_changed_url_is_resolved(self):
        url = reverse('password-changed')
        print(resolve(url))
        self.assertEquals(resolve(url).func, password_changed)

   
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.new_account_url = reverse('register')
        self.login_form_url = reverse('login')
       

    def test_register_form_GET(self):
        client = Client()
        response = client.get(self.new_account_url)
        self.assertTemplateUsed(response, 'accounts/registration.html')
    
    def test_login_form_GET(self):
        client = Client()
        response = client.get(self.login_form_url)
        self.assertTemplateUsed(response, 'accounts/login.html',)
