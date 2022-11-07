FROM ubuntu:latest

COPY  BACKEND /home/JovianImageProcessing/BACKEND

ENV BACKEND=/home/JovianImageProcessing/BACKEND
#ENV FRONTEND=/home/JovianImageProcessing/FRONTEND

RUN apt-get update 
#&& apt-get -y upgrade
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y ffmpeg libsm6 libxext6 
RUN apt-get install -y apache2  
RUN apt-get install -y systemd

RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf

WORKDIR $BACKEND
RUN pip install -r requirements.txt

#WORKDIR $FRONTEND

#COPY FRONTEND /var/www/html

RUN apt-get clean
EXPOSE 80

#CMD apachectl -D FOREGROUND

WORKDIR /home
RUN cp home/JovianImageProcessing/BACKEND/backend-service.sh /usr/local/bin
RUN sudo chmod +x /usr/local/bin/backend-service.sh
RUN cp home/JovianImageProcessing/BACKEND/backend-service.service /etc/systemd/system
RUN chmod 640 /etc/systemd/system/backend-service.service
RUN systemctl enable backend-service.service

WORKDIR $BACKEND/api


CMD cat /home/backend-logs.log