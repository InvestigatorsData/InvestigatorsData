from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from database.forms import UserForm, UserProfileInfoForm, NewProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home')

@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('profile'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(
        request, 'signup.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'registered': registered
        })


def user_profile(request):
    if request.method == 'POST':
        new_user_form = NewProfile(data=request.POST)
        if new_user_form.is_valid():
            new_user = new_user_form.save()
            new_user.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print('Ocurrio un error inesperado')
    else:
        return render(request, 'profile.html', {})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                email, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
