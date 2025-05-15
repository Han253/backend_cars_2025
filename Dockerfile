FROM python:3.11-slim

RUN mkdir /home/backend
WORKDIR /home/backend

ADD requirements.txt /home/backend/
RUN pip install --no-cache-dir -r requirements.txt

COPY staticfiles /home/backend/staticfiles
ENV TZ=America/Bogota

ADD . /home/backend/