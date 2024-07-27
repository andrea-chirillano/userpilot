# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos
COPY requirements.txt requirements.txt

# Instala las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear el entorno virtual
RUN python -m venv venv

# Activar el entorno virtual e instalar dependencias
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .

# Establecer la variable de entorno para usar el venv
ENV PATH="/app/venv/bin:$PATH"

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "userpilot/manage.py", "runserver", "0.0.0.0:8000"]
