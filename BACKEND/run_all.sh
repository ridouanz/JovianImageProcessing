#!/bin/bash

service apache2 start &
gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker test:app 