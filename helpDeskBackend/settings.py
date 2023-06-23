"""
Django settings for helpDeskBackend project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPGroupQuery,GroupOfNamesType, NestedGroupOfNamesType,LDAPSearchUnion 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'rest_framework',
    "corsheaders",
    "rest_framework.authtoken",
    'apps',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",

]

ROOT_URLCONF = 'helpDeskBackend.urls'

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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication', # <-- And here
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# ldap authentification

LDAP_HOST = config("AUTH_LDAP_HOST")

LDAP_DC = config("AUTH_LDAP_DOMAIN_COMPONENT")


LDAP_BINDED_USER_GROUPS = config("AUTH_LDAP_BINDED_USER_GROUPS")

LDAP_SEARCH_USERS_IN = config("AUTH_LDAP_SEARCH_USERS_IN")

AUTH_LDAP_SERVER_URI = config("AUTH_LDAP_SERVER_URI")

AUTH_LDAP_BIND_DN = f'{config("AUTH_LDAP_BIND_DN_USER")},{LDAP_BINDED_USER_GROUPS}, DC={LDAP_HOST},DC={LDAP_DC}'

AUTH_LDAP_BIND_PASSWORD = config("AUTH_LDAP_BIND_PASSWORD")

AUTH_LDAP_USER_SEARCH = LDAPSearch(f'{LDAP_SEARCH_USERS_IN}, DC={LDAP_HOST},DC={LDAP_DC}',ldap.SCOPE_SUBTREE, '(sAMAccountName=%(user)s)')

AUTH_LDAP_GROUP_SEARCH = LDAPSearchUnion(
    LDAPSearch(f"{LDAP_SEARCH_USERS_IN},dc={LDAP_HOST},dc={LDAP_DC}", ldap.SCOPE_SUBTREE, "(objectClass=group)"),
    LDAPSearch(f"{LDAP_SEARCH_USERS_IN},dc={LDAP_HOST},dc={LDAP_DC}", ldap.SCOPE_SUBTREE, "(objectClass=organizationalUnit)"),
    LDAPSearch(f"{LDAP_SEARCH_USERS_IN},dc={LDAP_HOST},dc={LDAP_DC}", ldap.SCOPE_SUBTREE, "(objectClass=top)")
)

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

AUTH_LDAP_MIRROR_GROUPS = True

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    'username': 'sAMAccountName',
    'first_name': 'displayName',
    'last_name': 'sn',
    'email': 'mail',
}
LOGIN_URL = 'api/v1/sign-in/'

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     'is_active': 'CN=all, OU=HQ_Groups, DC=chitgu, DC=local',
#     'is_staff': 'CN=all, OU=HQ_Groups, DC=chitgu, DC=local',
#     'is_superuser': 'CN=all, OU=HQ_Groups, DC=chitgu, DC=local',
# }

AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600

#logging to console
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "loggers": {"django_auth_ldap": {"level": "DEBUG", "handlers": ["console"]}},
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

ALLOWED_HOSTS=['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
