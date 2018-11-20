"""research_network URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from database import views as database_views
from database.views import SignUp

app_name = 'database'

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('admin/', admin.site.urls),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^signup/$', database_views.signup, name='signup'),
    url(r'^login/$', database_views.user_login, name='login'),
]

