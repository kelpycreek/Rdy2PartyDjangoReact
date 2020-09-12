'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']
DEBUG = True

WSGI_APPLICATION = 'src.wsgi.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'changethisandalsodevsettings',
        'HOST': 'db',
        'PORT': 5432,
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)
