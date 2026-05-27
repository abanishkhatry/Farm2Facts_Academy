---
layout: default
title: "Guide: Filing Good Issues"
---

# Guide: Filing Good Issues

## Context

Issues are how the team builds its backlog. Every problem, inconsistency, or improvement idea you discover should become a GitHub issue. This is not busywork; it's how real projects organize work.

> **Beyond this project:** The structure of a good issue (what you observed, where, why it matters, proposed fix) is the same structure you'd use to describe a problem to a manager, write a bug report for a vendor, or scope a project request. Master this format here and you'll use it everywhere.

## Before You Start

- [ ] You've completed your codebase trace (or explored the code enough to find things)
- [ ] You have access to the GitHub repo

## How to Write a Good Issue

### Title

Clear and specific. A developer should be able to understand the problem from the title alone.

Good:
- "Import paths inconsistent between api_server.py and routes.py"
- "CORS origin hardcoded to Tapis URL, breaks local development"
- "household.py:85 - normalized formula uses unexplained magic numbers"

Bad:
- "fix imports"
- "CORS doesn't work"
- "clean up code"

### Body

Use the issue templates provided in `.github/ISSUE_TEMPLATE/`. At minimum include:

- **What you observed** (quote the specific code if possible)
- **Where it is** (file + line number)
- **Why it's a problem**
- **Proposed fix** (optional, but a suggestion helps the person who picks it up)

### Labels

- `bug` - Something is broken or produces wrong results
- `enhancement` - New feature or capability
- `refactor` - Code cleanup, no behavior change

## Examples of Issues You Should Find

These are real problems in the current FEAST codebase:

- `api_server.py` imports from `repository.db_repository` but `routes.py` imports from `food_access_model.repository.db_repository`
- CORS is hardcoded to `https://fassfrontstage.pods.icicleai.tapis.io`
- `pyproject.toml` says Python 3.11.11, Dockerfile uses 3.12
- `profiling` module is imported in `api_server.py` but doesn't exist in the source tree
- `print()` used instead of `logging` in `api_server.py` and `geo_model.py`
- Magic numbers in `household.py`: `normalized = abs(((value)-40)/60)`, scores of 95 and 55, income thresholds of 10000/15000/25000
- Deprecated `on_event("startup")` pattern in `routes.py`
- `MapComponent.js` uses raw DOM manipulation (`createElement`, `appendChild`) instead of React components
- Frontend mixes Bootstrap and Tailwind CSS frameworks
- `SEARCHRADIUS` and `CRS` defined in both `constants.py` and `geo_model.py`

## LLM Usage

- You CAN ask the LLM to explain why something you found might be a problem
- You should NOT ask the LLM to "find all the issues in this file"

## Definition of Done

- [ ] At least 3 issues filed
- [ ] Each has a clear title, description, file/line location, and label
- [ ] Issues are on the GitHub project board
