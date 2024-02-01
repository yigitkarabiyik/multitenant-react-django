# Django Dockerfile
FROM python:3.9

# Çalışma dizinini ayarla
WORKDIR /app

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Uygulama komutunu ayarla
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]