from pydantic import BaseModel
from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime

class ApplicationBase(BaseModel):
    job_id: UUID
    candidate_id: UUID

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    status: Optional[str] = None
    notes: Optional[str] = None

class ApplicationResponse(ApplicationBase):
    id: UUID
    status: str
    ai_score: Optional[float]
    ai_analysis: Optional[Dict[str, Any]]
    created_at: datetime
    
    class Config:
        from_attributes = True