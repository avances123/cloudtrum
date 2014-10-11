from cloudtrum.settings.base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG



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
STATIC_URL = "https://cloudtrum.fabio.rueda.guru.s3.amazonaws.com/" 
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'



# Set up Amazon S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_FILE_OVERWRITE = False
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", '')
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", '')
AWS_STORAGE_BUCKET_NAME = "cloudtrum.fabio.rueda.guru"
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True




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