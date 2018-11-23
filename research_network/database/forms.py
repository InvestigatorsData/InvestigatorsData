from django import forms
from database.models import UserProfileInfo
from django.contrib.auth.models import User
from .models import New_User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = New_User
        fields = ('username','email', 'academic_level', 'degree',
                  'personal_telephone')

