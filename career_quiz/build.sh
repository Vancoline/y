#!/bin/bash
# Vercel Build Script

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Initializing database..."
python init_db.py

echo "Build complete!"
