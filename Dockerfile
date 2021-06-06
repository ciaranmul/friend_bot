FROM python:slim

RUN apt-get update
RUN apt-get -y install build-essential

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN apt-get -y remove build-essential
RUN apt clean && \
    rm -rf \
        /tmp/* \
        /var/lib/apt/lists/* \
        /var/tmp/*
