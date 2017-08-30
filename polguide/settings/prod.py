from polguide.settings.base import *

with open('SECRET_KEY') as secret_key_file:
    SECRET_KEY = secret_key_file.read().strip()

ALLOWED_HOSTS = ['polguide.no']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

