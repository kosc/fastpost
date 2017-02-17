# fastpost
Blog engine in Django Framework, just for fun

![I developed](http://s5.pikabu.ru/post_img/big/2015/04/23/8/1429794583_343353562.png)

# Installation instructions:
Install python3.5 or later and pip, also you will need postgresql9.4 or later.
Clone the repo and install all necessary python modules:
```shell
git clone https://github.com/kosc/fastpost.git
cd fastpost
pip install --user requirements/dev.txt # if you want to help me with this project or just test this.
pip install --user requirements/base.txt # if you want to use this on production
```
Create user and database for fastpost in postgresql, and create fastpost/local\_settings.py with following content:
```python
SECRET_KEY = 'Your secret key'
DEBUG = True # False if your want to use fastpost in production
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost', # server with postgresql (can be different from localhost)
        'NAME': 'fastpost', # database for fastpost
        'USER': 'fastpost_user', # database user for fastpost
        'PASSWORD': 'T3mpPassw0rd', # password for your fastpost user
    }
}

```
Fill your database and run Django development server:
```shell
python manage.py migrate
python manage.py runserver
```
Fastpost will be able on [localhost:8000](http://127.0.0.1:8000) (by default).
