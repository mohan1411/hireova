from pydantic import BaseModel
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime

class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: Optional[str] = None
    job_type: Optional[str] = None
    experience_level: Optional[str] = None
    salary_min: Optional[str] = None
    salary_max: Optional[str] = None

class JobCreate(JobBase):
    requirements: Optional[Dict[str, Any]] = None

class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    requirements: Optional[Dict[str, Any]] = None
    location: Optional[str] = None
    job_type: Optional[str] = None
    experience_level: Optional[str] = None
    salary_min: Optional[str] = None
    salary_max: Optional[str] = None
    status: Optional[str] = None

class JobResponse(JobBase):
    id: UUID
    organization_id: UUID
    requirements: Optional[Dict[str, Any]]
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True