# Kuro AI

A modern AI application built with FastAPI and Next.js.

## Project Structure

- `backend/` - FastAPI backend service
- `frontend/` - Next.js frontend application

## Tech Stack

### Backend
- FastAPI
- Python 3.11
- SQLAlchemy
- Alembic for migrations
- pytest for testing

### Frontend
- Next.js 14
- TypeScript
- Tailwind CSS
- ESLint + Prettier

## Prerequisites

- Docker
- Docker Compose
- Git

## Quick Start

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd kuroai
   ```

2. Switch to development branch
   ```bash
   git checkout dev
   ```

3. Start services
   ```bash
   docker-compose up --build
   ```

4. Access the applications:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Development

We follow a structured development workflow to maintain code quality and collaboration. Please read our [Contributing Guidelines](CONTRIBUTING.md) before starting development.

### Key Points

- Branch from `dev` for new features and fixes
- Follow conventional commits
- Write tests for new features
- Update documentation as needed

## Documentation

- [Contributing Guidelines](CONTRIBUTING.md)
- [API Documentation](http://localhost:8000/docs)

## License

[MIT License](LICENSE)

