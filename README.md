# Hireova AI - Intelligent Hiring Assistant

An AI-powered hiring platform that automates candidate screening, matching, and initial assessments.

## Features

- 🤖 AI-powered resume parsing and analysis
- 🔗 Multiple application methods (LinkedIn, Email, Upload, etc.)
- 📊 Smart candidate-job matching
- 💬 Automated screening conversations
- 📈 Real-time analytics and insights

## Prerequisites

- Python 3.11+
- PostgreSQL 16
- Redis 7
- Node.js 18+ (for frontend)

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/mohan1411/hireova.git
cd hireova
```

### 2. Set up the backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Edit .env with your configuration
```

### 3. Start the databases

```bash
# From the project root
docker-compose up -d
```

### 4. Run database migrations

```bash
# From backend directory
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### 5. Start the backend server

```bash
# From backend directory
python run.py
```

The API will be available at:
- API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Get current user

### Jobs
- `GET /api/v1/jobs` - List jobs
- `POST /api/v1/jobs` - Create job
- `GET /api/v1/jobs/{id}` - Get job details
- `PUT /api/v1/jobs/{id}` - Update job
- `DELETE /api/v1/jobs/{id}` - Delete job

### Candidates
- `GET /api/v1/candidates` - List candidates
- `POST /api/v1/candidates/upload` - Upload resume
- `GET /api/v1/candidates/{id}` - Get candidate details
- `POST /api/v1/candidates/search` - Search candidates

### Applications
- `GET /api/v1/applications` - List applications
- `POST /api/v1/applications` - Create application
- `GET /api/v1/applications/{id}` - Get application details
- `PUT /api/v1/applications/{id}` - Update application status

## Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app
```

## Development

### Code Style
```bash
# Format code
ruff format .

# Lint code
ruff check .
```

### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1
```

## Production Deployment

See [Technical Implementation Guide](docs/technical/technical-implementation-guide.md) for detailed deployment instructions.

## License

Copyright (c) 2025 Hireova AI. All rights reserved.
