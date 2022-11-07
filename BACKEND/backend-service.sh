#!/bin/bash
cd /home/JovianImageProcessing/BACKEND/api
uvicorn main:app >> /var/www/html/index.html
