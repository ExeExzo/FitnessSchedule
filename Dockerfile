FROM python:3.8-alpine

WORKDIR /usr/src/app


RUN apk update \
    && apk add postgresql-libs postgresql-dev \
    gettext \
    gcc \
    musl-dev \
    zlib-dev \
    libffi-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
