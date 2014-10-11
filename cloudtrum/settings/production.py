from cloudtrum.settings.base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG



INSTALLED_APPS += (
    'storages',
    'raven.contrib.django.raven_compat',
)



# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/home/ubuntu/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/home/ubuntu/src/cloudtrum/static/dist/",
)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#STATICFILES_STORAGE = 'storages.backends.s3.S3Storage'


# Set up Amazon S3
#DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", '')
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", '')
AWS_STORAGE_BUCKET_NAME = "cloudtrum.fabio.rueda.guru"


RAVEN_CONFIG = {
    'dsn' : os.environ.get("RAVEN_DSN", ''),
}





CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        #'LOCATION': '127.0.0.1:6379:0',
        'LOCATION': 'cloudtrum.scwvxh.0001.euw1.cache.amazonaws.com:6379:0',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            #'PASSWORD': 'secretpassword',  # Optional
        }
    }
}