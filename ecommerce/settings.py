"""
Django settings for ecommerce project.

Optimized for Railway deployment with PostgreSQL.
"""

import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv  # جديد

# Load environment variables
load_dotenv()  # جديد

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ======== Security Settings ========
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-here')  # تم التعديل

DEBUG = os.getenv('DEBUG', 'False') == 'True'  # تم التعديل

ALLOWED_HOSTS = ['*']  # تم التعديل (يمكن تحديد نطاقات محددة لاحقاً)

# ======== Application Definition ========
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # جديد
    'django.contrib.staticfiles',
    'super',  # تطبيقك الخاص
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # جديد
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

# ======== Templates ========
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # يمكن إضافة مسارات إضافية
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

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# ======== Database ========
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True  # جديد للأمان
    )
}

# ======== Password Validation ========
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ======== Internationalization ========
LANGUAGE_CODE = 'ar'  # يمكن تغييرها لـ 'en-us'
TIME_ZONE = 'Africa/Cairo'  # تم التعديل
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ======== Static & Media Files ========
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # مهم للنشر
STATICFILES_DIRS = [BASE_DIR / 'static']  # ملفاتك الثابتة الإضافية
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # جديد

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ======== Session Settings ========
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 86400  # 24 ساعة
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# ======== Security Headers ========
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

# ======== Other Settings ========
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = 'login'  # مسار تسجيل الدخول