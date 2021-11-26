FROM python:3.8-slim-buster

WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get -y install netcat gcc curl

COPY req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY . .