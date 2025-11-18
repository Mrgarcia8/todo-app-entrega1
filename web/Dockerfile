FROM python:3.9
WORKDIR /app
COPY web/requirements.txt .
RUN pip install -r web/requirements.txt .
COPY . .
CMD ["python", "app.py"]
