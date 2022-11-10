#!/bin/bash

gunicorn -b 127.0.0.1:8000 -k uvicorn.workers.UvicornWorker test:app &> /dev/null
service apache2 start
apachectl -D FOREGROUND &
wait