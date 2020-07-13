# fastpost
Blog engine in Django Framework, just for fun. You can see the demo site on http://fastpost.hotkosc.ru

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
Create following envorinment variables:
```shell
export DEBUG=True # False for production envorinment
export SECRET_KEY=SecretKey # Some secret key, keep it secure. Remember - sessions will be erased in case of changing this key.
export DATABASE_NAME=fastpost.sqlite3 # Filename of the database
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
