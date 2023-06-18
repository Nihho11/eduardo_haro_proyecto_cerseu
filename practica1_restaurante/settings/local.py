from .base import *

SECRET_KEY = 'django-insecure-sa&@df8+58zyhcd+2%115bxxbldp5@*446liostjp#5y=8!!mo'

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bd_restaurant_app',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'

    }
}

STATIC_URL = '/static/'
