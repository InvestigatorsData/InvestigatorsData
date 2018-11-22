from django import forms
#from database.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email','password',)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 
                  'last_name', 
                  'email',
                  'password1',
                  'password2',
                  'personal_telephone',
                  )




