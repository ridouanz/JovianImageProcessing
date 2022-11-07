FROM ubuntu:latest

COPY  . /JovianImageProcessing

ENV BACKEND=/JovianImageProcessing/BACKEND
ENV FRONTEND=/JovianImageProcessing/FRONTEND

RUN apt-get update && apt-get -y upgrade

WORKDIR $BACKEND

RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y ffmpeg libsm6 libxext6  
RUN pip install -r requirements.txt

WORKDIR $FRONTEND

RUN apt-get install -y apache2 
RUN apt-get install -y apache2-utils 

RUN apt-get install -y systemd
RUN systemctl enable apache2
RUN systemctl start apache2

RUN apt-get clean
EXPOSE 80

CMD systemctl status apache2

#WORKDIR $BACKEND/api

#CMD uvicorn main:app --reload