"""
Django settings for ohdeer project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from os import environ
#changed from dirname to abspath
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GEOS_LIBRARY_PATH = environ.get('GEOS_LIBRARY_PATH')
GDAL_LIBRARY_PATH = environ.get('GDAL_LIBRARY_PATH')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&^lan!p2#@rx1@cg7$9fj-4*8@6p#2y2$icgntvwpb@a+6fv#p'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['ohdeer.herokuapp.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
		'django.contrib.gis',    
		'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',	
		'deermap'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ohdeer.urls'

TEMPLATE_DIRS = (
	#[os.path.join(BASE_DIR,'templates')]
	'templates',
)

WSGI_APPLICATION = 'ohdeer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

'default': {
  		'ENGINE': 'django.contrib.gis.db.backends.postgis',
    	'NAME': 'deermap',
		'USER': 'morgan',
		'PASSWORD': '',
		'HOST': '',

#DATABASES['default'] = dj_database_url.config()
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
		#os.path.join(BASE_DIR,'static'),
	'deermap/static/',					
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
