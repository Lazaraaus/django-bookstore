# accounts/admin.py

# IMPORTS
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm 

# Get User Model 
CustomUser = get_user_model()

# Create Custom Admin
class CustomUserAdmin(UserAdmin):
    # Add Custom Forms
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm 
    # Add Custom Model
    model = CustomUser
    # Specify which fields to list 
    list_display = ['email', 'username',]

# Register CustomUser, CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

