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
from .models import Institutes, Subinstitutes, States, People, Groups, Papers,Campus
from .forms import *

#Metodo que redirecciona al menu principal
def index(request):
    return render(request, 'base.html')

@login_required
def special(request):
    return HttpResponse(" Bienvenido !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('base'))

#Metodo que llena el mapa con los investigadores y redirecciona a las busquedas del menu principal
def base(request):
    states = States.objects.all().order_by('name')
    Aguascalientes = States.objects.get(name = 'Aguascalientes')
    BajaCaliNort = States.objects.get(name = 'Baja California')
    BajaCaliSur = States.objects.get(name = 'Baja California Sur')
    Campeche = States.objects.get(name = 'Campeche')
    Chiapas = States.objects.get(name = 'Chiapas')
    Chihuahua = States.objects.get(name = 'Chihuahua')
    Colima = States.objects.get(name = 'Colima')
    Coahuila = States.objects.get(name = 'Coahuila')
    CiudadMX = States.objects.get(name = 'Ciudad de México')
    Durango = States.objects.get(name = 'Durango')
    Guanajuato = States.objects.get(name = 'Guanajuato')
    Guerrero = States.objects.get(name = 'Guerrero')
    Hidalgo = States.objects.get(name = 'Hidalgo')
    Jalisco = States.objects.get(name = 'Jalisco')
    EstadoMex = States.objects.get(name = 'Estado de México')
    Michoacan = States.objects.get(name = 'Michoacán')
    Morelos = States.objects.get(name = 'Morelos')
    Nayarit = States.objects.get(name = 'Nayarit')
    NuevoLeo = States.objects.get(name = 'Nuevo León')
    Oaxaca = States.objects.get(name = 'Oaxaca')
    Puebla = States.objects.get(name = 'Puebla')
    Queretaro = States.objects.get(name = 'Querétaro')
    QuintanaRoo = States.objects.get(name = 'Quintana Roo')
    SanLuisPotosi = States.objects.get(name = 'San Luis Potosí')
    Sinaloa = States.objects.get(name = 'Sinaloa')
    Sonora = States.objects.get(name = 'Sonora')
    Tabasco = States.objects.get(name = 'Tabasco')
    Tamaulipas = States.objects.get(name = 'Tamaulipas')
    Tlaxcala = States.objects.get(name = 'Tlaxcala')
    Veracruz = States.objects.get(name = 'Veracruz')
    Yucatan = States.objects.get(name = 'Yucatán')
    Zacatecas = States.objects.get(name = 'Zacatecas')
    return render(request, 'base.html', context={'states': states, 'Aguascalientes' : Aguascalientes,
    'BajaCaliNort' : BajaCaliNort, 'BajaCaliSur' : BajaCaliSur, 'Campeche' : Campeche,
    'Chiapas' : Chiapas, 'Chihuahua' : Chihuahua, 'Coahuila' : Coahuila, 'Colima' : Colima,
    'CiudadMX' : CiudadMX, 'Durango' : Durango, 'Guanajuato' : Guanajuato,
    'Guerrero' : Guerrero, 'Hidalgo' : Hidalgo, 'Jalisco' : Jalisco,
    'EstadoMex' : EstadoMex, 'Michoacan' : Michoacan, 'Morelos' : Morelos,
    'Nayarit' : Nayarit, 'NuevoLeo' : NuevoLeo, 'Oaxaca' : Oaxaca, 'Puebla' : Puebla,
    'Queretaro' : Queretaro, 'QuintanaRoo' : QuintanaRoo, 'SanLuisPotosi' : SanLuisPotosi,
    'Sinaloa' : Sinaloa, 'Sonora' : Sonora, 'Tabasco' : Tabasco, 'Tamaulipas' : Tamaulipas,
    'Tlaxcala' : Tlaxcala, 'Veracruz' : Veracruz, 'Yucatan' : Yucatan, 'Zacatecas' : Zacatecas})

#Metodo que no permite que los usuarios registren nombres repetidos
def name_is_repeated(name_required, request):
    try:
        person = People.objects.get(name=name_required)
    except:
        return False
    if person.user == request.user:
        return False
    return True

#Metodo que no permite que los usuarios registren emails repetidos
def email_is_repeated(email_required, request):
    try:
        person = People.objects.get(email=email_required)
    except:
        return False
    if person.user == request.user:
        return False
    return True

#Metodo que no permite que los usuarios registren emails repetidos
def username_is_repeated(username_required, request):
    try:
        user = User.objects.get(username=username_required)
    except:
        return False
    if user == request.user:
        return False
    return True

#Metodo que no permite que los usuarios registren publicaciones repetidas
def topic_is_repeated(topic_required, request):
    try:
        paper = Papers.objects.get(url_name_paper=topic_required)
    except:
        return False
    return True

#Metodo que no permite que los usuarios registren grupos repetidos
def group_is_repeated(name, request):
    try:
        group = Groups.objects.get(url_name_group=name)
    except:
        return False
    return True

#Metodo que registra al usuario en la base de datos y envia el correo de confirmacion
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

#Metodo que permite la edicion del usuario
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
    person_cover = person.img
    person_personal_telephone = person.personal_telephone
    person_state = person.state
    person_academic_level = person.academic_level
    person_degree = person.degree
    person_institute = person.institute
    person_subinstitute = person.subinstitute
    #Si el usuario guarda los cambios, actualizamos la base de datos
    if request.method == 'POST':
        modify_form = UserProfileInfoForm(request.POST,request.FILES)
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
            person_edit.img = modify_form.cleaned_data['img']
            #Actualizamos el valor del estad viejo
            old_state = person_edit.state
            obj_old_state = States.objects.get(name=str(old_state))
            value_old = int(obj_old_state.value)
            value_new = value_old - 1
            obj_old_state.value = value_new
            obj_old_state.save()
            #Actualizamos el valor del estado nuevo
            person_edit.state = modify_form.cleaned_data.get('state')
            new_state = person_edit.state
            obj_new_state = States.objects.get(name=str(new_state))
            value_old_new = int(obj_new_state.value)
            value_new_new = value_old_new + 1
            obj_new_state.value = value_new_new
            obj_new_state.save()
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
                    'person_name': person_name, 'person_email': person_email,'person_cover':person_cover,'person_personal_telephone': person_personal_telephone,
                    'person_state': person_state, 'person_academic_level': person_academic_level, 'person_degree': person_degree,
                    'person_institute': person_institute, 'person_subinstitute': person_subinstitute, })

#Metodo que da el estado de activo al usuario una vez que aceptan el correo
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user_ac = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user_ac = None
    if user_ac is not None and default_token_generator.check_token(user_ac, token):
        user_ac.is_active = True
        person = People.objects.get(user=user_ac)
        person_state = person.state
        state = States.objects.get(name=str(person_state))
        value_old = int(state.value)
        value_new = value_old + 1
        state.value = value_new
        state.save()
        user_ac.save()
        login(request, user_ac)
        return redirect(reverse('profile',args=(user_ac.username,)))
    else:
        return HttpResponse('El link de activación es inválido')

#Metodo que permite al usuario acceder con su contraseña y password
def user_login(request):
    if request.method == 'POST':
        email_request = request.POST.get('email')
        password = request.POST.get('password')
        try:
             user_person = User.objects.get(email=email_request)
        except:
            return HttpResponse("Usuario no registrado")
        try:
             person = People.objects.get(user=user_person)
        except:
            return HttpResponseRedirect('/admin/')
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

#Metodo que envia un correo para cambio de contraseña
def email_reset(request):
    if request.method == 'POST':
        to_email = request.POST.get('email')
        try:
            user = User.objects.get(email = str(to_email))
            current_site = get_current_site(request)
            mail_subject = 'Petición cambio de contraseña RENAIN'
            message = render_to_string('change_pass_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':default_token_generator.make_token(user),
            })
            email = EmailMessage(
                    mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Se te ha enviado un correo para cambiar tu contraseña')
        except:
            return HttpResponse('El correo no esta registrado')
    else:
        return render(request, 'password_reset.html', {})

#Metodo que permite el cambio de contraseña una vez activado el link de cambio
def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            password = request.POST.get('password')
            user.set_password(str(password))
            user.save()
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'changePassword.html', {})
    else:
        return HttpResponse('El link de activación es inválido')

#Metodo que permite buscar en todos los campos de la base de datos
def user_search(request):
    required = request.POST.get('entry')
    people = People.objects.filter(name__icontains=required)
    institutes = Institutes.objects.filter(name__icontains=required)
    subinstitutes = Subinstitutes.objects.filter(name__icontains=required)
    groups = Groups.objects.filter(name__icontains=required).distinct()
    papers = Papers.objects.filter(topic__icontains=required).distinct()
    return render(request, "search.html", context={'people':people, 'institutes':institutes, 'subinstitutes':subinstitutes, 'groups':groups, 'papers':papers,'required':required})

#Metodo que permite buscar institutos por estados
def state_search(request,slug):
    state_name = request.POST.get('state')
    state_obj = States.objects.get(url_name_state = slug)
    campus = Campus.objects.filter(state = state_obj)
    if request.method == 'POST':
        return redirect(reverse('search_profile',args=(slug,)))
    return render(request, "search_state.html", context={'state': state_obj, 'campus':campus,})

#Metodo que permite mostrar todas las publicaciones de un usuario
def paper_list(request,slug):
    person = People.objects.get(url_name=slug)
    name = person.url_name
    papers = person.papers
    return render(request,'paper_list.html',{
    'papers':papers,'name':name,
    })

#Metodo que permite subir publicaciones en el perfil
def upload_paper(request,slug):
    person = People.objects.get(url_name=slug)
    persons = People.objects.filter().exclude(url_name=slug)
    if request.method == 'POST':
        form = UploadPapersForm(request.POST,request.FILES)
        if form.is_valid():
            url = request.POST.get('topic')
            url = url.replace(" ","_")
            if topic_is_repeated(url, request):
                return HttpResponse("Ya existe un articulo con ese nombre, elige otro")
            paper = form.save()
            paper.url_name_paper = url
            paper.save()
            person.papers.add(paper)
            autors = request.POST.getlist('autors')
            if len(autors) > 0:
                for autor in autors:
                    coautor = People.objects.get(id_people=autor)
                    coautor.papers.add(paper)
            return redirect(reverse('paper_list',args=(slug,)))
    else:
        form = UploadPapersForm()
    return render(request,'upload_paper.html', {
        'form': form, 'autors':persons,
    })

#Metodo que permite mostrar todos los grupos de un usuario
def group_list(request,slug):
    person  = People.objects.get(url_name = slug)
    name = person.url_name
    groups = person.groups
    return render(request,'groups.html',{
        'groups':groups,'name':name,
    })

#Metodo que permite crear un grupo
def add_group(request,slug):
    person = People.objects.get(url_name=slug)
    persons = People.objects.filter().exclude(url_name=slug)
    if(request.method == 'POST'):
        form = AddGroupsForm(request.POST)
        if form.is_valid():
            url = request.POST.get('name')
            url = url.replace(" ","_")
            if group_is_repeated(url,request):
                return HttpResponse("Ya se encuentra un grupo con el mismo nombre")
            group = form.save()
            group.url_name_group = url
            group.save()
            person.groups.add(group)
            integrantes = request.POST.getlist('integrantes')
            if len(integrantes) > 0:
                for integrante in integrantes:
                    investigador = People.objects.get(id_people=integrante)
                    investigador.groups.add(group)
            return redirect(reverse('group_list',args=(slug,                )))
    else:
        form = AddGroupsForm()
    return render(request,'add_group.html',{
        'form':form,'integrantes':persons,
    })
