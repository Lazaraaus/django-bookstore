# accounts/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model 


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


