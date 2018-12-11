from django.urls import path,re_path
from django.conf.urls import url
from . import views
import database.views

urlpatterns = [
    path('', views.BasePageView.as_view(), name='base'),
    path('signup/', database.views.user_signup, name='signup'),
    path('activate/<uidb64>/<token>/',
    database.views.activate, name='activate'),
    path('login/', database.views.user_login, name='login'),
    path('loginadmin/', database.views.user_login, name='loginadmin'),
    url(r'logout/$', database.views.user_logout, name='logout'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutOfPageView.as_view(), name='about'),
    path('search/', database.views.user_search, name='search'),
    path('profile/<slug>/', views.UserProfielView.as_view(), name='profile'),
    path('profile/<slug>/edit_profile/', views.ProfileModifyPageView.as_view(), name='edit_profile'),
    path('institute/<slug>/', views.InstituteProfielView.as_view(), name='institute_profile'),
    path('reset/',views.ChangePasswordView.as_view(),name='change_password'),
    #path('profile/<slug>/groups/', views.UserProfielView.as_view(), name='profile_groups'),
]
