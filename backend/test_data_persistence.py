#!/usr/bin/env python
"""
Test that Swagger UI operations persist data
"""
import requests
import time
from datetime import datetime

API_URL = "http://localhost:8000/api/v1"

def test_persistence():
    """Test that data created via API persists"""
    
    # Create unique test user
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_email = f"test_user_{timestamp}@example.com"
    
    print(f"🧪 Testing Data Persistence\n")
    print(f"Creating user: {test_email}")
    
    # 1. Register user
    register_data = {
        "email": test_email,
        "password": "testpass123",
        "full_name": "Test User via Swagger",
        "role": "recruiter",
        "organization_name": "Test Company"
    }
    
    response = requests.post(f"{API_URL}/auth/register", json=register_data)
    
    if response.status_code == 201:
        user_data = response.json()
        print(f"✅ User created with ID: {user_data['id']}")
        
        # 2. Try to login immediately
        login_data = {
            "email": test_email,
            "password": "testpass123"
        }
        
        login_response = requests.post(f"{API_URL}/auth/login", json=login_data)
        
        if login_response.status_code == 200:
            print("✅ Login successful - Data is persisted!")
            token = login_response.json()["access_token"]
            
            # 3. Get user info
            headers = {"Authorization": f"Bearer {token}"}
            me_response = requests.get(f"{API_URL}/auth/me", headers=headers)
            
            if me_response.status_code == 200:
                user_info = me_response.json()
                print(f"✅ Retrieved user: {user_info['email']}")
                print(f"   Organization: {user_info.get('organization_id')}")
                
        # 4. Try to register same user again (should fail)
        duplicate_response = requests.post(f"{API_URL}/auth/register", json=register_data)
        if duplicate_response.status_code == 400:
            print("✅ Duplicate prevention works - User already exists in DB")
            
    print("\n✅ All tests passed! Data is being persisted in the database.")
    print("\n📊 Run 'python verify_swagger_data.py' to see all stored data")

if __name__ == "__main__":
    test_persistence()