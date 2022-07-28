from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from home.views import form_review, my_reviews, update_review, delete_review

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, form_review)

    def test_form_review_url_is_resolved(self):
        url = reverse('form_review')
        print(resolve(url))
        self.assertEquals(resolve(url).func, form_review)

    def test_my_reviews_url_is_resolved(self):
        url = reverse('myreviews')
        print(resolve(url))
        self.assertEquals(resolve(url).func, my_reviews)

    def test_update_review_url_is_resolved(self):
        url = reverse('update_review', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_review)

    def test_delete_review_url_is_resolved(self):
        url = reverse('delete_review', args=['booking_id'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_review)
