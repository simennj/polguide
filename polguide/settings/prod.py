from polguide.settings.base import *

with open(os.path.join(BASE_DIR, 'settings', 'SECRET_KEY')) as secret_key_file:
    SECRET_KEY = secret_key_file.read().strip()

ALLOWED_HOSTS = ['polguide.no']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'polguide'
    }
}
