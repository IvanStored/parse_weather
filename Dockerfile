FROM python:3.10-alpine
LABEL maintainer="jus1stored@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY . .

RUN adduser --disabled-password --no-create-home django-user

USER django-user
