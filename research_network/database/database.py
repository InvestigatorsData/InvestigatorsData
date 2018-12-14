from django.conf import settings

#Metodo que permite tener una base de datos en mysql o en postgres
def info():
    db_settings = settings.DATABASES['default']
    if 'postgres' in db_settings['ENGINE']:
        engine = 'PostgreSQL'
        url = '{HOST}:{PORT}/{NAME}'.format(**db_settings)
    elif 'mysql' in db_settings['ENGINE']:
        engine = 'MySQL'
        url = '{HOST}:{PORT}/{NAME}'.format(**db_settings)
    else:
        engine = 'unknown'
        url = ''
    return {
        'engine': engine,
        'url': url,
        }
