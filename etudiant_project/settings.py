# -*- coding: UTF-8 -*-
"""
Django settings for etudiant_project project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from __future__ import unicode_literals
import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-yuug-q6ky^6^6f)6qp)dw5ifn1acwysv=lk2o5cevd8&2_fia'

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = ['easem.herokuapp.com', 'localhost', 'www.easem.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'Etudiant',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'etudiant_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # This line add Dossiers template from project root
            os.path.join(BASE_DIR, "templates/")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'etudiant_project.context_processors.get_infos',
            ],
        },
    },
]

WSGI_APPLICATION = 'etudiant_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'yattara',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_URL = '/media/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Les medias de l'admin sont enfin une URL comme une autre qu'on peut
# mettre sous notre propre arborescence
# ADMIN_MEDIA_PREFIX = '/static/admin/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static/dossiers/")
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


if os.environ.get('ENV') == 'PRODUCTION':
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # ADMIN_MEDIA_PREFIX = os.path.join(BASE_DIR, '/static/dossiers/')

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )

    # AWS_S3_SECURE_URLS = False       # use http instead of https

    # don't add complex authentication-related query parameters for requests
    AWS_QUERYSTRING_AUTH = False

    # Your S3 Access Key
    AWS_S3_ACCESS_KEY_ID = os.environ["AKIAIRUCDH7VA4GH672Q"]

    # Problm with IndentationError: unindent does not match any indent
    # fix: indent to "if" condition until end to if
    # Your S3 Secret
    AWS_S3_SECRET_ACCESS_KEY = os.environ["zOHx80JWXOVZHMe5ygbE4iW9GDPD92oNUQn1OzXt"]

    AWS_STORAGE_BUCKET_NAME = os.environ["siteasem"]

    # Change to the media center you chose when creating the bucket
    # AWS_S3_HOST = "s3-us-east-1.amazonaws.com"

    MEDIA_URL = 'http://siteasem.s3.amazonaws.com/media/'

    DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"

    # STATICFILES_STORAGE = "etudiant_project.s3utils.StaticS3BotoStorage"

    # Gestion of staticfiles with whitenoise
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)


# REDIRECTION to lien
# LOGIN_URL = '/Etudiant/connexion/'

# EMAIL settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "myproject@gmail.com"
EMAIL_HOST_PASSWORD = "mygmailpassword"
EMAIL_PORT = 587
