FROM	python:3.7.9

ENV	PYTHONUNBUFFERED 1

RUN	mkdir /django
WORKDIR	/django

ADD requirements.txt	/django/

RUN	pip install --upgrade pip
RUN 	pip install -r requirements.txt

ADD	. /django/
