from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include
from django.views.generic.base import TemplateView
from database import views as database_views

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^signup/$', database_views.SignUp, name='signup'),
    url(r'^login/$', database_views.login, name='login'),
]