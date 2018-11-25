from django import forms
from django.contrib.auth.models import User
from .models import New_User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = New_User
        fields = ('username','email','academic_level', 'degree',
                  'personal_telephone', 'institute', 'subinstitute')

