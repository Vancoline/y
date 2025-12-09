# Hướng Dẫn Deploy Lên Vercel

## 📋 Yêu Cầu

- GitHub account (repository đã được push)
- Vercel account (https://vercel.com)

## 🚀 Các Bước Deploy

### 1. Đăng Nhập Vercel
```bash
# Truy cập https://vercel.com
# Đăng nhập hoặc đăng ký (có thể dùng GitHub)
```

### 2. Tạo Dự Án Mới
- Nhấp **"New Project"**
- Chọn repository `y` từ GitHub
- Hoặc import từ git

### 3. Cấu Hình Dự Án

**Root Directory**: `career_quiz`

**Build Command**: 
```
pip install -r requirements.txt
```

**Start Command**:
```
gunicorn app:app
```

**Environment Variables** (tùy chọn):
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### 4. Deploy
- Nhấp **"Deploy"**
- Chờ deployment hoàn tất (2-5 phút)
- Vercel sẽ tạo URL cho ứng dụng

## ⚠️ Lưu Ý Quan Trọng

### Database
- Vercel filesystem là **ephemeral** (tạm thời)
- **SQLite không phù hợp** cho production
- **Cần dùng**: PostgreSQL, MongoDB, hoặc database khác

### Giải Pháp Database

#### A. Sử Dụng PostgreSQL (Khuyên dùng)

**Cài đặt driver:**
```bash
pip install psycopg2-binary
```

**Sửa app.py:**
```python
import os

# Kiểm tra môi trường
if os.getenv('DATABASE_URL'):
    # Production: PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    # Development: SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///career_quiz.db'
```

**Các dịch vụ PostgreSQL miễn phí:**
- **Vercel Storage** (Postgres)
- **Railway** 
- **Render**
- **Supabase**

#### B. Sử Dụng Vercel KV/Blob (Nếu không cần relational DB)

#### C. Sử Dụng Firebase Realtime Database

### Ghi Chú Bảo Mật

1. **Thay đổi SECRET_KEY** - Không sử dụng default
2. **Thêm environment variables** trong Vercel dashboard:
   - `SECRET_KEY`
   - `DATABASE_URL` (nếu dùng PostgreSQL)
   - `FLASK_ENV=production`
3. **Bật HTTPS** - Tự động với Vercel
4. **Hash mật khẩu** - Nâng cấp bảo mật trong future

## 📊 Quy Trình Deploy Chi Tiết

### Bước 1: Chuẩn Bị
```bash
# Kiểm tra mọi thứ đã được commit
git status

# Nếu có thay đổi
git add -A
git commit -m "Prepare for Vercel deployment"
git push
```

### Bước 2: Tạo Dự Án Trên Vercel
1. Vào https://vercel.com/dashboard
2. Nhấp **"New Project"**
3. Kết nối GitHub account
4. Chọn repository `y`

### Bước 3: Cấu Hình Dự Án
```
Project Name: career-quiz (hoặc tên khác)
Framework Preset: Other
Root Directory: career_quiz
```

### Bước 4: Build Settings
```
Build Command: pip install -r requirements.txt
Output Directory: (để trống)
Install Command: pip install -r requirements.txt
```

### Bước 5: Environment Variables
Thêm trong **Settings → Environment Variables**:
```
SECRET_KEY = your-very-secret-key-here
FLASK_ENV = production
```

### Bước 6: Deploy
- Nhấp **"Deploy"**
- Chờ build hoàn tất

### Bước 7: Kiểm Tra
- Vercel sẽ cung cấp URL (vd: https://career-quiz.vercel.app)
- Truy cập URL để kiểm tra
- Xem logs nếu gặp lỗi

## 🔧 Khắc Phục Sự Cố

### Error: "500 Internal Server Error"

**Kiểm tra logs:**
1. Vào Vercel Dashboard
2. Chọn dự án
3. Xem **"Deployments"** → **"Logs"**

**Nguyên nhân phổ biến:**
- Database không khả dụng
- Missing environment variables
- Module import error

### Error: "WSGI application not found"

Đảm bảo file `vercel.json` đúng:
```json
{
  "version": 2,
  "builds": [{"src": "app.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "app.py"}]
}
```

### Database Connection Error

**Giải pháp:**
1. Kiểm tra DATABASE_URL đúng
2. Thêm `-sslmode=require` nếu dùng PostgreSQL
3. Kiểm tra firewall/IP whitelist

## 📱 Testing Trên Production

```bash
# Sau khi deploy, test các feature:
# 1. Trang chủ
# 2. Đăng ký & đăng nhập
# 3. Trắc nghiệm
# 4. Xem kết quả
# 5. Admin dashboard
```

## 🔄 Update Code

Mỗi khi push code lên GitHub, Vercel tự động deploy:

```bash
# Sửa code
git add -A
git commit -m "Fix: issue description"
git push origin main

# Vercel sẽ tự động deploy
# Kiểm tra status trong Vercel Dashboard
```

## 💡 Tips

1. **Preview URLs** - Mỗi PR sẽ có preview URL
2. **Rollback** - Có thể rollback về version trước
3. **Custom Domain** - Có thể gắn domain riêng
4. **Analytics** - Xem traffic và performance
5. **Serverless Functions** - Tối ưu hóa cho serverless

## 📚 Tài Liệu Thêm

- [Vercel Python Guide](https://vercel.com/docs/functions/python)
- [Flask + Vercel](https://vercel.com/guides/deploying-a-flask-app)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

## 🎯 Tiếp Theo

Sau khi deploy thành công:

1. **Cấu hình Database** (PostgreSQL/MongoDB)
2. **Thêm Custom Domain**
3. **Set Up CI/CD**
4. **Monitoring & Logging**
5. **Performance Optimization**

---

**Vercel URL sẽ ở dạng**: `https://your-project-name.vercel.app`

🚀 **Chúc deploy thành công!**
