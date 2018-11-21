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
        Subinstitutes.objects.create(institute=institute_i, id_reference_sub=subinstitute_i,
        name="Cubículo 2")

    def test_insert_in_db(self):
        """
        Test that checks that the datbase is PostgreSQL
        """
        state = States.objects.get(name="Ciudad de México")
        college = College.objects.get(name="UNAM")
        campus = Campus.objects.get(name="Ciudad Universitaria")
        institute = Institutes.objects.get(name="Facultad de Ciencias")
        subinstitute1 = Subinstitutes.objects.get(name="Departamento de Matemáticas")
        subinstitute2 = Subinstitutes.objects.get(name="Cubículo 2")
        print(state + " " + college + " " + campus + " " + institute + " " + subinstitute1 + " "
        + subinstitute2)
