

from pathlib import Path
import os
from urllib.parse import urlparse


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=798a&hf%harj%b_vmta2%4@-^ohea)%7=*(#(a01xb*lcezae'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# #HTTPS Protokolni Yoqish
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'cart',
    'orders',
    'payment',
    'coupons',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'myshop.urls'

CART_SESSION_ID = 'cart'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
# STATICFILES_DIRS = [BASE_DIR, 'static/']
STATIC_ROOT = BASE_DIR / 'static'


MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CELERY_IMPORTS = ('payment', )

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#ORDER BOLGANDA ORDER BOLGANNI VA ID SINI EMAILGA YUBORISH
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'asadbektuygunov9@gmail.com'
EMAIL_HOST_PASSWORD = 'qgiihrhgrjfnphwe'
EMAIL_PORT = 587

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#TO'LOV TIZIMINI BAJARISHDA STRIPE KEYLARI
STRIPE_PUBLISHABLE_KEY = 'pk_test_51Nz1sLEX8jFQPQV2zOHvoZB8D7YvpcFwiIobB9IrZo0IWghmiKMu6VKVkE0KFGy8CvFStyH6Exkl1Gfq1u5PvQhs00ykmD4WrS' # Publishable key
STRIPE_SECRET_KEY = 'sk_test_51Nz1sLEX8jFQPQV2LKXFw0UY8FLtbW9T17UPcX38BixuK6IPmlCYbLFfXGTcQkcSyc8O8q6aFWAs0wTDtYycW8uR00sK2Aajqx'
STRIPE_API_VERSION = '2022-08-01'


STRIPE_WEBHOOK_SECRET = 'whsec_751f47157311b0bc0b60532a75331299ebbdba2f4ce51713fe06c0930d0cb217'


#Seleri urli topish uchun
# CELERY_BROKER_URL = 'amqp://admin:1234@localhost:5672/book_blog'


# Redis settings
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1


redis_url = urlparse(os.environ.get('REDISCLOUD_URL', 'redis://localhost:6379'))

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("REDISCLOUD_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Celery sozlamalari
CELERY_BROKER_URL = os.environ.get('REDISCLOUD_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('REDISCLOUD_URL', 'redis://localhost:6379/0')