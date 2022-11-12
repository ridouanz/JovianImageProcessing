#!/bin/bash

gunicorn -k uvicorn.workers.UvicornWorker test:app &> /dev/null
service apache2 start
apachectl -D FOREGROUND &
wait