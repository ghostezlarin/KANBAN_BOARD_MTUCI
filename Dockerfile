FROM ubuntu:latest
FROM python:3.10-slim
WORKDIR /kanban
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD ["python", "main.py"]

LABEL authors="pavel"