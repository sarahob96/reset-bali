from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from accounts.views import new_account, login_form, logout_page, password_changed

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

   
