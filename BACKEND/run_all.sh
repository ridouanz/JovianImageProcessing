#!/bin/bash

service apache2 start &
cd /api &
gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker test:app