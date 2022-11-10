FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y ffmpeg libsm6 libxext6 
RUN apt-get install -y apache2  

RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf

RUN mv /var/www/html/index.html /var/www/html/index_apache.html

COPY ./FRONTEND/dist/front_space /var/www/html
COPY ./BACKEND /BACKEND

RUN pip install -r /BACKEND/requirements.txt

RUN apt-get clean

EXPOSE 80
EXPOSE 8000

WORKDIR /BACKEND/api

RUN gunicorn -w 4 -k uvicorn.workers.UvicornWorker test:app

CMD apachectl -D FOREGROUND
#CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker test:app