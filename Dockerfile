FROM python:3.10-slim

WORKDIR /bookstore

ADD ./ /bookstore/

RUN apt-get update
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential pkg-config




RUN pip install --upgrade pip

RUN pip install -r requirements.txt


CMD python store/manage.py makemigrations && python store/manage.py migrate && python store/manage.py runserver 0.0.0.0:8000
