FROM python:3.6
MAINTAINER Kosenko Artyom <kosc@hotkosc.ru>
COPY . /fastpost
WORKDIR /fastpost
RUN pip3.6 install -r requirements/base.txt
RUN python3.6 /fastpost/manage.py migrate
