FROM ubuntu:latest

COPY BACKEND /home/JovianImageProcessing/BACKEND

ENV BACKEND=/home/JovianImageProcessing/BACKEND

RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y ffmpeg libsm6 libxext6 
RUN apt-get install -y apache2  
RUN apt-get install -y cron

RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf

## creating a backend service
RUN cp /home/JovianImageProcessing/BACKEND/backend-service.sh /usr/local/bin 
RUN chmod +x /usr/local/bin/backend-service.sh 
###RUN cp /home/JovianImageProcessing/BACKEND/backend-service.service /etc/systemd/system
###RUN chmod 640 /etc/systemd/system/backend-service.service
###RUN systemctl enable backend-service.service

WORKDIR $BACKEND
RUN pip install -r requirements.txt

RUN (crontab -l 2>/dev/null; echo "@reboot /usr/local/bin/backend-service.sh")| crontab -
RUN service cron start

RUN mv /var/www/html/index.html /var/www/html/index_apache.html
#COPY FRONTEND/dist/front_space /var/www/html



RUN apt-get clean
EXPOSE 80
#RUN sh /usr/local/bin/backend-service.sh

CMD apachectl -D FOREGROUND
###CMD systemctl status backend-service.service
#CMD ["sh", "/usr/local/bin/backend-service.sh"]