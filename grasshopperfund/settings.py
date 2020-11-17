"""
Django settings for grasshopperfund project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from config import Config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ql!c&1vqc+*&ogeoztwl9k(cth#ki&5v&qae=a&4a)-=m80yb$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.humanize',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',

    #allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'material',

    # providers
    # TODO: use environmental vars or github secrets for google
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

    # Our apps
    'grasshopperfund.users.apps.UsersConfig',
    'grasshopperfund.campaigns.apps.CampaignsConfig',
    'grasshopperfund.organizations.apps.OrganizationsConfig',
    'grasshopperfund.tags.apps.TagsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'grasshopperfund.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'grasshopperfund/templates')],
        "APP_DIRS": True,
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

WSGI_APPLICATION = 'grasshopperfund.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

# set up allauth social apps
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
         'METHOD': 'oauth2',
         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
         'SCOPE': ['email', 'public_profile'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'INIT_PARAMS': {'cookie': True},
         'FIELDS': [
             'id',
             'first_name',
             'last_name',
             'name',
             'name_format',
             'picture',
             'short_name'
         ],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'ru_RU',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v7.0',

         # This portion is OPTIONAL if you'd like to use environmental variables
         # While 'APP' is commented out, you can use Django Admin to
         # populate the credential fields.
         # If this is uncommented, this block will OVERRIDE credentials in
         # Django admin
         'APP': {
             'client_id': Config.SOCIAL_AUTH_FACEBOOK_APP_ID,  # !!! THIS App ID
             'secret': Config.SOCIAL_AUTH_FACEBOOK_APP_SECRET,  # !!! THIS App Secret
             'key': Config.SOCIAL_AUTH_FACEBOOK_APP_KEY
        }

    },
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online'
        },

         # This portion is OPTIONAL if you'd like to use environmental variables
         # While 'APP' is commented out, you can use Django Admin to
         # populate the credential fields.
         # If this is uncommented, this block will OVERRIDE credentials in
         # Django admin
         'APP': {
             'client_id': Config.SOCIAL_AUTH_GOOGLE_APP_ID,  # !!! THIS App ID
             'secret': Config.SOCIAL_AUTH_GOOGLE_APP_SECRET,  # !!! THIS App Secret
             'key': Config.SOCIAL_AUTH_GOOGLE_APP_KEY
        }
    }


}


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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'login'

#Authentication
SITE_ID = 1

LOGIN_REDIRECT_URL = "/"

AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )



# AUTH_USER_MODEL = "users.Profile"