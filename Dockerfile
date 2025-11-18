FROM python:3.9

WORKDIR /app

# Copiar requirements desde web
COPY web/requirements.txt .

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar el código de la aplicación
COPY web/. .

CMD ["python", "app.py"]

