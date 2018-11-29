from django.urls import path
from django.conf.urls import url
from . import views
import database.views

urlpatterns = [

    path('', views.BasePageView.as_view(), name='base'),
    path('signup/', database.views.user_signup, name='signup'),
    path('activate/<uidb64>/<token>/',
    database.views.activate, name='activate'),
    path('login/', database.views.user_login, name='login'),
<<<<<<< HEAD
    path('loginadmin/', database.views.user_login, name='loginadmin'),
    url(r'logout/$', database.views.user_logout, name='logout'),
=======
    path('logout/', database.views.user_logout, name='logout'),
>>>>>>> 4d50ecf0a22c222e237f4cf2936d49d8fd7f7896
    path('home/', views.HomePageView.as_view(), name='home'),
    path('profile/', views.ProfilePageView.as_view(), name='profile'),
    path('profileM/', views.ProfileModifyPageView.as_view(), name='profileM'),
    path('about/', views.AboutOfPageView.as_view(), name='about'),
    path('search/', database.views.user_search, name='search'),
]
