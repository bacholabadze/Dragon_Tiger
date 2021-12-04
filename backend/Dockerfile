FROM python:3.9-slim-buster

WORKDIR /usr/src/app

RUN apt-get update \
  && apt-get -y install netcat gcc curl

COPY req.txt .
RUN pip install --upgrade pip
RUN pip install -r req.txt

COPY . .


# pull official base image
FROM python:3.9.6-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

# add app
COPY . .