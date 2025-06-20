from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict, Any
from uuid import UUID
from datetime import datetime

class CandidateBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None

class CandidateCreate(CandidateBase):
    resume_text: Optional[str] = None
    source: str = "upload"

class CandidateUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin_url: Optional[str] = None
    skills: Optional[List[str]] = None
    experience_years: Optional[str] = None

class CandidateResponse(CandidateBase):
    id: UUID
    skills: Optional[List[str]]
    experience_years: Optional[str]
    source: str
    created_at: datetime
    
    class Config:
        from_attributes = True