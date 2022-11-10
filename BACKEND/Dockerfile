FROM python:3

COPY . /BACKEND
RUN pip install --no-cache-dir -r /BACKEND/requirements.txt

WORKDIR /BACKEND/api

CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "80"]