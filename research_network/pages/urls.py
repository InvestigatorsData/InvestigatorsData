from django.urls import path
from . import views
urlpatterns = [
path('', views.HomePageView.as_view(), name='home'),
path('register.html', views.RegisterPageView.as_view(), name='register'),
path('Login.html', views.LoginPageView.as_view(), name='Login'),
]