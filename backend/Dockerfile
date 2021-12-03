
FROM python:3.9-slim-buster

WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get -y install netcat gcc \
    && apt-get clean

RUN pip install --upgrade pip
COPY . .
RUN pip install -r req.txt