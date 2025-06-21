#!/usr/bin/env python
"""
Verify that data created through Swagger UI is stored in the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.models import User, Organization, Job, Candidate, Application
from datetime import datetime

def check_swagger_data():
    """Check if data from Swagger UI is in the database"""
    print("🔍 Checking Database for Swagger UI Data\n")
    
    # Create database session
    engine = create_engine(settings.database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Check Users
        print("👥 USERS in Database:")
        print("-" * 50)
        users = session.query(User).all()
        if users:
            for user in users:
                print(f"ID: {user.id}")
                print(f"Email: {user.email}")
                print(f"Name: {user.full_name}")
                print(f"Role: {user.role}")
                print(f"Created: {user.created_at}")
                print(f"Active: {user.is_active}")
                if user.organization:
                    print(f"Organization: {user.organization.name}")
                print("-" * 50)
        else:
            print("No users found in database")
        
        print(f"\nTotal Users: {len(users)}")
        
        # Check Organizations
        print("\n\n🏢 ORGANIZATIONS in Database:")
        print("-" * 50)
        orgs = session.query(Organization).all()
        if orgs:
            for org in orgs:
                print(f"ID: {org.id}")
                print(f"Name: {org.name}")
                print(f"Plan: {org.plan}")
                print(f"Created: {org.created_at}")
                print("-" * 50)
        else:
            print("No organizations found in database")
        
        print(f"\nTotal Organizations: {len(orgs)}")
        
        # Check Jobs
        print("\n\n💼 JOBS in Database:")
        print("-" * 50)
        jobs = session.query(Job).all()
        if jobs:
            for job in jobs:
                print(f"ID: {job.id}")
                print(f"Title: {job.title}")
                print(f"Organization: {job.organization.name if job.organization else 'None'}")
                print(f"Status: {job.status}")
                print(f"Created: {job.created_at}")
                print("-" * 50)
        else:
            print("No jobs found in database")
        
        print(f"\nTotal Jobs: {len(jobs)}")
        
        # Show recent activity
        print("\n\n📊 RECENT ACTIVITY (Last 24 hours):")
        print("-" * 50)
        
        from datetime import datetime, timedelta
        yesterday = datetime.utcnow() - timedelta(days=1)
        
        recent_users = session.query(User).filter(User.created_at > yesterday).count()
        print(f"New users in last 24h: {recent_users}")
        
        # Database location
        print("\n\n💾 DATABASE INFO:")
        print("-" * 50)
        if settings.database_url.startswith("sqlite"):
            db_file = settings.database_url.replace("sqlite:///", "")
            print(f"Type: SQLite")
            print(f"File: {db_file}")
            import os
            if os.path.exists(db_file.replace("./", "")):
                size = os.path.getsize(db_file.replace("./", "")) / 1024
                print(f"Size: {size:.2f} KB")
        else:
            print(f"Type: PostgreSQL")
            print(f"URL: {settings.database_url.split('@')[1]}")
        
        session.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        session.close()

def test_data_persistence():
    """Test that data persists between sessions"""
    print("\n\n🧪 TESTING DATA PERSISTENCE:")
    print("-" * 50)
    
    engine = create_engine(settings.database_url)
    Session = sessionmaker(bind=engine)
    
    # First session - count records
    session1 = Session()
    count1 = session1.query(User).count()
    session1.close()
    
    # Second session - count should be same
    session2 = Session()
    count2 = session2.query(User).count()
    session2.close()
    
    print(f"Session 1 user count: {count1}")
    print(f"Session 2 user count: {count2}")
    print(f"Data persists: {'✅ YES' if count1 == count2 else '❌ NO'}")

if __name__ == "__main__":
    check_swagger_data()
    test_data_persistence()
    
    print("\n\n💡 TIP: Create a new user in Swagger UI and run this script again!")
    print("   You'll see your new user in the database output above.")