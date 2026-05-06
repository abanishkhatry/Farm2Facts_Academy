# CLAUDE.md
# Copy this file into the FEAST backend and frontend repos.

## Project Overview

FEAST (Food Equity Access Simulation Technology) is a full-stack food access simulation tool.
Backend: FastAPI + PostgreSQL + Mesa ABM. Frontend: React + Leaflet + Vite.

## Code Style

- Always use type hints for function parameters and return types
- Use modern Python syntax: `str | None` not `Optional[str]`, `list[dict]` not `List[Dict]`
- Use flake8 for linting; line length is unrestricted (ignore E501)
- Use descriptive variable and function names; avoid abbreviations

## LLM Usage Rules

- Always ask clarifying questions before generating code
- Never generate more than one function at a time
- When reviewing, check against the spec in the linked issue
- All new functions must have type hints
- All new functions must have corresponding tests
- Explain any generated code to the user before moving on

## Dependencies

- Use uv for Python dependency management
- Dependencies are defined in pyproject.toml and locked with uv lock
- Use uv run to execute commands within the project environment

## Testing

- Use pytest for backend tests
- Run tests: uv run pytest tests/ -v
- All new code should have tests. If you can't test something, document why.

## Git Workflow

- main is stable; dev is integration
- Feature branches off dev, named feature/issue-NUMBER-short-desc
- PRs must link to an issue and include a test plan
