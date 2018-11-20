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
admin.site.register(New_User)
admin.site.register(Modify_User)
admin.site.register(Events)
admin.site.register(Requests)
admin.site.register(Log)
admin.site.register(Remove_Document)
admin.site.register(Upload_Document)
admin.site.register(Join_Group)
admin.site.register(Register_Place)
admin.site.register(Modify_Place)
admin.site.register(UserProfileInfo)
