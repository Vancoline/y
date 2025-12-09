# 📚 Trang Chỉ Mục - Ứng Dụng Trắc Nghiệm Ngành Nghề

## 🎯 Bắt Đầu Nhanh

Nếu bạn muốn chạy ứng dụng ngay lập tức, hãy xem:
- 📖 **[QUICK_START.md](./QUICK_START.md)** - Hướng dẫn 5 phút

## 📋 Tài Liệu Chi Tiết

### Tiếng Việt
- 📖 **[README_VI.md](./README_VI.md)** - Tài liệu đầy đủ (600+ dòng)
- ✅ **[HOÀN_TẤT.md](./HOÀN_TẤT.md)** - Tóm tắt dự án

### English
- 📖 **[SUMMARY.md](./SUMMARY.md)** - Project summary

## 🗂️ Cấu Trúc File

```
career_quiz/
├── 🎯 QUICK_START.md         ← BẮT ĐẦU TỪ ĐÂY!
├── 📖 README_VI.md           ← Tài liệu chi tiết (VN)
├── ✅ HOÀN_TẤT.md            ← Tóm tắt dự án
├── 📖 SUMMARY.md             ← Summary (EN)
│
├── 🔧 Tệp Cấu Hình
│   ├── app.py                # Flask ứng dụng chính
│   ├── requirements.txt      # Python packages
│   ├── init_db.py           # Khởi tạo database
│   └── professions_data.py  # Dữ liệu 60 ngành
│
├── 🎨 HTML Templates (templates/)
│   ├── index.html           # Trang chủ
│   ├── login.html           # Đăng nhập
│   ├── register.html        # Đăng ký
│   ├── quiz.html            # Bài trắc nghiệm
│   ├── results.html         # Kết quả
│   ├── admin.html           # Bảng điều khiển
│   └── admin_login.html     # Đăng nhập admin
│
├── 🎨 CSS & JavaScript (static/)
│   ├── css/style.css        # CSS toàn bộ ứng dụng
│   └── js/
│       ├── main.js          # Navigation chung
│       ├── quiz.js          # Logic quiz
│       ├── results.js       # Hiển thị kết quả
│       └── admin.js         # Admin functions
│
└── 💾 Database
    └── career_quiz.db       # SQLite (tự tạo)
```

## 🚀 Hướng Dẫn Cài Đặt

### 1️⃣ Cài Đặt Dependencies
```bash
cd /workspaces/y/career_quiz
pip install -r requirements.txt
```

### 2️⃣ Khởi Tạo Database
```bash
python init_db.py
```

### 3️⃣ Chạy Ứng Dụng
```bash
python app.py
```

### 4️⃣ Truy Cập
Mở trình duyệt: **http://localhost:5000**

## 👤 Tài Khoản Demo

| Loại | Username | Password |
|------|----------|----------|
| Admin | `admin` | `admin123` |
| User | Tự đăng ký | Tùy ý |

## 📚 Đọc Gì Tiếp?

1. **Muốn chạy ngay?** → [QUICK_START.md](./QUICK_START.md)
2. **Muốn biết chi tiết?** → [README_VI.md](./README_VI.md)
3. **Muốn tóm tắt?** → [HOÀN_TẤT.md](./HOÀN_TẤT.md)
4. **Là lập trình viên?** → [SUMMARY.md](./SUMMARY.md)

## ✨ Tính Năng Chính

### 👥 Người Dùng
- ✅ Đăng ký/Đăng nhập
- ✅ Làm bài quiz 10 câu
- ✅ Xem kết quả chi tiết
- ✅ Xem lịch sử bài làm

### 🔐 Admin
- ✅ Xem tất cả người dùng
- ✅ Xem thống kê điểm
- ✅ Chi tiết câu trả lời
- ✅ Phân tích kết quả

## 🎓 60 Ngành Nghề

Bao gồm:
- 📱 IT/Công nghệ (Lập trình viên, KS phần mềm, etc)
- 🏥 Y tế (Bác sĩ, Y tá, Dược sĩ, etc)
- 🎓 Giáo dục (Giáo viên, Nhà báo)
- 💰 Kinh tế (Kế toán, Marketing, etc)
- 🔧 Kỹ thuật (KS xây dựng, điện, cơ khí, etc)
- ⚖️ Pháp luật (Luật sư, Chuyên viên pháp lý)
- 🍽️ Dịch vụ (Đầu bếp, Du lịch, Bán lẻ, etc)
- ... và nhiều ngành khác!

## 🔧 Công Nghệ

- **Backend**: Flask 2.3, SQLAlchemy 2.0
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Server**: Flask dev (production: Gunicorn)

## 📊 Thống Kê Dự Án

| Metric | Số Lượng |
|--------|----------|
| Python code | 400+ lines |
| HTML files | 7 files |
| CSS code | 600+ lines |
| JavaScript | 400+ lines |
| Professions | 60 |
| Questions | 60 |
| Database tables | 5 |
| API endpoints | 12+ |

## ⚠️ Lưu Ý Bảo Mật

⚠️ **Đây là phiên bản DEMO**

Trước khi triển khai sản xuất:
- Thay đổi mật khẩu admin
- Sử dụng HTTPS
- Hash mật khẩu (bcrypt)
- Dùng database sản xuất (PostgreSQL)
- Tắt debug mode

## 🐛 Khắc Phục Sự Cố

### Cổng 5000 đang sử dụng
```bash
lsof -i :5000
kill -9 <PID>
```

### Lỗi Database
```bash
rm career_quiz.db
python init_db.py
```

### Module không tìm thấy
```bash
pip install --upgrade -r requirements.txt
```

## 📞 Liên Hệ & Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra Python/pip: `python --version` & `pip --version`
2. Cài lại packages: `pip install -r requirements.txt`
3. Xóa DB: `rm career_quiz.db`
4. Khởi tạo: `python init_db.py`
5. Chạy: `python app.py`

## 🎯 Các Bước Tiếp Theo

1. ✅ Cài đặt dependencies
2. ✅ Khởi tạo database
3. ✅ Chạy ứng dụng
4. ✅ Truy cập http://localhost:5000
5. ✅ Đăng ký & làm bài quiz
6. ✅ Đăng nhập admin xem kết quả

## 📝 Ghi Chú

- ✅ Hỗ trợ tiếng Việt 100%
- ✅ Responsive (mobile-friendly)
- ✅ Không cần framework JS ngoài
- ✅ Database tự tạo
- ✅ Admin dashboard tích hợp
- ✅ Tài liệu đầy đủ

## 🎉 Status

```
✅ Phát triển hoàn tất
✅ Database khởi tạo thành công
✅ Server chạy tốt
✅ Tất cả tính năng hoạt động
✅ Tài liệu đầy đủ
🚀 SẴN DÙNG NGAY!
```

---

## 📖 Chọn Tài Liệu Phù Hợp

### Bạn là:
- **👨‍💻 Lập trình viên muốn hiểu code** → [SUMMARY.md](./SUMMARY.md) (English)
- **🚀 Người muốn chạy ngay** → [QUICK_START.md](./QUICK_START.md)
- **📚 Người muốn tài liệu chi tiết** → [README_VI.md](./README_VI.md)
- **✅ Người muốn tóm tắt nhanh** → [HOÀN_TẤT.md](./HOÀN_TẤT.md)

---

**Bản phát hành**: 1.0  
**Ngày tạo**: 2024-12-09  
**License**: MIT

🎉 **Chúc bạn sử dụng vui vẻ!**
