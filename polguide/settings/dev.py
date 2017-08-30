from polguide.settings.base import *


## Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '62jdxr2%v)wg+7-o5h4h+7cp3y73wh3r5)w(^rt*h%+r52)h^j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS.append('corsheaders')

MIDDLEWARE.insert(
    2,'corsheaders.middleware.CorsMiddleware'
)

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

# https://github.com/ottoyiu/django-cors-headers/

CORS_ORIGIN_ALLOW_ALL = True
