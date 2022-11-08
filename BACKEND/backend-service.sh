#!/bin/bash
cd /home/JovianImageProcessing/BACKEND/api
touch /var/www/html/index-test.html
uvicorn test:app
