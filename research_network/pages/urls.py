from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup.html', views.RegisterPageView.as_view(), name='register'),
    path('login.html', views.LoginPageView.as_view(), name='login'),
    path('profile.html', views.ProfilePageView.as_view(), name='profile'),
]
