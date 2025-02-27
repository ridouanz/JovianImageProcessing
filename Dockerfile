FROM ubuntu:latest

RUN apt-get update 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 
RUN apt-get install -y ffmpeg libsm6 libxext6 
#RUN apt-get install -y apache2  

#RUN echo "ServerName 0.0.0.0" >> /etc/apache2/apache2.conf

#RUN mv /var/www/html/index.html /var/www/html/index_apache.html

#COPY ./FRONTEND/dist/front_space .
#COPY ./FRONTEND/dist/front_space ./BACKEND/api
COPY ./BACKEND /BACKEND

#RUN chmod +x /BACKEND/api/run_all.sh

RUN pip install -r /BACKEND/requirements.txt

RUN apt-get clean

#EXPOSE 8000
#EXPOSE 80

WORKDIR /BACKEND/api

#CMD apachectl -D FOREGROUND
CMD gunicorn -k uvicorn.workers.UvicornWorker test:app  

#ENTRYPOINT [ "/bin/sh" ]
#CMD ["./run_all.sh"]