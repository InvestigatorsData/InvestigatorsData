from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from database.models import *
from django.views.generic import ListView,DetailView

#Clases que declaran htmls como templates de Django
class BasePageView(TemplateView):
    template_name = 'base.html'
class RegisterPageView(TemplateView):
    template_name = 'signup.html'
class LoginPageView(TemplateView):
    template_name = 'login.html'
class LoginPageView(TemplateView):
    template_name = 'loginadmin.html'
class HomePageView(TemplateView):
    template_name = 'home.html'
class ProfilePageView(TemplateView):
    template_name = 'profile.html'
class ProfileModifyPageView(TemplateView):
    model = People
    template_name = 'profileM.html'
    slug_field = 'url_name'
class AboutOfPageView(TemplateView):
    template_name = 'aboutOf.html'
class ChangePasswordDone(TemplateView):
    template_name = 'password_reset_done.html'
class ChangePasswordView(TemplateView):
    template_name = 'changePassword.html'
class GroupsView(TemplateView):
    template_name = 'groups.html'
class UserProfielView(DetailView):
    model = People
    template_name = 'profile.html'
    slug_field = 'url_name'
class InstituteProfielView(DetailView):
    model = Institutes
    template_name = 'institute_profile.html'
    slug_field = 'url_name_institute'
class SubinstituteProfielView(DetailView):
    model = Subinstitutes
    template_name = 'subinstitute_profile.html'
    slug_field = 'url_name_subinstitute'
class GroupProfielView(DetailView):
    model = Groups
    template_name = 'group_profile.html'
    slug_field = 'url_name_group'
class CampusProfileView(DetailView):
    model = Campus
    template_name = 'campus_profile.html'
    slug_field = 'url_name_campus'

#Metodo que muestra la vista de publicaciones con la informacion necesaria
def paper_view(request, slug):
    papers = Papers.objects.get(url_name_paper=slug)
    autors = papers.people_set.all()
    return render(request, "paper_profile.html", context={'autors':autors, 'papers':papers,})

#Metodo que muestra la vista de colegios con la informacion necesaria
def college_view(request, slug):
    required_college = College.objects.get(url_name_college=slug)
    institutes = Institutes.objects.filter(college=required_college)
    college_campus =Campus.objects.filter(college=required_college)
    return render(request, "college_profile.html", context={'institutes':institutes, 'college':required_college, 'college_campus':college_campus,})

def institute_view(request, slug):
    required_institute = Institutes.objects.get(url_name_institute=slug)
    subinstitutes = Subinstitutes.objects.filter(institute=required_institute)
    return render(request, "institute_profile.html", context={'institutes': required_institute, 'subinstitutes': subinstitutes,})    

def campus_view(request, slug):
    required_campus = Campus.objects.get(url_name_campus=slug)
    institutes = Institutes.objects.filter(campus=required_campus)
    return render(request, "campus_profile.html", context={'institutes':institutes, 'campus': required_campus,})

def subinstitute_view(request, slug):
    required_subinstitute = Subinstitutes.objects.get(url_name_subinstitute=slug)
    people = People.objects.filter(subinstitute=required_subinstitute)
    return render(request, "subinstitute_profile.html", context={'subinstitutes': required_subinstitute, 'people': people,})

#Metodo que muestra la vista de grupos con la informacion necesaria
def group_view(request,slug):
    groups = Groups.objects.get(url_name_group=slug)
    integrantes = groups.people_set.all()
    return render(request,"group_profile.html",context={'groups':groups,'integrantes':integrantes})




