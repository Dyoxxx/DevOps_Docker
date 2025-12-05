# pour lancer docker run -p 8000:8000 (mlops-server:0.1)
FROM python:3.9-slim

COPY requirements.txt /app/requirements.txt
WORKDIR /app 

RUN pip install -r requirements.txt

COPY app.py app.py

COPY model.pkl /app/model.pkl

CMD ["uvicorn", "--reload", "--host", "0.0.0.0", "app:app"]