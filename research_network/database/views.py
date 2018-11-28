from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from database.forms import UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Institutes, Subinstitutes, States, Roles, People, Groups, Papers


def index(request):
    return render(request, 'base.html')

@login_required
def special(request):
    return HttpResponse(" Bienvenido !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))


def user_signup(request):
    registered = False
    institutes = Institutes.objects.all().order_by('name')
    subinstitues = Subinstitutes.objects.all().order_by('name')
    states = States.objects.all().order_by('name')
    rol = Roles.objects.get(role='user')
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            name = profile_form.cleaned_data.get('name')
            username_normalize = name.replace(' ','')
            email = profile_form.cleaned_data.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username_normalize, email, password)
            user.save()
            profile.user = user
            profile.role = rol
            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse(" Datos invalidos: " + str(profile_form.errors))
    else:
        profile_form = UserProfileInfoForm()
    return render(
        request, 'signup.html', context={'institutes':institutes, 'subinstitutes': subinstitues, 'states': states,})


def user_profile(request):
    if request.method == 'POST':
        new_user_form = NewProfile(data=request.POST)
        if new_user_form.is_valid():
            new_user = new_user_form.save()
            new_user.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Ocurrio un error inesperado')
    else:
        return render(request, 'profile.html', {})


def user_login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        name_normalize = name.replace(' ','')
        password = request.POST.get('password')
        user = authenticate(username=name_normalize, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse(" Tu cuenta aun no esta activa ")
        else:
            print(" Datos incorrectos")
            print(" Nombre: {} Password: {}".format(
                username, password))
            return HttpResponse(" Ingresaste el password o nombre incorrectos ")
    else:
        return render(request, 'login.html', {})


def user_search(request):
    required = request.POST.get('entry')
    people = People.objects.filter(name__contains=required)
    institutes = Institutes.objects.filter(name__contains=required)
    subinstitutes = Subinstitutes.objects.filter(name__contains=required)
    groups = Groups.objects.filter(name__contains=required)
    papers = Papers.objects.filter(topic__contains=required)
    return render(request, "search.html", context={'people':people, 'institutes':institutes, 'subinstitutes':subinstitutes, 'groups':groups, 'papers':papers,'required':required})






