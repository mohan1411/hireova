# Hireova AI - Technical Stack Documentation

## Overview

This document outlines the technical stack for Hireova AI, an intelligent hiring assistant platform. The stack is designed to minimize costs while maintaining scalability and performance.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Core Technologies](#core-technologies)
3. [AI/ML Stack](#aiml-stack)
4. [Backend Stack](#backend-stack)
5. [Frontend Stack](#frontend-stack)
6. [Database & Storage](#database--storage)
7. [Infrastructure & Deployment](#infrastructure--deployment)
8. [Development Setup](#development-setup)
9. [Git Workflow](#git-workflow)
10. [API Documentation](#api-documentation)
11. [Testing Strategy](#testing-strategy)
12. [Monitoring & Analytics](#monitoring--analytics)
13. [Cost Analysis](#cost-analysis)
14. [Implementation Status](#implementation-status)
15. [Security Considerations](#security-considerations)

## Architecture Overview

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Web Client    │     │  Mobile Client  │     │   API Client    │
│   (Next.js)     │     │ (React Native)  │     │  (Third-party)  │
└────────┬────────┘     └────────┬────────┘     └────────┬────────┘
         │                       │                         │
         └───────────────────────┴─────────────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │     API Gateway         │
                    │    (FastAPI/Nginx)      │
                    └────────────┬────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
┌───────▼────────┐     ┌────────▼────────┐     ┌────────▼────────┐
│  Auth Service  │     │   Core API      │     │   ML Service    │
│    (JWT)       │     │   (FastAPI)     │     │  (Python/AI)    │
└───────┬────────┘     └────────┬────────┘     └────────┬────────┘
        │                       │                         │
        └───────────────────────┼─────────────────────────┘
                                │
                    ┌───────────▼───────────┐
                    │     Data Layer        │
                    │  PostgreSQL + Redis   │
                    └───────────────────────┘
```

## Core Technologies

### Programming Languages
- **Backend**: Python 3.11+
- **Frontend**: TypeScript 5.0+
- **Database**: SQL (PostgreSQL/SQLite)

### Key Frameworks
- **Backend API**: FastAPI 0.104.1
- **Frontend**: Next.js 14+
- **CSS**: Tailwind CSS 3.4+
- **Testing**: Pytest, Jest

### Repository
- **GitHub**: https://github.com/mohan1411/hireova
- **Branching Strategy**: Git Flow
- **Main Branches**: main, develop, feature/*, bugfix/*, hotfix/*

## AI/ML Stack

### Language Models

#### Primary Option (Cost-Effective)
```python
# OpenAI GPT-3.5-turbo for cost efficiency
OPENAI_CONFIG = {
    "model": "gpt-3.5-turbo",
    "temperature": 0.3,
    "max_tokens": 500,
    "cost_per_1k_tokens": 0.002  # $0.002 per 1000 tokens
}
```

#### Alternative Options
- **Groq API**: 70% cheaper for simple tasks
- **Claude Haiku**: Fast and affordable via Anthropic
- **Self-hosted**: Llama 3.1 8B on RunPod ($0.40/hour)

### Embeddings & Vector Search
```python
# Using Sentence Transformers (free, runs on CPU)
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(resume_texts)
```

### Vector Database
- **ChromaDB** (self-hosted, free)
- **Qdrant** (self-hosted alternative)

### Resume Parsing
```python
# Custom parser using open-source libraries
import pypdf2
import docx2txt
import re

class ResumeParser:
    def parse_pdf(self, file_path):
        # Implementation using pypdf2
        pass
    
    def parse_docx(self, file_path):
        # Implementation using docx2txt
        pass
```

### AI Cost Optimization
- **Redis Caching**: Reduces API calls by 70-80%
- **Batch Processing**: Process multiple resumes in single API call
- **Smart Routing**: Use cheaper models for simple tasks

## Backend Stack

### API Framework: FastAPI

```python
# app/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
import time
import logging
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.database import engine, Base
from app.api import api_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting up Hireova AI API")
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    logger.info("Shutting down Hireova AI API")

app = FastAPI(
    title="Hireova AI",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan
)

# Include API routes
app.include_router(api_router, prefix=settings.api_prefix)
```

### Project Structure
```
hireova/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── candidates.py
│   │   │   ├── jobs.py
│   │   │   └── applications.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── organization.py
│   │   │   ├── candidate.py
│   │   │   ├── job.py
│   │   │   └── application.py
│   │   ├── schemas/
│   │   │   └── [pydantic schemas]
│   │   ├── services/
│   │   │   ├── ai_service.py
│   │   │   ├── parser_service.py
│   │   │   └── matching_service.py
│   │   └── utils/
│   │       └── cache.py
│   ├── tests/
│   ├── requirements.txt
│   ├── run.py
│   └── Dockerfile
├── frontend/
├── docs/
│   ├── technical/
│   ├── business/
│   ├── product/
│   └── design/
├── docker-compose.yml
├── .gitignore
├── CONTRIBUTING.md
└── README.md
```

### Dependencies (requirements.txt)
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
sqlalchemy==2.0.23
alembic==1.13.0
psycopg2-binary==2.9.9
redis==5.0.1
celery==5.3.4
openai==1.3.5
pydantic==2.5.0
pydantic-settings==2.1.0
python-dotenv==1.0.0
httpx==0.25.2
slowapi==0.1.9
pypdf2==3.0.1
python-docx==1.1.0
email-validator==2.1.0
aiofiles==23.2.1

# Database drivers
aiosqlite==0.19.0  # For SQLite support

# Development dependencies
pytest==7.4.3
pytest-asyncio==0.21.1
pytest-cov==4.1.0
ruff==0.1.7
```

## Frontend Stack

### Framework: Next.js with TypeScript

```typescript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    domains: ['localhost', 'api.hireova.ai'],
  },
}

module.exports = nextConfig
```

### Dependencies (package.json)
```json
{
  "name": "hireova-frontend",
  "version": "1.0.0",
  "dependencies": {
    "next": "14.0.4",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "typescript": "5.3.3",
    "@tanstack/react-query": "5.13.4",
    "axios": "1.6.2",
    "zustand": "4.4.7",
    "react-hook-form": "7.48.2",
    "zod": "3.22.4",
    "tailwindcss": "3.4.0",
    "lucide-react": "0.294.0"
  }
}
```

## Database & Storage

### Database Options

#### Production: PostgreSQL
```bash
DATABASE_URL=postgresql://hireova_user:hireova_pass@localhost:5432/hireova_db
```

#### Development: SQLite (Quick Setup)
```bash
DATABASE_URL=sqlite:///./hireova.db
```

### PostgreSQL Schema

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(50) NOT NULL DEFAULT 'recruiter',
    is_active BOOLEAN DEFAULT true,
    is_verified BOOLEAN DEFAULT false,
    organization_id UUID REFERENCES organizations(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Organizations table
CREATE TABLE organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255),
    plan VARCHAR(50) DEFAULT 'free',
    industry VARCHAR(100),
    size VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Jobs table
CREATE TABLE jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organization_id UUID REFERENCES organizations(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    requirements JSONB,
    location VARCHAR(255),
    job_type VARCHAR(50),
    experience_level VARCHAR(50),
    salary_min VARCHAR(50),
    salary_max VARCHAR(50),
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Candidates table
CREATE TABLE candidates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    phone VARCHAR(50),
    location VARCHAR(255),
    linkedin_url VARCHAR(500),
    linkedin_id VARCHAR(255) UNIQUE,
    resume_url VARCHAR(500),
    resume_text TEXT,
    parsed_data JSONB,
    skills JSONB,
    experience_years VARCHAR(20),
    source VARCHAR(50),
    last_matched TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Applications table
CREATE TABLE applications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id UUID REFERENCES jobs(id),
    candidate_id UUID REFERENCES candidates(id),
    status VARCHAR(50) DEFAULT 'pending',
    ai_score FLOAT,
    ai_analysis JSONB,
    ai_screening_result JSONB,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_applications_job_id ON applications(job_id);
CREATE INDEX idx_applications_status ON applications(status);
CREATE INDEX idx_candidates_email ON candidates(email);
CREATE INDEX idx_users_email ON users(email);
```

### Redis Configuration
```python
# app/utils/cache.py
import redis
import json
from typing import Optional, Any
from app.core.config import settings

# Try Redis, fallback to in-memory cache for development
try:
    redis_client = redis.Redis.from_url(settings.redis_url, decode_responses=True)
    redis_client.ping()
except:
    # Simple in-memory cache for development
    class InMemoryCache:
        def __init__(self):
            self.store = {}
        
        def get(self, key: str) -> Optional[str]:
            return self.store.get(key)
        
        def setex(self, key: str, seconds: int, value: str):
            self.store[key] = value
    
    redis_client = InMemoryCache()
```

## Infrastructure & Deployment

### Development Environment

#### Docker Compose (Recommended)
```yaml
# docker-compose.yml
version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: hireova_db
      POSTGRES_USER: hireova_user
      POSTGRES_PASSWORD: hireova_pass
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U hireova_user -d hireova_db"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Optional: pgAdmin for database management
  # pgadmin:
  #   image: dpage/pgadmin4
  #   environment:
  #     PGADMIN_DEFAULT_EMAIL: admin@hireova.ai
  #     PGADMIN_DEFAULT_PASSWORD: admin
  #   ports:
  #     - "5050:80"
  #   depends_on:
  #     - postgres

volumes:
  postgres_data:
```

#### Quick Start Options

##### Option 1: Docker (Full Features)
```bash
docker compose up -d
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python run.py
```

##### Option 2: SQLite (Quick Development)
```bash
cd backend
copy .env.sqlite .env  # Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

### Production Deployment Options

#### Option 1: Free Tier Strategy
- **Frontend**: Vercel (free tier)
- **Backend**: Render.com (free tier) or Railway ($5 credit)
- **Database**: Supabase (500MB free) or Neon (free tier)
- **Redis**: Upstash (10,000 commands/day free)

#### Option 2: VPS Strategy ($20-50/month)
- **Provider**: Hetzner, DigitalOcean, or Linode
- **Setup**: Coolify or Dokku for PaaS-like experience
- **SSL**: Let's Encrypt (free)

## Development Setup

### Windows Development

#### Quick Setup Script
```batch
@echo off
REM setup_windows.bat
echo Setting up Hireova AI for Windows...

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Copy environment file
if not exist .env copy .env.example .env

echo Setup complete! Run 'python run.py' to start the server.
```

#### Development Scripts
- `start_dev.bat` - Start development server
- `check_docker_db.bat` - Inspect Docker PostgreSQL
- `test_api.py` - Test API endpoints
- `db_check.py` - Check database contents

### Environment Configuration

```bash
# .env.example
# Application
ENVIRONMENT=development
APP_NAME="Hireova AI"
APP_VERSION=1.0.0
DEBUG=true

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_PREFIX=/api/v1
ALLOWED_HOSTS=["localhost","127.0.0.1"]

# Security
SECRET_KEY=your-secret-key-here-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
BCRYPT_ROUNDS=12

# Database (PostgreSQL for production)
DATABASE_URL=postgresql://hireova_user:hireova_pass@localhost:5432/hireova_db

# Database (SQLite for quick development)
# DATABASE_URL=sqlite:///./hireova.db

# Redis
REDIS_URL=redis://localhost:6379/0
REDIS_CACHE_TTL=3600

# OpenAI
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=500
OPENAI_TEMPERATURE=0.3

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM_EMAIL=noreply@hireova.ai

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60
RATE_LIMIT_PER_HOUR=1000

# Feature Flags
ENABLE_AI_SCREENING=true
ENABLE_BATCH_PROCESSING=true
ENABLE_WEBSOCKETS=true
```

## Git Workflow

### Repository
- **URL**: https://github.com/mohan1411/hireova
- **Default Branch**: `develop`

### Branch Structure
```
main (production)
│
└── develop (integration)
    ├── feature/job-management
    ├── feature/resume-processing
    ├── feature/ai-integration
    └── feature/frontend
```

### Commit Convention
```
<type>(<scope>): <subject>

Types: feat, fix, docs, style, refactor, test, chore
Example: feat(auth): add LinkedIn OAuth integration
```

### Workflow
1. Create feature branch from `develop`
2. Make changes and commit
3. Push to GitHub
4. Create Pull Request to `develop`
5. After review, merge to `develop`
6. Periodically merge `develop` to `main` for releases

## API Documentation

### Interactive Documentation
- **Swagger UI**: http://localhost:8000/api/docs
- **ReDoc**: http://localhost:8000/api/redoc

### Current Endpoints

#### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/auth/me` - Get current user

#### Jobs (Planned)
- `GET /api/v1/jobs` - List jobs
- `POST /api/v1/jobs` - Create job
- `GET /api/v1/jobs/{id}` - Get job details
- `PUT /api/v1/jobs/{id}` - Update job
- `DELETE /api/v1/jobs/{id}` - Delete job

#### Candidates (Planned)
- `GET /api/v1/candidates` - List candidates
- `POST /api/v1/candidates/upload` - Upload resume
- `GET /api/v1/candidates/{id}` - Get candidate details
- `POST /api/v1/candidates/search` - Search candidates

### Testing with Swagger UI
1. Start the server: `python run.py`
2. Open: http://localhost:8000/api/docs
3. Use "Try it out" to test endpoints
4. Authorize with JWT token for protected endpoints

## Testing Strategy

### Test Structure
```
backend/tests/
├── unit/
│   ├── test_services/
│   ├── test_models/
│   └── test_utils/
├── integration/
│   ├── test_api/
│   └── test_database.py
├── fixtures/
└── conftest.py
```

### Running Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=app

# Specific test
pytest tests/test_auth.py -v
```

### Test Database
- Uses separate test database
- SQLite for fast testing
- Fixtures for test data

## Monitoring & Analytics

### Free Monitoring Stack
1. **Error Tracking**: Sentry (5,000 errors/month free)
2. **Analytics**: PostHog (1M events/month free)
3. **Uptime**: Better Stack (free tier)
4. **Application Monitoring**: Built-in health checks

### Health Check Endpoints
- `GET /health` - Basic health check
- `GET /health/detailed` - Comprehensive system status

## Cost Analysis

### Development Costs

| Setup Type | Monthly Cost | Features |
|------------|--------------|----------|
| SQLite + Local | $0 | Basic development |
| Docker + Local | $0 | Full features locally |
| Cloud Free Tier | $0-10 | Limited resources |
| Small VPS | $20-50 | Production ready |

### API Costs with Caching

| Users | Without Cache | With Redis Cache | Savings |
|-------|---------------|------------------|---------|
| 100 | $200 | $50 | 75% |
| 500 | $1,000 | $250 | 75% |
| 1,000 | $2,000 | $500 | 75% |

### Cost Optimization
1. **Redis Caching**: 70-80% reduction in AI API calls
2. **Batch Processing**: Process multiple items per API call
3. **Smart Routing**: Use cheaper models for simple tasks
4. **Rate Limiting**: Prevent abuse and cost overruns

## Implementation Status

### ✅ Completed
- [x] Project structure and setup
- [x] FastAPI backend foundation
- [x] Database models (User, Organization, Job, Candidate, Application)
- [x] JWT authentication system
- [x] API documentation (Swagger/ReDoc)
- [x] Docker configuration
- [x] Git repository setup
- [x] Development scripts

### 🚧 In Progress
- [ ] Job CRUD endpoints
- [ ] Resume upload and parsing
- [ ] AI integration
- [ ] Candidate matching algorithm

### 📋 Planned
- [ ] Frontend (Next.js)
- [ ] Email notifications
- [ ] Background job processing
- [ ] Analytics dashboard
- [ ] Payment integration

## Security Considerations

### Authentication & Authorization
- JWT tokens with 24-hour expiration
- Password hashing with bcrypt (12 rounds)
- Role-based access control (RBAC)
- Secure password requirements (min 8 characters)

### API Security
- CORS configuration for specific domains
- Rate limiting (60/min, 1000/hour)
- Request validation with Pydantic
- SQL injection prevention with SQLAlchemy
- XSS protection headers

### Data Protection
- Environment variables for secrets
- HTTPS enforcement in production
- Database connection pooling
- Secure file upload handling
- GDPR compliance measures

## Troubleshooting

### Common Issues

#### Docker Not Found
```bash
# Install Docker Desktop for Windows
# Or use SQLite for development:
copy .env.sqlite .env
```

#### Database Connection Failed
```bash
# Check if PostgreSQL is running
docker ps

# Or switch to SQLite
DATABASE_URL=sqlite:///./hireova.db
```

#### Import Errors
```bash
# Ensure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt
```

### Debug Tools
- `python test_setup.py` - Verify installation
- `python db_check.py` - Inspect database
- `python test_api.py` - Test API endpoints
- Swagger UI for API testing

## Next Steps

1. **Complete API Implementation**
   - Implement job management endpoints
   - Add resume upload functionality
   - Integrate AI services

2. **Build Frontend**
   - Set up Next.js project
   - Create authentication flow
   - Build dashboard components

3. **Deploy MVP**
   - Choose hosting platform
   - Set up CI/CD pipeline
   - Configure monitoring

4. **Iterate Based on Feedback**
   - User testing
   - Performance optimization
   - Feature enhancement

---

For questions or contributions, see [CONTRIBUTING.md](../../CONTRIBUTING.md) or visit the [GitHub repository](https://github.com/mohan1411/hireova).