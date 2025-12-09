# Hướng Dẫn Deploy Trên Render

## 🚀 Lợi Ích Của Render

- ✅ Hỗ trợ PostgreSQL free
- ✅ Deploy từ GitHub tự động
- ✅ HTTPS miễn phí
- ✅ Custom domain
- ✅ Không cần credit card cho free tier

## 📋 Bước 1: Tạo Database PostgreSQL Trên Render

### 1.1 Đăng ký / Đăng nhập
- Vào https://render.com
- Click "Sign up" hoặc "Sign in"
- Chọn "GitHub" để dễ dàng

### 1.2 Tạo PostgreSQL Database
1. Trên dashboard, click **"New +"** → **"PostgreSQL"**
2. Điền thông tin:
   - **Name**: `career-quiz-db`
   - **Database**: `career_quiz`
   - **User**: `career_user`
   - **Region**: Chọn gần nhất (VN → Singapore)
   - **PostgreSQL Version**: Latest (15.x)
3. Chọn **Free Plan** (tính từ 90 ngày sử dụng miễn phí)
4. Click **"Create Database"**

### 1.3 Lấy Connection String
- Đợi database tạo xong (2-3 phút)
- Vào phần "Connections"
- Copy **"Internal Database URL"** hoặc **"External Database URL"**
- Ví dụ:
  ```
  postgresql://career_user:password@dpg-xxxx.render.internal/career_quiz
  ```

**💾 Lưu connection string này!**

---

## 📋 Bước 2: Deploy Web Service Trên Render

### 2.1 Tạo Web Service
1. Vào https://render.com/dashboard
2. Click **"New +"** → **"Web Service"**
3. Chọn **"Deploy an existing Git repository"**
   - Nếu chưa kết nối GitHub: Click "Connect account"
4. Chọn repository **"y"**
5. Chọn branch: **"main"**

### 2.2 Cấu Hình Web Service

Điền các thông tin sau:

| Trường | Giá Trị |
|--------|---------|
| **Name** | `career-quiz-app` |
| **Root Directory** | `career_quiz` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt && python init_db.py` |
| **Start Command** | `gunicorn wsgi:app` |
| **Plan** | **Free** |

### 2.3 Thêm Environment Variables

Click **"Add Environment Variable"** và thêm:

```
SECRET_KEY = your-very-secret-key-here-min-32-chars

FLASK_ENV = production

DATABASE_URL = (paste connection string từ bước 1.3)

PORT = 10000
```

**Ví dụ DATABASE_URL:**
```
postgresql://career_user:xxxxxxxxx@dpg-xxxx.render.internal/career_quiz
```

### 2.4 Deploy
- Click **"Create Web Service"**
- Render sẽ:
  1. Clone repository từ GitHub
  2. Cài đặt dependencies (pip install)
  3. Chạy build command (init_db.py)
  4. Khởi động app với gunicorn
  5. Cấp URL tự động

**⏳ Chờ 2-5 phút cho deployment hoàn tất**

---

## 🔗 Lấy URL Render

Sau khi deploy thành công:
- URL sẽ có dạng: `https://career-quiz-app.render.com`
- Hiển thị trên dashboard Render
- Tự động HTTPS

---

## 🔄 Auto-Deploy Từ GitHub

Render sẽ **tự động deploy** khi bạn push lên GitHub:

```bash
# Mỗi lần push → Render tự động deploy
git add -A
git commit -m "Update app"
git push origin main
```

Xem logs deployment: Dashboard Render → Select Web Service → "Logs"

---

## 📝 File Cấu Hình Render

Render sẽ tự động detect từ file cấu hình:

### Procfile
```
web: gunicorn wsgi:app
```

### requirements.txt
```
Flask==2.3.0
Flask-SQLAlchemy==3.0.5
SQLAlchemy==2.0.0
gunicorn==21.2.0
python-dotenv==1.0.0
psycopg2-binary==2.9.9
```

### build.sh (nếu cần custom build)
```bash
#!/bin/bash
pip install -r requirements.txt
python init_db.py
```

---

## ✅ Kiểm Tra Sau Deploy

```bash
# 1. Vào trang chủ app
https://career-quiz-app.render.com

# 2. Đăng ký tài khoản
# 3. Thử làm quiz
# 4. Đăng nhập admin (admin / admin123)
# 5. Xem kết quả
```

---

## 🚨 Khắc Phục Lỗi

### Error: Database connection failed
```
❌ FATAL: Ident authentication failed
❌ no password supplied

✅ Kiểm tra:
  - DATABASE_URL format đúng không?
  - Copy cả password từ Render dashboard
```

### Error: 500 Internal Server Error
```bash
# Xem logs Render
1. Render Dashboard → Select service → "Logs"
2. Kiểm tra error message
3. Phổ biến: DATABASE_URL không đúng
```

### Error: Module not found
```
❌ ModuleNotFoundError: No module named 'flask'

✅ Kiểm tra:
  - requirements.txt có đầy đủ packages?
  - Build command chạy pip install?
```

### Error: Port already in use
```
❌ Address already in use

✅ Render sẽ tự động gán PORT
  - Không cần chỉ định cứng port 5000
  - app.py đã support PORT từ env
```

---

## 🔐 Bảo Mật

### Thay Đổi Admin Password

1. **Cách 1: Qua Database**
   ```bash
   # SSH vào Render (nếu enable)
   # Hoặc dùng Render CLI
   ```

2. **Cách 2: Tạo Admin Mới**
   - Đăng nhập với admin/admin123
   - Tạo user mới, cấp quyền admin
   - Xóa tài khoản admin mặc định

3. **Cách 3: Reset Database**
   - Xóa database cũ
   - Tạo database mới
   - Render auto re-deploy

### Bảo Mật SECRET_KEY
- ✅ Dùng key ngẫu nhiên dài >= 32 ký tự
- ✅ Không chia sẻ key trong code
- ✅ Lưu trữ trong Environment Variables Render

---

## 📊 Database Storage

Render cung cấp:
- **Free Plan**: 256 MB database
- **PostgreSQL 15**: Latest version
- **Backup tự động**: 7 ngày
- **Nâng cấp**: Tính phí theo usage

---

## 🔄 Cập Nhật Code

Mỗi khi update code:

```bash
cd /workspaces/y

# Sửa code
# ... edit app.py, templates, etc ...

# Commit và push
git add -A
git commit -m "Update features"
git push origin main

# Render tự động deploy
# Xem logs: Dashboard → Select service → Logs
```

---

## 📈 Monitoring & Logs

### Xem Logs Real-time
- Dashboard Render → Select Web Service
- Tab **"Logs"** → Xem output
- Auto-refresh mỗi vài giây

### Kiểm Tra Health
- Dashboard → Service
- Status: "Live" = OK
- Status: "Deploying" = Đang cập nhật
- Status: "Failed" = Có lỗi

---

## 💡 Tips & Tricks

### 1. Custom Domain
```
1. Dashboard → Select service → Settings
2. "Custom Domain"
3. Thêm domain (example.com)
4. Update DNS records
5. Render cấp SSL tự động
```

### 2. Environment Variables Thay Đổi
```
1. Dashboard → Environment
2. Edit biến
3. Render tự động re-deploy
```

### 3. Xóa Deployment
```
1. Dashboard → Select service
2. Settings → "Delete Web Service"
3. Confirm xóa
```

### 4. Rollback Deployment
```
1. Dashboard → Deployments
2. Chọn deployment cũ
3. Click "Redeploy"
```

---

## 🎯 Quy Trình Deployment Hoàn Chỉnh

### Lần Đầu Tiên:
1. ✅ Tạo PostgreSQL database trên Render
2. ✅ Lấy connection string
3. ✅ Tạo Web Service trên Render
4. ✅ Thêm Environment Variables (DATABASE_URL, SECRET_KEY, FLASK_ENV)
5. ✅ Chờ deployment hoàn tất (2-5 phút)
6. ✅ Test app trên `https://career-quiz-app.render.com`

### Lần Tiếp Theo:
1. ✅ Sửa code
2. ✅ `git push origin main`
3. ✅ Render tự động deploy
4. ✅ Kiểm tra logs

---

## 📚 Tài Liệu Tham Khảo

- [Render Flask Guide](https://render.com/docs/deploy-flask)
- [Render PostgreSQL](https://render.com/docs/databases)
- [Render Environment Variables](https://render.com/docs/environment-variables)

---

## 🎉 Hoàn Tất

Sau deployment thành công trên Render:

✅ App chạy tại: `https://career-quiz-app.render.com`  
✅ Database: PostgreSQL 256MB  
✅ HTTPS: Tự động SSL  
✅ Auto-deploy từ GitHub  
✅ Free tier: Miễn phí 90 ngày  

🚀 **Happy deploying on Render!**

---

## ❓ Câu Hỏi Thường Gặp

**Q: Render có giống Vercel không?**
A: Khác nhau - Render tốt hơn cho web services, Vercel tốt hơn cho serverless. Render hỗ trợ database free.

**Q: Có thể dùng SQLite trên Render không?**
A: Không khuyến khích - filesystem Render tạm thời. Dùng PostgreSQL tốt hơn.

**Q: Database sẽ mất khi tắt máy không?**
A: Không - PostgreSQL trên Render là managed service, persistent.

**Q: Bao lâu thì database hết bộ nhớ?**
A: Free tier có 256MB - đủ cho hàng ngàn users. Có thể upgrade sau.

**Q: Làm sao để backup database?**
A: Render tự động backup 7 ngày. Hoặc export manual từ Render dashboard.

---

**Nếu gặp vấn đề:**
1. Xem logs Render dashboard
2. Kiểm tra Environment Variables
3. Kiểm tra DATABASE_URL format
4. Tính xem requirements.txt có đầy đủ không
5. Contact Render support: https://render.com/support
