# Hirova AI - Technical Implementation Guide for Multiple Application Methods

## Overview

This guide details the technical implementation of Hirova AI's multiple application methods, including the AI Talent Scout feature that proactively mines existing resume databases, ensuring both active applications and passive candidate discovery while maintaining data consistency and security.

## Application Methods Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Application Entry Points                     │
├─────────────┬──────────────┬──────────────┬────────────────────┤
│  LinkedIn   │    Email     │  Job Boards  │   Direct Input    │
│   OAuth     │   Parser     │  (Indeed)    │  (Upload/Paste)   │
└──────┬──────┴───────┬──────┴───────┬──────┴─────────┬──────────┘
       │              │              │                │
       └──────────────┴──────────────┴────────────────┘
                              │
                              ├──────────────────────────┐
                              │                          │
                    ┌─────────▼─────────┐      ┌────────▼────────┐
                    │  Unified Resume   │      │  AI Talent      │
                    │   Processing API  │      │  Scout Engine   │
                    └─────────┬─────────┘      └────────┬────────┘
                              │                          │
                              │     ┌────────────────┐   │
                              │     │ Resume Database│   │
                              │     │   Mining API   │───┘
                              │     └────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   AI Parser &     │
                    │   Standardizer    │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │  Candidate Record │
                    │    Database       │
                    └───────────────────┘
```

## 1. LinkedIn Integration

### OAuth2 Flow Implementation

```python
# app/services/linkedin_service.py
import httpx
from urllib.parse import urlencode
from app.core.config import settings

class LinkedInService:
    OAUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
    TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
    PROFILE_URL = "https://api.linkedin.com/v2/me"
    
    def get_authorization_url(self, job_id: str) -> str:
        """Generate LinkedIn OAuth URL"""
        params = {
            "response_type": "code",
            "client_id": settings.linkedin_client_id,
            "redirect_uri": f"{settings.app_url}/auth/linkedin/callback",
            "state": job_id,  # Pass job_id in state
            "scope": "r_liteprofile r_emailaddress"
        }
        return f"{self.OAUTH_URL}?{urlencode(params)}"
    
    async def exchange_code_for_token(self, code: str) -> str:
        """Exchange authorization code for access token"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.TOKEN_URL,
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "redirect_uri": f"{settings.app_url}/auth/linkedin/callback",
                    "client_id": settings.linkedin_client_id,
                    "client_secret": settings.linkedin_client_secret
                }
            )
            return response.json()["access_token"]
    
    async def get_profile_data(self, access_token: str) -> dict:
        """Fetch LinkedIn profile data"""
        headers = {"Authorization": f"Bearer {access_token}"}
        
        async with httpx.AsyncClient() as client:
            # Get basic profile
            profile_response = await client.get(
                self.PROFILE_URL,
                headers=headers
            )
            profile = profile_response.json()
            
            # Get email
            email_response = await client.get(
                "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))",
                headers=headers
            )
            email_data = email_response.json()
            
            return {
                "linkedin_id": profile["id"],
                "first_name": profile["localizedFirstName"],
                "last_name": profile["localizedLastName"],
                "email": email_data["elements"][0]["handle~"]["emailAddress"],
                "profile_url": f"https://linkedin.com/in/{profile['vanityName']}"
            }
```

### LinkedIn Data Parser

```python
# app/services/linkedin_parser.py
from typing import Dict, List
import re

class LinkedInParser:
    def parse_profile_to_resume(self, linkedin_data: dict) -> dict:
        """Convert LinkedIn profile to standardized resume format"""
        return {
            "personal_info": {
                "name": f"{linkedin_data['first_name']} {linkedin_data['last_name']}",
                "email": linkedin_data["email"],
                "linkedin_url": linkedin_data["profile_url"],
                "location": linkedin_data.get("location", {}).get("name", "")
            },
            "experience": self._parse_experience(linkedin_data.get("positions", [])),
            "education": self._parse_education(linkedin_data.get("educations", [])),
            "skills": self._parse_skills(linkedin_data.get("skills", [])),
            "summary": linkedin_data.get("summary", ""),
            "source": "linkedin",
            "raw_data": linkedin_data
        }
    
    def _parse_experience(self, positions: List[Dict]) -> List[Dict]:
        """Extract work experience"""
        experience = []
        for position in positions:
            exp = {
                "title": position.get("title", ""),
                "company": position.get("company", {}).get("name", ""),
                "location": position.get("location", ""),
                "start_date": self._format_date(position.get("startDate", {})),
                "end_date": self._format_date(position.get("endDate", {})),
                "description": position.get("description", ""),
                "is_current": position.get("isCurrent", False)
            }
            experience.append(exp)
        return experience
    
    def _format_date(self, date_obj: dict) -> str:
        """Format LinkedIn date object"""
        if not date_obj:
            return "Present"
        year = date_obj.get("year", "")
        month = date_obj.get("month", "")
        return f"{month}/{year}" if month else str(year)
```

## 2. Email Application Processing

### Email Parser Service

```python
# app/services/email_parser.py
import email
import imaplib
from typing import List, Tuple
import asyncio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import aiosmtplib

class EmailApplicationService:
    def __init__(self):
        self.imap_server = settings.email_imap_server
        self.smtp_server = settings.email_smtp_server
        self.email_address = settings.email_address
        self.email_password = settings.email_password
    
    async def process_email_applications(self):
        """Check for new email applications"""
        while True:
            try:
                emails = self._fetch_unread_emails()
                for email_data in emails:
                    await self._process_single_email(email_data)
            except Exception as e:
                logger.error(f"Email processing error: {e}")
            
            await asyncio.sleep(60)  # Check every minute
    
    def _fetch_unread_emails(self) -> List[dict]:
        """Fetch unread emails from inbox"""
        mail = imaplib.IMAP4_SSL(self.imap_server)
        mail.login(self.email_address, self.email_password)
        mail.select('inbox')
        
        # Search for unread emails
        status, messages = mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()
        
        emails = []
        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            email_body = msg_data[0][1]
            message = email.message_from_bytes(email_body)
            
            emails.append({
                "id": email_id,
                "from": message['From'],
                "to": message['To'],
                "subject": message['Subject'],
                "message": message,
                "body": self._get_email_body(message),
                "attachments": self._get_attachments(message)
            })
            
            # Mark as read
            mail.store(email_id, '+FLAGS', '\\Seen')
        
        mail.close()
        mail.logout()
        return emails
    
    async def _process_single_email(self, email_data: dict):
        """Process a single email application"""
        # Extract job ID from email address (e.g., apply-job123@company.hirova.ai)
        to_address = email_data['to']
        job_id = self._extract_job_id(to_address)
        
        if not job_id:
            await self._send_error_response(email_data['from'], "Invalid job application email")
            return
        
        # Extract candidate info
        candidate_email = self._extract_sender_email(email_data['from'])
        
        # Process attachments (resumes)
        resume_data = None
        for attachment in email_data['attachments']:
            if self._is_resume_file(attachment['filename']):
                resume_data = await self._parse_resume_attachment(attachment)
                break
        
        if not resume_data:
            # Try to extract from email body
            resume_data = self._extract_from_body(email_data['body'])
        
        if resume_data:
            # Create candidate record
            candidate = await self._create_candidate(
                email=candidate_email,
                job_id=job_id,
                resume_data=resume_data,
                source="email"
            )
            
            # Send confirmation
            await self._send_confirmation_email(candidate_email, candidate.id, job_id)
        else:
            await self._send_error_response(
                candidate_email, 
                "No resume found. Please attach your resume or include it in the email body."
            )
    
    def _extract_job_id(self, to_address: str) -> str:
        """Extract job ID from email address"""
        import re
        match = re.match(r'apply-(.+?)@', to_address)
        return match.group(1) if match else None
    
    async def _send_confirmation_email(self, to_email: str, candidate_id: str, job_id: str):
        """Send application confirmation"""
        message = MIMEMultipart()
        message['From'] = self.email_address
        message['To'] = to_email
        message['Subject'] = "Application Received - Hirova AI"
        
        body = f"""
        Thank you for your application!
        
        We've received your resume and you're now in our system.
        
        Your application ID: {candidate_id}
        
        What happens next:
        1. Our AI will review your application within the next hour
        2. You'll receive an invitation for an AI screening conversation
        3. If you're a match, the hiring team will be notified
        
        Track your application: {settings.app_url}/application/{candidate_id}
        
        Best regards,
        Hirova AI Team
        """
        
        message.attach(MIMEText(body, 'plain'))
        
        async with aiosmtplib.SMTP(hostname=self.smtp_server, port=587) as smtp:
            await smtp.login(self.email_address, self.email_password)
            await smtp.send_message(message)
```

## 3. Indeed Integration

### Indeed API Integration

```python
# app/services/indeed_service.py
import httpx
from typing import Optional

class IndeedService:
    def __init__(self):
        self.api_key = settings.indeed_api_key
        self.base_url = "https://api.indeed.com/v1"
    
    async def import_candidate_profile(self, indeed_resume_id: str) -> dict:
        """Import candidate data from Indeed"""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/resume/{indeed_resume_id}",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            
            indeed_data = response.json()
            return self._parse_indeed_profile(indeed_data)
    
    def _parse_indeed_profile(self, indeed_data: dict) -> dict:
        """Convert Indeed profile to standard format"""
        return {
            "personal_info": {
                "name": indeed_data.get("name", ""),
                "email": indeed_data.get("email", ""),
                "phone": indeed_data.get("phone", ""),
                "location": indeed_data.get("location", {}).get("city", "")
            },
            "experience": self._parse_indeed_experience(indeed_data.get("work", [])),
            "education": self._parse_indeed_education(indeed_data.get("education", [])),
            "skills": indeed_data.get("skills", []),
            "source": "indeed",
            "indeed_id": indeed_data.get("id"),
            "raw_data": indeed_data
        }
    
    async def setup_indeed_apply(self, job_id: str) -> dict:
        """Setup Indeed Apply button for a job"""
        job_data = await self._get_job_data(job_id)
        
        indeed_job = {
            "title": job_data.title,
            "company": job_data.company_name,
            "location": job_data.location,
            "description": job_data.description,
            "apply_url": f"{settings.app_url}/apply/indeed/{job_id}"
        }
        
        # Post to Indeed
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/jobs",
                json=indeed_job,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            
        return response.json()
```

## 4. Direct Input Methods

### File Upload Handler

```python
# app/api/upload.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import Optional
import aiofiles
import os

router = APIRouter()

ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.doc', '.txt'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

@router.post("/upload-resume/{job_id}")
async def upload_resume(
    job_id: str,
    file: UploadFile = File(...),
    email: Optional[str] = None
):
    """Handle direct resume upload"""
    # Validate file
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, f"File type {file_ext} not allowed")
    
    # Check file size
    content = await file.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(413, "File too large")
    
    # Save file temporarily
    temp_path = f"/tmp/{file.filename}"
    async with aiofiles.open(temp_path, 'wb') as f:
        await f.write(content)
    
    # Parse resume
    parser = ResumeParser()
    resume_data = await parser.parse_file(temp_path)
    
    # Create candidate
    candidate = await create_candidate(
        job_id=job_id,
        email=email or resume_data.get("email"),
        resume_data=resume_data,
        source="upload",
        file_path=temp_path
    )
    
    return {
        "candidate_id": candidate.id,
        "status": "processing",
        "next_step": "ai_screening"
    }
```

### Copy-Paste Text Handler

```python
# app/api/text_application.py
from pydantic import BaseModel

class TextApplicationRequest(BaseModel):
    job_id: str
    resume_text: str
    email: str
    name: Optional[str] = None

@router.post("/apply-with-text")
async def apply_with_text(request: TextApplicationRequest):
    """Handle copy-pasted resume text"""
    # Use AI to parse unstructured text
    ai_parser = AIResumeParser()
    resume_data = await ai_parser.parse_text(request.resume_text)
    
    # Enhance with provided info
    resume_data["email"] = request.email
    if request.name:
        resume_data["name"] = request.name
    
    # Create candidate
    candidate = await create_candidate(
        job_id=request.job_id,
        email=request.email,
        resume_data=resume_data,
        source="text_input"
    )
    
    return {
        "candidate_id": candidate.id,
        "parsed_data": resume_data,
        "confidence_score": ai_parser.confidence_score
    }
```

### Resume Builder

```python
# app/api/resume_builder.py
from pydantic import BaseModel
from typing import List, Optional

class WorkExperience(BaseModel):
    title: str
    company: str
    location: Optional[str]
    start_date: str
    end_date: Optional[str]
    description: str
    is_current: bool = False

class Education(BaseModel):
    degree: str
    institution: str
    graduation_year: Optional[int]
    gpa: Optional[float]

class ResumeBuilderRequest(BaseModel):
    job_id: str
    personal_info: dict
    experience: List[WorkExperience]
    education: List[Education]
    skills: List[str]
    summary: Optional[str]

@router.post("/build-resume")
async def build_resume(request: ResumeBuilderRequest):
    """Handle resume builder submissions"""
    # Structure the data
    resume_data = {
        "personal_info": request.personal_info,
        "experience": [exp.dict() for exp in request.experience],
        "education": [edu.dict() for edu in request.education],
        "skills": request.skills,
        "summary": request.summary,
        "source": "builder"
    }
    
    # AI enhancement
    ai_enhancer = ResumeEnhancer()
    enhanced_resume = await ai_enhancer.enhance(resume_data, request.job_id)
    
    # Create candidate
    candidate = await create_candidate(
        job_id=request.job_id,
        email=request.personal_info["email"],
        resume_data=enhanced_resume,
        source="resume_builder"
    )
    
    return {
        "candidate_id": candidate.id,
        "enhancements": ai_enhancer.get_suggestions()
    }
```

## 5. Unified Resume Processing

### Central Resume Processor

```python
# app/services/resume_processor.py
from typing import Dict, Any
import asyncio

class UnifiedResumeProcessor:
    def __init__(self):
        self.parser = ResumeParser()
        self.standardizer = ResumeStandardizer()
        self.ai_enhancer = AIEnhancer()
        self.validator = ResumeValidator()
    
    async def process_resume(
        self,
        raw_data: Any,
        source: str,
        job_id: str
    ) -> Dict:
        """Process resume from any source into standardized format"""
        
        # Parse based on source
        if source == "linkedin":
            parsed = self.parser.parse_linkedin(raw_data)
        elif source == "indeed":
            parsed = self.parser.parse_indeed(raw_data)
        elif source == "email":
            parsed = await self.parser.parse_email_attachment(raw_data)
        elif source == "upload":
            parsed = await self.parser.parse_file(raw_data)
        elif source == "text_input":
            parsed = await self.parser.parse_text(raw_data)
        elif source == "resume_builder":
            parsed = raw_data  # Already structured
        else:
            raise ValueError(f"Unknown source: {source}")
        
        # Standardize format
        standardized = self.standardizer.standardize(parsed)
        
        # Validate required fields
        validation_result = self.validator.validate(standardized)
        if not validation_result.is_valid:
            standardized = await self.ai_enhancer.fill_missing_fields(
                standardized,
                validation_result.missing_fields
            )
        
        # Extract skills using AI
        if not standardized.get("skills"):
            standardized["skills"] = await self.ai_enhancer.extract_skills(
                standardized
            )
        
        # Calculate match score
        job_requirements = await self._get_job_requirements(job_id)
        match_score = await self.calculate_match_score(
            standardized,
            job_requirements
        )
        
        return {
            "resume_data": standardized,
            "source": source,
            "match_score": match_score,
            "processing_timestamp": datetime.utcnow(),
            "job_id": job_id
        }
```

## 6. Mobile Optimizations

### Mobile-Specific Handlers

```python
# app/api/mobile.py
from fastapi import APIRouter, Request
from user_agents import parse

router = APIRouter()

@router.post("/mobile-apply/{job_id}")
async def mobile_apply(job_id: str, request: Request):
    """Optimized mobile application endpoint"""
    user_agent = parse(request.headers.get("user-agent", ""))
    
    if user_agent.is_mobile:
        # Return mobile-optimized options
        return {
            "methods": [
                {
                    "type": "linkedin",
                    "enabled": True,
                    "url": f"/auth/linkedin?job_id={job_id}&mobile=true",
                    "priority": 1
                },
                {
                    "type": "indeed",
                    "enabled": await check_indeed_app_installed(),
                    "url": f"indeed://apply?job_id={job_id}",
                    "priority": 2
                },
                {
                    "type": "camera",
                    "enabled": True,
                    "url": f"/mobile/camera-upload/{job_id}",
                    "priority": 3
                },
                {
                    "type": "cloud",
                    "enabled": True,
                    "providers": ["google_drive", "dropbox", "icloud"],
                    "priority": 4
                }
            ]
        }
```

### Camera Resume Capture

```python
# app/api/camera_capture.py
import base64
from PIL import Image
import pytesseract

@router.post("/camera-upload/{job_id}")
async def camera_upload(
    job_id: str,
    image_data: str,  # Base64 encoded image
    email: str
):
    """Handle camera-captured resume images"""
    # Decode base64 image
    image_bytes = base64.b64decode(image_data)
    image = Image.open(io.BytesIO(image_bytes))
    
    # OCR to extract text
    text = pytesseract.image_to_string(image)
    
    # Parse with AI
    ai_parser = AIResumeParser()
    resume_data = await ai_parser.parse_text(text)
    
    # Store original image
    image_path = await store_image(image_bytes, f"{job_id}_{email}")
    
    # Create candidate
    candidate = await create_candidate(
        job_id=job_id,
        email=email,
        resume_data=resume_data,
        source="camera",
        original_file=image_path
    )
    
    return {
        "candidate_id": candidate.id,
        "ocr_confidence": ai_parser.confidence_score
    }
```

## 7. Data Consistency & Deduplication

### Candidate Deduplication Service

```python
# app/services/deduplication.py
from typing import Optional
import hashlib

class CandidateDeduplicationService:
    async def find_existing_candidate(
        self,
        email: str,
        phone: Optional[str] = None,
        linkedin_id: Optional[str] = None
    ) -> Optional[Candidate]:
        """Find existing candidate by multiple identifiers"""
        # Check by email first (primary identifier)
        candidate = await self.db.query(Candidate).filter(
            Candidate.email == email
        ).first()
        
        if candidate:
            return candidate
        
        # Check by LinkedIn ID
        if linkedin_id:
            candidate = await self.db.query(Candidate).filter(
                Candidate.linkedin_id == linkedin_id
            ).first()
            if candidate:
                return candidate
        
        # Check by phone (if provided)
        if phone:
            normalized_phone = self._normalize_phone(phone)
            candidate = await self.db.query(Candidate).filter(
                Candidate.phone == normalized_phone
            ).first()
        
        return candidate
    
    async def merge_candidate_data(
        self,
        existing: Candidate,
        new_data: dict,
        source: str
    ) -> Candidate:
        """Merge new application data with existing candidate"""
        # Update with newer/better data
        if source in ["linkedin", "indeed"] and not existing.verified_email:
            existing.email = new_data.get("email", existing.email)
            existing.verified_email = True
        
        # Merge skills (union of both)
        existing_skills = set(existing.skills or [])
        new_skills = set(new_data.get("skills", []))
        existing.skills = list(existing_skills.union(new_skills))
        
        # Update experience if more recent
        if new_data.get("experience"):
            existing.experience = self._merge_experience(
                existing.experience,
                new_data["experience"]
            )
        
        # Track application source
        existing.application_sources = existing.application_sources or []
        if source not in existing.application_sources:
            existing.application_sources.append(source)
        
        await self.db.commit()
        return existing
```

## 8. Analytics & Monitoring

### Application Method Analytics

```python
# app/services/analytics.py
from typing import Dict
import asyncio

class ApplicationAnalytics:
    async def track_application_method(
        self,
        job_id: str,
        method: str,
        success: bool,
        time_taken: float
    ):
        """Track which application methods are most effective"""
        await self.redis.hincrby(
            f"stats:job:{job_id}:methods",
            f"{method}:attempts",
            1
        )
        
        if success:
            await self.redis.hincrby(
                f"stats:job:{job_id}:methods",
                f"{method}:success",
                1
            )
        
        # Track average time
        await self.redis.lpush(
            f"stats:job:{job_id}:methods:{method}:times",
            time_taken
        )
        
        # Trim to last 100 entries
        await self.redis.ltrim(
            f"stats:job:{job_id}:methods:{method}:times",
            0,
            99
        )
    
    async def get_method_effectiveness(self, job_id: str) -> Dict:
        """Get conversion rates by application method"""
        stats = await self.redis.hgetall(f"stats:job:{job_id}:methods")
        
        methods_data = {}
        for key, value in stats.items():
            method, metric = key.rsplit(":", 1)
            if method not in methods_data:
                methods_data[method] = {"attempts": 0, "success": 0}
            methods_data[method][metric] = int(value)
        
        # Calculate conversion rates
        for method, data in methods_data.items():
            if data["attempts"] > 0:
                data["conversion_rate"] = data["success"] / data["attempts"]
            else:
                data["conversion_rate"] = 0
        
        return methods_data
```

## 9. Security Considerations

### Input Validation

```python
# app/security/validators.py
import re
from typing import Optional

class ApplicationSecurityValidator:
    def validate_email_attachment(self, attachment: dict) -> bool:
        """Validate email attachments for security"""
        # Check file type
        allowed_types = {
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'text/plain'
        }
        
        if attachment.get('content_type') not in allowed_types:
            return False
        
        # Check file size (max 10MB)
        if attachment.get('size', 0) > 10 * 1024 * 1024:
            return False
        
        # Scan for malicious content (simplified)
        content = attachment.get('content', b'')
        if b'<script' in content.lower():
            return False
        
        return True
    
    def sanitize_text_input(self, text: str) -> str:
        """Sanitize copy-pasted resume text"""
        # Remove potential XSS
        text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL)
        text = re.sub(r'<.*?>', '', text)
        
        # Remove excessive whitespace
        text = ' '.join(text.split())
        
        # Limit length
        return text[:50000]  # Max 50k characters
```

## 10. AI Talent Scout - Resume Database Mining

### Resume Folder Import Service

```python
# app/services/talent_scout.py
import os
import asyncio
from typing import List, Dict, Optional
from pathlib import Path
import hashlib
from datetime import datetime, timedelta
import schedule
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ResumeFolderImporter:
    def __init__(self):
        self.supported_extensions = {'.pdf', '.docx', '.doc', '.txt'}
        self.import_queue = asyncio.Queue()
        self.processed_files = set()  # Track processed files by hash
        
    async def bulk_import_folder(
        self,
        folder_path: str,
        job_ids: Optional[List[str]] = None,
        recursive: bool = True
    ) -> Dict:
        """Import all resumes from a folder"""
        folder = Path(folder_path)
        if not folder.exists():
            raise ValueError(f"Folder {folder_path} does not exist")
        
        results = {
            "total_files": 0,
            "processed": 0,
            "duplicates": 0,
            "errors": 0,
            "matches_found": 0
        }
        
        # Scan folder for resume files
        pattern = "**/*" if recursive else "*"
        for file_path in folder.glob(pattern):
            if file_path.suffix.lower() in self.supported_extensions:
                results["total_files"] += 1
                
                # Check if already processed
                file_hash = self._calculate_file_hash(file_path)
                if file_hash in self.processed_files:
                    results["duplicates"] += 1
                    continue
                
                # Add to processing queue
                await self.import_queue.put({
                    "file_path": str(file_path),
                    "file_hash": file_hash,
                    "job_ids": job_ids,
                    "source": f"folder:{folder_path}"
                })
        
        # Process queue
        await self._process_import_queue(results)
        
        return results
    
    async def _process_import_queue(self, results: Dict):
        """Process queued files"""
        batch_size = 10
        batch = []
        
        while not self.import_queue.empty():
            file_data = await self.import_queue.get()
            batch.append(file_data)
            
            if len(batch) >= batch_size:
                await self._process_batch(batch, results)
                batch = []
        
        # Process remaining files
        if batch:
            await self._process_batch(batch, results)
    
    async def _process_batch(self, batch: List[Dict], results: Dict):
        """Process a batch of files concurrently"""
        tasks = []
        for file_data in batch:
            task = self._process_single_file(file_data, results)
            tasks.append(task)
        
        await asyncio.gather(*tasks)
    
    async def _process_single_file(
        self,
        file_data: Dict,
        results: Dict
    ):
        """Process a single resume file"""
        try:
            # Parse resume
            parser = ResumeParser()
            resume_data = await parser.parse_file(file_data["file_path"])
            
            # Check for existing candidate
            existing = await self._find_existing_candidate(
                resume_data.get("email"),
                resume_data.get("phone")
            )
            
            if existing:
                # Update existing candidate
                await self._update_candidate(
                    existing,
                    resume_data,
                    file_data["source"]
                )
            else:
                # Create new candidate
                candidate = await self._create_candidate(
                    resume_data,
                    file_data["source"],
                    file_data["file_path"]
                )
            
            # AI matching if job_ids specified
            if file_data.get("job_ids"):
                matches = await self._match_to_jobs(
                    candidate,
                    file_data["job_ids"]
                )
                if matches:
                    results["matches_found"] += len(matches)
            
            # Mark as processed
            self.processed_files.add(file_data["file_hash"])
            results["processed"] += 1
            
        except Exception as e:
            logger.error(f"Error processing {file_data['file_path']}: {e}")
            results["errors"] += 1
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash of file content"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
```

### AI Talent Scout Engine

```python
# app/services/ai_talent_scout.py
from typing import List, Dict, Optional
import asyncio
from datetime import datetime, timedelta
from sqlalchemy import select, and_

class AITalentScout:
    def __init__(self):
        self.min_match_score = 85
        self.scan_interval = timedelta(hours=1)
        self.notification_service = NotificationService()
        
    async def configure_scout(
        self,
        sources: List[Dict],
        job_ids: List[str],
        match_criteria: Dict,
        scan_frequency: str = "hourly"
    ):
        """Configure AI Talent Scout settings"""
        scout_config = {
            "id": str(uuid.uuid4()),
            "sources": sources,
            "job_ids": job_ids,
            "match_criteria": match_criteria,
            "scan_frequency": scan_frequency,
            "created_at": datetime.utcnow(),
            "is_active": True
        }
        
        # Save configuration
        await self.db.save("scout_configs", scout_config)
        
        # Schedule scanning
        if scan_frequency == "realtime":
            await self._setup_realtime_monitoring(sources)
        else:
            await self._schedule_periodic_scan(scout_config)
        
        return scout_config
    
    async def scan_for_matches(self, config_id: str) -> Dict:
        """Run AI matching scan on configured sources"""
        config = await self.db.get("scout_configs", config_id)
        if not config or not config["is_active"]:
            return {"error": "Invalid or inactive configuration"}
        
        results = {
            "scan_id": str(uuid.uuid4()),
            "started_at": datetime.utcnow(),
            "candidates_scanned": 0,
            "new_matches": [],
            "updated_matches": []
        }
        
        # Get job requirements
        jobs = await self._get_jobs_data(config["job_ids"])
        
        # Scan each source
        for source in config["sources"]:
            if source["type"] == "folder":
                await self._scan_folder_source(
                    source,
                    jobs,
                    config["match_criteria"],
                    results
                )
            elif source["type"] == "database":
                await self._scan_database_source(
                    source,
                    jobs,
                    config["match_criteria"],
                    results
                )
        
        # Send notifications for new matches
        if results["new_matches"]:
            await self._notify_new_matches(results["new_matches"])
        
        # Save scan results
        results["completed_at"] = datetime.utcnow()
        await self.db.save("scout_scans", results)
        
        return results
    
    async def _scan_database_source(
        self,
        source: Dict,
        jobs: List[Dict],
        criteria: Dict,
        results: Dict
    ):
        """Scan existing database for matches"""
        # Query candidates not recently matched
        last_scan = datetime.utcnow() - timedelta(days=criteria.get("rescan_days", 30))
        
        query = select(Candidate).where(
            and_(
                Candidate.source.like(f"%{source['filter']}%"),
                or_(
                    Candidate.last_matched == None,
                    Candidate.last_matched < last_scan
                )
            )
        )
        
        candidates = await self.db.execute(query)
        
        for candidate in candidates:
            results["candidates_scanned"] += 1
            
            # Run AI matching against all jobs
            for job in jobs:
                match_score = await self._calculate_match_score(
                    candidate,
                    job,
                    criteria
                )
                
                if match_score >= self.min_match_score:
                    match_data = {
                        "candidate_id": candidate.id,
                        "job_id": job["id"],
                        "match_score": match_score,
                        "discovered_at": datetime.utcnow(),
                        "source": "ai_scout",
                        "scout_config_id": source["config_id"]
                    }
                    
                    # Check if this is a new match
                    existing_match = await self._find_existing_match(
                        candidate.id,
                        job["id"]
                    )
                    
                    if existing_match:
                        results["updated_matches"].append(match_data)
                    else:
                        results["new_matches"].append(match_data)
                        await self._save_match(match_data)
            
            # Update last matched timestamp
            candidate.last_matched = datetime.utcnow()
            await self.db.commit()
    
    async def _calculate_match_score(
        self,
        candidate: Candidate,
        job: Dict,
        criteria: Dict
    ) -> float:
        """Calculate AI match score between candidate and job"""
        # Prepare data for AI
        candidate_text = self._prepare_candidate_text(candidate)
        job_text = self._prepare_job_text(job)
        
        # Call AI matching service
        prompt = f"""
        Analyze the match between this candidate and job.
        
        Candidate Profile:
        {candidate_text}
        
        Job Requirements:
        {job_text}
        
        Matching Criteria:
        - Required skills weight: {criteria.get('skill_weight', 40)}%
        - Experience weight: {criteria.get('experience_weight', 30)}%
        - Education weight: {criteria.get('education_weight', 10)}%
        - Location weight: {criteria.get('location_weight', 20)}%
        
        Return a match score from 0-100 and explain key strengths and gaps.
        """
        
        ai_response = await self.ai_service.analyze(prompt)
        return ai_response["match_score"]
```

### Folder Monitoring Service

```python
# app/services/folder_monitor.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ResumeFolderMonitor(FileSystemEventHandler):
    def __init__(self, scout_engine: AITalentScout):
        self.scout_engine = scout_engine
        self.observer = Observer()
        self.monitored_folders = {}
        self.executor = ThreadPoolExecutor(max_workers=5)
        
    def start_monitoring(self, folder_path: str, config: Dict):
        """Start monitoring a folder for new resumes"""
        event_handler = ResumeFolderHandler(
            folder_path,
            config,
            self.scout_engine
        )
        
        self.observer.schedule(
            event_handler,
            folder_path,
            recursive=config.get("recursive", True)
        )
        
        self.monitored_folders[folder_path] = {
            "config": config,
            "handler": event_handler
        }
        
        if not self.observer.is_alive():
            self.observer.start()
    
    def stop_monitoring(self, folder_path: str):
        """Stop monitoring a specific folder"""
        if folder_path in self.monitored_folders:
            # Remove handler
            del self.monitored_folders[folder_path]
            
            # Stop observer if no more folders
            if not self.monitored_folders:
                self.observer.stop()
                self.observer.join()

class ResumeFolderHandler(FileSystemEventHandler):
    def __init__(self, folder_path: str, config: Dict, scout_engine):
        self.folder_path = folder_path
        self.config = config
        self.scout_engine = scout_engine
        self.supported_extensions = {'.pdf', '.docx', '.doc', '.txt'}
        
    def on_created(self, event):
        """Handle new file creation"""
        if not event.is_directory:
            file_path = Path(event.src_path)
            if file_path.suffix.lower() in self.supported_extensions:
                # Process in background
                asyncio.create_task(
                    self._process_new_file(file_path)
                )
    
    def on_modified(self, event):
        """Handle file modification"""
        if not event.is_directory:
            file_path = Path(event.src_path)
            if file_path.suffix.lower() in self.supported_extensions:
                # Wait a bit for file to finish writing
                asyncio.create_task(
                    self._process_modified_file(file_path)
                )
    
    async def _process_new_file(self, file_path: Path):
        """Process newly added resume file"""
        try:
            # Wait for file to be fully written
            await asyncio.sleep(2)
            
            # Import and match
            importer = ResumeFolderImporter()
            results = await importer.bulk_import_folder(
                str(file_path.parent),
                job_ids=self.config.get("job_ids"),
                recursive=False
            )
            
            # Log activity
            logger.info(
                f"New resume detected: {file_path.name}, "
                f"Matches found: {results['matches_found']}"
            )
            
        except Exception as e:
            logger.error(f"Error processing new file {file_path}: {e}")
```

### Database Mining Scheduler

```python
# app/tasks/scout_scheduler.py
import schedule
import asyncio
from datetime import datetime

class ScoutScheduler:
    def __init__(self, scout_engine: AITalentScout):
        self.scout_engine = scout_engine
        self.active_configs = {}
        
    async def start(self):
        """Start the scheduler"""
        # Load active configurations
        configs = await self.db.query(
            "SELECT * FROM scout_configs WHERE is_active = true"
        )
        
        for config in configs:
            self._schedule_config(config)
        
        # Run scheduler
        while True:
            schedule.run_pending()
            await asyncio.sleep(60)  # Check every minute
    
    def _schedule_config(self, config: Dict):
        """Schedule scanning based on frequency"""
        config_id = config["id"]
        frequency = config["scan_frequency"]
        
        if frequency == "hourly":
            schedule.every().hour.do(
                lambda: asyncio.create_task(
                    self.scout_engine.scan_for_matches(config_id)
                )
            )
        elif frequency == "daily":
            schedule.every().day.at("02:00").do(
                lambda: asyncio.create_task(
                    self.scout_engine.scan_for_matches(config_id)
                )
            )
        elif frequency == "weekly":
            schedule.every().monday.at("03:00").do(
                lambda: asyncio.create_task(
                    self.scout_engine.scan_for_matches(config_id)
                )
            )
        
        self.active_configs[config_id] = config
```

### Analytics for Database Mining

```python
# app/services/scout_analytics.py
class ScoutAnalytics:
    async def get_scout_performance(self, days: int = 30) -> Dict:
        """Get AI Talent Scout performance metrics"""
        since = datetime.utcnow() - timedelta(days=days)
        
        # Get scan statistics
        scans = await self.db.query(
            """
            SELECT 
                COUNT(*) as total_scans,
                SUM(candidates_scanned) as total_candidates,
                SUM(ARRAY_LENGTH(new_matches, 1)) as total_matches
            FROM scout_scans
            WHERE started_at > %s
            """,
            [since]
        )
        
        # Get match outcomes
        outcomes = await self.db.query(
            """
            SELECT 
                COUNT(CASE WHEN interviewed THEN 1 END) as interviewed,
                COUNT(CASE WHEN hired THEN 1 END) as hired
            FROM scout_matches
            WHERE discovered_at > %s
            """,
            [since]
        )
        
        # Calculate ROI
        costs_saved = outcomes["hired"] * 4129  # Average cost per hire
        
        return {
            "period_days": days,
            "total_scans": scans["total_scans"],
            "candidates_analyzed": scans["total_candidates"],
            "matches_found": scans["total_matches"],
            "interviews_generated": outcomes["interviewed"],
            "hires_made": outcomes["hired"],
            "estimated_cost_savings": costs_saved,
            "match_to_hire_rate": (
                outcomes["hired"] / scans["total_matches"] * 100
                if scans["total_matches"] > 0 else 0
            )
        }
```

## 11. Testing Strategy

### Integration Tests

```python
# tests/test_application_methods.py
import pytest
from httpx import AsyncClient

class TestApplicationMethods:
    @pytest.mark.asyncio
    async def test_linkedin_oauth_flow(self, client: AsyncClient):
        """Test LinkedIn OAuth application flow"""
        # Get auth URL
        response = await client.get("/apply/linkedin/job_123")
        assert response.status_code == 302
        assert "linkedin.com/oauth" in response.headers["location"]
        
        # Simulate callback
        response = await client.get(
            "/auth/linkedin/callback?code=test_code&state=job_123"
        )
        assert response.status_code == 200
        assert "candidate_id" in response.json()
    
    @pytest.mark.asyncio
    async def test_email_application(self, mock_email):
        """Test email application processing"""
        # Send test email
        await mock_email.send_application(
            to="apply-job123@test.hirova.ai",
            from_email="candidate@example.com",
            attachment="resume.pdf"
        )
        
        # Process emails
        service = EmailApplicationService()
        await service.process_email_applications()
        
        # Verify candidate created
        candidate = await get_candidate_by_email("candidate@example.com")
        assert candidate is not None
        assert candidate.source == "email"
    
    @pytest.mark.asyncio
    async def test_mobile_camera_upload(self, client: AsyncClient):
        """Test mobile camera resume capture"""
        with open("tests/fixtures/resume_photo.jpg", "rb") as f:
            image_data = base64.b64encode(f.read()).decode()
        
        response = await client.post(
            "/camera-upload/job_123",
            json={
                "image_data": image_data,
                "email": "mobile@example.com"
            }
        )
        
        assert response.status_code == 200
        assert response.json()["ocr_confidence"] > 0.7
```

## Deployment Considerations

### Environment Variables

```bash
# Application Methods Configuration
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
INDEED_API_KEY=your_indeed_api_key
EMAIL_IMAP_SERVER=imap.gmail.com
EMAIL_SMTP_SERVER=smtp.gmail.com
EMAIL_ADDRESS=applications@company.com
EMAIL_PASSWORD=your_app_password

# AI Talent Scout Configuration
SCOUT_MIN_MATCH_SCORE=85
SCOUT_SCAN_INTERVAL=3600  # seconds
SCOUT_BATCH_SIZE=100
SCOUT_MAX_FOLDER_SIZE_GB=50

# Feature Flags
ENABLE_LINKEDIN_IMPORT=true
ENABLE_EMAIL_APPLICATIONS=true
ENABLE_INDEED_INTEGRATION=true
ENABLE_CAMERA_UPLOAD=true
ENABLE_RESUME_BUILDER=true
ENABLE_AI_TALENT_SCOUT=true
ENABLE_FOLDER_MONITORING=true
```

### Monitoring Metrics

```python
# Key metrics to track
METRICS = {
    "application_methods_used": Counter,
    "application_success_rate": Gauge,
    "parsing_errors": Counter,
    "average_application_time": Histogram,
    "method_conversion_rate": Gauge
}
```

## Conclusion

This implementation guide provides a comprehensive approach to supporting multiple application methods in Hirova AI, including proactive AI Talent Scout capabilities. The key principles are:

1. **Flexibility**: Support all major application methods including passive candidate discovery
2. **Proactivity**: AI continuously searches existing databases for matches
3. **Consistency**: Unified processing regardless of source
4. **Security**: Validate and sanitize all inputs
5. **Performance**: Async processing for scalability
6. **Intelligence**: AI-driven matching for both active and passive candidates
7. **Analytics**: Track effectiveness of each method and ROI of database mining

By implementing these methods, Hirova AI can:
- Maximize application rates through multiple channels
- Leverage existing resume databases effectively
- Reduce time-to-hire by proactively identifying candidates
- Provide significant cost savings through automated talent discovery

---

*For questions about implementation, contact: tech@hirova.ai*