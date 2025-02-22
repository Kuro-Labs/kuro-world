# Contributing to Kuro AI

Thank you for your interest in contributing to Kuro AI! This document outlines our development process and guidelines.

## Branch Structure

- `main` - Production-ready code
- `dev` - Main development branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent fixes for production
- `release/*` - Release preparation

## Development Workflow

1. **Starting New Work**
   ```bash
   # Update dev branch
   git checkout dev
   git pull origin dev

   # Create a feature branch
   git checkout -b feature/your-feature-name
   # or for bugs
   git checkout -b bugfix/issue-description
   ```

2. **Making Changes**
   - Make your changes in small, logical commits
   - Write meaningful commit messages following conventional commits:
     ```
     feat: add new feature
     fix: resolve bug
     docs: update documentation
     style: formatting changes
     refactor: code restructuring
     test: add/update tests
     chore: maintenance tasks
     ```

3. **Before Submitting**
   - Ensure all tests pass
   - Update documentation if needed
   - Follow code style guidelines
   - Test your changes locally

4. **Submitting Changes**
   ```bash
   # Push your branch
   git push origin feature/your-feature-name

   # Create a Pull Request to dev branch
   ```

5. **Pull Request Process**
   - Provide a clear description of changes
   - Link related issues
   - Request review from team members
   - Address review comments
   - Ensure CI checks pass

6. **After Merge**
   - Delete your feature branch
   - Pull latest dev branch

## Release Process

1. Create a release branch from dev
   ```bash
   git checkout -b release/v1.x.x dev
   ```

2. Version bump and final testing

3. Merge to main AND dev
   ```bash
   git checkout main
   git merge release/v1.x.x
   git tag -a v1.x.x -m "Release v1.x.x"
   
   git checkout dev
   git merge release/v1.x.x
   ```

4. Delete release branch
   ```bash
   git branch -d release/v1.x.x
   ```

## Hot Fixes

For urgent production fixes:
```bash
git checkout -b hotfix/issue-description main
# Fix the issue
# Merge to both main and dev
```

## Code Style Guidelines

### Python (Backend)
- Follow PEP 8
- Use type hints
- Document functions and classes
- Maximum line length: 88 characters (Black formatter)

### TypeScript/JavaScript (Frontend)
- Use ESLint configuration
- Use Prettier for formatting
- Follow React/Next.js best practices
- Use TypeScript types/interfaces

## Testing Requirements

### Backend
- Unit tests for new features
- Integration tests where appropriate
- Minimum 80% coverage

### Frontend
- Component tests
- Integration tests
- E2E tests for critical paths

## Local Development Setup

1. Clone the repository
   ```bash
   git clone <repository-url>
   git checkout dev
   ```

2. Start services with Docker
   ```bash
   docker-compose up --build
   ```

3. Access services:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000
   - API Docs: http://localhost:8000/docs
