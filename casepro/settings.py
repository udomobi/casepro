from __future__ import unicode_literals

import os
import urllib
import dj_database_url
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration
from decouple import config

# import our default settings
from casepro.settings_common import *  # noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [
                       s.strip() for s in v.split(',')])

SEND_EMAILS = config('SEND_EMAILS', default=True, cast=bool)

DEFAULT_FROM_EMAIL = config(
    'DEFAULT_FROM_EMAIL', default='webmaster@localhost')
SERVER_EMAIL = config('SERVER_EMAIL')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)

ADMINS = config('ADMINS',
                default='',
                cast=lambda v: [
                    tuple(s.strip().split('|'))
                    for s in v.split(',')
                ] if v else [])

HOSTNAME = config('HOSTNAME', default='inbox.push.al')
SITE_API_HOST = config('SITE_API_HOST', default='https://push.ilhasoft.mobi/')
SITE_HOST_PATTERN = config(
    'SITE_HOST_PATTERN', default='http://%s.inbox.push.al')

SITE_EXTERNAL_CONTACT_URL = config(
    'SITE_EXTERNAL_CONTACT_URL', default='https://push.ilhasoft.mobi/contact/read/%s/')
SITE_BACKEND = 'casepro.backend.rapidpro.RapidProBackend'

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(
    config(
        'DEFAULT_DATABASE'))
DATABASES['default']['ATOMIC_REQUESTS'] = True

REDIS_HOST = config('REDIS_HOST')
REDIS_DATABASE = config('REDIS_DATABASE')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://{}:6379/{}'.format(REDIS_HOST, REDIS_DATABASE),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

sentry_sdk.init(
    dsn=config('RAVEN_CONFIG', default=''),
    integrations=[DjangoIntegration()]
)

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='', cast=str)
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='', cast=str)
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='', cast=str)

AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = ''

BROKER_URL = "sqs://{}:{}@".format(urllib.parse.quote(
    AWS_ACCESS_KEY_ID, safe=''), urllib.parse.quote(AWS_SECRET_ACCESS_KEY, safe=''))

BROKER_TRANSPORT_OPTIONS = {
    'region': 'us-east-1',
    'polling_interval': 20,
    'visibility_timeout': 3600,
    'queue_name_prefix': 'inbox-'
}

CELERY_ACCEPT_CONTENT = ['application/json', 'application/x-python-serialize']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

CELERY_ALWAYS_EAGER = config('CELERY_ALWAYS_EAGER', default=False, cast=bool)
CELERY_RESULT_BACKEND = None
CELERY_RESULT_PERSISTENT = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

COMPRESS_ENABLED = config('COMPRESS_ENABLED', default=True, cast=bool)
COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', default=True, cast=bool)

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.cssmin.CSSMinFilter']
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']

TIME_ZONE = config('TIME_ZONE', default='UTC')
