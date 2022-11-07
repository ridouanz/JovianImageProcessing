#!/bin/bash
cd /home/JovianImageProcessing/BACKEND/api
uvicorn main:app >> /home/backend_logs.log 
