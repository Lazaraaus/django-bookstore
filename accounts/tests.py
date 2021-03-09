# accounts/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model 
from django.urls import reverse, resolve
# No Longer Needed, using all-auth
# from .forms import CustomUserCreationForm 
# from .views import SignupPageView 


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

# Test Signup Functionality 
class SignupTests(TestCase):
    # User Attribs 
    username = 'newuser'
    email = 'newuser@email.com'
    # Helper Function 
    def setUp(self):
        url = reverse('account_signup') 
        self.response = self.client.get(url)
    # Test Template
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on this page.')
    # Test Form
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

        # Test Password Change Functionality 
class PasswordChangeTests(TestCase):
    # User Attribs 
    username = 'newuser'
    email = 'newuser@email.com'
    password = 'pass123'
    # Helper Function 
    def setUp(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email, self.password
        )
        url = reverse('account_change_password') 
        self.response = self.client.get(url)

    # Test Template
    def test_password_change_template(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertTemplateUsed(self.response, 'account/password_change.html')
        self.assertContains(self.response, 'Change Password')
        self.assertNotContains(self.response, 'Hi there! I should not be on this page.')

class PasswordResetTests(TestCase):
    # User Attribs 
    username = 'newuser'
    email = 'newuser@email.com'
    password = 'pass123'
    # Helper Function 
    def setUp(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email, self.password
        )
        url = reverse('account_reset_password') 
        self.response = self.client.get(url)

    # Test Template
    def test_password_reset_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/password_reset.html')
        self.assertContains(self.response, 'Something Catchy and Eye Grabbing')
        self.assertNotContains(self.response, 'Hi there! I should not be on this page.')

    # No Longer Needed, using all-auth forms/views
    # def test_signup_form(self):
    #     # Get form from HTTP Response
    #     form = self.response.context.get('form')
    #     # Check if Form ISA CustomUserCreationForm
    #     self.assertIsInstance(form, CustomUserCreationForm)
    #     # Check if CSRF is properly implemented
    #     self.assertContains(self.response, 'csrfmiddlewaretoken')

    # def test_signup_view(self):
    #     # Get resolved view from url pattern
    #     view = resolve('/accounts/signup/')
    #     # Check if match 
    #     self.assertEqual(
    #         view.func.__name__,
    #         SignupPageView.as_view().__name__
    #  