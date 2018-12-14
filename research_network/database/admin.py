from django.contrib import admin

from .models import *

#Modulo donde se registran los modelos en el sitio de administracion de Django
admin.site.register(States)
admin.site.register(Campus)
admin.site.register(College)
admin.site.register(Institutes)
admin.site.register(Subinstitutes)
admin.site.register(Groups)
admin.site.register(People)
admin.site.register(Public)
admin.site.register(Papers)

admin.site.site_title = 'RENAIN'
admin.site.site_header = 'Sitio de administración'
