#!/bin/bash

gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker test:app &
apachectl -D FOREGROUND &

wait -n
exit $?