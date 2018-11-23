from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup2/', views.RegisterPageView.as_view(), name='signup2'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login2/', views.LoginPageView.as_view(), name='login2'),
    path('register/',views.RegisterupView.as_view(),name='register')


]
