import os
from pathlib import Path

import sentry_sdk
from decouple import Csv, config
from dj_database_url import parse as dburl
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminlte3',
    'adminlte3_theme',
    'crispy_forms',
    'debug_toolbar',
    'django_filters',
    'widget_tweaks',
    'bootstrap4',
    'django_q',
    'django_extensions',
    'indicadores_esus.core',
    'indicadores_esus.esus',
    'indicadores_esus.indicator',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'indicadores_esus.core.middleware.DisableCSRF',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'login_required.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'indicadores_esus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'indicadores_esus.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
default_dburl_esus = 'sqlite:///' + os.path.join(BASE_DIR, 'db_esus.sqlite3')

DATABASES = {
    'default': config('SYSTEM_DATABASE_URL', default=default_dburl, cast=dburl),
    'esus': config('ESUS_DATABASE_URL', default=default_dburl_esus, cast=dburl)
}

DATABASE_ROUTERS = [
    'indicadores_esus.esus.db.router.EsusRouter'
]

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'core:home'
LOGOUT_REDIRECT_URL = 'login'
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Add this

CSRF_TRUSTED_ORIGINS = ['http://137.184.17.203', 'http://127.0.0.1']

SHORT_DATE_FORMAT = 'd/m/Y'

SHORT_DATETIME_FORMAT = 'd/m/Y H:i:s'

DECIMAL_SEPARATOR = ','

Q_CLUSTER = {
    'name': 'indicadores_esus',
    'orm': 'default',
    'timeout': 86400,
    'retry': 90000,
    'error_reporter': {
        'sentry': {
            'dsn': 'https://fe87d0b62d5f45c798f4f3b4b48b0a36@o373511.ingest.sentry.io/4504373524103168'
        }
    }
}

LOGIN_REQUIRED_IGNORE_PATHS = [
    r'/accounts/login/$',
    r'/admin/$',
    r'__debug__/$',
    r'/login/$',
    r'/logout/$',
]


sentry_sdk.init(
    dsn="https://fe87d0b62d5f45c798f4f3b4b48b0a36@o373511.ingest.sentry.io/4504373524103168",
    integrations=[
        DjangoIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
