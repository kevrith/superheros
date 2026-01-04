#!/bin/bash

echo "Setting up Superheroes API..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Initialize database
echo "Initializing database..."
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Seed database
echo "Seeding database..."
python seed.py

echo "Setup complete! Run 'source venv/bin/activate' then 'python app.py' to start the server."
