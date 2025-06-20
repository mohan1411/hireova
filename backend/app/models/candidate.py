from sqlalchemy import Column, String, Text, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid
from datetime import datetime

class Candidate(Base):
    __tablename__ = "candidates"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), nullable=False, index=True)
    name = Column(String(255))
    phone = Column(String(50))
    location = Column(String(255))
    linkedin_url = Column(String(500))
    linkedin_id = Column(String(255), unique=True, nullable=True)
    resume_url = Column(String(500))
    resume_text = Column(Text)
    parsed_data = Column(JSON)  # Structured resume data
    skills = Column(JSON)  # List of skills
    experience_years = Column(String(20))
    source = Column(String(50))  # linkedin, upload, email, etc.
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_matched = Column(DateTime)
    
    # Relationships
    applications = relationship("Application", back_populates="candidate")