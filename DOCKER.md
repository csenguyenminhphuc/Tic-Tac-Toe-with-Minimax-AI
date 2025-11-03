# 🐳 Docker Deployment Guide

Hướng dẫn chi tiết triển khai ứng dụng Tic-Tac-Toe với Docker.

---

## 📦 Quick Start với Docker Compose

### 1. Build và chạy (Background mode)
```bash
docker-compose up -d
```

### 2. Truy cập ứng dụng
Mở trình duyệt: `http://localhost:5000`

### 3. Xem logs
```bash
docker-compose logs -f
```

### 4. Dừng ứng dụng
```bash
docker-compose down
```

---

## 🛠️ Docker Commands Chi Tiết

### Build Image
```bash
docker build -t tictactoe-game .
```

### Chạy Container
```bash
# Foreground mode (xem logs trực tiếp)
docker run -p 5000:5000 --name tictactoe tictactoe-game

# Background mode (daemon)
docker run -d -p 5000:5000 --name tictactoe tictactoe-game
```

### Quản lý Container
```bash
# Xem logs
docker logs tictactoe
docker logs -f tictactoe  # Follow logs

# Dừng container
docker stop tictactoe

# Khởi động lại
docker restart tictactoe

# Xóa container
docker rm tictactoe

# Xóa cả image
docker rmi tictactoe-game
```

---

## 🌐 Deploy trên VPS/Cloud

### 1. Cài đặt Docker trên VPS
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker

# Cài Docker Compose
sudo apt install docker-compose-plugin
```

### 2. Clone project
```bash
git clone <your-repo-url>
cd tik_tok_toe
```

### 3. Chạy với Docker Compose
```bash
docker-compose up -d
```

### 4. Cấu hình Firewall
```bash
# UFW (Ubuntu)
sudo ufw allow 5000/tcp
sudo ufw reload

# Firewalld (CentOS/RHEL)
sudo firewall-cmd --permanent --add-port=5000/tcp
sudo firewall-cmd --reload
```

### 5. Kiểm tra
```bash
docker-compose ps
docker-compose logs
curl http://localhost:5000
```

---

## 🔧 Custom Configuration

### Thay đổi Port
Chỉnh sửa `docker-compose.yml`:
```yaml
ports:
  - "8080:5000"  # External:Internal
```

### Thêm Environment Variables
```yaml
environment:
  - FLASK_ENV=production
  - MAX_GAMES=2000
  - SECRET_KEY=your-secret-key
```

### Mount Volume (để lưu data)
```yaml
volumes:
  - ./data:/app/data
```

---

## 🔄 CI/CD với Docker

### GitHub Actions Example
Tạo `.github/workflows/docker.yml`:
```yaml
name: Docker Build & Deploy

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Docker Image
        run: docker build -t tictactoe-game .
      
      - name: Push to Docker Hub
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker tag tictactoe-game username/tictactoe-game:latest
          docker push username/tictactoe-game:latest
```

---

## 📊 Monitoring & Debugging

### Xem resource usage
```bash
docker stats tictactoe
```

### Exec vào container
```bash
docker exec -it tictactoe /bin/bash
```

### Kiểm tra network
```bash
docker network inspect tictactoe-network
```

### Inspect container
```bash
docker inspect tictactoe
```

---

## 🐛 Troubleshooting

### Container không start
```bash
# Xem logs chi tiết
docker logs tictactoe

# Rebuild image
docker-compose down
docker-compose build --no-cache
docker-compose up
```

### Port đã được sử dụng
```bash
# Tìm process đang dùng port
sudo lsof -i :5000

# Kill process
sudo kill -9 <PID>
```

### Permission denied
```bash
# Thêm user vào docker group
sudo usermod -aG docker $USER
newgrp docker
```

---

## 🚀 Production Best Practices

1. **Sử dụng Nginx reverse proxy**
2. **Cấu hình SSL/TLS với Let's Encrypt**
3. **Giới hạn resources:**
   ```yaml
   deploy:
     resources:
       limits:
         cpus: '0.5'
         memory: 512M
   ```
4. **Health checks:**
   ```yaml
   healthcheck:
     test: ["CMD", "curl", "-f", "http://localhost:5000"]
     interval: 30s
     timeout: 10s
     retries: 3
   ```
5. **Logging với driver:**
   ```yaml
   logging:
     driver: "json-file"
     options:
       max-size: "10m"
       max-file: "3"
   ```

---

**Happy Deploying! 🐳✨**
