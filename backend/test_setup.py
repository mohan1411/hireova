#!/usr/bin/env python
"""
Test script to verify the basic setup is working
"""
import sys

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    try:
        import fastapi
        print("✓ FastAPI")
        
        import sqlalchemy
        print("✓ SQLAlchemy")
        
        import pydantic
        print("✓ Pydantic")
        
        import jose
        print("✓ Python-JOSE")
        
        import redis
        print("✓ Redis")
        
        from app.core.config import settings
        print("✓ App configuration")
        
        from app.main import app
        print("✓ FastAPI app")
        
        print("\nAll imports successful! ✨")
        return True
        
    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        print("\nPlease make sure you've installed all dependencies:")
        print("pip install -r requirements.txt")
        return False

def test_config():
    """Test if configuration is loaded correctly"""
    print("\nTesting configuration...")
    try:
        from app.core.config import settings
        
        print(f"✓ App name: {settings.app_name}")
        print(f"✓ Environment: {settings.environment}")
        print(f"✓ API port: {settings.api_port}")
        print(f"✓ Debug mode: {settings.debug}")
        
        if "your-secret-key-here" in settings.secret_key:
            print("\n⚠️  Warning: Using default secret key. Change this for production!")
        
        if "your-openai-api-key" in settings.openai_api_key:
            print("⚠️  Warning: OpenAI API key not configured. Add your key to .env file.")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Configuration error: {e}")
        print("\nMake sure you have a .env file with all required variables.")
        return False

def main():
    print("🚀 Hireova AI Setup Test\n")
    
    if not test_imports():
        sys.exit(1)
    
    if not test_config():
        sys.exit(1)
    
    print("\n✅ Basic setup is complete!")
    print("\nNext steps:")
    print("1. Start the databases: docker-compose up -d")
    print("2. Run the server: python run.py")
    print("3. Visit API docs: http://localhost:8000/api/docs")

if __name__ == "__main__":
    main()