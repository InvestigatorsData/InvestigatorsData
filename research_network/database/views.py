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
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('fist_name')
            user.profile.email = form.cleaned_data.get('email')
            user.profile.password1 = form.cleaned_data.get('password1')
            user.profile.password2 = form.cleaned_data.get('password2')
            #user.profile.academic_level = 
            #user.degree = 
            user.set_password(user.profile.password1)
            personal_telephone = form.cleaned_data.get('phone')
            user.save()    
            username = form.cleaned_data.get('first_name')
            password = form.cleaned_data.get('password1')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print('>>>>>>> REGISTRO EXITOSO <<<<<<<<<<<')
            return redirect('home.html')
        else:
            print(form.errors + ' ERROR')
    else:
        print('>>>>>>>>>>> LA FORMA NO ES VALIDA <<<<<<<<<<')
        form = SignUpForm()
    print(' >>>>>>>>>> ERROR <<<<<<<<<<<<< ')
    return render(request, 'signup.html', {'form': form})

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