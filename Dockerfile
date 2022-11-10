FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y ffmpeg libsm6 libxext6 
#RUN apt-get install -y apache2  

#RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf

#RUN mv /var/www/html/index.html /var/www/html/index_apache.html

#COPY ./FRONTEND/dist/front_space /var/www/html
COPY ./BACKEND ./BACKEND

RUN apt-get clean

#EXPOSE 80

WORKDIR /BACKEND/api

##CMD apachectl -D FOREGROUND
CMD ["uvicorn", "test:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]