from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from database.forms import UserForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

class SignUp(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = SignUpForm
    sucess_url = reverse_lazy('home.html')

def index(request):
    return render(request, 'base.html')

@login_required
def special(request):
    return HttpResponse(" Has iniciado sesion ")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base.html'))

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.profile.name = user_form.cleaned_data.get('fist_name')
            user.profile.email = user_form.cleaned_data.get('email')
            user.profile.password = user_form.cleaned_data.get('password1')
            user.save()    
            username = user_form.cleaned_data.get('first_name')
            password = user_form.cleaned_data.get('password1')
            raw_password = user_form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home.html')
    else:
        user_form = SignUpForm()
    return render(request, 'signup.html', {'form': user_form})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home.html'))
            else:
                return HttpResponse(" Usuario inactivo.")
        else:
            print("No se puede acceder")
            print("Email: {} Password: {}".format(
                email, password))
            return HttpResponse(" Acceso invalido ")
    else:
        return render(request, 'login.html', {})