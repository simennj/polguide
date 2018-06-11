from polguide.settings.base import *

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = ['polguide.no', 'alpha.polguide.no']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'polguide'
    }
}
