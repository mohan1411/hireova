@echo off
echo ========================================
echo    Hireova - Git Repository Setup
echo ========================================
echo.

REM Initialize git repository
echo [1/6] Initializing Git repository...
git init

REM Add remote origin
echo.
echo [2/6] Adding remote origin...
git remote add origin https://github.com/mohan1411/hireova.git

REM Create initial commit
echo.
echo [3/6] Creating initial commit...
git add .
git commit -m "Initial commit: Hireova AI Hiring Assistant

- FastAPI backend setup
- Authentication system with JWT
- Database models (User, Organization, Job, Candidate, Application)
- Docker compose for PostgreSQL and Redis
- API documentation with Swagger UI
- Project structure and configuration"

REM Push to main branch
echo.
echo [4/6] Pushing to main branch...
git push -u origin main

REM Create development branch
echo.
echo [5/6] Creating development branch...
git checkout -b develop
git push -u origin develop

REM Create feature branches
echo.
echo [6/6] Creating feature branch structure...

REM Feature branch for job management
git checkout -b feature/job-management
git push -u origin feature/job-management

REM Back to develop
git checkout develop

REM Feature branch for resume processing
git checkout -b feature/resume-processing
git push -u origin feature/resume-processing

REM Back to develop
git checkout develop

REM Feature branch for AI integration
git checkout -b feature/ai-integration
git push -u origin feature/ai-integration

REM Back to develop
git checkout develop

REM Feature branch for frontend
git checkout -b feature/frontend
git push -u origin feature/frontend

REM Back to develop
git checkout develop

echo.
echo ========================================
echo    Git Setup Complete!
echo ========================================
echo.
echo Branch Structure:
echo   main              - Production-ready code
echo   develop           - Development branch (current)
echo   feature/job-management     - Job CRUD operations
echo   feature/resume-processing  - Resume upload and parsing
echo   feature/ai-integration     - AI/ML features
echo   feature/frontend           - Next.js frontend
echo.
echo Current branch: develop
echo.
echo Next steps:
echo 1. Work on features in their respective branches
echo 2. Merge completed features back to develop
echo 3. When ready for release, merge develop to main
echo.
pause