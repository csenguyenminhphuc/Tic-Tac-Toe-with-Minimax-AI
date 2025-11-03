# 🎮 Tic-Tac-Toe (XO) Game - Web Application

Một ứng dụng web Tic-Tac-Toe (trò chơi XO) được xây dựng với **Python Flask** backend và **Vanilla JavaScript** frontend. Máy tính sử dụng thuật toán **Minimax** với **Alpha-Beta Pruning** để chơi.

## ✨ Tính Năng

- ✅ **3 Mức Độ Khó**:
  - 🟢 **Dễ**: Máy chơi ngẫu nhiên
  - 🟡 **Trung bình**: Máy có chiến lược cơ bản với tìm kiếm độ sâu giới hạn
  - 🔴 **Khó**: Máy sử dụng Minimax với Alpha-Beta Pruning - **Gần như bất khả thi**

- 🤖 **AI Thông Minh**: 
  - Thuật toán Minimax đầy đủ
  - Alpha-Beta Pruning để tối ưu hóa hiệu suất
  - Chiến lược phòng thủ và tấn công

- 🎨 **Giao Diện Đẹp**:
  - Responsive design (thích ứng với điện thoại, tablet, máy tính)
  - Hiệu ứng hoạt hình mượt mà
  - Giao diện hiện đại với gradient màu

- ⌨️ **Phím Tắt**:
  - **Phím 1-9**: Di chuyển vào các ô tương ứng trên bàn cờ
  - **N**: Chơi ván mới (sau khi game kết thúc)
  - **R**: Đặt lại game

- 📱 **Không Yêu Cầu Đăng Nhập**: Chơi ngay mà không cần tài khoản

## 🛠️ Công Nghệ Sử Dụng

### Backend
- **Python 3.8+**
- **Flask 2.3.3** - Web framework

### Frontend
- **HTML5** - Cấu trúc trang
- **CSS3** - Styling với gradient, flexbox, grid
- **JavaScript** (Vanilla) - Không sử dụng framework

### AI
- **Minimax Algorithm** - Tìm kiếm toàn bộ cây trò chơi
- **Alpha-Beta Pruning** - Tối ưu hóa hiệu suất

## 📋 Yêu Cầu

- Python 3.8 trở lên
- pip (Package installer for Python)

## 🚀 Cài Đặt & Chạy

### 1. Cài Đặt Dependencies

```bash
pip install -r requirements.txt
```

### 2. Chạy Ứng Dụng

```bash
python app.py
```

### 3. Truy Cập Ứng Dụng

Mở trình duyệt web và truy cập:
```
http://127.0.0.1:5000
```

## 📁 Cấu Trúc Dự Án

```
tik_tok_toe/
├── app.py                          # Flask backend chính
├── game_logic.py                   # Logic game & AI Minimax
├── requirements.txt                # Python dependencies
├── # 🎮 Tic-Tac-Toe Web Application

Ứng dụng web chơi Tic-Tac-Toe (Caro 3x3) với trí tuệ nhân tạo sử dụng thuật toán **Minimax** và **Alpha-Beta Pruning**.

**Phát triển bởi: Kỹ sư Nguyễn Minh Phúc - DevSecOps & Infrastructure Engineer**

---

## 📋 Mục lục

- [Tính năng](#-tính-năng)
- [Công nghệ](#-công-nghệ-sử-dụng)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt](#-cài-đặt)
  - [Phương pháp 1: Chạy trực tiếp (Python)](#phương-pháp-1-chạy-trực-tiếp-python)
  - [Phương pháp 2: Sử dụng Docker](#phương-pháp-2-sử-dụng-docker)
  - [Phương pháp 3: Self-Hosting](#phương-pháp-3-self-hosting-production)
- [Hướng dẫn chơi](#-hướng-dẫn-chơi)
- [Thuật toán Minimax](#-về-thuật-toán-minimax)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)

---

---

## ✨ Tính năng

- 🎯 **3 mức độ khó:**
  - **Dễ**: AI chơi ngẫu nhiên - dễ dàng đánh bại
  - **Trung bình**: AI kết hợp 70% Minimax và 30% ngẫu nhiên
  - **Khó (Bất khả thi)**: AI sử dụng Minimax hoàn chỉnh với Alpha-Beta Pruning - gần như không thể thắng!

- 🎨 **Giao diện đẹp mắt:**
  - Modal giới thiệu dự án và tác giả
  - Hiệu ứng animation mượt mà
  - Responsive design trên mọi thiết bị (PC, tablet, mobile)
  - Custom scrollbar và gradient màu gradient

- 🎲 **Tính năng gameplay:**
  - Chọn chơi X (đi trước) hoặc O (đi sau)
  - AI random nước đầu tiên (không cố định ở giữa)
  - Highlight 3 ô thắng với animation
  - Hiển thị thống kê thắng/thua/hòa real-time
  - Nút Chơi lại, Game mới, Thông tin, Thoát

- 🔒 **Bảo mật:**
  - Rate limiting (chống DDoS)
  - Input validation và sanitization
  - Session-based game storage
  - Giới hạn số lượng game sessions (MAX_GAMES)

- ⌨️ **Phím tắt:**
  - **ESC**: Đóng modal
  - **R**: Chơi lại (khi đang chơi)

## 🛠️ Công nghệ sử dụng

### Backend
- **Python 3.11+**: Ngôn ngữ lập trình
- **Flask 3.0.0**: Web framework
- **Minimax Algorithm**: Thuật toán AI
- **Alpha-Beta Pruning**: Tối ưu hóa thuật toán

### Frontend
- **HTML5**: Cấu trúc trang web
- **CSS3**: Styling thuần (gradient, flexbox, grid, custom scrollbar)
- **JavaScript (Vanilla)**: Logic frontend, AJAX calls - không sử dụng framework

### DevOps & Deployment
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Gunicorn**: WSGI HTTP Server (production)

## 📦 Yêu cầu hệ thống

### Chạy trực tiếp (Python)
- Python 3.8+ (khuyến nghị 3.11+)
- pip (Python package manager)

### Sử dụng Docker
- Docker 20.10+
- Docker Compose 2.0+ (optional)

---

## 🚀 Cài đặt

### Phương pháp 1: Chạy trực tiếp (Python)

#### Bước 1: Clone hoặc tải về dự án
```bash
git clone <repository-url>
cd tik_tok_toe
```

#### Bước 2: Tạo virtual environment (khuyến nghị)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### Bước 3: Cài đặt dependencies
```bash
pip install -r requirements.txt
```

#### Bước 4: Chạy ứng dụng
```bash
python app.py
```

#### Bước 5: Truy cập ứng dụng
Mở trình duyệt và truy cập:
```
http://localhost:5000
```

---

### Phương pháp 2: Sử dụng Docker

#### Option A: Docker Compose (Khuyến nghị)

**Bước 1: Build và chạy**
```bash
docker-compose up -d
```

**Bước 2: Truy cập ứng dụng**
```
http://localhost:5000
```

**Bước 3: Xem logs (nếu cần)**
```bash
docker-compose logs -f
```

**Bước 4: Dừng ứng dụng**
```bash
docker-compose down
```

#### Option B: Docker (Manual)

**Bước 1: Build Docker image**
```bash
docker build -t tictactoe-game .
```

**Bước 2: Chạy container**
```bash
docker run -d -p 5000:5000 --name tictactoe tictactoe-game
```

**Bước 3: Xem logs**
```bash
docker logs -f tictactoe
```

**Bước 4: Dừng container**
```bash
docker stop tictactoe
docker rm tictactoe
```

---

### Phương pháp 3: Self-Hosting (Production)

#### Option A: Sử dụng Gunicorn (Khuyến nghị cho Production)

**Bước 1: Cài đặt Gunicorn**
```bash
pip install gunicorn
```

**Bước 2: Chạy với Gunicorn**
```bash
# 4 workers, bind to all interfaces
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

**Nâng cao: Chạy với systemd (Linux)**

Tạo file `/etc/systemd/system/tictactoe.service`:
```ini
[Unit]
Description=Tic-Tac-Toe Game Service
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/tik_tok_toe
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

**Khởi động service:**
```bash
sudo systemctl daemon-reload
sudo systemctl start tictactoe
sudo systemctl enable tictactoe
sudo systemctl status tictactoe
```

#### Option B: Sử dụng Nginx Reverse Proxy

**Bước 1: Cài đặt Nginx**
```bash
sudo apt install nginx  # Ubuntu/Debian
```

**Bước 2: Cấu hình Nginx**

Tạo file `/etc/nginx/sites-available/tictactoe`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Bước 3: Kích hoạt cấu hình**
```bash
sudo ln -s /etc/nginx/sites-available/tictactoe /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Option C: Deploy với Docker trên VPS

**Bước 1: Cài đặt Docker trên VPS**
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

**Bước 2: Clone project và chạy**
```bash
git clone <repository-url>
cd tik_tok_toe
docker-compose up -d
```

**Bước 3: Cấu hình firewall (nếu cần)**
```bash
sudo ufw allow 5000/tcp
sudo ufw reload
```

---

## 📁 Cấu trúc dự án

```
tik_tok_toe/
│
├── app.py                    # Flask application chính + Security
├── game_logic.py             # Logic game Tic-Tac-Toe
├── ai_player.py              # AI với Minimax & Alpha-Beta Pruning
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── docker-compose.yml        # Docker Compose configuration
├── .dockerignore             # Docker ignore file
├── README.md                 # Documentation (file này)
│
├── templates/
│   └── index.html           # Template HTML chính
│
└── static/
    ├── style.css            # CSS styling với responsive
    └── script.js            # JavaScript frontend logic
```

---

## 📡 API Documentation

### 1. Tạo game mới
**Endpoint:** `POST /api/new_game`

**Request Body:**
```json
{
  "difficulty": "easy|medium|hard",
  "player_symbol": "X|O"
}
```

**Response:**
```json
{
  "game_id": "1",
  "board": ["", "", "", "", "", "", "", "", ""],
  "player_symbol": "X",
  "ai_symbol": "O",
  "status": "playing"
}
```

### 2. AI đi nước đầu tiên
**Endpoint:** `POST /api/ai_first_move`

**Request Body:**
```json
{
  "game_id": "1"
}
```

**Response:**
```json
{
  "board": ["", "", "", "", "O", "", "", "", ""],
  "ai_move": 4,
  "status": "playing"
}
```

### 3. Người chơi đánh nước
**Endpoint:** `POST /api/make_move`

**Request Body:**
```json
{
  "game_id": "1",
  "position": 0
}
```

**Response (game tiếp tục):**
```json
{
  "board": ["X", "", "", "", "O", "", "", "O", ""],
  "ai_move": 7,
  "status": "playing"
}
```

**Response (game kết thúc):**
```json
{
  "board": ["X", "X", "X", "O", "O", "", "", "", ""],
  "winner": "X",
  "winning_line": [0, 1, 2],
  "status": "finished"
}
```

### 4. Reset game
**Endpoint:** `POST /api/reset_game/<game_id>`

**Response:**
```json
{
  "board": ["", "", "", "", "", "", "", "", ""],
  "status": "playing"
}
```

---

## 🎮 Hướng dẫn chơi

1. **Chọn độ khó** (Dễ / Trung bình / Khó)
2. **Chọn người chơi:**
   - **X (Đi trước)**: Màu xanh - bạn đi nước đầu tiên
   - **O (Đi sau)**: Màu đỏ - AI đi nước đầu tiên (ngẫu nhiên)
3. **Nhấn "BẮT ĐẦU CHƠI"**
4. **Click vào ô** trên bàn cờ để đánh dấu
5. **Mục tiêu**: Tạo thành hàng ngang, dọc hoặc chéo với 3 ký hiệu giống nhau
6. **Kết quả**:
   - 🎉 **Thắng**: Bạn tạo được 3 ký hiệu liên tiếp
   - 😢 **Thua**: AI tạo được 3 ký hiệu liên tiếp
   - 🤝 **Hòa**: Bảng đầy mà không ai thắng
7. **Chơi tiếp**: Nhấn "Chơi lại" hoặc "Game mới"

---

## 🧠 Về thuật toán Minimax

### Minimax là gì?

Minimax là một thuật toán đệ quy được sử dụng trong lý thuyết trò chơi và AI để tìm nước đi tối ưu:

- **Maximizer (AI)**: Cố gắng **tối đa hóa** điểm số
- **Minimizer (Người chơi)**: Cố gắng **tối thiểu hóa** điểm số của AI

### Alpha-Beta Pruning

Kỹ thuật tối ưu hóa giúp giảm số lượng nút cần đánh giá trong cây trò chơi:
- **Alpha (α)**: Điểm tốt nhất tìm được cho Maximizer
- **Beta (β)**: Điểm tốt nhất tìm được cho Minimizer
- **Pruning**: Bỏ qua các nhánh không thể mang lại kết quả tốt hơn

### Cách hoạt động trong game

#### Độ khó Dễ:
- AI chọn nước đi **ngẫu nhiên**
- Không sử dụng Minimax
- Thời gian: < 1ms

#### Độ khó Trung bình:
- **70% Minimax** + 30% ngẫu nhiên
- Độ sâu giới hạn để tăng tốc
- Thời gian: ~50-100ms

#### Độ khó Khó (Bất khả thi):
- **Minimax đầy đủ** với Alpha-Beta Pruning
- Đánh giá tất cả nước đi có thể
- AI **không bao giờ thua** - chỉ thắng hoặc hòa
- Thời gian: ~200-500ms (nước đầu tiên)

### Công thức đánh giá
```python
AI thắng:        +10 - depth  # Ưu tiên thắng nhanh
Người thắng:     -10 + depth  # Ưu tiên thua chậm
Hòa:             0
```

---

## 🔐 Bảo mật

### Các biện pháp bảo mật đã triển khai:

1. **Rate Limiting**
   - Giới hạn 50 requests/60s cho `/api/new_game`
   - Giới hạn 100 requests/60s cho `/api/make_move`
   - Chống DDoS attacks

2. **Input Validation**
   - Kiểm tra `difficulty` chỉ nhận `easy`, `medium`, `hard`
   - Kiểm tra `player_symbol` chỉ nhận `X`, `O`
   - Kiểm tra `position` phải là số từ 0-8
   - Kiểm tra `game_id` tồn tại

3. **Session Management**
   - Session-based game storage
   - Tự động xóa old sessions khi đạt MAX_GAMES (1000)
   - Mỗi game độc lập, không ảnh hưởng lẫn nhau

4. **Error Handling**
   - Try-except blocks cho tất cả API endpoints
   - Trả về error messages rõ ràng
   - Không expose sensitive information

---

## � Troubleshooting

### Lỗi: "ModuleNotFoundError: No module named 'flask'"
**Giải pháp:**
```bash
pip install -r requirements.txt
```

### Lỗi: "Address already in use" (Port 5000)
**Giải pháp 1:** Tìm và kill process đang dùng port
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

**Giải pháp 2:** Đổi port trong `app.py`
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Docker container không start
**Kiểm tra logs:**
```bash
docker-compose logs
```

**Rebuild image:**
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Game chậm ở độ khó "Khó"
**Đây là bình thường:**
- Minimax cần tính toán nhiều trạng thái (~5,000-20,000)
- Nước đầu tiên chậm nhất (~500ms)
- Các nước tiếp theo nhanh hơn do pruning

### Cannot connect to server
**Kiểm tra:**
1. Server đang chạy: `ps aux | grep python` hoặc `docker ps`
2. Port đúng: `5000`
3. Firewall không block port
4. Truy cập đúng URL: `http://localhost:5000`

---

## 📊 Performance

### Minimax với Alpha-Beta Pruning trên bàn cờ 3x3:

| Độ khó | Thuật toán | Avg Time | States Evaluated |
|--------|-----------|----------|------------------|
| Dễ | Random | < 1ms | 1 |
| Trung bình | Minimax Limited | ~50ms | ~500-1,000 |
| Khó | Full Minimax + Pruning | ~200-500ms | ~5,000-20,000 |

**Lưu ý:** Alpha-Beta Pruning giảm ~50-70% số states cần đánh giá so với Minimax thuần.

---

## 🎓 Học từ dự án này

Dự án này là ví dụ tốt để học:

- ✅ **Python & Flask**: Backend web development, RESTful API
- ✅ **Vanilla JavaScript**: Frontend development không framework
- ✅ **Algorithms**: Minimax, Alpha-Beta Pruning, Game Theory
- ✅ **Security**: Rate limiting, input validation, CSRF protection
- ✅ **DevOps**: Docker, Docker Compose, deployment
- ✅ **UI/UX**: Responsive design, animations, user experience
- ✅ **Clean Code**: Modular architecture, separation of concerns

---

## 💡 Ý tưởng mở rộng

- [ ] Multiplayer mode (chơi online với người khác qua WebSocket)
- [ ] Lưu trữ thống kê vào database (PostgreSQL/MongoDB)
- [ ] Leaderboard system
- [ ] Game replay với animation
- [ ] Bàn cờ 4x4 hoặc 5x5
- [ ] Dark mode theme
- [ ] Mobile app (React Native/Flutter)
---

## 👨‍💻 Tác giả

**Kỹ sư Nguyễn Minh Phúc**  
*DevSecOps & Infrastructure Engineer*

- GitHub: [https://github.com/csenguyenminhphuc](https://github.com/csenguyenminhphuc)
- Dự án: Được xây dựng hoàn toàn từ đầu, không sử dụng template

---

## 📄 License

Dự án này là open-source cho mục đích giáo dục và học tập.

---

## � Lời cảm ơn

Dự án này được phát triển như một phần của môn **Nhập môn Trí tuệ nhân tạo**, vận dụng kiến thức về:
- Thuật toán tìm kiếm
- Game theory
- Heuristic evaluation
- Alpha-Beta Pruning

---

**Chúc bạn chơi game vui vẻ! 🎮✨**