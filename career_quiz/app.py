from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import json

app = Flask(__name__)

# Database configuration - Vercel compatible
# Priority: DATABASE_URL (PostgreSQL on Vercel) > SQLite (Local development)
database_url = os.getenv('DATABASE_URL')
if database_url:
    # Production: PostgreSQL on Vercel
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    # Development: SQLite locally
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///career_quiz.db'

# Secret key from environment or default
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-change-in-production')
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    results = db.relationship('QuizResult', backref='user', lazy=True, cascade='all, delete-orphan')

class Profession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    skills = db.Column(db.Text)  # JSON format
    qualities = db.Column(db.Text)  # JSON format
    
    questions = db.relationship('Question', backref='profession', lazy=True, cascade='all, delete-orphan')

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(255), nullable=False)
    option_b = db.Column(db.String(255), nullable=False)
    option_c = db.Column(db.String(255), nullable=False)
    option_d = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)  # A, B, C, or D
    
    answers = db.relationship('UserAnswer', backref='question', lazy=True, cascade='all, delete-orphan')

class QuizResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, default=10)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    answers = db.relationship('UserAnswer', backref='result', lazy=True, cascade='all, delete-orphan')

class UserAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result_id = db.Column(db.Integer, db.ForeignKey('quiz_result.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    user_answer = db.Column(db.String(1))  # A, B, C, or D
    is_correct = db.Column(db.Boolean)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Tên người dùng đã tồn tại'}), 400
        
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['is_admin'] = user.is_admin
        
        return jsonify({'success': True, 'user_id': user.id})
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = User.query.filter_by(username=username, password=password).first()
        
        if not user:
            return jsonify({'error': 'Tên đăng nhập hoặc mật khẩu không đúng'}), 401
        
        session['user_id'] = user.id
        session['username'] = user.username
        session['is_admin'] = user.is_admin
        
        return jsonify({'success': True, 'is_admin': user.is_admin})
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/api/quiz/questions', methods=['GET'])
def get_quiz_questions():
    import random
    
    # Get 10 random questions from all professions
    all_questions = Question.query.all()
    if len(all_questions) < 10:
        return jsonify({'error': 'Không đủ câu hỏi'}), 400
    
    questions = random.sample(all_questions, 10)
    
    result = []
    for q in questions:
        result.append({
            'id': q.id,
            'profession': q.profession.name,
            'question': q.question_text,
            'options': {
                'A': q.option_a,
                'B': q.option_b,
                'C': q.option_c,
                'D': q.option_d
            }
        })
    
    return jsonify(result)

@app.route('/api/quiz/submit', methods=['POST'])
def submit_quiz():
    if 'user_id' not in session:
        return jsonify({'error': 'Vui lòng đăng nhập'}), 401
    
    data = request.get_json()
    answers = data.get('answers')  # Dict with question_id: answer
    
    user_id = session['user_id']
    score = 0
    total = len(answers)
    
    quiz_result = QuizResult(user_id=user_id, total_questions=total, score=0)
    db.session.add(quiz_result)
    db.session.flush()
    
    for question_id, user_answer in answers.items():
        question = Question.query.get(int(question_id))
        if not question:
            continue
        
        is_correct = question.correct_answer == user_answer
        if is_correct:
            score += 1
        
        user_answer_record = UserAnswer(
            result_id=quiz_result.id,
            question_id=int(question_id),
            user_answer=user_answer,
            is_correct=is_correct
        )
        db.session.add(user_answer_record)
    
    quiz_result.score = score
    db.session.commit()
    
    return jsonify({
        'score': score,
        'total': total,
        'percentage': round(score / total * 100, 2),
        'result_id': quiz_result.id
    })

@app.route('/api/quiz/result/<int:result_id>', methods=['GET'])
def get_quiz_result(result_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Vui lòng đăng nhập'}), 401
    
    result = QuizResult.query.get(result_id)
    if not result:
        return jsonify({'error': 'Không tìm thấy kết quả'}), 404
    
    user_id = session['user_id']
    if result.user_id != user_id and not session.get('is_admin'):
        return jsonify({'error': 'Không có quyền truy cập'}), 403
    
    answers_detail = []
    for answer in result.answers:
        answers_detail.append({
            'question': answer.question.question_text,
            'profession': answer.question.profession.name,
            'user_answer': answer.user_answer,
            'correct_answer': answer.question.correct_answer,
            'is_correct': answer.is_correct,
            'options': {
                'A': answer.question.option_a,
                'B': answer.question.option_b,
                'C': answer.question.option_c,
                'D': answer.question.option_d
            }
        })
    
    return jsonify({
        'score': result.score,
        'total': result.total_questions,
        'percentage': round(result.score / result.total_questions * 100, 2),
        'completed_at': result.completed_at.isoformat(),
        'answers': answers_detail
    })

@app.route('/api/admin/dashboard', methods=['GET'])
def admin_dashboard():
    if 'user_id' not in session or not session.get('is_admin'):
        return jsonify({'error': 'Không có quyền truy cập'}), 403
    
    # Get all users and their scores
    users = User.query.all()
    
    users_data = []
    for user in users:
        results = QuizResult.query.filter_by(user_id=user.id).all()
        
        if results:
            avg_score = sum(r.score for r in results) / len(results)
            latest_score = results[-1].score if results else 0
            total_attempts = len(results)
        else:
            avg_score = 0
            latest_score = 0
            total_attempts = 0
        
        users_data.append({
            'user_id': user.id,
            'username': user.username,
            'total_attempts': total_attempts,
            'latest_score': latest_score,
            'average_score': round(avg_score, 2),
            'is_admin': user.is_admin
        })
    
    return jsonify(users_data)

@app.route('/api/admin/user/<int:user_id>/results', methods=['GET'])
def admin_user_results(user_id):
    if 'user_id' not in session or not session.get('is_admin'):
        return jsonify({'error': 'Không có quyền truy cập'}), 403
    
    results = QuizResult.query.filter_by(user_id=user_id).all()
    
    results_data = []
    for result in results:
        results_data.append({
            'result_id': result.id,
            'score': result.score,
            'total': result.total_questions,
            'percentage': round(result.score / result.total_questions * 100, 2),
            'completed_at': result.completed_at.isoformat()
        })
    
    return jsonify(results_data)

@app.route('/admin')
def admin_page():
    if 'user_id' not in session or not session.get('is_admin'):
        return render_template('admin_login.html')
    
    return render_template('admin.html')

@app.route('/api/professions', methods=['GET'])
def get_professions():
    professions = Profession.query.all()
    
    result = []
    for prof in professions:
        result.append({
            'id': prof.id,
            'name': prof.name,
            'description': prof.description,
            'skills': json.loads(prof.skills) if prof.skills else [],
            'qualities': json.loads(prof.qualities) if prof.qualities else []
        })
    
    return jsonify(result)

@app.route('/api/profession/<int:profession_id>', methods=['GET'])
def get_profession(profession_id):
    prof = Profession.query.get(profession_id)
    if not prof:
        return jsonify({'error': 'Không tìm thấy ngành nghề'}), 404
    
    return jsonify({
        'id': prof.id,
        'name': prof.name,
        'description': prof.description,
        'skills': json.loads(prof.skills) if prof.skills else [],
        'qualities': json.loads(prof.qualities) if prof.qualities else []
    })

@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

@app.route('/results')
def results_page():
    return render_template('results.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Initialize professions if empty
        if Profession.query.count() == 0:
            from professions_data import PROFESSIONS_DATA
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
    
    # Development mode
    debug_mode = os.getenv('FLASK_ENV') != 'production'
    port = int(os.getenv('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)

