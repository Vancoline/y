#!/bin/bash
# Script to initialize the database with admin user and start the application

cd /workspaces/y/career_quiz

# Create a Python script to set up admin user
python3 << 'EOF'
from app import app, db, User

with app.app_context():
    db.create_all()
    
    # Check if admin user exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', password='admin123', is_admin=True)
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
        print("Username: admin")
        print("Password: admin123")
    else:
        print("Admin user already exists!")

EOF

echo "Starting Flask application..."
python3 app.py
