"""
Django settings for Test_project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n59f$9-y$tw4x0=w02ubkuwh+jk_$n=+4in451z_=n=i6c=6ai'

# SECURITY WARNING: don't run with debug turned on in production!
# true thi ghi lai log (nang server), false thi khong ghi lai
DEBUG = True

#gan domain vo trong nay
#ALLOWED_HOSTS = ['okuro.vn']
#ALLOWED_HOSTS = ['localhost:8000']
ALLOWED_HOSTS = []


# Application definition
# package kem theo de xu ly
INSTALLED_APPS = [
    'django.contrib.admin',
    # xu ly truy cap tu ben ngoai
    'django.contrib.auth',
    # ho tro define, xu ly bien
    'django.contrib.contenttypes',
    # luu request cua user de xu ly
    'django.contrib.sessions',
    # notification 
    'django.contrib.messages',
    # media, duong dan
    'django.contrib.staticfiles',
    'products'
]

# tuong lua
# chan request lon, hacker ......v......v....
#?tu tao middleware rieng - ok
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Test_project.DemoMiddleware.DemoMiddleware'
]

# domain chinh
#ROOT_URLCONF = 'okuro.vn'
ROOT_URLCONF = 'Test_project.urls'

#view
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


WSGI_APPLICATION = 'Test_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# tim hieu cach ket noi 2 database
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "djangosql",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "4306"
    },
    "DB2": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_mysql",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "4306"
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#tao router o trong product voi method post
#xu ly data o view nhan payload va xu ly de luu vao products
