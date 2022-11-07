FROM ubuntu:latest

COPY  BACKEND /JovianImageProcessing

ENV BACKEND=/JovianImageProcessing/BACKEND
#ENV FRONTEND=/JovianImageProcessing/FRONTEND

RUN apt-get update 
#&& apt-get -y upgrade

RUN pwd
RUN ls -al 

RUN pwd
RUN ls -al JovianImageProcessing
RUN ls -al JovianImageProcessing/BACKEND

WORKDIR $BACKEND
RUN pwd
RUN ls -al 

RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y ffmpeg libsm6 libxext6  
RUN pip install -r requirements.txt

#WORKDIR $FRONTEND

RUN apt-get install -y apache2 

#RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf

RUN apt-get clean
EXPOSE 80

#CMD apachectl -D FOREGROUND

WORKDIR $BACKEND/api

CMD uvicorn main:app --reload