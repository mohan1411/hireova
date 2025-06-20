#!/usr/bin/env python
"""
Quick start script for Hireova AI
Helps set up the development environment
"""
import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.11+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 11):
        print(f"❌ Python 3.11+ required. You have {version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor} detected")
    return True

def setup_venv():
    """Create virtual environment if it doesn't exist"""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("\nCreating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
        print("✓ Virtual environment created")
    else:
        print("✓ Virtual environment exists")
    
    # Provide activation instructions
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
    else:  # Unix/Linux/Mac
        activate_cmd = "source venv/bin/activate"
    
    print(f"\nTo activate virtual environment, run:")
    print(f"  {activate_cmd}")

def check_env_file():
    """Check if .env file exists, create from example if not"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    env_sqlite = Path(".env.sqlite")
    
    if not env_file.exists():
        print("\n.env file not found.")
        
        # Ask user about database preference
        print("\nChoose your database setup:")
        print("1. SQLite (easiest, no setup required)")
        print("2. PostgreSQL (requires Docker or local installation)")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            if env_sqlite.exists():
                env_sqlite.rename(env_file)
                print("✓ Created .env file with SQLite configuration")
            else:
                print("❌ .env.sqlite not found")
                return False
        else:
            if env_example.exists():
                import shutil
                shutil.copy(env_example, env_file)
                print("✓ Created .env file from .env.example")
                print("\n⚠️  Remember to:")
                print("  1. Start PostgreSQL and Redis (docker compose up -d)")
                print("  2. Update database credentials in .env if needed")
            else:
                print("❌ .env.example not found")
                return False
    else:
        print("✓ .env file exists")
    
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\nInstalling dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✓ Dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def test_imports():
    """Test if the application can be imported"""
    print("\nTesting application imports...")
    try:
        from app.main import app
        from app.core.config import settings
        print("✓ Application imports successful")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def create_database():
    """Create database tables"""
    print("\nCreating database tables...")
    try:
        from app.core.database import engine, Base
        from app.models import User, Organization, Job, Candidate, Application
        
        Base.metadata.create_all(bind=engine)
        print("✓ Database tables created")
        return True
    except Exception as e:
        print(f"❌ Database error: {e}")
        print("\nIf using PostgreSQL, make sure:")
        print("  1. PostgreSQL is running")
        print("  2. Database credentials in .env are correct")
        return False

def main():
    print("🚀 Hireova AI Quick Start\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Setup virtual environment
    setup_venv()
    
    # Check if we're in virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("\n⚠️  Virtual environment not activated!")
        print("Please activate it and run this script again.")
        sys.exit(1)
    
    # Check/create .env file
    if not check_env_file():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Test imports
    if not test_imports():
        sys.exit(1)
    
    # Create database
    if not create_database():
        sys.exit(1)
    
    print("\n✅ Setup complete!")
    print("\nTo start the application:")
    print("  python run.py")
    print("\nThen visit:")
    print("  - API: http://localhost:8000")
    print("  - API Docs: http://localhost:8000/api/docs")
    print("\nTo test the setup:")
    print("  python test_setup.py")

if __name__ == "__main__":
    main()