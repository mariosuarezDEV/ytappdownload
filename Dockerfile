# 1. Escoger la Imagen
FROM python:3.12.12-alpine3.23

# 2. Crear espacio de trabajo en el contenedor
WORKDIR /app

# 3. Pasar el archivo de dependencias para instalarlas posteriormente
COPY requirements.txt .
RUN pip install -r requirements.txt

# Mover el proyecto al contenedor
COPY . .

# Exponer los puertos necesarios
EXPOSE 8080

# Correr el proyecto
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]