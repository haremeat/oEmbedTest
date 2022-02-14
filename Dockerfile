FROM python:3.8.0-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYECODE 1
ENV PYTHONUNBUFFERD 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
