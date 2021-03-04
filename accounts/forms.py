# accounts/forms.py

# IMPORTS 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

# Class for Custom User Creation Forms
class CustomUserCreationForm(UserCreationForm):
    # Use Django's Meta class feature 
    class Meta:
        # Set model to custom user model
        model = get_user_model()
        # Set custom user fields 
        fields = ('email', 'username',)


# Class for Custom User Change Form 
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
