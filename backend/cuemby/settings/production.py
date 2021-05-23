from .common import *
from .partials.util import get_secret


# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
DEBUG = False
# Here you should put the URL of your site for the application
ALLOWED_HOSTS = ['127.0.0.1']
SECRET_KEY = get_secret('DJANGO_SECRET_KEY')


if get_secret('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
