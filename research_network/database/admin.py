from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(States)
admin.site.register(Campus)
admin.site.register(College)
admin.site.register(Institutes)
admin.site.register(Subinstitutes)
admin.site.register(Roles)
admin.site.register(User_profiles)
admin.site.register(Groups)
admin.site.register(People)
admin.site.register(Public)
admin.site.register(Papers)
