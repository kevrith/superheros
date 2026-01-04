#!/usr/bin/env python3
"""
Setup verification script for Superheroes API
Run this to verify your environment is correctly configured
"""

import sys
import os
from pathlib import Path


def check_file(filepath, required=True):
    """Check if a file exists"""
    if Path(filepath).exists():
        print(f" {filepath} found")
        return True
    else:
        status = "X" if required else "YES"
        print(f"{status} {filepath} {'missing (required)' if required else 'not found (optional)'}")
        return not required


def check_directory(dirpath, required=True):
    """Check if a directory exists"""
    if Path(dirpath).exists() and Path(dirpath).is_dir():
        print(f" {dirpath}/ directory found")
        return True
    else:
        status = "X" if required else "YES"
        print(f"{status} {dirpath}/ {'missing (required)' if required else 'not found (optional)'}")
        return not required


def check_import(module_name):
    """Check if a Python module can be imported"""
    try:
        __import__(module_name)
        print(f" {module_name} module installed")
        return True
    except ImportError:
        print(f" {module_name} module not installed")
        return False


def check_env_file():
    """Check .env file configuration"""
    env_path = Path('.env')
    if not env_path.exists():
        print(" .env file not found")
        return False

    print(" .env file found")

    # Check for required variables
    required_vars = [
        'FLASK_APP',
        'DATABASE_URI',
        'MAIL_SERVER',
        'MAIL_PORT',
        'MAIL_USERNAME',
        'MAIL_PASSWORD'
    ]

    with open(env_path, 'r') as f:
        content = f.read()

    missing_vars = []
    for var in required_vars:
        if var not in content:
            missing_vars.append(var)

    if missing_vars:
        print(f"  Missing environment variables: {', '.join(missing_vars)}")
        return False
    else:
        print(" All required environment variables present")
        return True


def main():
    print("="*60)
    print("Superheroes API - Setup Verification")
    print("="*60)
    print()

    all_ok = True

    # Check core files
    print("Checking core files...")
    all_ok &= check_file('app.py')
    all_ok &= check_file('models.py')
    all_ok &= check_file('config.py')
    all_ok &= check_file('seed.py')
    all_ok &= check_file('requirements.txt')
    print()

    # Check documentation
    print("Checking documentation...")
    all_ok &= check_file('README.md')
    all_ok &= check_file('.env.example')
    all_ok &= check_file('QUICKSTART.md', required=False)
    all_ok &= check_file('SUBMISSION_CHECKLIST.md', required=False)
    print()

    # Check environment
    print("Checking environment configuration...")
    all_ok &= check_env_file()
    print()

    # Check virtual environment
    print("Checking virtual environment...")
    check_directory('venv', required=False)
    print()

    # Check Python packages
    print("Checking Python packages...")
    packages = [
        'flask',
        'flask_sqlalchemy',
        'flask_migrate',
        'flask_mail',
        'sqlalchemy',
        'sqlalchemy_serializer',
        'dotenv'
    ]

    packages_ok = True
    for package in packages:
        if not check_import(package):
            packages_ok = False

    if not packages_ok:
        print()
        print("  Some packages are missing. Run: pip install -r requirements.txt")

    all_ok &= packages_ok
    print()

    # Check database
    print("Checking database...")
    if check_file('app.db', required=False):
        print(" Database file exists")
    else:
        print("   Database not initialized. Run migrations:")
        print("   flask db init")
        print("   flask db migrate -m 'Initial migration'")
        print("   flask db upgrade")
        print("   python seed.py")
    print()

    # Check migrations
    print("Checking migrations...")
    check_directory('migrations', required=False)
    print()

    # Final summary
    print("="*60)
    if all_ok:
        print("  Setup verification PASSED")
        print()
        print("Your environment is ready! Next steps:")
        print("1. Review and update .env with your email credentials")
        print("2. Run migrations if not done:")
        print("   flask db init")
        print("   flask db migrate -m 'Initial migration'")
        print("   flask db upgrade")
        print("3. Seed the database: python seed.py")
        print("4. Start the server: python app.py")
    else:
        print("  Setup verification FAILED")
        print()
        print("Please address the issues above before proceeding.")
        print("See README.md for detailed setup instructions.")

    print("="*60)

    return 0 if all_ok else 1


if __name__ == '__main__':
    sys.exit(main())
