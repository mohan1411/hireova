# Contributing to Hireova

We love your input! We want to make contributing to Hireova as easy and transparent as possible.

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Git Workflow

We use [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) for our branching strategy.

### Branches

- `main` - Production-ready code
- `develop` - Development branch (default branch for PRs)
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches
- `hotfix/*` - Emergency fixes for production
- `release/*` - Release preparation branches

### Creating a Feature

1. Create your feature branch from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. Make your changes:
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

3. Push to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request to `develop` branch

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Build process or auxiliary tool changes
- `ci`: CI configuration changes

### Examples
```bash
feat(auth): add LinkedIn OAuth integration
fix(resume): correct PDF parsing error
docs(api): update authentication endpoints
```

## Code Style

### Python (Backend)
- Follow PEP 8
- Use type hints where possible
- Format with `ruff format`
- Lint with `ruff check`

```bash
# Format code
ruff format .

# Check linting
ruff check .
```

### TypeScript (Frontend)
- Use TypeScript strict mode
- Follow Airbnb style guide
- Format with Prettier
- Lint with ESLint

## Testing

### Backend Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_auth.py
```

### Writing Tests
- Write tests for all new features
- Maintain test coverage above 80%
- Use descriptive test names

Example:
```python
def test_user_registration_with_valid_data_creates_user():
    # Test implementation
    pass
```

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Ensure all tests pass
3. Update documentation if you're changing APIs
4. The PR will be merged once you have approval from maintainers

### PR Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] Branch is up to date with develop

## Development Setup

1. Fork the repo
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/hireova.git
   ```

3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/mohan1411/hireova.git
   ```

4. Keep your fork updated:
   ```bash
   git fetch upstream
   git checkout develop
   git merge upstream/develop
   ```

## Reporting Issues

Use GitHub Issues to report bugs or request features.

### Bug Reports
Include:
- Quick summary
- Environment details
- Steps to reproduce
- Expected behavior
- Actual behavior
- Code samples if applicable

### Feature Requests
Include:
- Problem description
- Proposed solution
- Alternative solutions considered
- Additional context

## Code of Conduct

### Our Standards
- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Our Responsibilities
Project maintainers are responsible for clarifying standards and are expected to take appropriate action in response to unacceptable behavior.

## Questions?

Feel free to contact the project maintainers.

Thank you for contributing! 🚀