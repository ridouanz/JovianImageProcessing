#!/bin/bash

gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker test:app &> /dev/null
apachectl -D FOREGROUND &
echo "Both services are running :D"
wait 