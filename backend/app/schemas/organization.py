from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class OrganizationBase(BaseModel):
    name: str
    domain: Optional[str] = None
    industry: Optional[str] = None
    size: Optional[str] = None

class OrganizationCreate(OrganizationBase):
    pass

class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    industry: Optional[str] = None
    size: Optional[str] = None

class OrganizationResponse(OrganizationBase):
    id: UUID
    plan: str
    created_at: datetime
    
    class Config:
        from_attributes = True