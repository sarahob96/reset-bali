from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from home.views import form_review, my_reviews, update_review, delete_review
from home.models import Review
from home.forms import ReviewForm

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


class TestModels(TestCase):
    

    def test_Review_empty_form(self):
        form = ReviewForm()
        self.assertIn("programme_attended", form.fields)
        self.assertIn("your_experience", form.fields)
        self.assertIn("rating", form.fields)
    
  
    def test_Review_form_no_data(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())
    

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.form_review_url = reverse('form_review')
       

    def test_form_review_GET(self):
        client = Client()
        response = client.get(self.form_review_url)
        self.assertTemplateUsed(response, "home_page/index.html")
