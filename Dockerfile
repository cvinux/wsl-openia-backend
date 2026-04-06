# Imagen base
FROM python:3.12-slim

# Carpeta de trabajo
WORKDIR /app

# Copiar archivos
COPY . .

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install openai python-dotenv

# Ejecutar app
CMD ["python", "-m", "app.main"]