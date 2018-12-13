from django import forms
from django.contrib.auth.models import User
from .models import People,Papers,Groups

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = People
        fields = ('name','email','academic_level', 'degree','state',
                  'personal_telephone', 'institute', 'subinstitute')

class PapersForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('papers',)

class UploadPapersForm(forms.ModelForm):
    class Meta:
        model = Papers
        fields = ('topic','publication_date','file',)

class GroupsForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('groups',)

class AddGroupsForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('name',)
