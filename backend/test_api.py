#!/usr/bin/env python
"""
Test script for Hireova API endpoints
"""
import requests
import json
from datetime import datetime

API_BASE_URL = "http://localhost:8000/api/v1"

def test_register():
    """Test user registration"""
    print("\n1. Testing User Registration...")
    
    user_data = {
        "email": f"test_{datetime.now().timestamp()}@example.com",
        "password": "testpass123",
        "full_name": "Test User",
        "role": "recruiter",
        "organization_name": "Test Company"
    }
    
    response = requests.post(f"{API_BASE_URL}/auth/register", json=user_data)
    
    if response.status_code == 201:
        print("✓ Registration successful!")
        user = response.json()
        print(f"  User ID: {user['id']}")
        print(f"  Email: {user['email']}")
        return user_data['email'], user_data['password']
    else:
        print(f"✗ Registration failed: {response.status_code}")
        print(f"  Error: {response.json()}")
        return None, None

def test_login(email, password):
    """Test user login"""
    print("\n2. Testing User Login...")
    
    login_data = {
        "email": email,
        "password": password
    }
    
    response = requests.post(f"{API_BASE_URL}/auth/login", json=login_data)
    
    if response.status_code == 200:
        print("✓ Login successful!")
        token_data = response.json()
        print(f"  Token type: {token_data['token_type']}")
        print(f"  Access token: {token_data['access_token'][:50]}...")
        return token_data['access_token']
    else:
        print(f"✗ Login failed: {response.status_code}")
        print(f"  Error: {response.json()}")
        return None

def test_get_current_user(token):
    """Test getting current user info"""
    print("\n3. Testing Get Current User...")
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(f"{API_BASE_URL}/auth/me", headers=headers)
    
    if response.status_code == 200:
        print("✓ Get current user successful!")
        user = response.json()
        print(f"  User: {user['full_name']} ({user['email']})")
        print(f"  Role: {user['role']}")
        print(f"  Active: {user['is_active']}")
    else:
        print(f"✗ Get current user failed: {response.status_code}")
        print(f"  Error: {response.json()}")

def test_health_check():
    """Test health check endpoint"""
    print("\n4. Testing Health Check...")
    
    response = requests.get("http://localhost:8000/health")
    
    if response.status_code == 200:
        print("✓ Health check successful!")
        health = response.json()
        print(f"  Status: {health['status']}")
        print(f"  Version: {health['version']}")
    else:
        print(f"✗ Health check failed: {response.status_code}")

def main():
    print("🧪 Hireova API Test Suite")
    print("=" * 50)
    
    # Test health check
    test_health_check()
    
    # Test registration
    email, password = test_register()
    
    if email and password:
        # Test login
        token = test_login(email, password)
        
        if token:
            # Test authenticated endpoints
            test_get_current_user(token)
    
    print("\n" + "=" * 50)
    print("✅ API tests completed!")
    print("\nNext steps:")
    print("1. Check the API docs at http://localhost:8000/api/docs")
    print("2. Try creating jobs and uploading resumes")
    print("3. Implement the remaining endpoints")

if __name__ == "__main__":
    main()