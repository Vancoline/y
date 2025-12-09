#!/usr/bin/env python3
"""
Script để khởi tạo database và tạo tài khoản admin
"""

from app import app, db, User, Profession, Question, QuizResult
from professions_data import PROFESSIONS_DATA
import json

def init_database():
    """Khởi tạo cơ sở dữ liệu"""
    with app.app_context():
        # Xóa tất cả bảng và tạo lại
        print("Đang tạo các bảng database...")
        db.create_all()
        
        # Kiểm tra xem dữ liệu đã tồn tại chưa
        if Profession.query.count() == 0:
            print(f"Đang thêm 50 ngành nghề...")
            for prof_data in PROFESSIONS_DATA:
                profession = Profession(
                    name=prof_data['name'],
                    description=prof_data['description'],
                    skills=json.dumps(prof_data['skills']),
                    qualities=json.dumps(prof_data['qualities'])
                )
                db.session.add(profession)
                db.session.flush()
                
                for question_data in prof_data['questions']:
                    question = Question(
                        profession_id=profession.id,
                        question_text=question_data['question'],
                        option_a=question_data['options']['A'],
                        option_b=question_data['options']['B'],
                        option_c=question_data['options']['C'],
                        option_d=question_data['options']['D'],
                        correct_answer=question_data['correct_answer']
                    )
                    db.session.add(question)
            
            db.session.commit()
            print(f"✓ Đã thêm {Profession.query.count()} ngành nghề")
            print(f"✓ Đã thêm {Question.query.count()} câu hỏi")
        else:
            print(f"✓ Dữ liệu đã tồn tại ({Profession.query.count()} ngành nghề)")
        
        # Tạo admin user
        print("\nĐang thiết lập tài khoản admin...")
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            admin = User(username='admin', password='admin123', is_admin=True)
            db.session.add(admin)
            db.session.commit()
            print("✓ Tài khoản admin đã được tạo")
            print(f"  Username: admin")
            print(f"  Password: admin123")
            print("\n⚠️  CẢNH BÁO: Vui lòng thay đổi mật khẩu admin trước khi triển khai!\n")
        else:
            print("✓ Tài khoản admin đã tồn tại")
        
        # In thông tin thống kê
        print("\n" + "="*50)
        print("THỐNG KÊ DATABASE")
        print("="*50)
        print(f"Tổng số ngành nghề: {Profession.query.count()}")
        print(f"Tổng số câu hỏi: {Question.query.count()}")
        print(f"Tổng số người dùng: {User.query.count()}")
        print(f"Tổng số bài trắc nghiệm: {QuizResult.query.count()}")
        print("="*50)

if __name__ == '__main__':
    init_database()
    print("\n✓ Khởi tạo hoàn tất! Bạn có thể chạy: python app.py")

if __name__ == '__main__':
    init_database()
    print("\n✓ Khởi tạo hoàn tất! Bạn có thể chạy: python app.py")
