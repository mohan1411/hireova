# Docker PostgreSQL Database Commands

## 🔍 Quick Commands to Check Data

### 1. Connect to PostgreSQL Interactive Shell
```bash
docker exec -it hireova-postgres-1 psql -U hireova_user -d hireova_db
```
Password: `hireova_pass`

### 2. Run SQL Queries Directly
```bash
# Show all users
docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "SELECT * FROM users;"

# Count records in all tables
docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "SELECT 'users' as table, COUNT(*) FROM users UNION ALL SELECT 'organizations', COUNT(*) FROM organizations UNION ALL SELECT 'jobs', COUNT(*) FROM jobs;"

# Show recent users (last 24 hours)
docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "SELECT email, full_name, created_at FROM users WHERE created_at > NOW() - INTERVAL '24 hours';"
```

### 3. Check if Container is Running
```bash
# List running containers
docker ps

# Check PostgreSQL logs
docker logs hireova-postgres-1
```

## 📊 Useful PostgreSQL Commands (Inside psql)

Once connected to psql:

```sql
-- List all databases
\l

-- List all tables
\dt

-- Describe a table structure
\d users
\d jobs

-- Show all users
SELECT * FROM users;

-- Show users with their organizations
SELECT u.email, u.full_name, o.name as organization 
FROM users u 
LEFT JOIN organizations o ON u.organization_id = o.id;

-- Count records by table
SELECT COUNT(*) as user_count FROM users;
SELECT COUNT(*) as job_count FROM jobs;

-- Show recent activity
SELECT * FROM users ORDER BY created_at DESC LIMIT 5;

-- Exit psql
\q
```

## 🛠️ Advanced Database Operations

### Export Data
```bash
# Export users table to CSV
docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "COPY users TO STDOUT WITH CSV HEADER;" > users.csv
```

### Backup Database
```bash
# Create backup
docker exec hireova-postgres-1 pg_dump -U hireova_user hireova_db > backup.sql

# Restore backup
docker exec -i hireova-postgres-1 psql -U hireova_user -d hireova_db < backup.sql
```

### View Database Size
```bash
docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "SELECT pg_database_size('hireova_db')/1024/1024 as size_mb;"
```

## 🖥️ GUI Tools for PostgreSQL

### 1. pgAdmin (Web-based)
Add to docker-compose.yml:
```yaml
pgadmin:
  image: dpage/pgadmin4
  environment:
    PGADMIN_DEFAULT_EMAIL: admin@hireova.ai
    PGADMIN_DEFAULT_PASSWORD: admin
  ports:
    - "5050:80"
```

Access at: http://localhost:5050

### 2. DBeaver (Desktop)
- Download: https://dbeaver.io/
- Connection settings:
  - Host: localhost
  - Port: 5432
  - Database: hireova_db
  - Username: hireova_user
  - Password: hireova_pass

### 3. VS Code Extension
- Install: "PostgreSQL" by Chris Kolkman
- Connect using same credentials

## 🔧 Troubleshooting

### Container name might be different:
```bash
# Find the correct container name
docker ps | grep postgres

# Use the actual name in commands
docker exec -it <container_name> psql -U hireova_user -d hireova_db
```

### Permission denied:
```bash
# Run with PGPASSWORD environment variable
docker exec -e PGPASSWORD=hireova_pass hireova-postgres-1 psql -U hireova_user -d hireova_db -c "SELECT * FROM users;"
```