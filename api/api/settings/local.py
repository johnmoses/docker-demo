# Local settings
from .base import *

"""
Local settings
"""
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True


ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(' ')
CORS_ORIGIN_WHITELIST = env('CORS_ORIGIN_WHITELIST').split(' ')

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': env.db(),

#     'extra': env.db_url(
#         'SQLITE_URL',
#         default='sqlite:////db.sqlite3'
#     )
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
