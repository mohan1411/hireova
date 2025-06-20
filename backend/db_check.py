#!/usr/bin/env python
"""
Check database tables and data
"""
from sqlalchemy import create_engine, inspect, text
from app.core.config import settings
from app.models import User, Organization, Job, Candidate, Application
from sqlalchemy.orm import sessionmaker
import json

def check_database():
    """Check database connection and tables"""
    print("🔍 Checking Hireova Database\n")
    
    try:
        # Create engine
        engine = create_engine(settings.database_url)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Check connection
        result = session.execute(text("SELECT 1"))
        print("✅ Database connection successful!\n")
        
        # List all tables
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"📊 Found {len(tables)} tables:")
        for table in tables:
            print(f"  - {table}")
        
        print("\n📈 Table Statistics:")
        
        # Count records in each table
        stats = {}
        
        # Users
        user_count = session.query(User).count()
        stats['users'] = user_count
        print(f"  - Users: {user_count}")
        
        # Organizations
        org_count = session.query(Organization).count()
        stats['organizations'] = org_count
        print(f"  - Organizations: {org_count}")
        
        # Jobs
        job_count = session.query(Job).count()
        stats['jobs'] = job_count
        print(f"  - Jobs: {job_count}")
        
        # Candidates
        candidate_count = session.query(Candidate).count()
        stats['candidates'] = candidate_count
        print(f"  - Candidates: {candidate_count}")
        
        # Applications
        app_count = session.query(Application).count()
        stats['applications'] = app_count
        print(f"  - Applications: {app_count}")
        
        # Show recent users
        if user_count > 0:
            print("\n👥 Recent Users:")
            users = session.query(User).order_by(User.created_at.desc()).limit(5).all()
            for user in users:
                print(f"  - {user.email} ({user.role}) - {user.full_name or 'No name'}")
                if user.organization:
                    print(f"    Organization: {user.organization.name}")
        
        # Show database type
        print(f"\n💾 Database Type: ", end="")
        if settings.database_url.startswith("sqlite"):
            print("SQLite (Development)")
            print(f"   File: {settings.database_url.replace('sqlite:///', '')}")
        elif settings.database_url.startswith("postgresql"):
            print("PostgreSQL")
            db_parts = settings.database_url.split('/')
            print(f"   Database: {db_parts[-1]}")
        
        session.close()
        
        return stats
        
    except Exception as e:
        print(f"❌ Database Error: {e}")
        return None

def show_sample_queries():
    """Show some sample SQL queries for reference"""
    print("\n📝 Sample SQL Queries:")
    print("\n-- Find all recruiters:")
    print("SELECT * FROM users WHERE role = 'recruiter';")
    print("\n-- Find jobs by organization:")
    print("SELECT j.*, o.name as org_name")
    print("FROM jobs j")
    print("JOIN organizations o ON j.organization_id = o.id;")
    print("\n-- Find applications for a job:")
    print("SELECT a.*, c.name as candidate_name")
    print("FROM applications a")
    print("JOIN candidates c ON a.candidate_id = c.id")
    print("WHERE a.job_id = 'your-job-id';")

if __name__ == "__main__":
    stats = check_database()
    if stats:
        show_sample_queries()
        print("\n✅ Database check complete!")
    else:
        print("\n❌ Database check failed!")
        print("\nTroubleshooting:")
        print("1. Make sure the database service is running")
        print("2. Check your .env file for correct credentials")
        print("3. Try running: python run.py")