# GenAI RAG Agent Platform — Complete Codebase Explanation

> This file contains the FULL detailed explanation for the GenAI RAG Agent Platform codebase.
> - Every application file explained line by line
> - Infrastructure, Docker, and Configuration explained
> - Notebooks detailed for data exploration and RAG evaluation

---

## End-to-End Execution Guide & Workflow

Welcome to the GenAI RAG Agent Platform. This workflow will guide you step-by-step from zero to a fully running local application, including vector database ingestion, pipeline evaluation, and frontend deployment.

### Step 1: Prerequisites
Before starting, ensure you have the following installed on your machine:
- **Docker** and **Docker Compose**: Required to spin up the Qdrant database, FastAPI backend, and Streamlit frontend in isolated containers.
- **uv**: A fast Rust-based Python package manager. It is required for local dependency management and running evaluations.
- **Make**: For running the convenient alias commands in the `Makefile`.

### Step 2: Environment Configuration (`.env`)
1. In the root of the project, locate the `env.example` file.
2. Create a copy of it and name it `.env`:
   ```bash
   cp env.example .env
   ```
3. Open the `.env` file and fill in your actual API keys. At a minimum, you'll need:
   - `GOOGLE_API_KEY`: Used by Gemini for embedding generation and text generation.
   - `LANGSMITH_API_KEY`: (Optional but recommended) Used for tracing your pipeline runs and evaluating the RAG architecture.

### Step 3: Local Environment Setup (`uv sync`)
To run the Jupyter notebooks locally or execute evaluations from your terminal, you must sync your local Python dependencies into a virtual environment:

1. **Sync dependencies**: Run this command in the project root. It creates a `.venv` folder with all required packages.
   ```bash
   uv sync
   ```
2. **Activate the Virtual Environment**: Ensure your terminal uses the local dependencies.
   - On **Linux/macOS**: `source .venv/bin/activate`
   - On **Windows**: `.venv\Scripts\activate.bat`
   *(Your terminal prompt should now show `(.venv)`).*

3. **Launch Jupyter (Browser Method)**: Start the Jupyter Notebook server:
   ```bash
   uv run jupyter notebook
   ```
4. **Selecting the Kernel**:
   - **In VSCode (Recommended)**: Open a `.ipynb` file, click "Select Kernel" in the top right, choose "Python Environments", and select the `.venv` path.
   - **In Jupyter Web UI**: Ensure the active kernel is set to your `.venv` environment.

### Step 4: Data Ingestion & Pipeline Exploration (Notebooks)
To understand how the RAG pipeline is built and to ingest data into Qdrant, follow the Jupyter Notebooks located in the `notebooks/week_1/` directory. Run them sequentially:
1. `01-explore-amazon-dataset.ipynb`: Data exploration of the raw Amazon dataset.
2. `02-RAG-preprocessing-Amazon.ipynb`: Chunking data, generating Gemini embeddings, and pushing them to Qdrant.
3. `03-RAG-pipeline.ipynb`: Structuring the core Python RAG pipeline logic (Retrieval + Generation).
4. `04-evaluation-dataset.ipynb`: Using LLMs to synthetically generate a QA dataset for testing.
5. `05-RAG-Evals.ipynb`: Scoring the pipeline against the evaluation dataset using RAGAS.

### Step 5: Launching the Production Services (Docker)
Once data is ingested into your Qdrant instance via the notebooks, you can spin up the full production application stack (Backend + Frontend + VectorDB).

**To build and start all services, run this command in your terminal:**
```bash
make run-docker-compose
```
*(Alternatively, you can run `docker compose up --build` directly).*

When you run this command:
1. Docker builds the FastAPI backend (`api`) and Streamlit UI (`chatbot_ui`) images.
2. It pulls the official Qdrant image.
3. It mounts local volumes (so code changes reflect instantly without rebuilding).
4. It starts all containers. Wait until the logs show the services are listening.

**Access the Applications:**
- **Ecommerce Assistant UI (Streamlit)**: Open your browser to `http://localhost:8501`. Talk to the chatbot here!
- **Backend API Docs (FastAPI)**: Available at `http://localhost:8000/docs` to test endpoints manually.
- **Qdrant Vector DB Dashboard**: Available at `http://localhost:6333/dashboard`.

### Step 6: Running Automated Evaluations
To formally assess the retriever's performance directly from the command line, run:
```bash
make run-evals-retriever
```
This command uses `uv` to sync dependencies and runs the evaluation script (`evals/eval_retriever.py`) against your configuration, logging the results to LangSmith.

---

## GitHub Collaboration & CI/CD Workflow

To effectively collaborate on this RAG platform and maintain production code quality, we follow a strict Git and GitHub Actions workflow.

### 1. Branching Strategy
Never push directly to the `main` branch. Always create a feature branch for your work:
```bash
git checkout -b feature/add-hybrid-search
```
- Use descriptive branch names (`feature/`, `bugfix/`, `hotfix/`).
- Commit often with clear messages explaining the *why*, not just the *what*.

### 2. Preparing for a Pull Request (PR)
Before pushing your branch, ensure your code is clean and tested locally:
1. **Clean Notebooks**: Never commit notebooks with giant output cells or raw API keys embedded in them. Run `make clean-notebook-outputs` to strip the outputs.
2. **Local Evals**: Run `make run-evals-retriever` locally to ensure your changes didn't degrade the RAG performance.

### 3. Creating the Pull Request
1. Push your branch to GitHub: `git push origin feature/add-hybrid-search`.
2. Open a PR against the `main` branch.
3. In the PR description, explicitly state:
   - What the change is.
   - Which LangSmith evaluation traces correspond to this branch (provide a link to the LangSmith dashboard if possible).

### 4. GitHub Actions (Automated CI/CD)
Ideally, the repository should contain a `.github/workflows/main.yml` file that automates the testing process. A standard GitHub Action for this RAG platform does the following on every PR:
1. **Setup**: Spins up an Ubuntu runner and installs the `uv` package manager.
2. **Install**: Runs `uv sync` to install dependencies.
3. **Format/Lint**: Runs a linter (like Ruff) to ensure PEP8 compliance.
4. **Evaluate**: Runs the `eval_retriever.py` script automatically using securely stored GitHub Secrets (e.g., `GOOGLE_API_KEY` and `LANGSMITH_API_KEY`) to ensure the RAG evaluation scores meet the minimum threshold before the code is allowed to be merged.

#### Example: `.github/workflows/main.yml`
Here is the complete workflow code you can use for reference. You can place this code in `.github/workflows/main.yml` in your repository:

```yaml
name: RAG Pipeline CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test-and-evaluate:
    runs-on: ubuntu-latest

    steps:
    - name: Check out repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.12"

    - name: Install uv package manager
      uses: astral-sh/setup-uv@v2
      with:
        version: "latest"

    - name: Install dependencies
      run: uv sync

    - name: Run RAGAS Evaluations
      env:
        GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
        LANGSMITH_API_KEY: ${{ secrets.LANGSMITH_API_KEY }}
        LANGCHAIN_TRACING_V2: "true"
        LANGCHAIN_PROJECT: "pr-evaluations"
      run: |
        # Set PYTHONPATH to include the api directories
        export PYTHONPATH=$PWD/apps/api:$PWD/apps/api/src:$PYTHONPATH
        # Run the evaluation script via uv
        uv run python -m evals.eval_retriever
```

---


## PART 1 — Project Setup & Infrastructure

---

### 1. `Makefile`
The `Makefile` defines short, memorable command-line aliases for complex or frequently used tasks. It standardizes how developers run the project.

```makefile
run-docker-compose:
	uv sync
	docker compose up --build

clean-notebook-outputs:
	jupyter nbconvert --clear-output --inplace notebooks/*/*.ipynb

run-evals-retriever:
	uv sync
	PYTHONPATH=${PWD}/apps/api:${PWD}/apps/api/src:$$PYTHONPATH:${PWD} uv run --env-file .env python -m evals.eval_retriever
```

#### Line-by-Line Explanation:
- **`run-docker-compose:`** — Defines a Make target. When you type `make run-docker-compose` in the terminal, it executes the indented lines below it.
- **`uv sync`** — Uses the `uv` package manager to ensure all Python dependencies are installed locally based on `pyproject.toml` and `uv.lock`.
- **`docker compose up --build`** — Starts the Docker containers defined in `docker-compose.yml`. The `--build` flag ensures Docker rebuilds the images if any files (like Dockerfiles or source code) have changed since the last run.
- **`clean-notebook-outputs:`** — Another target name.
- **`jupyter nbconvert --clear-output --inplace notebooks/*/*.ipynb`** — Uses Jupyter's CLI tool (`nbconvert`) to strip the output cells from all notebooks in the `notebooks/` subdirectories. This is a best practice before committing notebooks to Git to prevent bloated diffs.
- **`run-evals-retriever:`** — Target to run the retriever evaluation script.
- **`uv sync`** — Ensures dependencies are installed before running evals.
- **`PYTHONPATH=... uv run ...`** — Sets the Python path so imports work correctly across the `apps/api` folder, then uses `uv run` to execute the Python script `evals/eval_retriever.py` while explicitly loading the `.env` file.

---

### 2. `pyproject.toml` (Root Workspace)
This is the modern replacement for `requirements.txt` and `setup.py`. It defines the project metadata and manages dependencies using `uv` workspaces.

```toml
[project]
name = "cohort-repo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "google-genai>=1.58.0",
    "google-generativeai>=0.8.6",
    "groq>=1.0.0",
    "ipykernel>=7.1.0",
    "openai>=2.15.0",
    "pydantic>=2.12.5",
    "pydantic-settings>=2.12.0",
    "python-dotenv>=1.2.1",
    "streamlit>=1.53.0",
]

[tool.uv.workspace]
members = [
    "apps/api",
    "apps/chatbot_ui",
]

[dependency-groups]
dev = [
    "langgraph>=1.0.6",
    "langsmith>=0.6.4",
    "matplotlib>=3.10.8",
    "qdrant-client>=1.16.2",
    "ragas>=0.4.3",
]
```

#### Line-by-Line Explanation:
- **`[project]`** — Start of the project configuration section.
- **`name = "cohort-repo"`** — The name of the Python project/package.
- **`version = "0.1.0"`** — Current version of the project.
- **`description` / `readme`** — Metadata about the project.
- **`requires-python = ">=3.12"`** — Enforces that developers must use Python 3.12 or newer. `uv` will automatically download this Python version if it's missing.
- **`dependencies = [...]`** — The list of core Python packages required for the project to run. Includes LLM SDKs (OpenAI, Groq, Google), web framework dependencies (Streamlit), and data validation (Pydantic).
- **`[tool.uv.workspace]`** — This is a crucial section. It tells `uv` that this is a **monorepo workspace**.
- **`members = ["apps/api", "apps/chatbot_ui"]`** — Registers two sub-packages. Instead of having separate environments for the backend and frontend, `uv` creates a single unified virtual environment and lockfile (`uv.lock`) that resolves dependencies across all apps.
- **`[dependency-groups]` & `dev = [...]`** — Defines packages that are only needed for development (like testing tools or notebook libraries). These will NOT be installed in production Docker containers. Includes `langsmith` for tracing, `ragas` for evaluation, and `qdrant-client` for vector DB interaction in notebooks.

---

### 3. `env.example`
A template showing what environment variables the application requires to function. It is committed to Git because it contains no real secrets.

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=<your-api-key>
LANGSMITH_PROJECT="cohort-project"
```

#### Line-by-Line Explanation:
- **`OPENAI_API_KEY` / `GOOGLE_API_KEY` / `GROQ_API_KEY`** — Placeholders for the API keys needed to call the respective LLM providers.
- **`LANGSMITH_TRACING=true`** — Enables LangSmith to trace and monitor LLM calls (useful for debugging prompt chains and RAG pipelines).
- **`LANGSMITH_ENDPOINT`** — The API endpoint for LangChain's LangSmith service.
- **`LANGSMITH_API_KEY` / `LANGSMITH_PROJECT`** — Authentication and project grouping for LangSmith logs.
> **Note:** A developer must copy this file to `.env` and fill in real values. The actual `.env` file is ignored by Git.

---

### 4. `docker-compose.yml`
This file defines and orchestrates multiple Docker containers so they can run together seamlessly on a shared internal network.

```yaml
services:
  streamlit-app:
    build:
      context: . 
      dockerfile: apps/chatbot_ui/Dockerfile 
    ports:
      - "8501:8501"
    env_file:
      - .env 
    restart: unless-stopped 
    volumes:
      - ./apps/chatbot_ui/src:/app/apps/chatbot_ui/src 

  api:
    build:
      context: .
      dockerfile: apps/api/Dockerfile
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped
    volumes:
      - ./apps/api/src:/app/apps/api/src

  qdrant:
    image: qdrant/qdrant
    ports:
      - 6333:6333
      - 6334:6334
    volumes:
      - ./qdrant_storage:/qdrant/storage:z
    restart: unless-stopped
```

#### Line-by-Line Explanation:
- **`services:`** — Defines the different containers (microservices) that make up the platform.
- **`streamlit-app:`** — The first service, representing the frontend UI.
- **`build:`** — Tells Docker to build this image from local source code rather than downloading it from a registry.
- **`context: .`** — The build context is the root directory. This means the Dockerfile can access `pyproject.toml` and other workspace files.
- **`dockerfile: apps/chatbot_ui/Dockerfile`** — The path to the specific instructions for building the Streamlit image.
- **`ports: - "8501:8501"`** — Maps port 8501 on your local host machine to port 8501 inside the container (Streamlit's default port).
- **`env_file: - .env`** — Automatically loads all environment variables from the `.env` file into the container at runtime.
- **`restart: unless-stopped`** — If the container crashes, Docker will automatically restart it (unless you manually stopped it).
- **`volumes: - ./apps/chatbot_ui/src:/app/apps/chatbot_ui/src`** — Hot-reloading! This maps the local source code into the running container. If you edit a Python file, Streamlit inside the container instantly updates without rebuilding the image.
- **`api:`** — The FastAPI backend service.
- **`dockerfile: apps/api/Dockerfile`** — Uses the backend-specific build instructions.
- **`ports: - "8000:8000"`** — Maps the host's port 8000 to the container's port 8000 (FastAPI/Uvicorn default).
- **`qdrant:`** — The vector database service.
- **`image: qdrant/qdrant`** — Does not build from local code; instead, downloads the official pre-built Qdrant image from Docker Hub.
- **`ports: - 6333:6333`** (HTTP API) and **`6334:6334`** (gRPC API).
- **`volumes: - ./qdrant_storage:/qdrant/storage:z`** — Persistent storage. Maps Qdrant's internal data directory to a local folder (`./qdrant_storage`). This ensures your vector embeddings survive container restarts.

---

### 5. `.gitignore`
The `.gitignore` file tells Git which files and directories to ignore and never commit to version control. 

*(Note: Standard Python boilerplates are omitted from explanation for brevity)*
```gitignore
# ... standard python ignores (__pycache__, *.pyc, etc.) ...
# Environments
.env
.envrc
.venv

# UV / poetry
#uv.lock
#poetry.lock

# Custom project paths
data/
data_1/
qdrant_storage/
```

#### Key Elements Explained:
- **`.env` and `.venv`** — **CRITICAL**: The `.env` file contains secret API keys. Committing it would expose secrets. The `.venv` folder contains downloaded libraries (hundreds of MBs) which should be installed locally, not pushed.
- **`#uv.lock`** — Interestingly, `uv.lock` is commented out, meaning it **WILL** be committed. Committing the lockfile is a best practice for applications because it guarantees that every developer and production server installs the exact same version of every dependency.
- **`data/`, `data_1/`, `qdrant_storage/`** — Ignores local datasets and the local persistent vector database. These files are often huge and specific to a single developer's run.

---

## PART 2 — Containerization (Docker)

---

### 1. `apps/api/Dockerfile`
This Dockerfile defines the environment for the FastAPI backend. It utilizes the `uv` package manager's official image to install dependencies rapidly.

```dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Create non-root user and home directory first
RUN addgroup --system app && \
    adduser --system --ingroup app app && \
    mkdir -p /home/app /app

# Set environment variables
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONOPTIMIZE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV HOME=/home/app
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app/apps/api/src:$PYTHONPATH"

WORKDIR /app

# Copy workspace root files for dependency resolution
COPY pyproject.toml uv.lock ./

# Copy application code (needed before uv sync for workspace packages)
COPY apps/api ./apps/api

# Install dependencies AS ROOT (before switching to app user)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --package api

# Fix permissions - give ownership to app user
RUN chown -R app:app /app /home/app

# Switch to non-root user
USER app

# Expose the FastAPI port
EXPOSE 8000

WORKDIR /app/apps/api/src

# Command to run the application
CMD ["uv", "run", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

#### Line-by-Line Explanation:
- **`FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim`** — The base image. It runs Debian "Bookworm", contains a minimal ("slim") Python 3.12 installation, and comes with `uv` pre-installed.
- **`RUN addgroup --system app && ...`** — Security best practice: Creates a non-root user named `app`. Running applications as the root user inside a container is a security risk.
- **`ENV UV_COMPILE_BYTECODE=1`** — Tells `uv` to precompile Python files to `.pyc` for slightly faster startup times.
- **`ENV PYTHONUNBUFFERED=1`** — Ensures Python prints log messages immediately instead of buffering them. This means you see terminal logs in real time.
- **`ENV PYTHONDONTWRITEBYTECODE=1`** — Prevents Python from writing local `.pyc` files everywhere (which clutters the container), relying instead on UV's compilation.
- **`ENV PATH=...` and `ENV PYTHONPATH=...`** — Adds the virtual environment (`.venv`) to the system path so you don't have to explicitly type `source .venv/bin/activate`. Sets `PYTHONPATH` so imports like `from api.api.endpoints import ...` work.
- **`WORKDIR /app`** — Changes the active directory. All subsequent commands will execute inside `/app`.
- **`COPY pyproject.toml uv.lock ./`** — Copies the workspace root dependency files. We do this *before* copying the source code to take advantage of Docker layer caching (if dependencies don't change, Docker skips reinstalling them).
- **`COPY apps/api ./apps/api`** — Copies the specific `api` package into the container.
- **`RUN --mount=type=cache... uv sync --frozen --no-dev --package api`** — Installs dependencies.
    - `--frozen`: Ensures `uv` strictly obeys the lockfile and doesn't try to upgrade versions.
    - `--no-dev`: Skips installing development tools (like pytest or ragas).
    - `--package api`: Only installs the dependencies required by the `api` app.
    - `--mount=type=cache`: A Docker trick that speeds up subsequent builds by locally caching downloaded Python wheels.
- **`RUN chown -R app:app /app /home/app`** — Changes the file owner from `root` to `app`, so the app user has permission to read and execute the code.
- **`USER app`** — Switches from the `root` user to the secure `app` user for the rest of the build and runtime.
- **`EXPOSE 8000`** — Documentation telling developers that the container listens on port 8000.
- **`WORKDIR /app/apps/api/src`** — Moves into the source directory before running the final command.
- **`CMD ["uv", "run", "uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]`** — The command that runs when the container starts. Starts the Uvicorn ASGI server hosting the FastAPI `app` object defined in `api.app.py`.

---

### 2. `apps/chatbot_ui/Dockerfile`
This Dockerfile defines the environment for the Streamlit frontend. It shares identical structure to the API Dockerfile, with just a few different paths and commands.

```dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# 1. Setup non-root user and home directory
RUN addgroup --system app && \
    adduser --system --ingroup app app && \
    mkdir -p /home/app/.streamlit/data /home/app/.streamlit/cache /app

# 2. Set environment variables
ENV \
    WORKDIR=/app \
    HOME=/home/app \
    UV_COMPILE_BYTECODE=1 \
    PYTHONOPTIMIZE=1 \
    UV_LINK_MODE=copy \
    PYTHONPATH="/app/apps/chatbot_ui/src:$PYTHONPATH" \
    PATH="/app/.venv/bin:$PATH"

WORKDIR $WORKDIR

# 3. Copy workspace files and application code
COPY pyproject.toml uv.lock ./
COPY apps/chatbot_ui ./apps/chatbot_ui

# 4. Install dependencies AS ROOT
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --package chatbot_ui

# 5. Fix permissions
RUN chown -R app:app /app /home/app

# 6. Runtime configuration
EXPOSE 8501

USER app
WORKDIR /app/apps/chatbot_ui/src

CMD ["uv", "run", "streamlit", "run", "chatbot_ui/app.py", "--server.address=0.0.0.0"]
```

#### Line-by-Line Explanation (Differences from API):
- **`mkdir -p /home/app/.streamlit/data ...`** — Streamlit writes cache data to local directories. Creating these explicitly prevents permission errors when the non-root user tries to write to them.
- **`COPY apps/chatbot_ui ./apps/chatbot_ui`** — Copies the frontend application code instead of the backend code.
- **`--package chatbot_ui`** — Tells `uv` to only install the dependencies listed in `apps/chatbot_ui/pyproject.toml` (e.g., Streamlit), avoiding installing FastAPI and backend tools.
- **`EXPOSE 8501`** — Streamlit's default port.
- **`CMD ["uv", "run", "streamlit", "run", "chatbot_ui/app.py", "--server.address=0.0.0.0"]`** — The startup command. Runs the Streamlit web server. `--server.address=0.0.0.0` is required in Docker to allow outside traffic to access the UI (otherwise it binds to `localhost` inside the container, which is unreachable).

---

## PART 3 — FastAPI Backend (RAG Service)

---

### 1. `apps/api/pyproject.toml`
This file configures the `api` app as a sub-package in the `uv` workspace.

```toml
[project]
name = "api"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Misa", email = "you@example.com" }
]
requires-python = ">=3.12"
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

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv.sources]
shared = {workspace = true}
```

#### Line-by-Line Explanation:
- **`[project]`** — Standard metadata block for the backend API package.
- **`dependencies = [...]`** — The backend strictly lists what it needs. Notice that `streamlit` is absent because the backend doesn't serve the UI. It includes `fastapi`, `uvicorn` (the server), `qdrant-client` (vector DB connection), and the LLM SDKs.
- **`[build-system] ... requires = ["hatchling"]`** — Tells `uv` that this package should be built using the `hatchling` backend.
- **`[tool.uv.sources] shared = {workspace = true}`** — This line links this package to the parent `uv` workspace in the root directory.

---

### 2. `apps/api/src/api/core/config.py`
This module loads `.env` variables safely and ensures the app fails fast if a key is missing.

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str
    GROQ_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

config = Config()
```

#### Line-by-Line Explanation:
- **`from pydantic_settings import BaseSettings...`** — Imports Pydantic Settings, a library that maps environment variables directly into Python objects with strict type checking.
- **`class Config(BaseSettings):`** — Defines the schema for required configuration.
- **`OPENAI_API_KEY: str` ...** — By explicitly typing these as `str` without a default value, Pydantic makes them **mandatory**. If you start the app and `OPENAI_API_KEY` is missing from the environment, the app crashes immediately with a clear error message instead of failing cryptically hours later.
- **`model_config = SettingsConfigDict(env_file=".env"...)`** — Automatically searches for a `.env` file and loads the values into this class.
- **`config = Config()`** — Instantiates the class as a singleton. Whenever another file needs an API key, they just do `from core.config import config` and use `config.OPENAI_API_KEY`.

---

### 3. `apps/api/src/api/api/middleware.py`
Middleware is code that runs before and after every single API request. Here, it adds a unique tracking ID to requests.

```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import uuid
import logging

logger = logging.getLogger(__name__)

class RequestIDMiddleware(BaseHTTPMiddleware):
    """Middleware that adds a unique request ID to each request."""

    async def dispatch(self, request: Request, call_next):
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        
        logger.info(f"Request started: {request.method} {request.url.path} (request_id: {request_id})")

        response = await call_next(request)

        response.headers["X-Request-ID"] = request_id
        logger.info(f"Request completed: {request.method} {request.url.path} (request_id: {request_id})")

        return response
```

#### Line-by-Line Explanation:
- **`class RequestIDMiddleware(BaseHTTPMiddleware):`** — Inherits from Starlette's base middleware class (FastAPI is built on Starlette).
- **`async def dispatch(self, request: Request, call_next):`** — The function that intercepts every incoming request.
- **`request_id = str(uuid.uuid4())`** — Generates a random, universally unique identifier (UUID).
- **`request.state.request_id = request_id`** — Attaches the ID to the `request.state` object. This allows any endpoint down the line to read this ID.
- **`logger.info(...)`** — Logs that the request has started.
- **`response = await call_next(request)`** — Pauses the middleware and passes the request down to the actual API endpoint. When the endpoint finishes, it returns the `response` back here.
- **`response.headers["X-Request-ID"] = request_id`** — Adds the generated ID to the HTTP response headers sent back to the client (so the client knows the ID).
- **`return response`** — Finally sends the response back over the network.

---

### 4. `apps/api/src/api/app.py`
The entry point of the FastAPI backend. It wires together middleware and API routes.

```python
from fastapi import FastAPI
from api.api.middleware import RequestIDMiddleware
from fastapi.middleware.cors import CORSMiddleware
from api.api.endpoints import api_router
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(RequestIDMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
```

#### Line-by-Line Explanation:
- **`logging.basicConfig(...)`** — Sets up global logging so all `logger.info()` statements print nicely formatted timestamps to the terminal.
- **`app = FastAPI()`** — Creates the core FastAPI application instance.
- **`app.add_middleware(RequestIDMiddleware)`** — Registers the custom tracking ID middleware explained above.
- **`app.add_middleware(CORSMiddleware...)`** — Adds Cross-Origin Resource Sharing (CORS) middleware. Setting `allow_origins=["*"]` allows any web frontend (like a local Streamlit app or React app) to make requests to this backend without getting blocked by the browser's security policies.
- **`app.include_router(api_router)`** — Connects the routes defined in `endpoints.py` to the main application.

---

### 5. `apps/api/src/api/api/models.py`
Pydantic schemas that define exactly what data the API accepts and returns.

```python
from pydantic import BaseModel, Field

class RAGRequest(BaseModel):
    query: str = Field(..., description="The query to be used in the RAG pipeline")

class RAGResponse(BaseModel):
    request_id: str = Field(..., description="The request ID")
    answer: str = Field(..., description="The answer to the query")
```

#### Line-by-Line Explanation:
- **`class RAGRequest(BaseModel):`** — Defines the JSON body shape the API expects when a client asks a question.
- **`query: str = Field(...)`** — Requires a `query` string. `Field(...)` means it's strictly required.
- **`class RAGResponse(BaseModel):`** — Defines the JSON body shape the API returns.
- **`request_id` and `answer`** — Returns both the generated answer and the tracking ID for the frontend to display.

---

### 6. `apps/api/src/api/api/endpoints.py`
Defines the HTTP routes (the URL endpoints like `/rag/`) that clients can call.

```python
from fastapi import Request, APIRouter
from api.api.models import RAGRequest, RAGResponse
from api.agents.retrieval_generation import rag_pipeline
import logging

# ... logging setup ...

rag_router = APIRouter()

@rag_router.post("/")
def rag(
    request: Request,
    payload: RAGRequest
) -> RAGResponse:

    answer = rag_pipeline(payload.query)

    return RAGResponse(
        request_id=request.state.request_id,
        answer=answer
    )

api_router = APIRouter()
api_router.include_router(rag_router, prefix="/rag", tags=["rag"])
```

#### Line-by-Line Explanation:
- **`rag_router = APIRouter()`** — Creates a mini-FastAPI router to group related RAG endpoints.
- **`@rag_router.post("/")`** — A Python decorator mapping HTTP POST requests to the `rag()` function.
- **`def rag(request: Request, payload: RAGRequest) -> RAGResponse:`** — The function signature. FastAPI automatically reads the incoming JSON, validates it against `RAGRequest`, and binds it to `payload`.
- **`answer = rag_pipeline(payload.query)`** — Calls the actual AI logic (defined in another file), passing the user's question.
- **`return RAGResponse(...)`** — Constructs the Pydantic response object. Notice it pulls the `request_id` out of `request.state.request_id` (put there by our middleware). FastAPI auto-converts this to JSON.
- **`api_router.include_router(rag_router, prefix="/rag")`** — Mounts the `rag_router` so that its `/` endpoint becomes accessible at `/rag/`.

---

### 7. `apps/api/src/api/agents/retrieval_generation.py`
This is the **Core AI Brain** of the backend. It handles embedding generation, Vector DB querying, prompt assembly, and LLM text generation.

```python
from qdrant_client import QdrantClient
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file!")

gemini_client = genai.Client(api_key=GOOGLE_API_KEY)
```

#### Initialization Explanation:
- Imports necessary clients (Qdrant, Google GenAI SDK).
- Checks for the `GOOGLE_API_KEY` explicitly and crashes loudly if missing.
- Instantiates the `genai.Client` globally for reuse.

```python
def get_embedding(text, model="gemini-embedding-001"):
    response = gemini_client.models.embed_content(
        model="gemini-embedding-001", 
        contents=text,
        config=types.EmbedContentConfig()
    )
    return response.embeddings[0].values
```

#### Embedding Explanation:
- **`get_embedding(...)`** — Converts a string of text into a vector of numbers (an embedding) using Google's embedding model.
- **`response.embeddings[0].values`** — Extracts the actual float array from the API response object.

```python
def retrieve_data(query, qdrant_client, k=5):
    query_embedding = get_embedding(query)

    results = qdrant_client.query_points(
        collection_name="Amazon-items-collection-03",
        query=query_embedding,
        limit=k,
    )

    retrieved_context_ids = []
    retrieved_context = []
    similarity_scores = []
    retrieved_context_ratings = []

    for result in results.points:
        retrieved_context_ids.append(result.payload["parent_asin"])
        retrieved_context.append(result.payload["description"])
        retrieved_context_ratings.append(result.payload["average_rating"])
        similarity_scores.append(result.score)

    return {
        "retrieved_context_ids": retrieved_context_ids,
        "retrieved_context": retrieved_context,
        "retrieved_context_ratings": retrieved_context_ratings,
        "similarity_scores": similarity_scores,
    }
```

#### Retrieval Explanation:
- **`query_embedding = get_embedding(query)`** — First, turn the user's text question into an embedding vector.
- **`qdrant_client.query_points(...)`** — Queries the vector database. It searches the `Amazon-items-collection-03` collection for vectors mathematically similar to the `query_embedding`. `limit=k` returns the top 5 matches.
- **`for result in results.points:`** — Loops over the matched vectors and extracts the JSON metadata (`payload`) attached to each vector (like item ID, description, and rating).
- Returns a dictionary containing lists of the matched context pieces.

```python
def process_context(context):
    formatted_context = ""
    for id, chunk, rating in zip(context["retrieved_context_ids"], context["retrieved_context"], context["retrieved_context_ratings"]):
        formatted_context += f"- ID: {id}, rating: {rating}, description: {chunk}\n"
    return formatted_context

def build_prompt(preprocessed_context, question):
    prompt = f"""
You are a shopping assistant that can answer questions about the products in stock.
You will be given a question and a list of context.
Instructtions:
- You need to answer the question based on the provided context only.
- Never use word context and refer to it as the available products.

Context:
{preprocessed_context}

Question:
{question}
"""
    return prompt
```

#### Prompt Engineering Explanation:
- **`process_context()`** — Takes the raw lists of retrieved data and zips them together into a readable text string (e.g., `- ID: 123, rating: 4.5, description: Great laptop`).
- **`build_prompt()`** — Takes the formatted context and the user's question, injecting them into a strict system prompt. It instructs the LLM to act as a shopping assistant and explicitly forbids hallucination ("based on the provided context only").

```python
def generate_answer(prompt, model_name="gemini-2.5-flash"):
    response = gemini_client.models.generate_content(
        model=model_name,
        contents=prompt,
    )
    return response.text

def rag_pipeline(question, top_k=5):
    qdrant_client = QdrantClient(url="http://qdrant:6333", check_compatibility=False)
    retrieved_context = retrieve_data(question, qdrant_client, top_k)
    preprocessed_context = process_context(retrieved_context)
    prompt = build_prompt(preprocessed_context, question)
    answer = generate_answer(prompt)
    return {"answer": answer, "retrieved_context": retrieved_context["retrieved_context"]}
```

#### Pipeline Integration Explanation:
- **`generate_answer()`** — Sends the massive compiled prompt to `gemini-2.5-flash` and returns the generated text.
- **`rag_pipeline()`** — The orchestrator function. It links the previous steps sequentially:
  1. Retrieve raw data from DB.
  2. Preprocess data into a string.
  3. Build the prompt.
  4. Generate the LLM answer.
  5. Return the answer (the `endpoints.py` file calls this function).

---

### 8. `apps/api/evals/eval_retriever.py`
This script uses the **Ragas** framework to evaluate the performance of the RAG pipeline.

```python
from api.agents.retrieval_generation import rag_pipeline
import os

from qdrant_client import QdrantClient
from langsmith import Client

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper

from ragas.dataset_schema import SingleTurnSample 
from ragas.metrics import IDBasedContextPrecision, IDBasedContextRecall, Faithfulness, ResponseRelevancy

os.environ["LANGCHAIN_CONCURRENCY_LIMIT"] = "10"

ls_client = Client()
qdrant_client = QdrantClient(
    url=f"http://localhost:6333"
)

ragas_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4.1-mini"))
ragas_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="text-embedding-3-small"))
```

#### Initialization Explanation:
- **`os.environ["LANGCHAIN_CONCURRENCY_LIMIT"] = "10"`** — Limits parallel requests so we don't hit OpenAI API rate limits during evaluation.
- **`ragas_llm` / `ragas_embeddings`** — Sets up the "Judge LLM". Here, we use OpenAI's models to judge the quality of our Gemini RAG system's answers.

```python
async def ragas_faithfulness(run, example):
    sample = SingleTurnSample(
            user_input=run.outputs["question"],
            response=run.outputs["answer"],
            retrieved_contexts=run.outputs["retrieved_context"]
        )
    scorer = Faithfulness(llm=ragas_llm)
    return await scorer.single_turn_ascore(sample)
```

#### Metrics Explanation:
- **`ragas_faithfulness`** — Measures if the answer is completely faithful to the retrieved context (no hallucinations). It extracts the input, response, and context from the pipeline run, and uses the `Faithfulness` scorer to generate a metric (0.0 to 1.0).
- **`ragas_responce_relevancy`** — Measures if the generated answer actually addresses the user's question.
- **`ragas_context_precision_id_based`** and **`ragas_context_recall_id_based`** — Measure the quality of the retriever. Did it fetch the correct product IDs? Did it rank them highly?

```python
results = ls_client.evaluate(
    lambda x: rag_pipeline(x["question"]),
    data="rag-evaluation-dataset",
    evaluators=[
        ragas_faithfulness,
        ragas_responce_relevancy,
        ragas_context_precision_id_based,
        ragas_context_recall_id_based
    ],
    experiment_prefix="retriever",
)
```

#### Evaluation Runner Explanation:
- **`ls_client.evaluate(...)`** — Uses LangSmith to execute the evaluation.
- **`lambda x: rag_pipeline(...)`** — For every row in the dataset, run our custom `rag_pipeline`.
- **`data="rag-evaluation-dataset"`** — The name of the dataset stored in LangSmith (created previously in the notebooks).
- **`evaluators=[...]`** — Applies the 4 custom Ragas scoring functions defined above to every result, and logs everything to LangSmith under the `retriever` experiment name.

---

## PART 4 — Streamlit Frontend (Chatbot UI)

---

### 1. `apps/chatbot_ui/pyproject.toml`
This file configures the Streamlit frontend as the second sub-package in the `uv` workspace.

```toml
[project]
name = "chatbot-ui"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Misa", email = "you@example.com" }
]
requires-python = ">=3.12"
dependencies = [
    "pydantic>=2.12.5",
    "pydantic-settings>=2.12.0",
    "streamlit>=1.53.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv.sources]
shared = {workspace = true}
```

#### Line-by-Line Explanation:
- **`dependencies = [...]`** — The frontend requires only `streamlit` for the UI, and `pydantic`/`pydantic-settings` for validating configuration. It deliberately does not include the LLM SDKs or FastAPI because all AI processing happens on the backend.
- **`[tool.uv.sources] shared = {workspace = true}`** — Links this sub-package to the shared root `uv.lock` file.

---

### 2. `apps/chatbot_ui/src/chatbot_ui/core/config.py`
This module defines where the frontend should look for the backend API.

```python
"""according to instructor, this is just a placeholder to maintain structure"""
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    API_URL: str = "http://api:8000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

config = Config()
```

#### Line-by-Line Explanation:
- **`API_URL: str = "http://api:8000"`** — This is the internal URL that Streamlit uses to talk to FastAPI. `http://api` works because Docker Compose magically routes the hostname `api` to the backend container.
- If a developer needs to run it differently, they can override this by adding `API_URL="http://localhost:8000"` to their `.env` file.

---

### 3. `apps/chatbot_ui/src/chatbot_ui/app.py`
This is the Streamlit web application. It handles user input, communicates with the API over HTTP, and displays the conversation.

```python
import streamlit as st
import requests
from chatbot_ui.core.config import config

def api_call(method, url, **kwargs):
    def _show_error_popup(message):
        """Show error message as a popup in the top-right corner."""
        st.session_state["error_popup"] = {
            "visible": True,
            "message": message,
        }

    try:
        response = getattr(requests, method)(url, **kwargs)

        try:
            response_data = response.json()
        except requests.exceptions.JSONDecodeError:
            response_data = {"message": "Invalid response format from server"}

        if response.ok:
            return True, response_data

        return False, response_data

    except requests.exceptions.ConnectionError:
        _show_error_popup("Connection error. Please check your network connection.")
        return False, {"message": "Connection error"}
    except requests.exceptions.Timeout:
        _show_error_popup("The request timed out. Please try again later.")
        return False, {"message": "Request timeout"}
    except Exception as e:
        _show_error_popup(f"An unexpected error occurred: {str(e)}")
        return False, {"message": str(e)}
```

#### HTTP Helper Explanation:
- **`api_call(method, url, **kwargs)`** — A central wrapper function for all network requests. Centralizing API calls prevents writing messy `try/except` blocks everywhere in the UI code.
- **`response = getattr(requests, method)(url, **kwargs)`** — Dynamically calls `requests.get()` or `requests.post()` based on the `method` string passed in.
- **`response_data = response.json()`** — Parses the backend's JSON response (like `RAGResponse`).
- **`if response.ok:`** — Returns a tuple: `(True, data)` if the HTTP status is 200 OK.
- **`except requests.exceptions.ConnectionError:`** — Gracefully handles the scenario where the FastAPI backend crashes or isn't running, saving the error message to the session state so Streamlit can display a popup instead of crashing completely.

```python
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
```

#### Chat Initialization Explanation:
- **`st.session_state`** — Streamlit reruns the *entire script from top to bottom* every time a user interacts with the app. `st.session_state` is a dictionary that survives these reruns. We use it to store the chat history.
- **`if "messages" not in ...`** — On the very first page load, initialize the chat history with a greeting from the assistant.
- **`for message in st.session_state.messages:`** — Loops through the saved conversation history.
- **`st.chat_message(message["role"])`** — Creates a visual chat bubble UI element. If the role is "assistant", it gives it an AI icon. If "user", it gives it a human icon.
- **`st.markdown(message["content"])`** — Renders the text inside the bubble, supporting Markdown (bold, lists, code blocks).

```python
if prompt := st.chat_input("Hello! How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        is_success, response_data = api_call("post", f"{config.API_URL}/rag", json={"query": prompt})
        
        if is_success:
            answer = response_data.get("answer", "No answer provided.")
        else:
            answer = f"⚠️ API Error: {response_data.get('detail', response_data.get('message', 'Unknown error'))}"
            
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
```

#### Chat Interaction Loop Explanation:
- **`if prompt := st.chat_input(...)`** — Displays a text input box at the bottom of the screen. The script pauses here until the user types something and presses Enter. The `:=` operator assigns the typed text to `prompt` and checks if it's not empty in one line.
- **`st.session_state.messages.append(...)`** — Saves the user's new message to the persistent history.
- **`with st.chat_message("user"): st.markdown(prompt)`** — Immediately draws the user's message on the screen.
- **`with st.chat_message("assistant"):`** — Creates an empty AI chat bubble on the screen while we wait for the backend.
- **`output = api_call("post", f"{config.API_URL}/rag", json={"query": prompt})`** — Sends a POST request to `http://api:8000/rag` with a JSON payload: `{"query": "User text"}`.
- **`answer = response_data["answer"]`** — Extracts the LLM's answer from the parsed JSON response.
- **`st.write(answer)`** — Prints the LLM's response into the AI chat bubble on the screen.
- **`st.session_state...append({"role": "assistant", "content": answer})`** — Finally, saves the AI's response to the persistent history so it stays on screen during the next script rerun.
## Part 5: Notebooks

---

## Part 5.0: LLM API Prerequisites (`notebooks/prerequisites/01-llm-apis.ipynb`)

### Overview
Before building a complex RAG system, we must ensure our foundational tools—the LLM APIs—are configured and responding correctly. This short prerequisite notebook acts as a "Hello World" to verify connectivity with three major AI providers: OpenAI, Google (Gemini), and Groq. 

### Step 1: Loading the Environment
```python
from dotenv import load_dotenv
import os

load_dotenv("../../.env")
```
*   **The "Why"**: APIs require authentication via secret keys. Instead of hardcoding them (a major security risk), we load them securely from the `.env` file located in the root of our workspace.

### Step 2: Testing the Clients
The notebook proceeds to test each client individually by asking them to "print random words".

1.  **OpenAI Client**: Tests connectivity using the standard `openai` SDK. 
2.  **Google GenAI Client**: Uses the `google-genai` SDK and our `GOOGLE_API_KEY` to prompt the `gemini-2.5-flash` model. This is the model we will use for our final RAG generation.
3.  **Groq Client**: Tests Groq's high-speed inference engine using the `llama-3.3-70b-versatile` open-source model.

If all three cells execute and return random words without `Unauthorized` or `Connection` errors, our environment is fully ready for the bootcamp.

---

## Part 5.1: Exploring the Amazon Dataset (`notebooks/week_1/01-explore-amazon-dataset.ipynb`)

### Overview
Data wrangling is the unglamorous but essential first step of any ML project. In this notebook, we take the massive raw Amazon Electronics dataset (millions of rows) and filter it down into a clean, highly relevant subset of 100 items that we can comfortably embed and search locally on our laptops.

### Step 1: Parsing Raw JSONL Data
The raw data comes in `.jsonl` (JSON Lines) format, where every single line is a complete JSON object representing one product.

```python
import json
import pandas as pd

with open('../../data/meta_Electronics.jsonl', 'r') as f:
    first_line = json.loads(f.readline())
```
*   **The "Why"**: We inspect the first line to understand the schema. We discover fields like `title`, `average_rating`, `description`, `images`, and `details`.

### Step 2: Temporal Filtering (2022 and Newer)
RAG systems are often used to answer questions about *recent* data. We write a filter to only keep products that became available in 2022 or later.

```python
def filter_data(data: dict) -> dict:
    filter = False
    if int(data['details']['Date First Available'][-4:]) < 2022:
        filter = True
    return filter
```
*   **The "Why"**: We open the massive raw file, stream it line-by-line (to prevent running out of RAM), apply this filter, and write the valid lines to a new file: `meta_Electronics_2022_2023.jsonl`.

### Step 3: Categorical Filtering
We apply a second pass to remove any products that lack a `main_category` tag.

```python
def filter_category(data: dict) -> dict:
    filter = False
    if data['main_category'] == None:
        filter = True
    return filter
```

### Step 4: Data Visualization & Subsetting
We load our cleaned, recent, categorized data into a Pandas DataFrame to visualize it.

```python
df = pd.read_json("../../data/meta_Electronics_2022_2023_with_category.jsonl", lines=True)

# Count products per category
category_counts = df['main_category'].value_counts()
category_counts.plot(kind='bar', figsize=(10, 6))
```
*   **The "Why"**: Visualizing the distribution ensures we don't have massive imbalances (e.g., 99% phone cases and 1% laptops).
*   **The Final Output**: Finally, we extract exactly 100 diverse rows and save them to `Amazon-items-subset-100.jsonl`. This small, perfectly formatted file is what our RAG pipeline will ingest in the next notebook.

---


## Part 5.2: RAG Data Preprocessing & Vector Database Setup (`notebooks/week_1/02-RAG-preprocessing-Amazon.ipynb`)

### Overview
This notebook is the critical bridge between raw data and our Retrieval-Augmented Generation (RAG) system. Its primary purpose is to take the cleaned Amazon product data, convert the text into numerical vectors (embeddings) using Google's Gemini API, and store these vectors in our local Qdrant Vector Database. This enables the core semantic search capability of our RAG pipeline.

### Prerequisites & Setup
Before we begin vectorizing data, we need the right tools to connect to Gemini and Qdrant.

```python
!pip install -qU google-genai qdrant-client python-dotenv
```
*   **`google-genai`**: The official SDK to interact with Google's Gemini models (including the embedding model).
*   **`qdrant-client`**: The Python client to connect to and interact with our running Qdrant Vector Database container.
*   **`python-dotenv`**: A utility to load our `.env` file containing the `GOOGLE_API_KEY`.

### Step 1: Loading Dependencies and Data
We start by loading our previously cleaned JSONL dataset.

```python
import json
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from google import genai
from google.genai import types

# Load environment variables (importantly, GOOGLE_API_KEY)
load_dotenv()

# Load the previously extracted Amazon data
data_to_embed = []
with open("../../data/amazon_data.jsonl", "r") as f:
    for line in f:
        data_to_embed.append(json.loads(line))
```
*   **Why this matters**: We are loading the `amazon_data.jsonl` file we prepared in the previous notebook into memory. Each item in `data_to_embed` is a Python dictionary containing the product `description`, `image` URL, `price`, etc. 

### Step 2: Defining the Embedding Function
Embeddings are the backbone of semantic search. They convert human-readable text into a list of numbers (a vector) that captures the "meaning" of the text.

```python
gemini_client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_embedding(text, task_type="RETRIEVAL_DOCUMENT"):
    """
    Generates an embedding vector for the given text using Gemini's current model.
    """
    response = gemini_client.models.embed_content(
        model="gemini-embedding-001", 
        contents=text,
        config=types.EmbedContentConfig(
            task_type=task_type
        )
    )
    return response.embeddings[0].values

# Verify the embedding dimensionality
len(get_embedding("Hi")) # Returns 3072
```
*   **The "Why"**: 
    *   We initialize the `genai.Client`.
    *   We use the `gemini-embedding-001` model. This model converts any string of text into a vector of exactly **3072 dimensions** (floating-point numbers). 
    *   `task_type="RETRIEVAL_DOCUMENT"` tells the model that this text is intended to be stored and searched against later. This optimizes the vector representation for semantic search.

> [!WARNING]
> **Deprecation Notice Addressed**: Earlier versions of this codebase might have used the deprecated `google.generativeai` package. We have successfully migrated to the new, official `google.genai` SDK.

### Step 3: Setting up the Qdrant Vector Database
With our data in memory and an embedding function ready, we need a place to store the vectors.

```python
# Connect to local Qdrant container
qdrant_client = QdrantClient(url="http://localhost:6333")

# Create the collection
qdrant_client.create_collection(
    collection_name="Amazon-items-collection-03",
    vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
)
```
*   **The Connection**: We connect to `http://localhost:6333`, which is the default port for the Qdrant REST API exposed by our Docker container.
*   **Creating the Collection**: A "collection" in Qdrant is akin to a table in a relational database.
*   **`size=3072`**: This is crucial. We must explicitly tell Qdrant that every vector we insert will have exactly 3072 dimensions (matching the output of `gemini-embedding-001`). If there's a mismatch, Qdrant will throw an error.
*   **`distance=Distance.COSINE`**: This defines *how* we measure similarity. Cosine distance measures the angle between two vectors, which is the industry standard for determining semantic similarity between text embeddings.

### Step 4: Structuring Data for Qdrant (PointStructs)
Qdrant requires data to be formatted in a specific way before insertion: using the `PointStruct` object.

```python
pointstructs = []
for i, data in enumerate(data_to_embed):
    # Generate the vector for the product description
    embedding = get_embedding(data["description"])
    
    # Create the PointStruct
    pointstructs.append(
        PointStruct(
            id=i, # Unique integer ID
            vector=embedding, # The 3072-dimensional vector
            payload=data, # The original dictionary (metadata)
        )
    )
```
*   **The "Why"**: A `PointStruct` requires three components:
    1.  `id`: A unique identifier (we simply use the loop index `i`).
    2.  `vector`: The actual list of 3072 numbers representing the text.
    3.  `payload`: The metadata. By passing our entire `data` dictionary as the payload, we ensure that when we retrieve a vector later, we get back the `image` URL, `price`, and `rating_number` along with it.

### Step 5: Uploading to Qdrant (The Upsert)
Finally, we send all our structured points to the database.

```python
qdrant_client.upsert(
    collection_name="Amazon-items-collection-03",
    points=pointstructs,
)
```
*   **The Execution**: The `upsert` command ("update or insert") pushes the list of `pointstructs` to our Qdrant container. Once this completes, our Vector Database is fully populated and ready to serve semantic queries!

---
## Part 5.3: The End-to-End RAG Pipeline (`notebooks/week_1/03-RAG-pipeline.ipynb`)

### Overview
With our Vector Database populated, this notebook combines all the pieces to create a functional, interactive RAG (Retrieval-Augmented Generation) pipeline. It demonstrates how to take a user's natural language question, search the database for relevant products, format those products into a prompt, and ask a generative LLM (Gemini 2.5 Flash) to synthesize a coherent answer.

### Step 1: The Retrieval Function
The first half of RAG is **Retrieval**. When a user asks a question, we don't know the answer, but our database might have the relevant context.

```python
def retrieve_data(query, qdrant_client, k=5):
    # 1. Convert the user's text question into a vector
    query_embedding = get_embedding(query)

    # 2. Perform a semantic search in Qdrant
    results = qdrant_client.query_points(
        collection_name="Amazon-items-collection-03",
        query=query_embedding,
        limit=k,
    )

    # 3. Extract the useful information from the search results
    retrieved_context_ids = []
    retrieved_context = []
    similarity_scores = []
    retrieved_context_ratings = []

    for result in results.points:
        retrieved_context_ids.append(result.payload["parent_asin"])
        retrieved_context.append(result.payload["description"])
        retrieved_context_ratings.append(result.payload["average_rating"])
        similarity_scores.append(result.score)

    return {
        "retrieved_context_ids": retrieved_context_ids,
        "retrieved_context": retrieved_context,
        "retrieved_context_ratings": retrieved_context_ratings,
        "similarity_scores": similarity_scores,
    }
```
*   **The Vector Search**: Qdrant takes our query vector and compares it against all 3072-dimensional vectors in the database using Cosine Similarity. It returns the top `k` closest matches.
*   **Data Extraction**: The `results` object contains the `PointStructs` we inserted in the previous notebook. We loop through them and pull out the `payload` (our metadata) and the `score` (how closely it matched the query).

### Step 2: Processing and Prompt Building
Raw database results aren't useful to an LLM. We must format them into a human-readable string.

```python
def process_context(context):
    formatted_context = ""
    for id, chunk, rating in zip(context["retrieved_context_ids"], context["retrieved_context"], context["retrieved_context_ratings"]):
        formatted_context += f"- ID: {id}, rating: {rating}, description: {chunk}\n"
    return formatted_context

def build_prompt(preprocessed_context, question):
    prompt = f"""
You are a shopping assistant that can answer questions about the products in stock.

You will be given a question and a list of context.

Instructions:
- You need to answer the question based on the provided context only.
- Never use word context and refer to it as the available products.

Context:
{preprocessed_context}

Question:
{question}
"""
    return prompt
```
*   **Context Formatting**: `process_context` creates a bulleted list of the top retrieved products, including their ID, rating, and description.
*   **Prompt Engineering**: `build_prompt` uses an f-string to dynamically insert the retrieved product descriptions (`{preprocessed_context}`) and the user's original `{question}` into a strict set of instructions. 
    *   **Crucial Instruction**: *"You need to answer the question based on the provided context only."* This constraint minimizes hallucination, forcing the model to act solely as a synthesizer of our data rather than relying on its internal, potentially outdated knowledge base.

### Step 3: Generative Answer
The second half of RAG is **Generation**. We send our highly specific prompt to the LLM.

```python
def generate_answer(prompt, model_name="gemini-2.5-flash"):
    """
    Generates a response using the specified Gemini model.
    """
    response = gemini_client.models.generate_content(
        model=model_name,
        contents=prompt,
    )
    return response.text
```
*   **`gemini-2.5-flash`**: We utilize Google's `gemini-2.5-flash` model via the `google.genai` SDK. It is highly optimized for speed and low-latency text tasks, making it ideal for real-time chatbot interactions.

### Step 4: The Orchestrator (`rag_pipeline`)
Finally, we wrap all individual functions into a single pipeline.

```python
def rag_pipeline(question, top_k=5):
    qdrant_client = QdrantClient(url="http://localhost:6333")
    
    # 1. Retrieve raw data
    retrieved_context = retrieve_data(question, qdrant_client, top_k)
    
    # 2. Format context
    preprocessed_context = process_context(retrieved_context)
    
    # 3. Build Prompt
    prompt = build_prompt(preprocessed_context, question)
    
    # 4. Generate Answer
    answer = generate_answer(prompt)
    
    return answer

# Example Usage
print(rag_pipeline("What kind of earphones can I get with ratings above 4.3?"))
```
*   **The Full Flow**: In a single function call, a natural language query is vectorized, searched, formatted, and answered intelligently based *only* on the products in our Amazon dataset. This pipeline represents the core logic that will eventually be moved into the FastAPI backend (`apps/api/src/api/agents/retrieval_generation.py`).

---
## Part 5.4: Generating Synthetic Evaluation Data (`notebooks/week_1/04-evaluation-dataset.ipynb`)

### Overview
Before deploying a RAG system to production, we must measure its accuracy and reliability. However, creating a comprehensive evaluation dataset manually is extremely time-consuming. This notebook demonstrates a modern AI engineering technique: using a powerful LLM (like Gemini) to generate a synthetic evaluation dataset based on our own data, and then uploading it to an evaluation tracking platform (LangSmith).

### Step 1: Downloading Context from Qdrant
To generate questions about our products, the LLM first needs to know what products exist. 

```python
# Download 100 product entries from our local Vector DB
all_points = qdrant_client.scroll(
    collection_name="Amazon-items-collection-03",
    limit=100,
    offset=None,
    with_payload=True,
    with_vectors=False # We only need the text, not the numbers
)

# Format the data into a simple list of dictionaries
all_context = [{"id": data.payload["parent_asin"], "text": data.payload["description"]} for data in all_points[0]]
```
*   **The "Why"**: We extract a sample of our actual product data from Qdrant. We explicitly ask for `with_payload=True` (to get the text) but `with_vectors=False` (to save memory, since the LLM can't read vector numbers).

### Step 2: Prompt Engineering for Synthetic Data Generation
We create a highly specific `SYSTEM_PROMPT` to instruct Gemini on how to act as a dataset generator.

```python
# 1. Define the exact JSON structure we expect back
output_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "question": {"type": "string", "description": "Suggested question."},
            "chunk_ids": {"type": "array", "items": {"type": "string"}},
            "answer_example": {"type": "string", "description": "Suggested answer grounded in the context."},
            "reasoning": {"type": "string", "description": "Reasoning why the question could be answered with the chunks."},
        },
    },
}

# 2. Instruct the model on the distribution of questions
SYSTEM_PROMPT = f"""
I am building a RAG application. I have a collection of 50 chunks of text...
I want you to come up with 30 questions to which the answers could be grounded in the chunk context.
Construct 10 questions that could use multipple chunks in the answer.
Construct 15 questions that could use single chunk in the answer.
Construct 5 questions that can't be answered with the available chunks.

<OUTPUT JSON SCHEMA>
{json.dumps(output_schema, indent=2)}
</OUTPUT JSON SCHEMA>
"""
```
*   **Structured Output (JSON)**: By providing a strict JSON Schema, we ensure the LLM returns data that Python can easily parse, rather than a wall of unstructured text.
*   **Data Distribution**: We intentionally ask for different *types* of questions. 
    *   **Single-chunk**: Tests basic retrieval.
    *   **Multi-chunk**: Tests the system's ability to synthesize answers from multiple products (e.g., comparing two items).
    *   **Unanswerable**: Tests the system's ability to politely decline answering when it doesn't have the context (preventing hallucination).

### Step 3: LLM Generation and Parsing
We send the prompt and our `all_context` to Gemini, and parse the resulting JSON.

```python
# Send request to Gemini
response = gemini_client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[SYSTEM_PROMPT, all_context],
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
    )
)

# Parse the text response into a list of Python dictionaries
json_output = json.loads(response.text)
```

### Step 4: Uploading to LangSmith for Tracking
With our synthetic dataset generated (containing `question`, `answer_example`, and the ground truth `chunk_ids`), we upload it to LangSmith. LangSmith is an observability platform specifically built for LLM applications.

```python
from langsmith import Client

# Initialize the LangSmith client using the API key in our .env
client = Client(api_key=os.environ["LANGSMITH_API_KEY"])

# Create a new dataset project
dataset_name = "rag-evaluation-dataset"
dataset = client.create_dataset(
    dataset_name=dataset_name,
    description="Dataset for evaluating RAG pipeline"
)

# Upload each generated example to the LangSmith dataset
for item in json_output:
    client.create_example(
        dataset_id=dataset.id,
        inputs={"question": item["question"]},
        outputs={
            "ground_truth": item["answer_example"],
            "reference_context_ids": item["chunk_ids"],
            "reference_descriptions": [get_description(id) for id in item["chunk_ids"]]
        }
    )
```
*   **The "Why"**: 
    *   `inputs`: This is what our RAG pipeline will eventually be tested against (the user's question).
    *   `outputs`: This is the "answer key". It contains what the LLM *should* generate (`ground_truth`) and the specific database chunks it *should* retrieve (`reference_context_ids`). 
    *   In the next notebook, we will run our actual pipeline against this dataset and LangSmith will grade its performance!

---
## Part 5.5: Evaluating the RAG Pipeline with RAGAS (`notebooks/week_1/05-RAG-Evals.ipynb`)

### Overview
This final notebook closes the loop on our RAG architecture. We have a pipeline, and we have a synthetic evaluation dataset. Now, we use the **RAGAS** (Retrieval Augmented Generation Assessment) framework to score our pipeline against the dataset. This allows us to quantify performance and track improvements over time.

### Step 1: Loading the Evaluation Dataset
We start by retrieving the dataset we uploaded to LangSmith in the previous step.

```python
from langsmith import Client

client = Client()
dataset = client.read_dataset(dataset_name="rag-evaluation-dataset")

# Pull an example to evaluate
reference_input = list(client.list_examples(dataset_id=dataset.id, limit=10))[0].inputs
reference_output = list(client.list_examples(dataset_id=dataset.id, limit=10))[0].outputs
```
*   **The "Why"**: We need the `reference_input` (the question) to feed into our pipeline, and the `reference_output` (the ground truth answer and context IDs) to compare against our pipeline's output.

### Step 2: Running the RAG Pipeline
We define a slightly modified `rag_pipeline` function. Instead of just returning the text answer, it returns a dictionary containing all intermediate states (the retrieved contexts, IDs, and scores).

```python
def rag_pipeline(question, top_k=5):
    qdrant_client = QdrantClient(url="http://localhost:6333", check_compatibility=False)
    
    retrieved_context = retrieve_data(question, qdrant_client, top_k)
    preprocessed_context = process_context(retrieved_context)
    prompt = build_prompt(preprocessed_context, question)
    answer = generate_answer(prompt)
    
    return {
        "answer": answer,
        "question": question,
        "retrieved_context_ids": retrieved_context["retrieved_context_ids"],
        "retrieved_context": retrieved_context["retrieved_context"],
        "similarity_scores": retrieved_context["similarity_scores"]
    }

# Run the pipeline on the test question
result = rag_pipeline(reference_input["question"])
```

### Step 3: Setting up RAGAS Evaluators
RAGAS evaluates two distinct parts of our pipeline: **Generation** (how good the LLM's answer is) and **Retrieval** (how good Qdrant's search was).

```python
from ragas.dataset_schema import SingleTurnSample 
from ragas.metrics import IDBasedContextPrecision, IDBasedContextRecall, Faithfulness, ResponseRelevancy
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Initialize the "Judge" LLM used for evaluation
ragas_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))
ragas_embeddings = LangchainEmbeddingsWrapper(OpenAIEmbeddings(model="text-embedding-3-small"))
```
*   **The "Judge" LLM**: RAGAS uses an LLM to grade our LLM. Here, we configure `gpt-4o-mini` (or an equivalent model) as the objective scorer.

### Step 4: Generation Metrics (Faithfulness & Relevancy)
These metrics determine if the LLM is behaving correctly *given* the retrieved context.

```python
async def ragas_faithfulness(run, example):
    sample = SingleTurnSample(
        user_input=run["question"],
        response=run["answer"],
        retrieved_contexts=run["retrieved_context"]
    )
    scorer = Faithfulness(llm=ragas_llm)
    return await scorer.single_turn_ascore(sample)
```
*   **`Faithfulness`**: Measures hallucinations. Does the `answer` contain information that is *not* present in the `retrieved_contexts`? If yes, the score drops.
*   **`ResponseRelevancy`**: Measures if the `answer` actually addresses the user's `question`. It penalizes evasive or overly verbose, off-topic answers.

### Step 5: Retrieval Metrics (Precision & Recall)
These metrics determine if our Vector Database and Embedding model are finding the right documents.

```python
async def ragas_context_precision_id_based(run, example):
    sample = SingleTurnSample(
        retrieved_context_ids=run["retrieved_context_ids"],
        reference_context_ids=example["reference_context_ids"]
    )
    scorer = IDBasedContextPrecision()
    return await scorer.single_turn_ascore(sample)
```
*   **`IDBasedContextPrecision`**: Of the chunks we retrieved (`retrieved_context_ids`), how many were actually relevant (in the `reference_context_ids`)? And were the most relevant ones ranked at the top?
*   **`IDBasedContextRecall`**: Did we manage to retrieve *all* the relevant chunks that existed in the database? If the ground truth required 3 chunks, and we only retrieved 2 of them, our recall score drops.

> [!TIP]
> **Continuous Improvement**: By automating these evaluations, we can confidently experiment with different chunk sizes, embedding models, or prompts. If a change improves our RAGAS scores across the dataset, we know it's safe to deploy to production.

---

## PART 6 — Interview Preparation: Key Questions & Answers

### 1. Architecture & Infrastructure

**Q: Why did you choose FastAPI over Flask or Django for the backend?**
**A:** FastAPI was chosen for its high performance (built on Starlette and Pydantic) and native async/await support, which is critical for I/O-bound operations like calling the Gemini API and querying the Qdrant Vector DB. Additionally, its automatic generation of OpenAPI (Swagger) documentation makes testing endpoints straightforward.

**Q: How does the communication work between your Streamlit frontend, FastAPI backend, and Qdrant database in your Docker setup?**
**A:** We use a `docker-compose.yml` file to orchestrate three separate containers. By placing them on a shared custom bridge network (`rag-network`), they can communicate using their service names as hostnames (e.g., FastAPI connects to Qdrant via `http://qdrant:6333` and Streamlit connects to FastAPI via `http://api:8000`). This ensures secure internal communication without exposing all ports to the host machine.

### 2. Retrieval-Augmented Generation (RAG) vs. Fine-Tuning

**Q: Why use RAG instead of just fine-tuning the Gemini model on your Amazon product dataset?**
**A:** RAG provides three massive advantages over fine-tuning for this use case:
1. **Real-time Updates:** If a product's price or rating changes, or a new product is added, we just update the Qdrant database. Fine-tuning would require retraining the model entirely.
2. **Hallucination Prevention (Groundedness):** RAG forces the model to answer *only* based on the provided context chunks. Fine-tuned models still rely on their internal weights and can easily hallucinate fake features or prices.
3. **Cost & Speed:** Embedding text into Qdrant is drastically cheaper and faster than fine-tuning a massive LLM.

### 3. Embeddings & Vector Databases (Qdrant)

**Q: What is an embedding, and why are we using `gemini-embedding-001` with 3072 dimensions?**
**A:** An embedding is a numerical representation of text (a vector array) that captures semantic meaning. We use `gemini-embedding-001` to map our product descriptions into a 3072-dimensional space. Words or products with similar features (e.g., "wireless earbuds" and "Bluetooth headphones") will have vectors that point in roughly the same direction, allowing us to find related products even if the exact keywords don't match.

**Q: What metric do you use to calculate the similarity between the user's question and the product embeddings?**
**A:** We use **Cosine Similarity**. Cosine similarity measures the angle between two vectors rather than their magnitude (length). This is crucial for text search because a long product description and a short user query might have very different magnitudes, but if they point in the same semantic direction, the angle between them will be small, indicating high relevance.

### 4. Advanced Prompt Engineering

**Q: How do you prevent the LLM from answering questions outside the scope of your inventory?**
**A:** We enforce strict constraints in the System Prompt. We explicitly instruct the model: *"You need to answer the question based on the provided context only"* and *"If the answer cannot be found... politely state that you do not have that information."* By injecting the retrieved Qdrant results directly into the prompt as the sole source of truth, we tightly bound the model's reasoning capabilities.

### 5. Evaluation & RAGAS

**Q: How do you mathematically prove your RAG pipeline is working? What is RAGAS?**
**A:** We use the **RAGAS (Retrieval Augmented Generation Assessment)** framework. Because manual testing is unscalable, we first generate a synthetic evaluation dataset (questions paired with known ground-truth context IDs). RAGAS uses a "Judge LLM" to score our pipeline on two main fronts:
- **Generation Metrics:** 
  - **Faithfulness:** Does the generated answer contain hallucinations, or is it strictly derived from the retrieved context?
  - **Response Relevancy:** Did the answer actually address the user's question without useless verbosity?
- **Retrieval Metrics:**
  - **Context Precision:** Did Qdrant retrieve the most relevant chunks, and were they ranked at the top?
  - **Context Recall:** Did Qdrant successfully retrieve *all* the chunks necessary to fully answer the question?
