@echo off
echo ========================================
echo    Check PostgreSQL Data in Docker
echo ========================================
echo.

echo Choose an option:
echo 1. Connect to PostgreSQL CLI
echo 2. Run a quick query
echo 3. Show all tables
echo 4. Count records in each table
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo Connecting to PostgreSQL...
    echo Password is: hireova_pass
    echo.
    echo Once connected, try these commands:
    echo   \l          - List all databases
    echo   \dt         - List all tables
    echo   \d users    - Describe users table
    echo   SELECT * FROM users;  - Show all users
    echo   \q          - Quit
    echo.
    docker exec -it hireova-postgres-1 psql -U hireova_user -d hireova_db
) else if "%choice%"=="2" (
    echo.
    echo Running quick query to show users...
    docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "SELECT id, email, full_name, role, created_at FROM users;"
) else if "%choice%"=="3" (
    echo.
    echo Showing all tables...
    docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "\dt"
) else if "%choice%"=="4" (
    echo.
    echo Counting records in each table...
    docker exec hireova-postgres-1 psql -U hireova_user -d hireova_db -c "SELECT 'users' as table_name, COUNT(*) as count FROM users UNION ALL SELECT 'organizations', COUNT(*) FROM organizations UNION ALL SELECT 'jobs', COUNT(*) FROM jobs UNION ALL SELECT 'candidates', COUNT(*) FROM candidates UNION ALL SELECT 'applications', COUNT(*) FROM applications;"
)

echo.
pause