import datetime
import sys
from datetime import timedelta

from .secret import SECRET
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = SECRET['SECRET_KEY']
DEBUG = True

## add to apps directory path
PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR))
sys.path.insert(0, os.path.join(PARENT_DIR, 'apps'))

INSTALLED_APPS = [
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ## Local app
    'Accounts',
    'Diary',
    'KakaoOauth',

    ## 3rd party
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    'storages',
    'drf_yasg',

    # provider
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
]

SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'apps', 'KakaoOauth', 'templates')
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,

    'DEFAULT_RENDERER_CLASSES': [
        'config.renderers.CustomRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

# rest-auth/kakao 호출시 response되는 user 정보 custom serializer
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'KakaoOauth.serializers.KakaoUserSerializer',
}

# djangorestframework-jwt
JWT_AUTH = {
    'JWT_SECRET_KEY': SECRET['SECRET_KEY'],
    'JWt_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=9999),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=9999)
}

REST_USE_JWT = True

AUTH_USER_MODEL = 'Accounts.User'

# all-auth model custom
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'

## auth PROVIDERS and ADAPTER
SOCIALACCOUNT_PROVIDERS = SECRET['SOCIALACCOUNT_PROVIDERS']
SOCIALACCOUNT_ADAPTER = 'KakaoOauth.adapter.SocialAccountRegisterAdapter'



DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'path/to/store/my/files/')

SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'config.inspectors.MyAutoSchema',
    'SECURITY_DEFINITIONS': {
        'JWT Token': {
            'type': 'apiKey',
            'description': '''
                인증을 위한 jwt 토큰\n
                모든 http 통신에서 필요하고 Header에 담아서 보내주어야 한다.\n
                형식은 아래와 같다.\n
                key : Authorization,\n 
                value : jwt eyJ0eXAiOiJKV1.....0qR01ScLtrdU\n                
            ''',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}