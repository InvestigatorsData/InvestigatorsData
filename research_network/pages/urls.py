from django.urls import path
from django.conf.urls import url
from . import views
import database.views

urlpatterns = [
    path('', views.BasePageView.as_view(), name='base'),
    path('signup/', database.views.user_signup, name='signup'),
    path('login/', database.views.user_login, name='login'),
    url(r'logout/$', database.views.user_logout, name='logout'),
    path('home/', views.HomePageView.as_view(), name='home'),
]
