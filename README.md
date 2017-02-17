# fastpost
Blog engine in Django Framework, just for fun

![I developed](http://s5.pikabu.ru/post_img/big/2015/04/23/8/1429794583_343353562.png)

# Installation instructions:
Install python3.5 or later and pip, also you will need postgresql9.4 or later.
Clone the repo and install all necessary python modules:
```shell
git clone https://github.com/kosc/fastpost.git
cd fastpost
pip install --user requirements.txt
```
Create user and database for fastpost in postgresql, and edit fastpost/settings.py (section DATABASES) to set your db settings, then fill your database and run Django development server:
```shell
python manage.py migrate
python manage.py runserver
```
Fastpost will be able on [localhost:8000](http://127.0.0.1:8000) (by default).
