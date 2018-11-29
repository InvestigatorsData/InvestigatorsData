from django import forms
from django.contrib.auth.models import User
from .models import People

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = People
        fields = ('name','email','academic_level', 'degree','state',
                  'personal_telephone', 'institute', 'subinstitute')

