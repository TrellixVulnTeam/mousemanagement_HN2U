"""
Django settings for mousemanagement project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wtzs$+6_@w(u*+ol_zw^046#@r2e*fj!-1lu(**=whh#05xih2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['mousemanagement.herokuapp.com', '127.0.0.1', '192.168.50.194']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'harvestmouseapp.apps.HarvestmouseappConfig',
    'usermanagement.apps.UsermanagementConfig',
    # 'django_extensions'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

"""
By regulations of WW3, current browser added CORS, Access-Control-Allow-Origin, and SameSite cookies protection
from cross site access.
SameSite is a property that can be set in HTTP cookies to prevent Cross Site Request Forgery(CSRF) attacks in web applications:
When SameSite is set to Lax , the cookie is sent in requests within the same site and in GET requests from other sites
So basically, for cross site cookies,
1. Samesite must be none
2. Secure connection is needed
3. Allow credentials must be in the request heaeder in order to send session over to server.
4. CORS Origin Allow All origin
"""
CORS_ALLOW_CREDENTIALS = True
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = [
    'Access-Control-Allow-Origin',
    'access-control-allow-credentials',
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'enctype',
    'observe',
    'responseType',
    'withCredentials'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}

ROOT_URLCONF = 'mousemanagement.urls'

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mousemanagement.wsgi.application'

"""
THis is the default setting which use of the file-method to store the db data
"""
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


"""
THis is use for unbench testing where django app connecting to local postgresql server using psycopg2
"""
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mousemanagement',
            'USER': 'postgres',
            'PASSWORD': '33360411',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    """
    THis is used in the heroku environment to connect to the postgresql within the heroku app
    """
    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = ['mousemanagement.authbackend.LocalBackends']

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

django_heroku.settings(locals())

# API KEY for Send Grid services
SEND_GRID_API_KEY = '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'

MAINTAINANCE_EMAIL = "chenyuhang01@gmail.com"
MAINTAINANCE_SEND_GRID_API_KEY = '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'