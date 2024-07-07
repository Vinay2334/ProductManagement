FROM python:3.11
LABEL maintainer="docker"

ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /tmp/requirements.txt
COPY ./ /ProductManagement
WORKDIR /ProductManagement
EXPOSE 8000
ARG DEV=false

RUN apt-get update && \
    apt-get -y install sudo && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp/*

ENV PATH="/py/bin:$PATH"

USER root