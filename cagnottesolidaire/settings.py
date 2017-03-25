"""
Django settings for cagnottesolidaire project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

from os.path import abspath, dirname, join
from pathlib import Path

PROJECT = "cagnottesolidaire"
PROJECT_VERBOSE = "Cagnotte Solidaire"
MAIL_USER = "majo"
SELF_MAIL = False
ALLOWED_HOSTS = ["cagnottesolidaire.totheweb.fr"]
ALLOWED_HOSTS.append("www.%s" % ALLOWED_HOSTS[0])

BASE_DIR = dirname(dirname(abspath(__file__)))

CONF_DIR = Path("/etc/django/") / PROJECT

SECRET_KEY = (CONF_DIR / "secret_key.txt").open().read().strip()

DEBUG = not (CONF_DIR / "prod").is_file()
if DEBUG:
    ALLOWED_HOSTS.append("127.0.0.1")
    ALLOWED_HOSTS.append("localhost")

EMAIL_SUBJECT_PREFIX = ("[%s Dev] " if DEBUG else "[%s] ") % PROJECT_VERBOSE

EMAIL_USE_SSL = True
EMAIL_HOST = "mail.gandi.net" if SELF_MAIL else "SSL0.OVH.NET"
EMAIL_PORT = 465
EMAIL_HOST_USER = "%s@%s" % (MAIL_USER, ALLOWED_HOSTS[0] if SELF_MAIL else "totheweb.fr")
SERVER_EMAIL = "%s+%s@%s" % (MAIL_USER, PROJECT, ALLOWED_HOSTS[0] if SELF_MAIL else "totheweb.fr")
DEFAULT_FROM_EMAIL = "%s <%s@%s>" % (PROJECT_VERBOSE, MAIL_USER, ALLOWED_HOSTS[0] if SELF_MAIL else "totheweb.fr")
EMAIL_HOST_PASSWORD = (CONF_DIR / "email_password").open().read().strip()
EMAIL_BACKEND = 'django.core.mail.backends.%s' % ('locmem.EmailBackend' if DEBUG else 'smtp.EmailBackend')

ADMINS = (("Guilhem Saurel", "guilhem+admin-%s@saurel.me" % PROJECT),)
MANAGERS = ADMINS

INSTALLED_APPS = [
    PROJECT,
    'django.contrib.admin',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrap3',
    'projets',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '%s.urls' % PROJECT

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'fr-FR'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SITE_ID = 1

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static_dest') if DEBUG else '/var/www/%s/static_dest' % PROJECT

if not DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
            "LOCATION": "127.0.0.1:11211",
        }
    }

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
    },
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = ['yeouia.backends.YummyEmailOrUsernameInsensitiveAuth']

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
REGISTRATION_EMAIL_HTML = False
