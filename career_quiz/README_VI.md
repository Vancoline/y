# Ứng Dụng Trắc Nghiệm Ngành Nghề Việt Nam

Ứng dụng web toàn diện để trắc nghiệm về 50 ngành nghề tại Việt Nam, bao gồm các câu hỏi về năng lực và phẩm chất của mỗi ngành.

## Tính Năng

### Cho Người Dùng Thông Thường
- **Đăng ký và đăng nhập**: Tạo tài khoản để lưu kết quả
- **Trắc nghiệm**: 10 câu hỏi ngẫu nhiên từ 50 ngành nghề
- **Xem kết quả**: Kết quả tức thì với phần trăm chính xác
- **Lịch sử bài làm**: Xem tất cả các bài trắc nghiệm trước đó

### Cho Admin
- **Bảng điều khiển admin**: Xem thông tin về tất cả người dùng
- **Xem kết quả chi tiết**: Xem điểm số và kết quả của từng người dùng
- **Phân tích câu trả lời**: Xem chi tiết từng câu trả lời (đúng/sai)

## 50 Ngành Nghề Được Bao Gồm

1. Kỹ sư phần mềm
2. Bác sĩ
3. Giáo viên
4. Kế toán
5. Kỹ sư xây dựng
6. Nhân viên kinh doanh
7. Họa sĩ
8. Lập trình viên
9. Thiết kế đồ họa
10. Quản lý nhân sự
11. Kỹ sư điện
12. Y tá
13. Nhà báo
14. Luật sư
15. Chuyên gia mỹ phẩm
16. Đầu bếp
17. Quản lý dự án
18. Nhà khoa học
19. Marketing
20. Kỹ sư cơ khí
21. Nhân viên kế toán ngân hàng
22. Thợ cắt tóc
23. Phân tích dữ liệu
24. Thợ điện
25. Nhân viên bán lẻ
26. Kỹ sư hóa học
27. Nhiếp ảnh gia
28. Hướng dẫn viên du lịch
29. Tiếp lễ
30. Nhân viên CNTT
31. Thư ký
32. Lái xe
33. Kiến trúc sư
34. Nhà môi giới bất động sản
35. Thợ xây
36. Chuyên viên pháp lý
37. Nhân viên quản lý kho
38. Nhà thiết kế thời trang
39. Huấn luyện viên thể thao
40. Nhân viên tiếp tân
41. Nhà báo chuyên ngành
42. Chuyên gia môi trường
43. Chuyên viên marketing số
44. Lập trình viên web
45. Quản lý bán hàng
46. Nhân viên khảo sát
47. Nhà soạn nhạc
48. Nhân viên an ninh
49. Chuyên gia thương mại điện tử
50. Nhân viên hành chính

## Cách Cài Đặt

### Yêu Cầu
- Python 3.8+
- pip (trình quản lý gói Python)

### Các Bước Cài Đặt

1. **Điều hướng đến thư mục dự án**:
```bash
cd /workspaces/y/career_quiz
```

2. **Cài đặt các thư viện phụ thuộc**:
```bash
pip install -r requirements.txt
```

3. **Khởi động ứng dụng** (Windows/Linux/Mac):
```bash
python app.py
```

Hoặc sử dụng script:
```bash
chmod +x run.sh
./run.sh
```

4. **Truy cập ứng dụng**:
   - Mở trình duyệt web
   - Nhập URL: `http://localhost:5000`

## Thông Tin Đăng Nhập Admin

**Username**: admin  
**Password**: admin123

*Lưu ý: Thay đổi mật khẩu này trước khi triển khai lên môi trường sản xuất*

## Cách Sử Dụng

### Cho Người Dùng Thông Thường

1. **Đăng Ký**:
   - Nhấp vào "Đăng ký" trên thanh điều hướng
   - Nhập tên người dùng và mật khẩu
   - Nhấn "Đăng ký"

2. **Làm Bài Trắc Nghiệm**:
   - Sau khi đăng nhập, nhấp vào "Làm bài trắc nghiệm"
   - Bạn sẽ nhận được 10 câu hỏi ngẫu nhiên
   - Mỗi câu hỏi liên quan đến một ngành nghề cụ thể
   - Chọn đáp án và nhấn "Câu Tiếp Theo"

3. **Xem Kết Quả**:
   - Sau khi hoàn thành bài trắc nghiệm, bạn sẽ thấy:
     - Điểm số (ví dụ: 8/10)
     - Tỷ lệ phần trăm (80%)
     - Chi tiết từng câu trả lời
     - Câu trả lời đúng nếu bạn sai

4. **Xem Lịch Sử**:
   - Nhấp vào "Kết quả" để xem tất cả các bài trắc nghiệm trước đó

### Cho Admin

1. **Đăng Nhập Admin**:
   - Nhấp vào dropdown "Tài khoản"
   - Chọn "Admin"
   - Đăng nhập với thông tin admin

2. **Xem Bảng Điều Khiển**:
   - Bảng hiển thị danh sách tất cả người dùng
   - Xem số lần làm bài, điểm mới nhất, và điểm trung bình

3. **Xem Chi Tiết Người Dùng**:
   - Nhấp vào "Xem Chi Tiết" bên cạnh một người dùng
   - Xem tất cả bài trắc nghiệm của họ

4. **Xem Chi Tiết Câu Trả Lời**:
   - Nhấp vào "Chi Tiết" bên cạnh một kết quả
   - Xem chi tiết từng câu trả lời (đúng/sai)

## Cấu Trúc Dự Án

```
career_quiz/
├── app.py                 # Ứng dụng Flask chính
├── professions_data.py    # Dữ liệu 50 ngành nghề
├── requirements.txt       # Các thư viện phụ thuộc
├── templates/            # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── quiz.html
│   ├── results.html
│   ├── admin.html
│   └── admin_login.html
├── static/
│   ├── css/
│   │   └── style.css     # CSS styling
│   └── js/
│       ├── main.js       # JavaScript chung
│       ├── quiz.js       # Logic trắc nghiệm
│       ├── results.js    # Logic kết quả
│       └── admin.js      # Logic admin
└── career_quiz.db        # Cơ sở dữ liệu SQLite
```

## Công Nghệ Sử Dụng

### Backend
- **Flask**: Framework web Python
- **Flask-SQLAlchemy**: ORM cho database
- **SQLAlchemy 2.0**: Thao tác cơ sở dữ liệu
- **SQLite**: Cơ sở dữ liệu

### Frontend
- **HTML5**: Cấu trúc trang web
- **CSS3**: Styling và responsive design
- **JavaScript (Vanilla)**: Interactivity

## Cơ Sở Dữ Liệu

### Các Bảng

1. **User**
   - id (Primary Key)
   - username (Unique)
   - password
   - is_admin
   - created_at

2. **Profession**
   - id (Primary Key)
   - name
   - description
   - skills (JSON)
   - qualities (JSON)

3. **Question**
   - id (Primary Key)
   - profession_id (Foreign Key)
   - question_text
   - option_a, option_b, option_c, option_d
   - correct_answer

4. **QuizResult**
   - id (Primary Key)
   - user_id (Foreign Key)
   - score
   - total_questions
   - completed_at

5. **UserAnswer**
   - id (Primary Key)
   - result_id (Foreign Key)
   - question_id (Foreign Key)
   - user_answer
   - is_correct

## API Endpoints

### Xác Thực
- `POST /login` - Đăng nhập
- `POST /register` - Đăng ký
- `GET /logout` - Đăng xuất

### Trắc Nghiệm
- `GET /api/quiz/questions` - Lấy 10 câu hỏi ngẫu nhiên
- `POST /api/quiz/submit` - Nộp bài trắc nghiệm
- `GET /api/quiz/result/<result_id>` - Lấy chi tiết kết quả

### Admin
- `GET /api/admin/dashboard` - Lấy dữ liệu bảng điều khiển
- `GET /api/admin/user/<user_id>/results` - Lấy kết quả của một người dùng

### Dữ Liệu
- `GET /api/professions` - Lấy tất cả ngành nghề
- `GET /api/profession/<profession_id>` - Lấy chi tiết ngành nghề

## Bảo Mật

### Ghi Chú Bảo Mật Quan Trọng

1. **Mật khẩu**: Hiện tại, mật khẩu được lưu dưới dạng văn bản. Trong môi trường sản xuất, bạn nên:
   - Sử dụng hashing (bcrypt, argon2)
   - Không bao giờ lưu mật khẩu dưới dạng văn bản

2. **Session**: Ứng dụng sử dụng session server. Bạn nên:
   - Sử dụng HTTPS trong môi trường sản xuất
   - Đặt SECRET_KEY mạnh (không phải là "your-secret-key-change-in-production")
   - Sử dụng SameSite cookies

3. **CORS**: Xem xét thêm CORS headers cho môi trường sản xuất

## Triển Khai

Để triển khai ứng dụng này trên máy chủ sản xuất:

1. Thay đổi `debug=False` trong `app.run()`
2. Cấu hình SECRET_KEY mạnh
3. Sử dụng một máy chủ WSGI như Gunicorn
4. Thiết lập HTTPS với Let's Encrypt
5. Sử dụng một cơ sở dữ liệu sản xuất như PostgreSQL

## Giải Quyết Vấn Đề

### Cổng 5000 đã được sử dụng
```bash
# Tìm quy trình chiếm cổng 5000
lsof -i :5000

# Hoặc thay đổi cổng trong app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Lỗi Database
```bash
# Xóa cơ sở dữ liệu và tạo lại
rm career_quiz.db
python app.py
```

### Module không được tìm thấy
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

## Tài Liệu Thêm

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Bootstrap CSS Framework](https://getbootstrap.com/)

## Licen Se

Dự án này được cấp phép dưới MIT License

## Liên Hệ Hỗ Trợ

Nếu bạn gặp bất kỳ vấn đề nào, vui lòng kiểm tra:
1. Đảm bảo tất cả các phụ thuộc được cài đặt
2. Kiểm tra xem cổng 5000 có sẵn không
3. Xóa cơ sở dữ liệu và tạo lại nếu gặp lỗi database

## Cập Nhật Trong Tương Lai

- [ ] Thêm phân tích thống kê nâng cao
- [ ] Gửi email thông báo kết quả
- [ ] Xuất kết quả PDF
- [ ] Hỗ trợ nhiều ngôn ngữ
- [ ] Thêm hình ảnh cho các ngành nghề
- [ ] Tích hợp machine learning để gợi ý ngành nghề phù hợp
