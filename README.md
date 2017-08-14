# fastpost
Blog engine in Django Framework, just for fun

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fe9b5907856f438f9e9e4de0e114e342)](https://www.codacy.com/app/hotkosc/fastpost?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=kosc/fastpost&amp;utm_campaign=Badge_Grade)

# Installation instructions:
Install python3.5 or later and pip.
Clone the repo and install all necessary python modules:
```shell
git clone https://github.com/kosc/fastpost.git
cd fastpost
pip install --user -r requirements/dev.txt # if you want to help me with this project or just test this.
pip install --user -r requirements/base.txt # if you want to use this on production
```
Create fastpost/local\_settings.py with following content:
```python
# from .settings import INSTALLED_APPS, MIDDLEWARE_CLASSES
# Uncomment first line for development server

SECRET_KEY = 'Your secret key'
DEBUG = True # False if your want to use fastpost in production
ALLOWED_HOSTS = [] # for development
ALLOWED_HOSTS = ['*'] # for docker-compose
ALLOWED_HOSTS = ["your-production-domain"] # for production

STATIC_ROOT = "static/" # For nginx in docker

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'data/fastpostdb.sqlite3', # database for fastpost
    }
}

# if you want to use debug_toolbar
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')

```
Fill your database and run Django development server:
```shell
python manage.py migrate
python manage.py runserver
```
To run with a docker compose
```
docker-compose up
```

Fastpost will be available on [localhost:8000](http://127.0.0.1:8000) (by default).
