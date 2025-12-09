# Các Lệnh Để Chạy Trên Vercel

## 🚀 Lệnh Deployment Vercel

### 1. Install Vercel CLI (Local)
```bash
npm install -g vercel
```

### 2. Deploy từ Local
```bash
cd /workspaces/y/career_quiz

# Lần đầu tiên
vercel

# Hoặc
vercel deploy

# Deploy và set production
vercel deploy --prod
```

### 3. Link với GitHub Repository (Tự động deploy)
```bash
vercel link
# Sau đó mỗi lần push lên GitHub, Vercel tự động deploy
```

## 📋 Các Biến Môi Trường (Environment Variables) Cần Thiết

Trong Vercel Dashboard → Settings → Environment Variables, thêm:

```
SECRET_KEY = your-very-secret-key-here
FLASK_ENV = production
DATABASE_URL = postgresql://... (nếu sử dụng PostgreSQL)
```

### Ví Dụ DATABASE_URL:
```
postgresql://username:password@host:5432/dbname?sslmode=require
```

## 🏗️ Build Command

Vercel sẽ tự động detect Flask. Nếu cần cấu hình thủ công:

```
Build Command: pip install -r requirements.txt
Start Command: gunicorn wsgi:app
```

## 📁 Project Root

```
Root Directory: career_quiz
```

## 🔧 Cấu Hình Chi Tiết

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "wsgi.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "wsgi.py"
    }
  ]
}
```

### wsgi.py (Entry Point)
```python
from app import app

if __name__ == "__main__":
    app.run()
```

## 🎯 Quy Trình Deployment Chi Tiết

### Bước 1: Chuẩn Bị Code
```bash
# Commit tất cả thay đổi
git add -A
git commit -m "Prepare for Vercel deployment"
git push origin main
```

### Bước 2: Cấu Hình Database (QUAN TRỌNG!)

**Vercel không hỗ trợ SQLite** (filesystem tạm thời)

**Chọn một trong các tuỳ chọn:**

#### A. Vercel Postgres (Khuyên dùng)
```bash
# CLI
vercel env add DATABASE_URL

# Paste: postgresql://... (từ Vercel Storage)
```

#### B. Railway
```
1. Vào https://railway.app
2. Tạo database PostgreSQL
3. Copy connection string
4. Thêm vào Vercel env
```

#### C. Render
```
1. Vào https://render.com
2. Tạo PostgreSQL database
3. Copy connection string
4. Thêm vào Vercel env
```

#### D. Supabase
```
1. Vào https://supabase.com
2. Tạo project
3. Copy connection string
4. Thêm vào Vercel env
```

### Bước 3: Tạo Dự Án Trên Vercel

**Cách 1: Qua Dashboard**
```
1. https://vercel.com/dashboard
2. New Project
3. Import Git Repository
4. Chọn repository "y"
5. Configure:
   - Root Directory: career_quiz
   - Build: pip install -r requirements.txt
   - Environment: Thêm DATABASE_URL
6. Deploy
```

**Cách 2: Qua CLI**
```bash
vercel deploy --prod
```

### Bước 4: Kiểm Tra Deployment

```bash
# Xem status
vercel status

# Xem logs
vercel logs

# Xem URL
vercel inspect
```

## 🔍 Debug Trên Vercel

### Xem Logs Real-time
```bash
vercel logs --follow
```

### Xem Build Output
```bash
vercel list          # Xem deployments
vercel inspect [url] # Chi tiết deployment
```

## 📊 File Cấu Hình Vercel

| File | Mục Đích |
|------|---------|
| **vercel.json** | Cấu hình build & routes |
| **wsgi.py** | Entry point WSGI |
| **Procfile** | Production process |
| **runtime.txt** | Python version |
| **.vercelignore** | Files loại trừ |

## ✅ Kiểm Tra Trước Deploy

```bash
# 1. Test locally
python app.py

# 2. Test WSGI
gunicorn wsgi:app

# 3. Kiểm tra requirements
pip install -r requirements.txt

# 4. Kiểm tra database
python init_db.py
```

## 🚨 Khắc Phục Lỗi

### Error: 500 Internal Server Error
```bash
# Xem logs
vercel logs --follow

# Phổ biến: DATABASE_URL không đúng
# Kiểm tra: Environment Variables → DATABASE_URL
```

### Error: Module not found
```bash
# Kiểm tra requirements.txt
vercel env list

# Reinstall
pip install -r requirements.txt
```

### Error: StaticFiles not found
```bash
# Kiểm tra folder static/
# Vercel hỗ trợ static files tự động
```

### Error: Database connection failed
```bash
# 1. Kiểm tra DATABASE_URL format
# 2. Kiểm tra database online
# 3. Thêm -sslmode=require nếu PostgreSQL
```

## 🎯 Domain Custom (Tuỳ Chọn)

```bash
# Thêm domain custom
vercel domains add your-domain.com

# Kiểm tra DNS
vercel domains inspect your-domain.com
```

## 📈 Performance Tips

1. **Sử dụng connection pooling**
   ```python
   app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
       'pool_size': 10,
       'pool_recycle': 3600,
       'pool_pre_ping': True,
   }
   ```

2. **Enable gzip compression**
3. **Minify static assets**
4. **Use CDN cho static files**

## 🔄 Auto Deploy Từ GitHub

Khi linked với GitHub:
- Mỗi push → Auto deploy
- Mỗi PR → Preview URL
- Có thể rollback dễ dàng

## 📚 Tài Liệu Tham Khảo

- [Vercel Python](https://vercel.com/docs/functions/python)
- [Vercel Flask](https://vercel.com/guides/deploying-a-flask-app)
- [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres)

## 💡 Lệnh Nhanh

```bash
# Deploy
vercel deploy

# Deploy prod
vercel deploy --prod

# Xem logs
vercel logs

# Xem URL
vercel inspect

# Liên kết GitHub
vercel link

# Remove deployment
vercel remove [url]
```

## 🎉 Hoàn Tất

Sau khi deploy thành công:

✅ App sẽ chạy trên: `https://your-project.vercel.app`  
✅ Tự động HTTPS  
✅ Free tier: 100GB bandwidth/tháng  
✅ Custom domain (pro)  

---

**Cần giúp?** Xem `VERCEL_DEPLOY.md` để có hướng dẫn chi tiết.

🚀 **Happy deploying!**
