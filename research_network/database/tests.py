import os

from django.test import TestCase
from .database import info
from .models import States
from .models import College
from .models import Campus
from .models import Institutes
from .models import Subinstitutes
from .models import Roles
from .models import User_profiles
from .models import Papers
from .models import Groups
from .models import People

class DbEngine(TestCase):
    """
    Test that checks that the datbase is PostgreSQL
    """
    def setUp(self):
        os.environ['ENGINE'] = 'PostgreSQL'

    def test_engine_setup(self):
        settings = info()
        self.assertEqual(settings['engine'], 'PostgreSQL')


class ManageDBTestCase(TestCase):
    def setUp(self):
        state_i = States.objects.create(key="MX-CDMX", name="Ciudad de México")
        college_i = College.objects.create(name="UNAM", telephone=56225568, address="")
        campus_i = Campus.objects.create(state=state_i, college=college_i, name="Ciudad Universitaria",
        telephone="55-56221-332", address="Av Universidad 3000, Cd. Universitaria, Coyoacán, 04510 Ciudad de México, CDMX")
        institute_i = Institutes.objects.create(campus=campus_i, name="Facultad de Ciencias",
        telephone="01-5556-224-992", address="Cto. Exterior s/n, Ciudad Universitaria, 04510 Ciudad de México, CDMX")
        subinstitute_i = Subinstitutes.objects.create(institute=institute_i, name="Departamento de Matemáticas")
        subinstitute_ii = Subinstitutes.objects.create(institute=institute_i, id_reference_sub=subinstitute_i,
        name="Cubículo 2")
        user_role = Roles.objects.create(role= "Administrador")
        profile_i = User_profiles.objects.create(profile = "Investigador")
        paper_i = Papers.objects.create(topic = "Ciencias de la Computación",
        publication_date = "21-06-2017")
        group_i = Groups.objects.create(name = "Grupo Animalitos")
        people_i = People.objects.create(mail = "example@gmail.com", password = "asadadda",
        user_profile =profile_i, institute=institute_i, subinstitute=subinstitute_i,
        role=user_role, name="Barbara Hamilton")
        people_i.groups.add(group_i)
        people_i.papers.add(paper_i)
        people2 =  People.objects.create(mail = "example@gmail.com", password = "asadadda",
        user_profile =profile_i, institute=institute_i, subinstitute=subinstitute_ii,
        role=user_role, name="Alexander Hansen")

    def test_insert_in_db(self):
        """
        Test that checks the database inserts correctly the data
        """
        state = States.objects.get(name="Ciudad de México")
        college = College.objects.get(name="UNAM")
        campus = Campus.objects.get(name="Ciudad Universitaria")
        institute = Institutes.objects.get(name="Facultad de Ciencias")
        subinstitute1 = Subinstitutes.objects.get(name="Departamento de Matemáticas")
        subinstitute2 = Subinstitutes.objects.get(name="Cubículo 2")
        role = Roles.objects.get(role = "Administrador")
        profile = User_profiles.objects.get(profile = "Investigador")
        paper = Papers.objects.get(topic="Ciencias de la Computación")
        group = Groups.objects.get(name = "Grupo Animalitos")
        person = People.objects.get(name="Barbara Hamilton")

        string_insert =("{}, {}, {}, {}, {}, {}, {}, {}, {} , {}, {}".format(state,
        college, campus, institute,subinstitute1, subinstitute2, role, profile,
        paper, group, person ))

        self.assertEqual(string_insert, "Ciudad de México, UNAM, Ciudad Universitaria, Facultad de Ciencias, Departamento de Matemáticas, Cubículo 2, Administrador, Investigador, Ciencias de la Computación , Grupo Animalitos, Barbara Hamilton")

    def test_consult_in_db(self):
        """
        Test that checks that the database makes correct consults
        """
        #SELECT institute FROM People WHERE name LIKE %Alexander%
        person_t= People.objects.get(name__contains = "Alexander")
        self.assertEqual(str(person_t.institute), "Facultad de Ciencias")
        #print(str(person_t.groups))    

        #SELECT  * FROM People
        person_list = People.objects.all()
        sperson = ''
        for person in person_list:
            sperson = sperson + str(person) + ' '
        self.assertEqual(sperson, "Barbara Hamilton Alexander Hansen ")

        #SELECT * FROM People JOIN Groups
