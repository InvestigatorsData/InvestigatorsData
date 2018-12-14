
import os

from django.core.wsgi import get_wsgi_application

#Sirve para el deployment

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'research_network.settings')

application = get_wsgi_application()
