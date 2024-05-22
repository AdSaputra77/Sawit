# Gunakan image Python sebagai base image
FROM python:3.9-slim

# Set lingkungan kerja
WORKDIR /app

# Copy requirements.txt dan install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file ke lingkungan kerja
COPY . /app

# Expose port aplikasi Flask
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]
