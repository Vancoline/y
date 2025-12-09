# 🚀 Deploy Lên Vercel - Hướng Dẫn Nhanh

## 📋 Chuẩn Bị

✅ GitHub repository: https://github.com/Vancoline/y  
✅ Vercel account (đăng ký tại https://vercel.com)

## ⚡ 3 Bước Deploy

### 1️⃣ Truy Cập Vercel
```
https://vercel.com/dashboard
```

### 2️⃣ Tạo Project Mới
- Nhấp **"New Project"**
- Chọn repository **"y"** từ GitHub
- Vercel sẽ detect framework là Flask

### 3️⃣ Cấu Hình
```
Root Directory: career_quiz
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

**Environment Variables**:
```
SECRET_KEY=your-secret-key-123
FLASK_ENV=production
```

### 4️⃣ Deploy
- Nhấp **"Deploy"**
- Chờ 2-5 phút
- Vercel sẽ tạo URL: `https://your-project.vercel.app`

## ✨ Kết Quả

```
✅ Ứng dụng đang chạy trên: https://your-project.vercel.app
✅ Tự động deploy khi push code
✅ Free HTTPS
✅ Custom domain (tùy chọn)
```

## ⚠️ Vấn Đề Database

**SQLite không hoạt động trên Vercel** (filesystem tạm thời)

**Giải pháp:**
- Sử dụng PostgreSQL
- Hoặc dùng managed database service (Railway, Render, Supabase)

Xem chi tiết trong: **VERCEL_DEPLOY.md**

---

**Cần giúp?** Xem: `VERCEL_DEPLOY.md` (hướng dẫn chi tiết)

🎉 **Deployment ready!**
