---
layout: default
title: "Backend Onboarding Guide"
---

# Farm2Facts Backend Onboarding Guide

This guide covers what the backend is, how to clone it, and how to run it locally.

---

## About this Repo

A Python API server that runs the food access simulation. It exposes REST endpoints the frontend calls, manages simulation instances in the database, and runs a Mesa agent-based model to compute food access scores for thousands of households.

**Key technologies:**
- FastAPI (REST API framework)
- Mesa + mesa-geo 0.8.0 (agent-based modeling with geographic support)
- asyncpg (async PostgreSQL driver, used for API queries)
- psycopg2 (sync PostgreSQL driver, used in the data repository layer -- a known inconsistency)
- shapely, osmnx, pyproj (spatial operations)
- multiprocessing (parallel simulation steps across CPU cores)

**Key architecture notes:**
- Serves the REST API at `/api/` prefix
- `GeoModel` manages all agents; each `Household` agent runs its own food access calculation on each simulation step
- Uses multiprocessing to split households across CPU cores -- configurable via `NUMBER_PROCESSES` in `.env`
- Preprocessing pipeline (`preprocessing/get_data.py`) fetches Census data and OpenStreetMap store locations to initialize a simulation area
- Currently hardcoded to Brown County, Wisconsin (FIPS 55009, center 44.5/-88.0, 15km radius)

**Active development branch:** `minimum_viable_product`

---

## Cloning the Repository

Follow the same SSH or HTTPS steps described in the [Frontend Guide](FRONTEND_GUIDE.md#cloning-the-repository), substituting the backend repo URL:

**SSH:**
```bash
git clone git@git.doit.wisc.edu:at-trad/farm2facts-backend.git
```

**HTTPS:**
```bash
git clone https://git.doit.wisc.edu/at-trad/farm2facts-backend.git
```

---

## Running Locally

### Step 1: Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Set up your `.env` file

Create a `.env` file at the root of the repo with your database credentials:

| Variable | Purpose |
| --- | --- |
| `DB_HOST` | Database host (e.g., `localhost`) |
| `DB_PORT` | Database port (e.g., `5432`) |
| `DB_NAME` | Database name |
| `DB_USER` | Database user |
| `DB_PASS` | Database password |
| `NUMBER_PROCESSES` | CPU cores for simulation steps (e.g., `4`) |

**Warning:** Always check `DB_HOST` before running. Never point a local backend at the staging database -- a local process writing to a shared database will corrupt shared data.

### Step 4: Start the server

```bash
python run_local.py
```

This runs `uvicorn food_access_model.main:app --reload --port 8000`.

Do not use `api_server.py` or `server.py` -- they have different CORS settings and will cause frontend connection issues.

### Step 5: Verify it works

Open `http://localhost:8000/docs` in your browser. The FastAPI auto-generated docs should load and list all available routes under `/api/`.
