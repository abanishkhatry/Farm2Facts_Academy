# Guide: Environment Setup

## Context

Get the FEAST backend and frontend running locally so you can use the tool and explore the code.

## Before You Start

- [ ] Python 3.11+ installed
- [ ] Node.js 18+ and npm installed
- [ ] PostgreSQL running locally (or access to a shared instance)
- [ ] Git configured with GitHub access
- [ ] uv installed (`pip install uv`)

## Steps

### 1. Clone the repos

```bash
git clone https://github.com/ICICLE-ai/Food-Access-Model.git
git clone <fass-frontend-repo-url>
```

### 2. Backend setup

```bash
cd Food-Access-Model
git checkout minimum_viable_product    # active development branch
cp .env.example .env                   # then edit with your DB credentials
uv sync                                # install Python dependencies
```

Required `.env` variables:
```
DB_NAME=fassdb
DB_USER=postgres
DB_PASS=<your-password>
DB_HOST=localhost
DB_PORT=5432
```

You'll need to create the database and tables. Check if there's a schema file or if the app creates tables on startup.

### 3. Run the backend

```bash
uv run uvicorn api_server:app --host 0.0.0.0 --port 8080 --reload
```

Test it:
```bash
curl http://localhost:8080/api/simulation-instances
```

You should get a JSON response (possibly an empty list if no data yet).

### 4. Frontend setup

```bash
cd fass-frontend/fass-react
npm install
```

Create or edit `.env`:
```
VITE_API_URL=http://localhost:8080/api
```

```bash
npm run dev
```

Open http://localhost:5173 in your browser.

### 5. See it work

You should see a Leaflet map centered on Brown County, WI. If there's data in the database, you'll see colored household markers and store markers.

## Common Problems

- **"Connection refused" on backend**: Is PostgreSQL running? Are `.env` creds correct?
- **Empty map**: Database might not have data. Check the preprocessing pipeline or ask if there's a database dump to restore.
- **CORS errors in browser console**: Backend CORS is hardcoded to a Tapis URL in `api_server.py:70`. Change it to allow your localhost origin, or set it to `["*"]` for local dev.
- **Import errors**: Make sure you're on the `minimum_viable_product` branch, not `main`.

## LLM Usage

- You CAN ask the LLM to explain error messages you encounter during setup
- You should NOT ask the LLM to write setup scripts for you

## Definition of Done

- [ ] Backend responds to `curl http://localhost:8080/api/simulation-instances`
- [ ] Frontend loads in browser and shows a map
- [ ] You can see households and/or stores on the map
