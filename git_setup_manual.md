# Git Setup Instructions for Hireova

## Initial Setup (First Time Only)

### 1. Initialize Git Repository
```bash
cd D:\Projects\AI\BusinessIdeas\SmallBusiness\Hireova
git init
```

### 2. Configure Git (if not already done)
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### 3. Add Remote Repository
```bash
git remote add origin https://github.com/mohan1411/hireova.git
```

### 4. Add Files and Create Initial Commit
```bash
git add .
git commit -m "Initial commit: Hireova AI Hiring Assistant

- FastAPI backend setup with authentication
- Database models for hiring workflow
- Docker compose for PostgreSQL and Redis
- API documentation with Swagger UI
- Project structure and configuration"
```

### 5. Push to GitHub
```bash
git push -u origin main
```

### 6. Create Development Branch
```bash
git checkout -b develop
git push -u origin develop
```

### 7. Create Feature Branches
```bash
# From develop branch
git checkout develop

# Create feature branches
git checkout -b feature/job-management
git push -u origin feature/job-management

git checkout develop
git checkout -b feature/resume-processing
git push -u origin feature/resume-processing

git checkout develop
git checkout -b feature/ai-integration
git push -u origin feature/ai-integration

git checkout develop
git checkout -b feature/frontend
git push -u origin feature/frontend

# Return to develop
git checkout develop
```

## Branch Structure

```
main
│
└── develop
    ├── feature/job-management      # Job CRUD operations
    ├── feature/resume-processing   # Resume upload and parsing
    ├── feature/ai-integration      # AI/ML capabilities
    └── feature/frontend           # Next.js frontend
```

## Common Git Commands

### Switch Branches
```bash
git checkout branch-name
```

### Create New Feature Branch
```bash
git checkout develop
git pull origin develop
git checkout -b feature/new-feature
```

### Commit Changes
```bash
git add .
git commit -m "feat: your feature description"
git push origin feature/new-feature
```

### Update Your Branch
```bash
git checkout develop
git pull origin develop
git checkout your-branch
git merge develop
```

### View Status
```bash
git status
git branch -a  # See all branches
git log --oneline --graph  # See commit history
```

## Setting Up Git Message Template

```bash
git config --local commit.template .gitmessage
```

## Troubleshooting

### If you get authentication errors:
1. Make sure you're using a Personal Access Token instead of password
2. Create one at: https://github.com/settings/tokens
3. Use it when prompted for password

### If push is rejected:
```bash
git pull origin branch-name --rebase
git push origin branch-name
```

### If you need to undo last commit:
```bash
git reset --soft HEAD~1  # Keep changes
# or
git reset --hard HEAD~1  # Discard changes
```