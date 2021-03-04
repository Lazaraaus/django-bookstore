# accounts/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model 
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm 
from .views import SignupPageView 


class CustomUserTests(TestCase):
    # Test Create User Functionality 
    def test_create_user(self):
        # Override User with our Custom User Model 
        User = get_user_model()
        # Create Test User 
        user = User.objects.create_user(
            username="test",
            email="test@email.com",
            password="testpass"
        )
        # Test User 
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # Test Create Super User Functionality 
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin",
            email="superadmin@email.com",
            password="superadminpass"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser) 

# Test Signup Page Functionality 
class SignupPageTests(TestCase):
    # Helper Function 
    def setUp(self):
        url = reverse('signup') 
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on this page.')

    def test_signup_form(self):
        # Get form from HTTP Response
        form = self.response.context.get('form')
        # Check if Form ISA CustomUserCreationForm
        self.assertIsInstance(form, CustomUserCreationForm)
        # Check if CSRF is properly implemented
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        # Get resolved view from url pattern
        view = resolve('/accounts/signup/')
        # Check if match 
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__
        )
