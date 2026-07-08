# Python Version Compatibility Guide

## Problem Summary

When attempting to install `langgraph` and `ragas` as development dependencies using:

```bash
uv add --dev langgraph ragas
```

The installation failed with the following error:

```
Failed to build `scikit-network==0.33.5`
error: Microsoft Visual C++ 14.0 or greater is required.
```

## Root Cause Analysis

### Dependency Chain
- `ragas` depends on `scikit-network` as a core (non-optional) dependency
- `scikit-network` contains Cython extensions that require C++ compilation
- The project was configured with `requires-python = ">=3.14.2"`

### Why It Failed
1. **Python 3.14 is cutting-edge**: Released recently, many packages don't yet have pre-built binary wheels for this version
2. **No pre-built wheels**: `scikit-network` doesn't have Windows wheels for Python 3.14
3. **Missing build tools**: Without Microsoft Visual C++ Build Tools, source compilation fails on Windows

### Key Insight
Pre-built binary wheels eliminate the need for local compilation. When wheels aren't available for your Python version, pip/uv must build from source, which requires appropriate compilers.

## Solution

### Approach: Downgrade Python Version

We downgraded from Python 3.14 to Python 3.12, which has excellent wheel availability across the ecosystem.

### Steps Taken

1. **Updated Python version requirement** in all `pyproject.toml` files:
   ```toml
   # Before
   requires-python = ">=3.14.2"

   # After
   requires-python = ">=3.12"
   ```

   Files modified:
   - `pyproject.toml` (root)
   - `apps/api/pyproject.toml`
   - `apps/chatbot_ui/pyproject.toml`

2. **Installed Python 3.12** via uv:
   ```bash
   uv python install 3.12
   ```

3. **Created `.python-version` file** to pin the Python version:
   ```bash
   echo "3.12" > .python-version
   ```
   This ensures uv consistently uses Python 3.12 for all operations.

4. **Recreated virtual environment and installed dependencies**:
   ```bash
   rm -rf .venv
   uv venv
   uv add --dev langgraph ragas
   ```

### Verification
```bash
uv run python --version        # Python 3.12.12
uv run python -c "import langgraph; print('langgraph OK')"
uv run python -c "import ragas; print('ragas OK')"
```

## Alternative Solutions

### Option A: Install Visual C++ Build Tools
If you need Python 3.14 specifically:
1. Download from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Install "Desktop development with C++" workload
3. Restart terminal and retry installation

### Option B: Docker-Only Development
The Docker images use Python 3.12 (`python3.12-bookworm-slim`), which handles compilation in a Linux environment where wheels are more readily available.

### Option C: Wait for Wheel Support
Package maintainers typically release wheels for new Python versions within months of release. Check PyPI for wheel availability.

## Prevention Strategies

### 1. Use Stable Python Versions
For production projects, prefer Python versions with at least 6-12 months of ecosystem maturity:
- Python 3.12 (recommended as of 2025)
- Python 3.11 (mature, widely supported)

### 2. Pin Python Version
Always include a `.python-version` file in your project root:
```
3.12
```

### 3. Check Dependency Compatibility
Before upgrading Python, verify critical dependencies have wheel support:
```bash
# Check available wheels on PyPI
pip index versions <package-name>
```

### 4. Align Local and Production Environments
Match your local Python version with Docker/production:
```dockerfile
# Dockerfile
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
```

## Files Reference

| File | Purpose |
|------|---------|
| `pyproject.toml` | Root workspace Python version and dependencies |
| `apps/*/pyproject.toml` | Sub-package Python version requirements |
| `.python-version` | Pins Python version for uv and other tools |
| `uv.lock` | Locked dependency versions (auto-generated) |

## Lessons Learned

1. **Cutting-edge Python versions have trade-offs**: Newer features vs. ecosystem compatibility
2. **Binary wheels matter on Windows**: Without them, you need build tools
3. **uv respects `.python-version`**: This file is essential for consistent environments
4. **Docker environments differ**: Linux containers often have better wheel availability than Windows

## Related Documentation

- [UV Package Manager Guide](UV_PACKAGE_MANAGER.md)
- [Ragas Installation](https://docs.ragas.io/en/stable/getstarted/install/)
- [LangGraph Installation](https://docs.langchain.com/oss/python/langgraph/install)
- [Python Version Support](https://devguide.python.org/versions/)
