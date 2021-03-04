# accounts/views.py

# IMPORTS
from django.urls import reverse_lazy
from django.views import generic 
from .forms import CustomUserCreationForm

# Create SignupPageView
class SignupPageView(generic.CreateView):
    # Use CustomUserCreationForm 
    form_class = CustomUserCreationForm 
    # Success url 
    success_url = reverse_lazy('login')
    # Template 
    template_name = 'registration/signup.html'
# Create your views here.
