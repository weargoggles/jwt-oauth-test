"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
import environ

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    JWT_PUBLIC_KEY=str,
    JWT_PRIVATE_KEY=str,
    SECRET_KEY=str,
    ADMINS=list,
    SERVER_EMAIL=str,
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

ADMINS = map(lambda x: (x, x), env('ADMINS'))

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.sessions',
    'project.test',
    'project.login',
    'project.home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': env.db(default='sqlite://memory'),
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

SESSION_ENGINE = 'project.sessions'

# RSA keys for JWT signing and validation
JWT_PUBLIC_KEY = env('JWT_PUBLIC_KEY')
JWT_PRIVATE_KEY = env('JWT_PRIVATE_KEY')

EMAIL_HOST = env('POSTMARK_SMTP_SERVER')
EMAIL_HOST_USER = env('POSTMARK_API_TOKEN')
EMAIL_HOST_PASSWORD = env('POSTMARK_API_TOKEN')
SERVER_EMAIL = env('SERVER_EMAIL')
EMAIL_USE_TLS = True


GITHUB_CLIENT_ID = env('GITHUB_CLIENT_ID')
GITHUB_CLIENT_SECRET = env('GITHUB_CLIENT_SECRET')
GITHUB_SCOPES = 'repo,user'

GITHUB_WEBHOOK_SECRET = env('GITHUB_WEBHOOK_SECRET')