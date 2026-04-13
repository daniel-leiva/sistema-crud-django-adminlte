import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

"""POSTGRESQL = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'sistema_django',
        'USER': 'tu-usuario',
        'PASSWORD': 'tu-password-de-ejemplo',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}"""

"""POSTGRESQL = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistema_django',
        'USER': 'tu-usuario',
        'PASSWORD': 'tu-password-de-ejemplo',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '3306',
    }
}"""
"""MYSQL = {
        'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistema_django',
        'USER': 'tu-usuario',
        'PASSWORD': 'tu-password-de-ejemplo',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '3306',
        } }"""