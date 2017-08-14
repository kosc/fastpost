FROM python:3.6
MAINTAINER Kosenko Artyom <kosc@hotkosc.ru>
ENV PYTHONBUFFERED 1
COPY . /fastpost
WORKDIR /fastpost
RUN pip install -r requirements/dev.txt
