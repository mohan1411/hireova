#!/usr/bin/env python
"""
Quick script to check if all models can be imported correctly
"""

def test_model_imports():
    """Test importing all models"""
    print("Testing model imports...")
    
    try:
        from app.models import User, Organization, Job, Candidate, Application
        print("✓ All models imported successfully")
        
        # Test creating instances (without saving to DB)
        user = User(email="test@example.com", password_hash="hash", role="recruiter")
        print("✓ User model instantiation works")
        
        org = Organization(name="Test Org")
        print("✓ Organization model instantiation works")
        
        job = Job(title="Test Job", organization_id=None)
        print("✓ Job model instantiation works")
        
        candidate = Candidate(email="candidate@example.com", name="Test Candidate")
        print("✓ Candidate model instantiation works")
        
        application = Application(job_id=None, candidate_id=None)
        print("✓ Application model instantiation works")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_model_imports()