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
from .models import Institutes, Subinstitutes, States, People, Groups, Papers
from .forms import *

def index(request):
    return render(request, 'base.html')

@login_required
def special(request):
    return HttpResponse(" Bienvenido !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))

def name_is_repeated(name_required, request):
    try:
        person = People.objects.get(name=name_required)
    except:
        return False 
    if person.user == request.user:
        return False    
    return True   

def email_is_repeated(email_required, request):
    try:
        person = People.objects.get(email=email_required)
    except:
        return False
    if person.user == request.user:
        return False    
    return True 

def username_is_repeated(username_required, request):
    try:
        user = User.objects.get(username=username_required)
    except:
        return False
    if user == request.user:
        return False    
    return True    

def user_signup(request):
    registered = False
    institutes = Institutes.objects.all().order_by('name')
    subinstitues = Subinstitutes.objects.all().order_by('name')
    states = States.objects.all().order_by('name')
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            name = profile_form.cleaned_data.get('name')
            username_normalize = name.replace(' ','')
            email = profile_form.cleaned_data.get('email')
            if name_is_repeated(name, request):
                return HttpResponse("Ya existe un usuario registrado con ese nombre")
            if email_is_repeated(email, request):
                return HttpResponse("Ya existe un usuario registrado con ese email")    
            if username_is_repeated(username_normalize, request):
                return HttpResponse("Ya existe un usuario registrado con un nombre similar")    
            password = request.POST.get('password')
            user = User.objects.create_user(username_normalize, email, password)
            user.save()
            profile.user = user
            profile.url_name = username_normalize
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

def user_edit(request, slug):
    institutes = Institutes.objects.all().order_by('name')
    subinstitues = Subinstitutes.objects.all().order_by('name')
    states = States.objects.all().order_by('name')
    try:
        person = People.objects.get(user=request.user)
    except:
        return HttpResponse(" Usuario no registrado")
    person_name = person.name
    person_email = person.email
    person_personal_telephone = person.personal_telephone
    person_state = person.state
    person_academic_level = person.academic_level
    person_degree = person.degree
    person_institute = person.institute
    person_subinstitute = person.subinstitute

    if request.method == 'POST':
        modify_form = UserProfileInfoForm(data=request.POST)
        if modify_form.is_valid():
            person_edit = People.objects.get(user=request.user)
            if name_is_repeated(modify_form.cleaned_data.get('name'), request):
                return HttpResponse("Ya existe un usuario registrado con ese nombre")
            if email_is_repeated(modify_form.cleaned_data.get('email'), request):
                return HttpResponse("Ya existe un usuario registrado con ese email")    
            person_edit.name= modify_form.cleaned_data.get('name')
            new_username_normalize = person_edit.name.replace(' ','')
            if username_is_repeated(new_username_normalize, request):
                return HttpResponse("Ya existe un usuario registrado con un nombre similar")
            password = request.POST.get('password')
            person_edit.url_name = new_username_normalize
            person_edit.email = modify_form.cleaned_data.get('email')
            person_edit.academic_level =  modify_form.cleaned_data.get('academic_level')
            person_edit.degree = modify_form.cleaned_data.get('degree')
            person_edit.personal_telephone = modify_form.cleaned_data.get('personal_telephone')
            person_edit.state = modify_form.cleaned_data.get('state')
            person_edit.subinstitute = modify_form.cleaned_data.get('subinstitute')
            person_edit.institute = modify_form.cleaned_data.get('institute')
            person_edit.user.username = new_username_normalize
            person_edit.user.email = person_edit.email = modify_form.cleaned_data.get('email')
            if len(password) > 0 :
                person_edit.user.set_password(password)    
            person_edit.user.save()
            person_edit.save()
            slug = new_username_normalize
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse("Ocurrio un error con el formulario")    
    else:
        modify_form = UserProfileInfoForm()
    return render (request, 'profileM.html', context={'institutes':institutes, 'subinstitutes': subinstitues, 'states': states, 
                    'person_name': person_name, 'person_email': person_email, 'person_personal_telephone': person_personal_telephone, 
                    'person_state': person_state, 'person_academic_level': person_academic_level, 'person_degree': person_degree,
                    'person_institute': person_institute, 'person_subinstitute': person_subinstitute, })    

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
        return redirect(reverse('profile',args=(user.username,)))
    else:
        return HttpResponse('El link de activación es inválido')

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
        slug = name_normalize
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('profile',args=(slug,)))
            else:
                return HttpResponse(" Tu cuenta aun no esta activa ")
        else:
            print(" Datos incorrectos")
            print(" Email: {} Password: {}".format(
                email_request, password))
            return HttpResponse(" Ingresaste el password o nombre incorrectos")
    else:
        return render(request, 'login.html', {})


def user_search(request):
    required = request.POST.get('entry')
    people = People.objects.filter(name__icontains=required)
    institutes = Institutes.objects.filter(name__icontains=required)
    subinstitutes = Subinstitutes.objects.filter(name__icontains=required)
    groups = Groups.objects.filter(name__icontains=required)
    papers = Papers.objects.filter(topic__icontains=required)
    return render(request, "search.html", context={'people':people, 'institutes':institutes, 'subinstitutes':subinstitutes, 'groups':groups, 'papers':papers,'required':required})



def paper_list(request):
    papers = Papers.objects.all()
    return render(request,'paper_list.html',{
    'papers':papers
    })

def upload_paper(request):
    if request.method == 'POST':
        form = PapersForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('paper_list')
    else:
        form = PapersForm()
    return render(request,'upload_paper.html',{
        'form': form
    })

