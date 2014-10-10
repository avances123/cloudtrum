from cloudtrum.settings.base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cloudtrum',                      
        'HOST': ''
    }
}