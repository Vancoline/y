# Hướng Dẫn Nhanh - Trắc Nghiệm Ngành Nghề

## 🚀 Bắt Đầu Nhanh (5 phút)

### 1. Cài Đặt
```bash
cd /workspaces/y/career_quiz
pip install -r requirements.txt
python init_db.py
python app.py
```

### 2. Truy Cập
- Mở trình duyệt: **http://localhost:5000**

### 3. Tài Khoản Demo
- **Người dùng thường**: Tự đăng ký
- **Admin**: 
  - Username: `admin`
  - Password: `admin123`

---

## 📚 Các Chức Năng Chính

### 👤 Cho Người Dùng
- ✅ Đăng ký tài khoản
- ✅ Làm bài trắc nghiệm 10 câu hỏi (ngẫu nhiên từ 60 ngành)
- ✅ Xem kết quả tức thì với phần trăm chính xác
- ✅ Xem lịch sử các bài làm trước

### 🔐 Cho Admin
- 👨‍💼 Xem danh sách tất cả người dùng
- 📊 Xem điểm số và thống kê
- 🔍 Chi tiết câu trả lời từng người dùng (đúng/sai)
- 📈 Phân tích kết quả

---

## 🌐 Các Ngành Nghề Bao Gồm

60 ngành nghề phổ biến tại Việt Nam bao gồm:
- Kỹ sư phần mềm
- Bác sĩ
- Giáo viên
- Luật sư
- Marketing
- Kỹ sư xây dựng
- Và 54 ngành khác...

---

## 📁 Cấu Trúc Thư Mục

```
career_quiz/
├── app.py                 # Ứng dụng chính
├── init_db.py            # Script khởi tạo DB
├── professions_data.py    # Dữ liệu 60 ngành
├── requirements.txt       # Packages cần thiết
├── templates/            # HTML files
├── static/
│   ├── css/style.css
│   └── js/
│       ├── main.js
│       ├── quiz.js
│       ├── results.js
│       └── admin.js
└── career_quiz.db        # Database
```

---

## 🔧 Khắc Phục Sự Cố

### ❌ Lỗi: "Port 5000 đang được sử dụng"
```bash
# Tìm và dừng tiến trình
lsof -i :5000
kill -9 <PID>

# Hoặc chạy trên port khác
# Sửa app.py: app.run(port=5001)
```

### ❌ Lỗi: "Module not found"
```bash
pip install --upgrade -r requirements.txt
```

### ❌ Lỗi: "Database error"
```bash
rm career_quiz.db
python init_db.py
```

---

## 📱 API Endpoints (Dev Only)

| Phương Thức | Endpoint | Mô Tả |
|-----------|----------|-------|
| POST | `/login` | Đăng nhập |
| POST | `/register` | Đăng ký |
| GET | `/logout` | Đăng xuất |
| GET | `/api/quiz/questions` | Lấy 10 câu hỏi |
| POST | `/api/quiz/submit` | Nộp bài |
| GET | `/api/quiz/result/<id>` | Xem kết quả |
| GET | `/api/admin/dashboard` | Bảng điều khiển |

---

## 🔒 Bảo Mật

⚠️ **Cảnh báo**: Ứng dụng này dùng cho mục đích demo/phát triển

Trước khi triển khai sản xuất:
- [ ] Thay đổi mật khẩu admin
- [ ] Thay SECRET_KEY
- [ ] Sử dụng HTTPS
- [ ] Hash mật khẩu (bcrypt)
- [ ] Sử dụng database sản xuất (PostgreSQL)

---

## 🎯 Chế Độ Quiz

Mỗi lần trắc nghiệm:
- **10 câu hỏi** ngẫu nhiên
- **Lấy từ 60 ngành nghề** khác nhau
- **Mỗi câu 4 lựa chọn** (A, B, C, D)
- **Kết quả tức thì** sau khi nộp bài

---

## 📊 Bảng Điều Khiển Admin

1. Truy cập: `/admin`
2. Xem:
   - Tổng số người dùng
   - Số lần làm bài của mỗi người
   - Điểm mới nhất và trung bình
   - Chi tiết từng câu trả lời

---

## 🚀 Triển Khai Sản Xuất

```bash
# Cài Gunicorn
pip install gunicorn

# Chạy ứng dụng
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Hoặc sử dụng Nginx + Gunicorn
# (Xem tài liệu chi tiết trong README_VI.md)
```

---

## 💡 Mẹo Sử Dụng

1. **Test Admin**: Đăng nhập bằng admin để thấy analytics
2. **Reset Database**: Xóa `career_quiz.db` rồi chạy `init_db.py`
3. **Debug Mode**: Đã bật, tự động reload khi thay đổi code
4. **Database**: SQLite, xem với `sqlite3 career_quiz.db`

---

## 📞 Liên Hệ Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra yêu cầu: `pip list`
2. Xóa DB: `rm career_quiz.db`
3. Khởi tạo lại: `python init_db.py`
4. Chạy: `python app.py`

---

## 📝 Ghi Chú

- ✅ Hỗ trợ tiếng Việt đầy đủ
- ✅ Responsive design (mobile-friendly)
- ✅ Không cần JavaScript framework ngoài
- ✅ Database tự tạo
- ✅ Admin dashboard tích hợp

---

**Phiên bản**: 1.0  
**Cập nhật lần cuối**: 2024-12-09  
**License**: MIT
