FROM ubuntu:latest

COPY  . .

ENV BACKEND=JovianImageProcessing/BACKEND
ENV FRONTEND=JovianImageProcessing/FRONTEND

WORKDIR $BACKEND

#BACKEND actions here
RUN apt-get install -y python3 
RUN python3 install pip 

WORKDIR $FRONTEND

RUN apt-get update && apt-get -y upgrade
RUN apt-get install –y apache2 
RUN apt-get install –y apache2-utils 
RUN apt-get clean

WORKDIR $BACKEND/api

EXPOSE 80
CMD uvicorn main:app --reload