# Sử dụng Python 3.11 slim image
FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy requirements.txt trước để tận dụng Docker cache
COPY requirements.txt .

# Cài đặt dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY . .

# Expose port 5000
EXPOSE 5000

# Thiết lập biến môi trường
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Chạy ứng dụng với 1 worker để tránh vấn đề shared memory
CMD ["gunicorn", "-w", "1", "--threads", "8", "-b", "0.0.0.0:5000", "app:app"]
