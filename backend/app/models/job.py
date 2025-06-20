from sqlalchemy import Column, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.core.database import Base
import uuid
from datetime import datetime

class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    organization_id = Column(UUID(as_uuid=True), ForeignKey("organizations.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    requirements = Column(JSON)
    location = Column(String(255))
    job_type = Column(String(50))  # full-time, part-time, contract, etc.
    experience_level = Column(String(50))  # entry, mid, senior, etc.
    salary_min = Column(String(50))
    salary_max = Column(String(50))
    status = Column(String(50), default="active")  # active, paused, closed
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    organization = relationship("Organization", back_populates="jobs")
    applications = relationship("Application", back_populates="job")