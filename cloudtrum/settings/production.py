from cloudtrum.settings.base import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:0',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            #'PASSWORD': 'secretpassword',  # Optional
        }
    }
}