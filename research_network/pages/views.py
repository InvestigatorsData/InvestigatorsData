from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from database.models import *

class HomePageView(TemplateView):
    template_name = 'base.html'
class RegisterPageView(TemplateView):
    template_name = 'signup2.html'
class LoginPageView(TemplateView):
    template_name = 'login2.html'

class RegisterupView(CreateView):
    model = New_User
    template_name = 'register.html'
    fields = '__all__'
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('register')
    template_name = 'signup.html'