# pages/tests.py

# IMPORTS 
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! This should not exist on the page.'
        )
    def test_homepage_contains_correct_html(self):
        self.assertContains(
            self.response, 'Bookstore Home'
        )

    def test_homepage_url_resolves_homepageview(self):
        # Get view used to resolve homepage url 
        view = resolve('/')
        # Check if resolved view and HomePageView are equal 
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! This should not exist on the page.'
        )
    def test_homepage_contains_correct_html(self):
        self.assertContains(
            self.response, 'About Page'
        )

    def test_homepage_url_resolves_homepageview(self):
        # Get view used to resolve homepage url 
        view = resolve('/about/')
        # Check if resolved view and HomePageView are equal 
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )

# Create your tests here.
