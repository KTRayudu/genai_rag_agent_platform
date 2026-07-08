# UV Package Manager Implementation Guide

This document provides a comprehensive explanation of how **uv** is implemented in this project. It is designed for developers who are learning modern Python dependency management practices.

## Table of Contents

1. [What is UV?](#what-is-uv)
2. [Why UV Over Other Tools?](#why-uv-over-other-tools)
3. [Project Structure Overview](#project-structure-overview)
4. [Understanding the Workspace Configuration](#understanding-the-workspace-configuration)
5. [The Lock File Explained](#the-lock-file-explained)
6. [Package-Specific Configuration](#package-specific-configuration)
7. [Docker Integration](#docker-integration)
8. [Common Commands Reference](#common-commands-reference)
9. [Development vs Production Workflows](#development-vs-production-workflows)
10. [Troubleshooting](#troubleshooting)

---

## What is UV?

**UV** is a modern Python package manager developed by Astral (the creators of Ruff). It serves as a drop-in replacement for pip, pip-tools, and virtualenv, offering significant performance improvements and better dependency resolution.

Key characteristics:
- Written in Rust for maximum performance
- Compatible with existing `pyproject.toml` standards
- Supports workspaces for monorepo architectures
- Generates deterministic lock files
- Integrates seamlessly with Docker

---

## Why UV Over Other Tools?

| Aspect | UV | pip/pip-tools | Poetry |
|--------|-----|---------------|--------|
| **Speed** | 10-100x faster | Baseline | Slower than pip |
| **Lock Files** | Native support | Requires pip-tools | Native support |
| **Workspaces** | Native support | Not supported | Limited |
| **Standards Compliance** | PEP 517/518/621 | Partial | Custom format |
| **Docker Optimization** | Built-in features | Manual setup | Manual setup |

For this project, UV was chosen because:

1. **Monorepo Support**: The project contains multiple packages (`api` and `chatbot_ui`) that need to share dependencies consistently.
2. **Reproducibility**: The lock file ensures every developer and deployment uses identical dependency versions.
3. **Docker Performance**: UV's caching and compilation features significantly reduce build times.
4. **Learning Value**: UV represents the future direction of Python tooling.

---

## Project Structure Overview

```
cohort-repo/
├── pyproject.toml          # Root workspace configuration
├── uv.lock                  # Shared lock file for all packages
├── apps/
│   ├── api/
│   │   ├── pyproject.toml  # API-specific dependencies
│   │   ├── Dockerfile
│   │   └── src/
│   └── chatbot_ui/
│       ├── pyproject.toml  # UI-specific dependencies
│       ├── Dockerfile
│       └── src/
├── docker-compose.yml
└── Makefile
```

### Key Concept: Monorepo Architecture

A **monorepo** (monolithic repository) contains multiple related projects in a single repository. In this case:

- **api**: A FastAPI backend service
- **chatbot_ui**: A Streamlit frontend application

Both packages live together but have their own dependencies, allowing for:
- Shared code and configuration
- Consistent versioning across services
- Simplified CI/CD pipelines
- Easier refactoring across boundaries

---

## Understanding the Workspace Configuration

### Root `pyproject.toml`

The root configuration file defines the workspace and shared settings:

```toml
[project]
name = "cohort-repo"
version = "0.1.0"
requires-python = ">=3.14.2"

[tool.uv.workspace]
members = [
    "apps/api",
    "apps/chatbot_ui",
]

[dependency-groups]
dev = [
    "langsmith>=0.6.4",
    "matplotlib>=3.10.8",
    "qdrant-client>=1.16.2",
]
```

#### Breaking Down Each Section

**`[project]`**: Standard Python project metadata following PEP 621.
- `name`: The workspace identifier
- `version`: Semantic version of the project
- `requires-python`: Minimum Python version for all packages

**`[tool.uv.workspace]`**: UV-specific workspace configuration.
- `members`: Lists all packages that belong to this workspace
- Each member path is relative to the root directory

**`[dependency-groups]`**: Groups dependencies by purpose.
- `dev`: Development-only dependencies not needed in production
- These are installed with `uv sync` but excluded with `--no-dev`

### Why Use Workspaces?

Without workspaces, each package would have its own lock file, potentially leading to:

```
Problem: Version Conflicts

apps/api/uv.lock      → pydantic==2.10.0
apps/chatbot_ui/uv.lock → pydantic==2.12.0

Result: Runtime errors when services communicate
```

With workspaces:

```
Solution: Single Lock File

uv.lock → pydantic==2.12.5 (used by both)

Result: Guaranteed compatibility
```

---

## The Lock File Explained

The `uv.lock` file is automatically generated and should be committed to version control. It contains:

### Lock File Structure

```toml
version = 1
revision = 3
requires-python = ">=3.14.2"

[manifest]
members = [
    "api",
    "chatbot-ui",
    "cohort-repo",
]

[[package]]
name = "fastapi"
version = "0.128.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "starlette" },
    { name = "typing-extensions" },
]

# ... continues for all 113 packages
```

### Why Lock Files Matter

| Without Lock File | With Lock File |
|-------------------|----------------|
| `pydantic>=2.0.0` could install 2.0.0 today, 2.15.0 tomorrow | Always installs exact version specified |
| "Works on my machine" problems | Identical environments everywhere |
| Unpredictable CI/CD builds | Reproducible deployments |
| Security vulnerabilities may slip in | Controlled, auditable updates |

### Updating Dependencies

```bash
# Update all dependencies to latest compatible versions
uv lock --upgrade

# Update a specific package
uv lock --upgrade-package fastapi

# After updating, sync to install new versions
uv sync
```

---

## Package-Specific Configuration

Each package in the workspace has its own `pyproject.toml`:

### API Package (`apps/api/pyproject.toml`)

```toml
[project]
name = "api"
version = "0.1.0"
requires-python = ">=3.14.2"
dependencies = [
    "fastapi>=0.128.0",
    "google-genai>=1.58.0",
    "groq>=1.0.0",
    "langsmith>=0.6.4",
    "openai>=2.15.0",
    "pydantic>=2.12.5",
    "pydantic-settings>=2.12.0",
    "qdrant-client>=1.16.2",
    "uvicorn>=0.40.0",
]

[tool.uv.sources]
shared = {workspace = true}

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### Chatbot UI Package (`apps/chatbot_ui/pyproject.toml`)

```toml
[project]
name = "chatbot-ui"
version = "0.1.0"
requires-python = ">=3.14.2"
dependencies = [
    "pydantic>=2.12.5",
    "pydantic-settings>=2.12.0",
    "streamlit>=1.53.0",
]

[tool.uv.sources]
shared = {workspace = true}

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### Understanding the Configuration

**`[project].dependencies`**: Runtime dependencies required for the package to function.
- Version specifiers like `>=0.128.0` allow compatible updates
- The lock file pins exact versions for reproducibility

**`[tool.uv.sources]`**: Defines where UV should look for packages.
- `shared = {workspace = true}` allows referencing other workspace members
- Useful when packages need to import from each other

**`[build-system]`**: Specifies how to build the package.
- Hatchling is a modern, standards-compliant build backend
- Required for creating distributable wheels

---

## Docker Integration

UV provides excellent Docker support through official base images and optimization features.

### Dockerfile Pattern

```dockerfile
# Use UV's official Python image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# UV optimization environment variables
ENV UV_COMPILE_BYTECODE=1    # Pre-compile Python files
ENV UV_LINK_MODE=copy        # Copy files instead of symlinks
ENV PYTHONOPTIMIZE=1         # Enable Python optimizations
ENV PYTHONUNBUFFERED=1       # Immediate output flushing
ENV PYTHONDONTWRITEBYTECODE=1 # Don't create .pyc files

WORKDIR /app

# Copy dependency files first (layer caching)
COPY pyproject.toml uv.lock ./
COPY apps/api ./apps/api

# Install with cache mounting for faster rebuilds
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --package api

# Security: run as non-root user
USER app
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables Explained

| Variable | Purpose |
|----------|---------|
| `UV_COMPILE_BYTECODE=1` | Pre-compiles `.py` to `.pyc` for faster startup |
| `UV_LINK_MODE=copy` | Copies files instead of creating symlinks (required in containers) |
| `PYTHONOPTIMIZE=1` | Removes assert statements and debug code |
| `PYTHONUNBUFFERED=1` | Ensures logs appear immediately |
| `PYTHONDONTWRITEBYTECODE=1` | Prevents runtime `.pyc` generation |

### Key Flags

| Flag | Purpose |
|------|---------|
| `--frozen` | Prevents any modification to `uv.lock` |
| `--no-dev` | Excludes development dependencies |
| `--package api` | Installs only dependencies for the specified package |

### Layer Caching Strategy

Docker builds are optimized by ordering operations from least to most frequently changed:

```dockerfile
# 1. Dependency files (rarely change)
COPY pyproject.toml uv.lock ./

# 2. Source code (frequently changes)
COPY apps/api ./apps/api

# 3. Install dependencies (cached if files unchanged)
RUN uv sync --frozen --no-dev --package api
```

When only source code changes, Docker reuses the cached dependency layer.

---

## Common Commands Reference

### Installation Commands

```bash
# Install all dependencies (including dev)
uv sync

# Install without development dependencies
uv sync --no-dev

# Install only a specific package's dependencies
uv sync --package api
uv sync --package chatbot_ui

# Install with frozen lock file (fail if lock is outdated)
uv sync --frozen
```

### Running Commands

```bash
# Run a Python script
uv run python script.py

# Run a module
uv run python -m pytest

# Run with environment file
uv run --env-file .env python script.py

# Run a package's entry point
uv run uvicorn api.app:app --reload
```

### Dependency Management

```bash
# Add a new dependency
uv add requests

# Add a development dependency
uv add --dev pytest

# Remove a dependency
uv remove requests

# Update the lock file
uv lock

# Upgrade all dependencies
uv lock --upgrade

# Upgrade specific package
uv lock --upgrade-package fastapi
```

### Utility Commands

```bash
# Show installed packages
uv pip list

# Show dependency tree
uv pip tree

# Check for outdated packages
uv pip list --outdated

# Export to requirements.txt (for compatibility)
uv pip compile pyproject.toml -o requirements.txt
```

---

## Development vs Production Workflows

### Local Development

```bash
# 1. Clone and enter the repository
cd cohort-repo

# 2. Install all dependencies
uv sync

# 3. Start the API server
uv run uvicorn api.app:app --reload --port 8000

# 4. In another terminal, start the UI
uv run streamlit run apps/chatbot_ui/src/chatbot_ui/app.py
```

### Docker Development

```bash
# Build and start all services
docker compose up --build

# Rebuild only the API
docker compose up --build api

# View logs
docker compose logs -f api
```

### Production Deployment

The Docker images are production-ready with:

- **Frozen dependencies**: `--frozen` ensures the exact lock file versions
- **No dev dependencies**: `--no-dev` reduces image size and attack surface
- **Compiled bytecode**: Faster cold starts
- **Non-root user**: Enhanced security

```bash
# Build production images
docker compose -f docker-compose.prod.yml build

# Deploy
docker compose -f docker-compose.prod.yml up -d
```

---

## Troubleshooting

### Common Issues and Solutions

#### Lock File Out of Sync

```
Error: The lockfile is not up to date with the project's dependencies
```

**Solution**: Update the lock file
```bash
uv lock
```

#### Package Not Found in Workspace

```
Error: Package 'shared' not found in workspace
```

**Solution**: Verify `[tool.uv.sources]` configuration and ensure the package exists in `[tool.uv.workspace].members`

#### Python Version Mismatch

```
Error: Requires Python >=3.14.2 but found 3.11.0
```

**Solution**: Install the correct Python version or update `requires-python` in `pyproject.toml`

#### Cache Issues

```bash
# Clear UV cache
uv cache clean

# Force reinstall all packages
uv sync --reinstall
```

#### Virtual Environment Issues

```bash
# Remove and recreate virtual environment
rm -rf .venv
uv sync
```

---

## Best Practices Summary

1. **Always commit `uv.lock`**: This ensures reproducible builds across all environments.

2. **Use `--frozen` in CI/CD**: Prevents accidental dependency updates during deployment.

3. **Separate dev dependencies**: Use `[dependency-groups]` to keep production images lean.

4. **Pin minimum versions**: Use `>=` specifiers in `pyproject.toml` but let the lock file handle exact versions.

5. **Review lock file changes**: When `uv.lock` changes, review the diff to understand what updated.

6. **Use package-specific installs**: In Docker, use `--package` to install only what each service needs.

7. **Leverage cache mounting**: Use `--mount=type=cache` in Dockerfiles for faster rebuilds.

---

## Additional Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [PEP 621 - Project Metadata](https://peps.python.org/pep-0621/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Docker Best Practices for Python](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

*This guide is part of the AI Engineering Bootcamp learning materials. For questions or contributions, please open an issue in the repository.*
