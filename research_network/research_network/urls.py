from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path,include
from database.views import paper_list,upload_paper,group_list,add_group
from django.conf.urls.static import static
from django.conf import settings

#En este modulo se asignan todas las urls de la aplicacion
urlpatterns = [
    path('admin/', admin.site.urls),
    path('database/', include('database.urls')),
    path('', include('pages.urls')),
    path('', include('django.contrib.auth.urls')),
    path('profile/<slug>/papers/upload/',upload_paper,name = "upload_paper" ),
    path('profile/<slug>/papers/', paper_list, name="paper_list"),
    path('profile/<slug>/groups/add/',add_group,name = "add_group" ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
