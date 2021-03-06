FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir fastquant

COPY ./app /app