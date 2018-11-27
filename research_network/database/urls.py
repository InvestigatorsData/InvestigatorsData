from django.conf.urls import url

from . import views

# urls.py

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language='es'
)

app_name = 'database'

urlpatterns = [
    #url(r'^register/$', views.register, name='register'),
    #url(r'^user_login/$', views.user_login, name='user_login'),
]
