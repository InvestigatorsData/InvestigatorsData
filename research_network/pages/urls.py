from django.urls import path
from django.conf.urls import url
from . import views
import database.views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup/', database.views.signup, name='signup'),
    path('login/', database.views.user_login, name='login'),
    #path('profile/' database.views.profile, name='profile'),
]
