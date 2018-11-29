from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from database.forms import UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
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
            user.is_active = False
            current_site = get_current_site(request)
            mail_subject = 'Activa tu cuenta de RENAIN'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':default_token_generator.make_token(user),
            })
            to_email = profile_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Se te ha enviado un correo de confirmación a tu correo para completar el registro')
        else:
            return HttpResponse(" Datos invalidos: " + str(profile_form.errors))
    else:
        profile_form = UserProfileInfoForm()
    return render(
        request, 'signup.html', context={'institutes':institutes, 'subinstitutes': subinstitues, 'states': states,})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('profile')
    else:
        return HttpResponse('El link de activación es inválido')

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
        email_request = request.POST.get('email')
        password = request.POST.get('password')
        try:
             person = People.objects.get(email=email_request)
        except:
            return HttpResponse(" Usuario no registrado")
        name = person.name
        name_normalize = name.replace(' ','')
        user = authenticate(username=name_normalize, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse(" Tu cuenta aun no esta activa ")
        else:
            print(" Datos incorrectos")
            print(" Email: {} Password: {}".format(
                email_request, password))
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
