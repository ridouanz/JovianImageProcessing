#!/bin/bash

gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker test:app &
service apache2 start
apachectl -D FOREGROUND
service apache2 status
echo "Both services are running :D"
wait 