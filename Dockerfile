FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /web_app
WORKDIR /web_app
COPY ./library /web_app

RUN adduser -D user
USER user