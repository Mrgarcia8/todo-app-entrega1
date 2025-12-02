# Imagen base de Python
FROM python:3.11-slim

# Crear directorio de la app
WORKDIR /app

# Copiar requerimientos desde la carpeta web
COPY web/requirements.txt /app/requirements.txt

# Instalar dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar todo el contenido del proyecto
COPY . /app

# Exponer el puerto de Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "web/app.py"]

