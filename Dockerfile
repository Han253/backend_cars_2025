FROM python:3.11-slim

RUN mkdir /backend
WORKDIR /backend

ADD requirements.txt /backend/
RUN pip install --no-cache-dir -r requirements.txt

COPY static /home/backend/staticfiles
ENV TZ=America/Bogota

ADD . /backend/