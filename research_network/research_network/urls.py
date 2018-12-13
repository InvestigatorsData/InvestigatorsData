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
from django.urls import path,include
from database.views import paper_list,upload_paper,group_list,add_group
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('database/', include('database.urls')),
    path('', include('pages.urls')),
    path('', include('django.contrib.auth.urls')),
    path('profile/<slug>/papers/upload/',upload_paper,name = "upload_paper" ),
    path('profile/<slug>/papers/', paper_list, name="paper_list"),
    path('profile/<slug>/groups/add/',add_group,name = "add_group" ),
    path('profile/<slug>/groups/', group_list, name="group_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
