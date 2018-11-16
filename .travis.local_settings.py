from .settings import INSTALLED_APPS, MIDDLEWARE

SECRET_KEY = 'Your secret key'
DEBUG = True # False if your want to use fastpost in production
ALLOWED_HOSTS = ['*'] # for docker-compose

STATIC_ROOT = "static/" # For nginx in docker

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data/fastpostdb.sqlite3', # database for fastpost
    }
}

# if you want to use debug_toolbar
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
