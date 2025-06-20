# Local Database Setup (Without Docker)

## Option 1: Using Docker (Recommended)

If you have Docker Desktop installed on Windows:

```bash
# From the project root directory (not backend)
cd ..
docker compose up -d
```

If the command still doesn't work, make sure:
1. Docker Desktop is installed and running
2. You're in the correct directory (project root, not backend)

## Option 2: Install PostgreSQL and Redis Locally

### PostgreSQL Setup

1. **Download PostgreSQL 16 for Windows:**
   - Visit: https://www.postgresql.org/download/windows/
   - Download the installer
   - Run the installer with default settings
   - Remember the password you set for the postgres user

2. **Create the database:**
   ```sql
   -- Open pgAdmin or psql
   CREATE USER hireova_user WITH PASSWORD 'hireova_pass';
   CREATE DATABASE hireova_db OWNER hireova_user;
   GRANT ALL PRIVILEGES ON DATABASE hireova_db TO hireova_user;
   ```

### Redis Setup

1. **Download Redis for Windows:**
   - Visit: https://github.com/microsoftarchive/redis/releases
   - Download Redis-x64-3.2.100.msi
   - Install with default settings

2. **Or use Memurai (Redis for Windows):**
   - Visit: https://www.memurai.com/
   - Download and install the free Developer Edition

## Option 3: Use Cloud Services (Free Tiers)

### PostgreSQL Cloud Options:
1. **Supabase** (https://supabase.com/)
   - 500MB free
   - Sign up and create a new project
   - Copy the connection string to your .env file

2. **Neon** (https://neon.tech/)
   - Generous free tier
   - Instant PostgreSQL database
   - Copy the connection string to your .env file

### Redis Cloud Options:
1. **Upstash** (https://upstash.com/)
   - 10,000 commands/day free
   - Sign up and create a Redis database
   - Copy the connection URL to your .env file

## Update Your .env File

After setting up your databases, update the `.env` file:

```env
# For local PostgreSQL
DATABASE_URL=postgresql://hireova_user:hireova_pass@localhost:5432/hireova_db

# For Supabase (example)
# DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres

# For local Redis
REDIS_URL=redis://localhost:6379/0

# For Upstash (example)
# REDIS_URL=redis://default:[YOUR-PASSWORD]@[YOUR-ENDPOINT].upstash.io:6379
```

## Option 4: SQLite for Development (Simplest)

If you just want to test the application quickly, you can use SQLite:

1. Update your `.env` file:
   ```env
   DATABASE_URL=sqlite:///./hireova.db
   ```

2. Install SQLite driver:
   ```bash
   pip install aiosqlite
   ```

Note: Some features might not work perfectly with SQLite, but it's fine for initial development.

## Verify Your Setup

After setting up your databases, run:

```bash
python test_setup.py
```

This will verify that your configuration is correct.