from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from database.models import *


class BasePageView(TemplateView):
    template_name = 'base.html'
class RegisterPageView(TemplateView):
    template_name = 'signup.html'
class LoginPageView(TemplateView):
    template_name = 'login.html'
class LoginPageView(TemplateView):
    template_name = 'loginadmin.html'
class HomePageView(TemplateView):
    template_name = 'home.html'
class ProfilePageView(TemplateView):
    template_name = 'profile.html'
class ProfileModifyPageView(TemplateView):
    template_name = 'profileM.html'
class AboutOfPageView(TemplateView):
    template_name = 'aboutOf.html'
