from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'home.html'
class RegisterPageView(TemplateView):
    template_name = 'register.html'
class LoginPageView(TemplateView):
    template_name = 'Login.html'