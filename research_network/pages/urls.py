from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('signup/', views.RegisterPageView.as_view(), name='signup'),
    path('login/', views.LoginPageView.as_view(), name='login'),

]
