FROM ubuntu:latest

COPY  . .

RUN pwd
RUN ls

ENV BACKEND=/JovianImageProcessing/BACKEND
ENV FRONTEND=/JovianImageProcessing/FRONTEND

RUN apt-get update && apt-get -y upgrade

WORKDIR $BACKEND

RUN pwd
RUN ls .

RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN pip install -r /JovianImageProcessing/BACKEND/requirements.txt

WORKDIR $FRONTEND

RUN pwd
RUN ls .

RUN apt-get install –y apache2 
RUN apt-get install –y apache2-utils 
RUN apt-get clean

EXPOSE 80

WORKDIR $BACKEND/api

RUN pwd
RUN ls .

CMD uvicorn main:app --reload