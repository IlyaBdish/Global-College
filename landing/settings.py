#-*- coding: cp1251-*-
"""
Django settings for landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


PATH = os.path.dirname(__file__).encode('cp1251')
MEDIA = os.path.join(PATH, 'media')
STATIC = os.path.join(PATH, 'static')
TEMPLATES = os.path.join(PATH, 'templates')

TEMPLATE_DIRS=(TEMPLATES, )
STATIC_ROOT=STATIC
STATIC_URL="/static/"

MEDIA_ROOT=MEDIA
MEDIA_URL="/media/"



STATICFILES_DIRS=()

SECRET_KEY = '=0k+%c5q%%*9ew*%8b6$p0xh5u@jm_0h5vrwz=oz)s3=kr!)t!'

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'landing.models',
    'django.contrib.admin',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'landing.urls'

WSGI_APPLICATION = 'landing.wsgi.application'



DATABASES = {'default': {'ENGINE': 'django.db.backends.mysql', 'NAME': 'land', 'HOST': '127.0.0.1', 'USER': 'root', 'PASSWORD': '06111971', 'PORT': '3307'
                         }
             }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

