from django import forms
#from database.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email','password',)

class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    password = forms.CharField(max_length=128)
    academic_level = forms.CharField(max_length=200)
    degree = forms.CharField(max_length=200)
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ('first_name', 
                  'last_name', 
                  'email',
                  'password1',
                  'password2',
                  )