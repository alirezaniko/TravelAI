"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 5.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import logging
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-avo+t3__x%nivtn&(73d0gc!8sg5)#0_fjg8(^rdxww4n_cdn^'

DEBUG = True

ALLOWED_HOSTS = ["*", "0.0.0.0","127.0.0.1"]

logger = logging.getLogger('django')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',

    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'django_filters',
    'corsheaders', 
    'allauth.socialaccount.providers.google',

    'users',
    'category',
    'predict',
    'about',
    'contactus',
    'tag'
    
    
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True  
CORS_ALLOWED_ORIGINS = [
   
]
ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR), 'templates'],
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

WSGI_APPLICATION = 'conf.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.environ.get('DB_TYPE') == 'postgresql':
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    DATABASES['default']['NAME'] = os.environ.get('DB_NAME')
    DATABASES['default']['USER'] = os.environ.get('DB_USER')
    DATABASES['default']['PASSWORD'] = os.environ.get('DB_PASSWORD')
    DATABASES['default']['HOST'] = os.environ.get('DB_HOST')
    DATABASES['default']['PORT'] = 5432

else:
    # If DB_TYPE is not set or not 'postgresql', use SQLite
    pass



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "pydevcasts@gmail.com"
EMAIL_HOST_PASSWORD = "yjbz fsim gaxi xeuj"

EMAIL_USE_TLS = True

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



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # مسیر فایل‌های استاتیک سفارشی
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # مسیر جمع‌آوری فایل‌های استاتیک توسط collectstatic

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # مسیر نگهداری فایل‌های آپلود شده

ACCOUNT_SIGNUP_REDIRECT_URL = '/rest-auth/registration/verify-email/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
    'JWT_AUTH_HTTPONLY':False
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,  # فعال‌سازی چرخش توکن‌های تازه
    'BLACKLIST_AFTER_ROTATION': True,  # فعال‌سازی لیست سیاه برای توکن‌های قدیمی
    "AUTH_HEADER_TYPES": ("Bearer",),
}

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False


AUTH_USER_MODEL = 'users.CustomUser'
LOGOUT_REDIRECT_URL = '/admin/'
LOGIN_URL = 'http://localhost:8000/rest-auth/login/'
LOGGING = {
    'version': 1,
    'disable_extras': False,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    },
}



CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    # "http://172.235.19.174/",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
    'https://0.0.0.0:8000'
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)
CORS_ALLOW_HEADERS = (
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
)


# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3  # Optional: Set expiration for confirmation

#social login setting

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP':{
            'client_id':'228488379476-gq1kf7e39hha7ce5d23tq5hreat6p3ga.apps.googleusercontent.com',
            'secret':'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',
        },
        'SCOPE':['profile','email',],
        'AUTH_PARAMS':{'access_type','online',},
        'METHOD':'oauth2',
        'VERIFIED_EMAIL':True,
    },
}

SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = "success"