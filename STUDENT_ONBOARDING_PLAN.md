# FEAST Student Developer Onboarding Plan

## Constraints

- **Group time**: ~2 hours/week, 6 weeks (buffer from 8)
- **Solo time**: Additional async hours later in the week (varies by student availability)
- **Team**: 5 CS students, freshmen to seniors, varying experience
- **Goal**: Revamp the FEAST tool while teaching LLM-assisted development practices
- **Repos**: `ICICLE-ai/Food-Access-Model` (backend, branch `minimum_viable_product`), `ICICLE-ai/FASS-Frontend` (frontend, branch `Brown-County-Frontend`)
- **Active backend variant**: The `bc_pantries` branch extends the model with food pantry support (FSA score of 25 for pantries, prioritized for low-income households). Check which branch is canonical before the cohort starts.

## How This Plan Works

Each week has three parts:
1. **Group session** (~2 hours): Short lesson + demo of a new LLM workflow pattern, then guided work on assigned issues using scaffolded guides
2. **Solo work** (async, later in the week): Students apply that week's patterns independently to push the codebase forward. This is where the real learning happens. Each week's solo section gives a clear "hunting ground" and the LLM workflow to use, but students choose *what* to work on.
3. **PR review + issue creation** (async): Review each other's PRs, and file issues for anything discovered during solo work

**Students own the roadmap.** Starting week 1, students file GitHub issues for every problem, inconsistency, or improvement they discover. By week 3, students participate in triaging and prioritizing issues. By week 5, students are proposing and scoping their own features. The backlog is a living artifact the team shapes together, not a static assignment list.

Issues from the real backlog are mapped to each week as **assigned work** (scaffolded, everyone does these). Solo work is **self-directed** (students pick from issues they or others have filed, or tackle stretch goals).

Students are labeled by experience tier:
- **J** (junior, freshmen/sophomores): More scaffolding, smaller scope
- **S** (senior, juniors/seniors): Less scaffolding, more autonomy

---

## Week 1: Orientation, Setup, and Understanding the System

This is the most important week. Students need to get the project running, understand what it does conceptually, and see how the pieces fit together before touching any code. Senior students act as guides for juniors throughout.

### Group Session Part 1: Domain, Concepts, and Architecture (~60 min)

**Topic: "What this project does, why it matters, and how it's built"**

Walk through these concepts as a group. This is lecture + discussion, not hands-on yet. The goal is that every student leaves this session able to explain the project to someone outside the team.

#### Food accessibility: the problem (~10 min)

**What is food access?** The ability of a household to regularly obtain adequate, affordable, nutritious food. It's not just about whether a grocery store exists nearby. It depends on:
- **Distance** to stores (especially supermarkets vs. convenience stores)
- **Transportation** (does the household have a vehicle? Is there public transit?)
- **Income** (can the household afford to make regular trips to more distant but better-stocked stores?)
- **Store quality** (a supermarket with fresh produce is different from a convenience store with mostly packaged food)

**Why it matters.** The USDA estimates that roughly 19 million Americans live in "food deserts," areas where access to affordable, nutritious food is limited. Low food access correlates with poor diet, higher rates of obesity and diabetes, and other health outcomes. It disproportionately affects low-income communities and communities of color.

**What decisions does this affect?** Cities and counties make decisions every year about zoning, subsidies, and infrastructure that affect food access:
- Should we subsidize a new grocery store in this underserved neighborhood?
- What happens to food access if this Walmart closes?
- Where should we invest in public transit to improve food access?
- How does adding a farmers' market affect the surrounding area?

These are the questions FEAST is built to help answer. The tool lets a user set up a geographic area, place stores and households, and simulate how food access scores change when stores are added, removed, or relocated.

#### Agent-based modeling: the approach (~15 min)

**What is agent-based modeling (ABM)?**

ABM is a simulation technique where you model individual "agents" that each follow simple rules, and then observe the emergent behavior of the whole system. Instead of writing one big equation that describes food access for a whole city, you create thousands of individual household agents that each independently figure out where to shop.

Key properties of ABMs:
- **Heterogeneous agents**: Each household has its own income, location, vehicle count, etc. No two agents are identical. This captures real-world diversity.
- **Local interactions**: Each agent only "sees" its local environment (nearby stores, its own resources). Global patterns emerge from many local decisions.
- **Steps over time**: The simulation advances in discrete steps. Each step, every agent re-evaluates its situation. This lets you model change: what happens over 6 months if a store opens or closes?
- **What-if scenarios**: You can add/remove stores and re-run to see counterfactual outcomes.

**How FEAST uses ABM:**

In FEAST, there are two types of agents:
- **Household agents**: Represent a single household. Each has attributes from Census data (income, household size, vehicles, workers) and a geographic location within a census tract.
- **Store agents**: Represent a food store (supermarket, convenience store, grocery, etc.). Each has a type, name, and location from OpenStreetMap.

On each simulation step, every household agent:
1. Calculates its distance to every store
2. Identifies the closest supermarket and the closest non-supermarket
3. Decides where to "shop" each of its monthly trips (based on distance, resources, and vehicle access)
4. Computes a food access score based on how many trips went to supermarkets (high food quality) vs. convenience stores (lower food quality)

The scoring uses the **MFAI (Monthly Food Access Index)** from Koh et al. 2019. The basic idea:
- A trip to a supermarket scores 95 (good food availability)
- A trip to a convenience store scores 55 (limited food availability)
- A trip to a food pantry scores 25 (minimal food availability; `bc_pantries` branch only)
- A household's MFAI is the average of its monthly trip scores
- Households with more resources (income, vehicles) make more trips (7-8/month) and are more likely to reach distant supermarkets
- Households without vehicles or with low income make fewer trips (6/month) and tend to use the closest store regardless of type
- Low-income households (income at or below $25k) may prioritize food pantries when available (`bc_pantries` branch)

This means a household's score isn't just about distance. A car-owning household far from a supermarket may score higher than a carless household next to a convenience store, because the car-owner can reach the supermarket.

The `has_resources()` function (household.py:169) determines resource status using income thresholds that vary by household size: $10k for singles, $15k for 2-person, $25k for 3+ person households.

**The Mesa framework:** FEAST uses [Mesa](https://mesa.readthedocs.io/) via [mesa-geo](https://github.com/projectmesa/mesa-geo) v0.8.0, a Python ABM library with geographic extensions. Mesa provides:
- A `Model` class that holds all agents and manages simulation steps (see `abm/geo_model.py`)
- A `GeoAgent` class that defines individual agent behavior with geographic coordinates (the `step()` method)
- A `GeoSpace` that enables spatial operations like distance calculations between agents
- A `DataCollector` that records agent state at each step
- A `RandomActivation` scheduler that runs agents in random order each step

You don't need to understand Mesa deeply to contribute. The key thing to know: when `GeoModel.step()` is called, it triggers `Household.step()` on every household agent, which is where all the food access math happens. In practice, this step is run via `batch_running.py` which splits households across CPU cores for parallelism.

#### Use cases and stakeholders (~5 min)

**Who uses this tool?**
- **Urban planners**: Evaluating proposed grocery store locations or transit improvements
- **Public health researchers**: Studying the relationship between food access and health outcomes across demographics
- **Policy analysts**: Modeling the impact of store closures (e.g., when a chain pulls out of a low-income area)
- **Community organizations**: Advocating for food access improvements with data-driven arguments
- **Students and researchers**: Learning about spatial modeling, food systems, and agent-based simulation

**Example scenarios:**
- A city wants to know: "If we give a tax break to attract a grocery store to neighborhood X, how many households see improved food access?"
- A Walmart announces closure. "Which households are most affected? Where should a replacement be located?"
- A transit agency asks: "If we add a bus route connecting neighborhood Y to the nearest supermarket, how does that change access scores for carless households?"
- A researcher wants to compare food access patterns across different counties by initializing FEAST with different Census geographies.

**Where the project came from:** FEAST originated through the NSF-funded ICICLE AI institute (OAC 2112606). The current implementation is focused on Brown County, Wisconsin as a proof of concept, with the goal of making it work for any US county.

#### How the three layers work together (~15 min)

Draw this on a whiteboard or shared screen:

```
+-------------------+     HTTP/JSON      +-------------------+     SQL       +------------+
|                   | ----------------> |                   | -----------> |            |
|  Frontend (React) |  Axios (client.js) |  Backend (FastAPI) |  asyncpg     | PostgreSQL |
|                   | <---------------- |                   | <----------- |            |
+-------------------+  ORJSONResponse    +-------------------+   rows        +------------+
  - Leaflet map                           - API routes (/api/)               - households
  - Marker clustering                     - Mesa ABM model                   - food_stores
  - User controls                         - Multiprocessing batch runner     - simulation_instances
  - Score visualization                   - MFAI calculation                 - roads (unused)
  - proj4 coord transform                 - Census data pipeline
                                          - Store polygon generation
```

**Frontend** (`ICICLE-ai/FASS-Frontend`, `fass-react/` directory, branch `Brown-County-Frontend`):
- **Live instance:** https://fassfrontstage.pods.icicleai.tapis.io/ (Tapis/ICICLE staging). Students should open this before setup to see the working product.
- React 19 app built with Vite
- Leaflet map displays households (colored by food access score: green=high, red=low) and stores (supermarket hexagons, convenience store triangles)
- Marker clustering groups households at low zoom levels, expanding at zoom 17+
- User can add stores (click map to place), multi-select and remove stores (Ctrl/Cmd+click), step the simulation, and reset
- Talks to backend via Axios HTTP client. The API base URL is **hardcoded** in `src/shared/client.js` (not an env var). Students must edit this file to point at their local backend.
- State management uses React Context API (`StoreContext`, `HouseholdContext`) plus `window` object globals (an anti-pattern students will notice)
- Deployed via Docker (multi-stage: Node build, Nginx serve) behind nginx
- Key dependencies: React 19, Leaflet, react-leaflet, Axios, Bootstrap, Tailwind, proj4 (coordinate projection)

**Backend** (`Food-Access-Model/`, branch `minimum_viable_product`):
- FastAPI serves the REST API (`/api/` prefix)
- **Two entry points exist** (a source of confusion for students):
  - `food_access_model/main.py` is the primary entry (used by `run_local.py`). CORS allows `localhost:5173`.
  - `api_server.py` at the repo root is an older alternative. CORS allows only a Tapis staging URL.
  - `server.py` at the repo root is yet another alternative with custom logging.
  - Students should use `food_access_model.main:app` via `run_local.py`.
- Uses the Mesa ABM framework (via mesa-geo 0.8.0): `GeoModel` holds all agents, `Household` and `Store` extend Mesa's `GeoAgent`
- On each simulation step, Mesa calls `step()` on every household agent, which recalculates distances, picks stores, and computes MFAI
- Simulation steps use multiprocessing (`model_multi_processing/batch_running.py`): households are split across CPU cores, each chunk runs in a separate process. Configurable via `NUMBER_PROCESSES` env var.
- The preprocessing pipeline (`preprocessing/get_data.py`, 1134 lines) fetches Census data from the Census Bureau API and store locations from OpenStreetMap to initialize a new simulation area. Store data can also be loaded from CSV via `insert_stores.py`.
- Currently hardcoded to Brown County, Wisconsin (FIPS code 55009, center 44.5/-88.0, 15km radius)
- Key dependencies: FastAPI, Mesa + mesa-geo, asyncpg, psycopg2, shapely, osmnx, pyproj, gunicorn, orjson
- A special `default_simulation` instance is protected from deletion and serves as the base dataset for new instances

**Database** (PostgreSQL, async via asyncpg connection pool):
- `simulation_instances` table: UUID primary key, name (unique), description, created_at
- `households` table: one row per household per simulation step (id, simulation_instance_id, simulation_step, centroid_wkt in EPSG:4326, income, household_size, vehicles, number_of_workers, walking/biking/transit/driving times, food_score, stores_within_1_mile, closest_store_miles)
- `food_stores` table: one row per store per simulation step (store_id, simulation_instance_id, simulation_step, name, shop type, geometry as WKT polygon in EPSG:3857)
- `roads` table exists but is unused (potential future feature)
- Stores and households are duplicated across steps (step 0, step 1, step 2...) so you can compare state over time
- Household coordinates stored in EPSG:4326 (lat/lon), store geometries in EPSG:3857 (Web Mercator, meters). This inconsistency is a known issue (see #67).

**Key concept for students**: When a user clicks "Step" in the UI, this happens:
1. Frontend calls `POST /api/simulation-instances/{id}/advance`
2. Backend reads all households and stores for the current step from the DB
3. Backend splits households into chunks (one per CPU core) for parallel processing
4. Each chunk creates a Mesa `GeoModel` with those households and all stores
5. Mesa's `RandomActivation` scheduler calls `Household.step()` on every household
6. Each household calculates distances to all stores, finds closest supermarket and convenience store, simulates monthly shopping trips, computes MFAI score, and assigns a color (red/yellow/green)
7. Results from all chunks are collected and bulk-inserted to the DB as a new step number (via `copy_records_to_table` for performance)
8. Frontend fetches the updated households via `GET /api/households?simulation_instance=...&simulation_step=...` and re-renders the map with new colors

#### How LLM tools fit into development (~5 min)

**Key rule: You must be able to explain every line in your PR without looking at your chat history.** This is the one rule that doesn't change across all 6 weeks.

Brief demo: Show how to use Claude Code to *understand* existing code conversationally. Walk through asking "What does this function do and why?" vs "Write me a function." The first question helps you learn; the second skips learning.

For this week, LLMs are for **asking questions about code you're reading**. Not for writing code.

### Group Session Part 2: Setup (~30 min)

**Before touching any code, have everyone open the live instance:** https://fassfrontstage.pods.icicleai.tapis.io/. Spend 2-3 minutes clicking around as a group: look at the map, click a household, click "Step," add a store. This gives students a concrete mental model of the product before they wade into setup and configuration.

Senior students guide juniors through setup. Pair each J student with an S student. If setup takes longer than 30 min (it often does), students finish during solo time. The important thing is that everyone has at least one working environment by the end of the session, even if it's one S student's machine that others can pair on.

[SCAFFOLD: Environment Setup Guide]
```
Prerequisites:
- Python 3.11+ installed
- Node.js 18+ and npm installed
- PostgreSQL running locally (or access to a shared instance)
- Git configured with GitHub access
- uv installed (pip install uv)

Step 1: Clone the repos
   git clone https://github.com/ICICLE-ai/Food-Access-Model.git
   git clone https://github.com/ICICLE-ai/FASS-Frontend.git

Step 2: Backend setup
   cd Food-Access-Model
   git checkout minimum_viable_product    # active development branch
   cp .env.example .env                   # then edit with your DB credentials
   uv sync                                # install Python dependencies

   Required .env variables:
   DB_NAME=fassdb            # your local PostgreSQL database name
   DB_USER=postgres          # your PostgreSQL username
   DB_PASS=<your-password>
   DB_HOST=localhost
   DB_PORT=5432
   NUMBER_PROCESSES=4        # CPU cores for multiprocessing (optional)

   You'll need to create the database and tables. Check if there's
   a schema file or if the app creates tables on startup.

Step 3: Run the backend
   uv run python run_local.py

   This runs: uvicorn food_access_model.main:app --reload --port 8000
   
   IMPORTANT: Use run_local.py or food_access_model.main:app.
   Do NOT use api_server.py (an older entry point with different
   CORS settings that will cause issues).
   
   For production-style: uv run gunicorn food_access_model.main:app \
     -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 --timeout 600

   Test it: curl http://localhost:8000/api/simulation-instances
   You should get a JSON response (possibly empty list if no data yet).
   Health check: curl http://localhost:8000/api/health

Step 4: Frontend setup
   cd FASS-Frontend/fass-react
   git checkout Brown-County-Frontend     # active development branch
   npm install

   Edit src/shared/client.js line 3:
   Change the baseURL to: 'http://127.0.0.1:8000/api'
   (The file has commented alternatives for staging/production URLs.
   There is no .env-based configuration; the URL is hardcoded.)

   npm run dev
   Open http://localhost:5173 in your browser.

Step 5: See it work
   You should see a Leaflet map centered on Brown County, WI
   (Green Bay area). If there's data in the database, you'll see
   colored household markers (clustered at low zoom, individual
   at zoom 17+) and store markers (hexagons for supermarkets,
   triangles for convenience stores).

   Try: Click a household marker to see its popup (income, vehicles,
   food access score). Click a store to see its name and type.

Common problems:
- "Connection refused" on backend: Is PostgreSQL running? Are .env
  creds correct? Is the backend on port 8000 (run_local.py) or
  8080 (gunicorn)? Make sure client.js matches.
- Empty map: Database might not have data. You may need to run the
  preprocessing pipeline or restore a database dump. Ask the
  instructor for the current data loading approach.
- CORS errors in browser console: If using food_access_model/main.py
  (via run_local.py), CORS already allows localhost:5173. If you
  accidentally used api_server.py, it only allows a Tapis staging
  URL and you'll get CORS errors.
- Import errors: Make sure you're on the minimum_viable_product
  branch (backend) and Brown-County-Frontend branch (frontend).
  The main branch has different code.
- Store data loading: If the database has no stores, use
  insert_stores.py with a CSV file to load store data:
  python insert_stores.py stores.csv

S students: Help J students debug setup issues. If you solve
something non-obvious, write it down. These notes become part of
the CONTRIBUTING.md you'll write later.
```

### Assigned Work (~30 min remaining, continues into solo time)

**Everyone: Use the running app, then trace one endpoint**

First, spend 10 minutes just *using* the application. Use your local instance if it's running, or the live instance at https://fassfrontstage.pods.icicleai.tapis.io/ if local setup isn't done yet:
- Create a simulation instance (if the UI supports it, or via curl)
- Look at the map. Click on households. Read the popup data.
- Click "Step" to advance the simulation. Watch the colors change.
- Add a store near a cluster of red (low-access) households. Step again. Did scores improve?
- Remove a store. Step. What happens?

Understanding what the tool *does* is prerequisite to understanding how it *works*.

Then, each student traces one API endpoint through the full stack and writes a short description (3-5 paragraphs) of the flow in their own words:

| Student | Endpoint | Key Files | What to Focus On |
|---------|----------|-----------|-----------------|
| Student A (J) | `GET /simulation-instances` | `food_access_model/api/routes.py:98` -> SQL query -> ORJSONResponse | Simplest endpoint. How does a request become a database query become a JSON response? |
| Student B (J) | `GET /households` | `routes.py:273` -> query with simulation_instance + step params -> WKT geometry | How is household data structured? What do the column names mean? What is WKT? |
| Student C (J/S) | `POST /stores` (add store) | `routes.py:308` -> `helpers.py:29 convert_centroid_to_polygon` -> polygon geometry -> SQL insert | How does a lat/lon become a polygon? Why hexagons for supermarkets and triangles for convenience stores? |
| Student D (S) | `POST /simulation-instances/{id}/advance` | `routes.py:155` -> `_run_model_step` -> `batch_running.py:batch_run` (multiprocessing) -> `GeoModel.step()` -> `Household.step()` | The core simulation loop. How does a "step" work? Why multiprocessing? |
| Student E (S) | `POST /simulation-instances` (create) | `routes.py:191` -> copies households/stores from default_simulation -> `_run_model_step` | What happens when you create a new simulation? What is the default_simulation and why can't it be deleted? |

**S students**: After finishing your own trace, check in with your paired J student. Help them understand their endpoint if they're stuck. Don't do it for them; ask guiding questions.

**LLM usage**: Students can ask the LLM to explain specific functions, but must verify explanations against the code. Deliverable is their own writing, not LLM output.

### Deliverable
Each student opens a PR adding their trace as a markdown file in `docs/traces/`. These get reviewed as a group next week.

### Solo Work (later in the week)

**Part 1: Explore more of the codebase and the domain.**

Now that you've traced one endpoint, explore the parts you didn't cover. Some suggestions by experience level:

**J students**: Read through the frontend code (`fass-react/src/App.jsx`, the component files in `src/components/`). Try to match what you see in the browser to what's in the code. Which component renders the map? (`MapComponent.js`, 526 lines). Which one handles "Add Store"? (`AddStoreButton.jsx` + `AddStoreModal.jsx`). Where do the household colors come from? (Hint: the backend sends them, but trace it.) Why does the code store things on the `window` object? Ask the LLM to explain things you don't understand, but verify against the code.

**S students**: Read `food_access_model/abm/household.py` carefully, especially `get_mfai()` (line 218), `has_resources()` (line 169), and `step()` (line 259). These are the core of the simulation. Try to understand the MFAI scoring logic. What do the magic numbers mean (95, 55, 0.8, 10000/15000/25000)? Read the data pipeline in `preprocessing/get_data.py` (1134 lines, focus on the main functions, not every line). How does Census data become synthetic households? Also look at `model_multi_processing/batch_running.py` to understand how simulation steps are parallelized.

**Part 2: File issues for everything you found.**

During your trace and exploration, you encountered things that seemed wrong, confusing, or inconsistent. Now turn each one into a GitHub issue. This is not busywork; this is how real projects build their backlog.

[SCAFFOLD: Issue Filing Guide]
```
For each problem you found, open a GitHub issue with:

Title: Clear, specific (e.g., "Import paths inconsistent between
   api_server.py and routes.py" not "fix imports")

Body:
- What you observed (quote the specific code)
- Where it is (file + line number)
- Why it's a problem
- (Optional) What you think the fix might be

Label it: bug, enhancement, or refactor

Examples of things you probably found:
- Three different entry points (api_server.py, server.py,
  food_access_model/main.py) with different CORS and logging configs
- api_server.py imports a `profiling` module that doesn't exist
  (dead code, import is commented out but still present)
- api_server.py CORS allows only a Tapis staging URL, while
  food_access_model/main.py allows localhost:5173
- pyproject.toml says Python 3.11.11, Dockerfile says 3.12
- deprecated on_event("startup"/"shutdown") pattern in routes.py
  (FastAPI lifespan context manager is the modern approach)
- print() used instead of logging in multiple files
- Magic numbers in household.py (95, 55, 0.8, 10000/15000/25000)
  with no explanation of what they represent
- Frontend stores state on the window object (window.simulationInstances,
  window.stepNumber, etc.) instead of using React state properly
- MapComponent.js uses raw DOM manipulation and imperative Leaflet
  API instead of React-Leaflet declarative components
- Frontend mixes Bootstrap and Tailwind CSS frameworks
- Frontend API URL hardcoded in client.js instead of using env vars
- No error handling or loading states if the API is unreachable
- Household coordinates stored as EPSG:4326, store geometries
  as EPSG:3857 (inconsistent CRS across tables)
- db_repository.py (sync psycopg2) and routes.py (async asyncpg)
  both query the same database with different connection patterns

Goal: Each student should file at least 3 issues. These become
the backlog your team works from in later weeks.
```

**Stretch (S students):** If you found something small enough to fix in 30 minutes (e.g., the CORS hardcoding, a print-to-logging conversion), fix it, open a PR, and link it to the issue you filed. First taste of the full cycle: find it, file it, fix it.

**S students helping J students:** If a J student is struggling to find issues, pair up over chat or a quick call. Walk them through one file together, pointing out things that seem off. The J student files the issues (they need the practice), but the S student helps them see what to look for.

### Roadmap Activity
Review each other's filed issues at the start of next week's session. As a group, label them by priority (must-fix, should-fix, nice-to-have) and add them to the GitHub project board.

---

## Week 2: Linting, Type Hints, and First Real PRs

### Group Session (30 min)
**Topic: "Using LLMs for edge case brainstorming and test design"**

Demo: Show the "interview first" pattern. Instead of "write tests for this function," show how to describe the function's behavior to the LLM and ask "What edge cases should I test?" Then the student writes the tests.

Also introduce: PR template, branch workflow (`dev` -> feature branches), commit conventions.

### Assigned Work

The following issues map directly to the backlog. Pair J students with S students where possible.

#### Issue #24: Incorporate linting (1 student, J or S)

[SCAFFOLD: Linting Setup Guide]
```
1. Add flake8 to dev dependencies in pyproject.toml
2. Create a .flake8 config file:
   - Ignore E501 (line length - per project convention)
   - Set max-complexity to 10
3. Run flake8 on the codebase. You'll get hundreds of errors.
   DON'T fix them all. Instead:
   - Fix only the files you can handle in ~45 min
   - Create a .flake8 exclude list for files you didn't touch
   - The goal is to get CI green, not to fix everything
4. Add a GitHub Actions workflow that runs flake8 on PRs
5. Add eslint check for the frontend (it already has eslint.config.js)

LLM usage: Ask the LLM to explain what each flake8 error code means
   if you encounter one you don't recognize. Don't ask it to fix the code.
```

#### Issues #18, #19, #20: Add Docstrings and Type Hints (2-3 students, mix of J and S)

Split by module. Each student takes one area:

| Student | Module | Files | Issue |
|---------|--------|-------|-------|
| J student | ABM files | `household.py`, `store.py`, `geo_model.py` | #18 |
| J student | API files | `routes.py`, `helpers.py`, `api_server.py` | #19 |
| S student | Preprocessing | `get_data.py`, `household_constants.py` | #20 |

[SCAFFOLD: Type Hints Guide]
```
For each function in your assigned files:
1. Read the function. Understand what it takes and returns.
2. Add parameter type hints and return type hints.
3. For complex types, use modern Python syntax:
   - list[dict] not List[Dict]
   - str | None not Optional[str]
   - Use TypedDict for dict structures with known keys
4. Add a one-line docstring if the function name isn't self-explanatory.
   Skip docstrings for obvious functions like getters.

Example before:
   def has_resources(self):
       if self.income < 10000:
           return False

Example after:
   def has_resources(self) -> bool:
       if self.income < 10000:
           return False

LLM usage: You can ask the LLM "What type does this function return?"
   if it's unclear from the code. Verify its answer by reading the callers.
   Do NOT ask the LLM to add all the type hints for you.
```

#### First tests: `household.py` pure functions (1 S student)

[SCAFFOLD: Testing Guide]
```
1. Set up pytest:
   - Add pytest and pytest-asyncio to pyproject.toml dev dependencies
   - Create tests/ directory with __init__.py and conftest.py
2. Write tests for these pure functions in household.py:

   has_resources() (line 169):
   - Test: income < 10000 returns False regardless of household size
   - Test: household_size >= 2 and income < 15000 returns False
   - Test: household_size >= 3 and income < 25000 returns False
   - Test: income = 25001, household_size = 3 returns True
   - Edge: exact boundary values (10000, 15000, 25000)

   get_monthly_trip_count() (line 178):
   - Test all 3 paths: resources+vehicles=7, resources+no_vehicles=8, no_resources=6

   get_color() (line 57):
   - Test: mfai=40 should produce pure red
   - Test: mfai=70 should produce green-ish
   - Test: mfai=100 should produce green
   - Test: boundary at normalized=0.5

3. Run tests: uv run pytest tests/ -v
4. Run mutation testing: uv run mutmut run --paths-to-mutate=food_access_model/abm/household.py

LLM usage: After writing your tests, ask the LLM:
   "I wrote tests for a function that classifies household resource
   access based on income and household size thresholds.
   What edge cases might I be missing?"
   Then add any good suggestions as additional test cases.
```

### Deliverable
Each student opens a PR for their assigned work. PRs are reviewed by a peer (not the author) in Week 3.

### Solo Work (later in the week)

**Apply the pattern you just learned to new territory.**

You now know how to add type hints, write tests, or set up linting. Apply that same skill to parts of the codebase beyond your assigned files.

| If your assigned work was... | Your solo hunting ground is... |
|------------------------------|-------------------------------|
| Type hints (#18 ABM files) | Add type hints to `repository/db_repository.py`, `model_multi_processing/batch_running.py` |
| Type hints (#19 API files) | Add type hints to `api/helpers.py`, clean up the duplicate entry points (`api_server.py`, `server.py`) |
| Type hints (#20 preprocessing) | Add type hints to root-level `constants.py`, `parallel_scheduler.py`, `insert_stores.py` |
| Linting (#24) | Fix flake8 warnings in files you excluded in your first pass |
| Tests (household.py) | Write tests for `Store` class, `convert_centroid_to_polygon` in `api/helpers.py` |

**File issues for anything you can't fix in this session** but that you notice along the way. Keep building the backlog.

**LLM usage**: Same rules as the group session. You can ask the LLM to explain unfamiliar code or brainstorm edge cases for tests, but write the code yourself.

### Roadmap Activity
At the start of week 3's group session, spend 10 minutes as a team:
- Review the project board. Are the priorities still right?
- Did anyone's solo work surface issues that change the priorities?
- Assign week 3's issues based on what each student has learned so far.

---

## Week 3: Bug Fixes and Code Quality

### Group Session (30 min)
**Topic: "Specs before code, and adversarial review"**

Demo: Show the adversarial review workflow. Take a recent PR and run it through Claude Code in a fresh session with the skeptical reviewer prompt. Show how to evaluate valid vs. false positive criticisms.

Introduce the concept: Every PR from here on gets (1) human peer review and (2) LLM adversarial review by a different student.

### Assigned Work

#### Issue #47: Check 'Stores within 1 Mile' logic (1 student, S)

This is a reported bug: after running a simulation step, all houses appear to have the same number of stores within 1 mile.

[SCAFFOLD: Bug Investigation Guide]
```
1. UNDERSTAND before you fix. Read food_access_model/abm/household.py:131
   (stores_with_1_miles).
   - It iterates self.model.stores_list
   - It reads self.distances_map[store.unique_id]
   - It counts stores where distance <= 1.0

2. Hypothesis: When is distances_map populated?
   - Look at calculate_distances() (line 246)
   - It's called in step() (line 259) only if distances_map is None
   - After step 0, distances_map is never recalculated even if stores change

3. Write a test that reproduces the bug BEFORE fixing it:
   - Create a Household with a known distances_map
   - Call stores_with_1_miles()
   - Verify the count matches expected

4. Now investigate: Does distances_map need to be recalculated
   when stores are added or removed between steps?

5. Write the fix. The test should now pass.

LLM usage: Describe the bug and your hypothesis to the LLM.
   Ask "What else could cause all households to report the
   same store count?" See if it suggests causes you missed.
```

#### Issue #74: Optimize step function (1 student, S)

The step function iterates all stores multiple times per household: once in `calculate_distances()`, once in `get_closest_cspm()`, once in `get_closest_spm()`, once in `stores_with_1_miles()`.

[SCAFFOLD: Optimization Guide]
```
1. Read household.py step() and all the functions it calls.
   Count: how many times does each household iterate over all stores?
   Answer: at least 4 times (calculate_distances, get_closest_cspm,
   get_closest_spm, stores_with_1_miles).

2. Write a SPEC (put it in the issue comment) before coding:
   "I propose consolidating into a single pass that computes:
   - distances_map (all store distances)
   - closest_spm and closest_cspm (by filtering distances_map)
   - stores_within_1_mile count (from distances_map)
   This reduces O(4*S) to O(S) per household where S = store count."

3. Write tests for the CURRENT behavior first (so you can verify
   your refactor doesn't change results).

4. Implement the optimization.

5. Verify tests still pass with identical results.

LLM usage: After writing your spec, ask the LLM to interview you:
   "I want to optimize a function that iterates stores 4 times per
   household. Ask me questions about my approach."
   The LLM should push back on edge cases you might miss.
```

#### Issue #27: Clean up redundant functions (1 student, J+S pair)

[SCAFFOLD: Redundancy Audit]
```
1. Map out every function that accesses households or stores:
   - repository/db_repository.py: get_households(), get_food_stores()
     (sync psycopg2 singleton, initialized via async initialize())
   - abm/geo_model.py: reads from model parameters passed at construction
   - api/routes.py: direct asyncpg queries using the global connection pool

2. For each, document: What does it return? Who calls it?
   Is it actually used? Also check the three entry points
   (api_server.py, server.py, food_access_model/main.py) for
   overlap.

3. Write an ADR: "Which data access pattern should we standardize on?"
   db_repository.py uses psycopg2 (sync) as a singleton.
   routes.py uses asyncpg (async) with a connection pool.
   Both query the same database. Which should we keep? Why?
   (Consider: FastAPI is async-native, so async is preferred.)

4. Remove the functions that are unused or redundant.
   Consolidate entry points if the team agrees.
   Make sure nothing breaks.

LLM usage: Ask the LLM to help you trace callers:
   "Where is get_households() from db_repository.py called?"
   Verify by grepping the codebase yourself.
```

#### Issue #50: Improve logging (1 student, J)

[SCAFFOLD: Logging Guide]
```
1. Read the current logging across the codebase. Note:
   - routes.py uses logging.info and logging.error
   - api_server.py and geo_model.py use print() with flush=True
   - server.py sets up its own custom logger with file + stream handlers
   - food_access_model/main.py has minimal logging setup
   - No consistent format across files, no shared logging config

2. Create a logging configuration:
   - Add LOG_LEVEL env var (default: INFO)
   - Use structured format: timestamp, level, module, message
   - Replace all print() statements with appropriate logging calls

3. Guidelines to follow:
   - logging.info: service start/stop, simulation step completed,
     instance created/deleted
   - logging.debug: query details, timing, intermediate values
   - logging.error: exceptions, failed operations
   - NEVER log: passwords, API keys, full SQL with user data

LLM usage: Ask the LLM "What are best practices for structured
   logging in a FastAPI application?" Use the answer as a reference,
   but implement it yourself.
```

### Review Protocol (starts this week)
For each PR:
1. Author writes PR with summary, test plan, tradeoffs
2. One peer does human review
3. A different student runs adversarial LLM review in a fresh session and posts findings as PR comments, marking each as "Valid" or "False positive (because...)"

### Solo Work (later in the week)

**Pick an issue from the backlog and work it yourself.**

By now the team has a mix of pre-existing issues and student-filed issues from weeks 1-2. This is the first week students choose their own work.

[SCAFFOLD: Self-Directed Work Guide]
```
1. Go to the GitHub project board.
2. Pick an issue that:
   - Is labeled "should-fix" or "nice-to-have"
   - Matches your comfort level
   - Isn't already claimed by someone else
3. Comment on the issue: "I'm picking this up."
4. Before coding, write a one-paragraph plan in the issue comment:
   what you'll change, what files you'll touch, how you'll test it.
5. Implement it. Open a PR.

If you finish early, pick another one or extend your work.
If you get stuck, file a comment describing where you're stuck
and move on. Someone else (or you next week) can pick it up.

Good candidates for solo work this week:
- Any remaining flake8 fixes from #24
- print() -> logging conversions (related to #50)
- Documenting magic numbers in household.py
- Small issues you filed in week 1
```

**LLM usage unlock**: You can now use the LLM to help you write a spec for your chosen issue (use the "interview first" pattern from the group session). You can also use it for adversarial review of your own PR in a fresh session before requesting peer review.

### Roadmap Activity
Before the week 4 session, each student comments on 1-2 issues they think should be prioritized for weeks 4-5, with a sentence explaining why. The group reviews these nominations at the top of the week 4 session and adjusts assignments.

---

## Week 4: Core Algorithm and Data Improvements

### Group Session (30 min)
**Topic: "ADRs: Documenting decisions you're about to make"**

Demo: Walk through writing an ADR for issue #91 (multiple stores for scoring). Show the MADR template. Emphasize that the ADR is reviewed *before* implementation begins.

### Assigned Work

#### Issue #91: Calculate food access scores using multiple stores (1-2 students, S)

This is the highest-impact algorithmic change in the backlog.

[SCAFFOLD: Algorithm Change Guide]
```
1. READ THE PAPER FIRST. Understand the MFAI methodology from
   Koh et al. 2019. The current implementation in
   food_access_model/abm/household.py:218 (get_mfai) only considers
   the single closest SPM and CSPM. Note: the bc_pantries branch
   extends this with pantry support for low-income households.

2. Write an ADR answering:
   - How many stores should we consider? Top 3? All within X miles?
   - How do we weight distance? Linear decay? Inverse square?
   - What does the paper say vs. what makes practical sense?
   - Performance impact: if we consider all stores, what's the
     complexity change for 50k households x 200 stores?

3. Get the ADR reviewed (post as a PR or issue comment) BEFORE coding.

4. Write tests for the CURRENT get_mfai() behavior first.

5. Implement the new algorithm. Tests for new behavior should be
   written alongside (not after).

6. Compare results: run both old and new on the same data.
   Document the difference in scores.

LLM usage: Use the LLM to discuss algorithm tradeoffs:
   "The current MFAI considers only the closest store. I'm considering
   [your approach]. What are the tradeoffs?" This is a legitimate
   design discussion where the LLM adds value.
```

#### Issue #67: Refactor spatial data handling (1 student, S)

[SCAFFOLD: Spatial Refactor Guide]
```
1. Understand the current flow:
   - Household data stored as EPSG:4326 (lat/lon WKT in centroid_wkt)
   - Store data stored as EPSG:3857 (polygon WKT in geometry column)
   - This CRS inconsistency means different coordinate handling per table
   - Backend (api/helpers.py:29) generates polygons when adding stores:
     hexagons (50m radius) for supermarkets, triangles (25m) for convenience
   - Frontend (MapComponent.js) uses proj4 to reproject store coords
   - The bc_pantries branch takes a different approach: stores take
     lat/lon and convert internally, households reproject internally

2. The issue says: store and deliver all data in 4326. Only use 3857
   for internal distance calculations. Stop generating polygons
   (frontend uses marker icons, not polygon shapes).

3. This touches multiple files. Plan the changes before coding:
   - preprocessing/get_data.py: stop polygon generation at data load time
   - api/helpers.py: stop polygon generation when adding stores via API
   - abm/store.py, abm/household.py: keep internal 3857 for distance math
   - api/routes.py: return 4326 coordinates in query results
   - Frontend MapComponent.js: remove proj4 reprojection
   - insert_stores.py: update to match new storage format

4. This is a cross-cutting change. Open it as a draft PR early
   and coordinate with whoever is working on frontend.

LLM usage: Ask the LLM to explain the difference between EPSG:4326
   and EPSG:3857, and when you'd use each. This is the kind of
   domain knowledge question where LLMs are genuinely helpful.
```

#### Issue #94: Reporting API + Issue #79: Show metrics + Frontend #36: Reporting View (2-3 students, J+S pair)

These issues are related: the backend needs a reporting API (#94), the backend needs to serve richer metrics (#79), and the frontend needs a view to display them (frontend #36).

[SCAFFOLD: Feature Development Guide]
```
Backend student (S or J/S):
1. Write a spec: What metrics should the reporting API return?
   Look at what get_household_stats already returns (routes.py:463).
   What's missing? Suggestions:
   - Score distribution (histogram buckets)
   - Scores by income bracket
   - Scores by vehicle ownership
   - Change between simulation steps
2. Design the API endpoint(s). Write the route signature and
   response model (Pydantic) before implementing the query.
3. Write tests for the new endpoint.
4. Implement.

Frontend student (J):
1. Wait for the API spec from the backend student.
2. Design a simple metrics panel (can be a sidebar or modal).
   The frontend already has a DataComponent.jsx that shows basic
   stats (household count, store counts, avg income/vehicles).
   You can extend it or build a new component.
3. Fetch from the new API endpoint via the Axios client in
   src/shared/client.js.
4. Display using basic charts or formatted tables.
   (Don't add a charting library unless needed. The app already
   mixes Bootstrap and Tailwind, so pick one and be consistent.)

LLM usage: Both students can use the LLM to brainstorm what
   metrics would be useful. The backend student can ask for help
   designing the SQL aggregation queries. The frontend student
   can ask for help with React component structure.
   Both must understand and be able to explain their code.
```

### Solo Work (later in the week)

**Continue self-directed work, but now with design authority.**

By week 4, students should be proposing issues, not just picking from the existing list. The assignment this week:

1. **File at least 1 new issue** based on something you discovered while working on your assigned task. These can be bugs, enhancements, or refactoring opportunities.
2. **Pick and work 1 issue from the backlog** (student-filed or original). Follow the full cycle: claim it, write a plan, implement, test, PR.

**For S students**: If you see a pattern (e.g., "there are 5 places where store type classification is hardcoded"), file a single issue that captures the systemic problem, not 5 individual ones. Propose a solution in the issue body. This is how you move from "contributor" to "maintainer."

**For J students**: Pair up with an S student on their assigned work if your solo issue feels too big. Or pick a small issue: a documentation gap, a missing type hint in a file nobody's touched yet, a test for an untested function.

**LLM usage**: Full design discussion. You can use the LLM to brainstorm solutions, discuss tradeoffs, and generate small code blocks against a spec you wrote. You must still explain every line in your PR.

### Roadmap Activity
At the week 5 session, spend 15 minutes on roadmap planning:
- What's realistic to finish in weeks 5-6?
- What should be documented and deferred?
- Each student commits to one thing they'll ship before the end.

---

## Week 5: Integration and Polish

### Group Session (30 min)
**Topic: "Security review and deployment readiness"**

Demo: Run Claude Code's adversarial security review on the current codebase. Show the real issues it finds (raw SQL patterns, hardcoded CORS, no input validation, global mutable state). Discuss which are real risks vs. theoretical.

### Assigned Work

#### Security hardening (1 student, any level)

[SCAFFOLD: Security Checklist]
```
Run through this checklist. Fix what you can; file issues for the rest.

[ ] Input validation: Add Pydantic models for all POST/DELETE endpoints
    that accept user input (routes.py:191, 308, 352)
[ ] CORS: Consolidate entry points and make CORS origins configurable
    via env var. Currently food_access_model/main.py hardcodes two
    origins; api_server.py hardcodes a different one.
[ ] SQL: Audit all raw SQL for injection risks. Both routes.py (asyncpg)
    and db_repository.py (psycopg2) execute queries. Check for
    string concatenation in query construction.
[ ] Rate limiting: The advance endpoint (routes.py:155) triggers
    expensive multiprocessing computation. Should it have rate limiting?
    What happens if two advance requests run concurrently?
[ ] Env vars: Verify .env.example is complete and .env is in .gitignore
[ ] Auth: There is currently zero authentication on any endpoint.
    Document whether this is acceptable for the deployment context.

Use the LLM adversarial review to scan for issues you missed:
   "Review this file for OWASP Top 10 security risks. Be thorough."
   Then evaluate each finding yourself.
```

#### Remaining issues and PR cleanup (all students)

- Merge all open PRs from weeks 2-4
- Resolve any review feedback
- Fix CI if anything is broken
- Clean up stale branches (the repo has 30+)

#### Issue #63: Unit conversion consistency (1 student, J or S)

```
Audit all distance calculations in the codebase.
- household.py: calculate_distances() (line 246) computes distances
  using self.model.space.distance() which returns meters (EPSG:3857)
- household.py: stores_with_1_miles() (line 131) compares to 1.0 (miles)
- household.py: get_closest_cspm/spm return distances in... what unit?
  Are they consistently miles or meters?
- constants.py: SEARCHRADIUS = 500 (in what unit? meters? miles?)
- household_constants.py: center point and radius (15km) for county bounds
- api/helpers.py: polygon generation uses meters (50m, 25m, 20m)
- The bc_pantries branch uses direct Euclidean distance from centroid
  coordinates instead of Mesa's GeoSpace.distance()

Document every conversion and verify consistency.
Write tests that assert expected distances for known coordinates.
Pay special attention to the CRS inconsistency: households are 4326
(degrees), stores are 3857 (meters). Distance math on mixed CRS
will produce garbage.
```

### Solo Work (later in the week)

**Full autonomy. Pick what matters most and ship it.**

By week 5, students have the full toolkit: reading code, writing specs, testing, adversarial review, issue filing. Solo work is now indistinguishable from "being a developer on this project."

Each student should:
1. Look at the project board. What's the highest-impact thing you can finish this week?
2. If nothing on the board excites you, scan the codebase for something that bugs you and file+fix it.
3. Ship a PR with the full protocol (spec, tests, adversarial self-review in a fresh session).

**Some high-value targets if students need direction:**
- Write tests for API endpoints (routes.py) using FastAPI TestClient
- Add missing validation to POST endpoints
- Improve error messages for common failure modes
- Frontend: add loading states, error handling for API failures,
  replace window-object state with proper React state management
- Frontend #10: Move the API base URL from hardcoded client.js to
  an environment variable (VITE_API_URL)
- Frontend #36: Build the reporting/metrics view
- Start a benchmarking script for #51 (simulation runtime) as a handoff artifact
- Consolidate the three backend entry points into one

### Roadmap Activity
Final prioritization before week 6. Each student reviews the full issue list and tags 2-3 issues as "recommended for next cohort" with a sentence about why and what context the next team would need.

---

## Week 6: Retrospective and Handoff

### Group Session (60 min)
**Topic: Retrospective + demo + knowledge transfer**

1. **Demo** (20 min): Each student demos one thing they shipped.
2. **Retro** (20 min): What worked? What didn't? Specifically:
   - Which LLM usage patterns were most helpful?
   - Where did LLM tools lead you astray?
   - What would you tell the next cohort?
3. **Handoff** (20 min): Finalize the roadmap for the next cohort.

### Assigned Work

#### Everyone: Update documentation
- Each student updates the README section for the area they worked on
- Ensure all new environment variables are in `.env.example`

#### Roadmap handoff document

This is the team's final output beyond the code itself. Write a `docs/ROADMAP.md` that includes:

1. **What we shipped** (with PR links): A summary of every merged improvement.
2. **What we started but didn't finish** (with issue links and status): Draft PRs, partial implementations, open questions.
3. **What the next cohort should tackle**, organized by priority:

| Priority | Issue | Context the Next Team Needs |
|----------|-------|---------------------------|
| High | #42: New location initialization | Census API integration, parameterize preprocessing for arbitrary counties. Currently hardcoded to Brown County (FIPS 55009). |
| High | #44: Schema migration (start_step/end_step) | Touches every query in routes.py. Need migration script + #45 query updates. |
| High | #67: Spatial data handling refactor | CRS inconsistency (households 4326, stores 3857) causes confusion. bc_pantries branch has a partial approach. |
| Medium | #43: Census block aggregation layer | Requires PostGIS, frontend map layer. Depends on #67 finishing. |
| Medium | #51: Simulation runtime improvements | Architecture-level. Benchmarking suite needed first. Multiprocessing helps but may not scale to very large counties. |
| Medium | #91: Multi-store MFAI scoring | Algorithmic change. Current impl uses only closest SPM + closest CSPM. Paper suggests considering multiple. ADR needed. |
| (add rows) | (student-filed issues) | (context from the students who filed them) |

4. **What we learned about LLM-assisted development**: 3-5 bullet points of advice for the next cohort, written by the students.

### Solo Work (week 6)

**Final push.** Ship anything that's close to done. Close or reassign anything that isn't. Leave the codebase cleaner than you found it.

---

## Issue-to-Week Mapping Summary

| Week | Assigned Issues (group session) | Solo Work Focus | LLM Pattern | Roadmap Activity |
|------|-------------------------------|----------------|-------------|-----------------|
| 1 | (orientation, codebase traces) | File issues for everything found | LLM as explainer | Seed the backlog |
| 2 | #24, #18, #19, #20 + first tests | Apply same skill to adjacent files | LLM for edge case brainstorming | Triage + prioritize backlog |
| 3 | #47, #74, #27, #50 | Pick an issue from backlog, work it | LLM for spec review + adversarial review | Nominate priorities for weeks 4-5 |
| 4 | #91, #67, #94/#36 (reporting), #79 | File new issues + pick from backlog | LLM as design discussion partner | Roadmap check: what's realistic? |
| 5 | #63 + security + frontend #10 + integration | Full autonomy: ship highest-impact work | LLM for adversarial security scanning | Tag issues for next cohort |
| 6 | Documentation + roadmap handoff | Final push: close or reassign everything | Reflection on LLM usage patterns | Write ROADMAP.md for next cohort |

Note: Issue numbers above are from the `ICICLE-ai/Food-Access-Model` repo unless prefixed with "frontend" (from `ICICLE-ai/FASS-Frontend`).

## Student Assignment Strategy

With 5 students of varying experience, assign based on challenge level:

| Role | Experience | Weeks 2-3 Focus | Weeks 4-5 Focus |
|------|-----------|-----------------|-----------------|
| Student A (J) | Freshman/sophomore | #18 (type hints, ABM) | Frontend #36 (reporting view, paired with C) |
| Student B (J) | Freshman/sophomore | #24 (linting + CI) | #63 (unit conversions) + security checklist + frontend #10 (env var) |
| Student C (J/S) | Mid-level | #19 (type hints, API) + #50 (logging) | #94 (reporting API, paired with A) + #79 (backend metrics) |
| Student D (S) | Junior/senior | First tests + #47 (bug fix) | #91 (MFAI algorithm improvement) |
| Student E (S) | Junior/senior | #20 (preprocessing) + #27 (redundancy) | #67 (spatial refactor) + #74 (optimization) |

Pair J and S students on cross-cutting work (e.g., #94 backend + #79 frontend).

---

## LLM Usage Progression

| Week | Allowed | Not Yet |
|------|---------|---------|
| 1 | Ask for explanations of existing code | Code generation |
| 2 | Edge case brainstorming, type hint questions, "what does this error mean" | Writing functions, writing tests |
| 3 | Spec review ("interview me about my approach"), adversarial PR review | "Fix this bug for me" |
| 4 | Design discussion ("what are the tradeoffs of X vs Y"), small code generation with spec | Generating without a spec |
| 5-6 | Full workflow, adversarial security review | n/a, full access earned |

The progression matters because students need to build the muscle of *thinking first* before they get the power of *generating*. A freshman who learns to generate code in week 1 will never learn to read code. A senior who is forced to read code in week 1 will use generation more effectively later.

---

## Coordination Mechanics

**Weekly rhythm:**
- **Group session** (~2 hours): Lesson (30 min) + roadmap check (10 min) + guided work (remaining time)
- **Solo work** (async, later in the week): Self-directed work applying that week's patterns
- **Friday**: PRs due for review (both assigned and solo work)
- **Before next session**: Reviews completed so PRs can merge

**Issue discipline:**
- Every problem, question, or improvement idea gets a GitHub issue. No exceptions.
- Issues must have: clear title, description of the problem, affected files, and (when applicable) a proposed approach
- Students claim issues by commenting before starting work
- Stale claims (no PR within a week) get unclaimed so others can pick them up

**PR rules:**
- Max ~200 lines of changed code (non-test). Smaller is better.
- Must include: summary, what was tested, one tradeoff considered
- Must link to the issue it addresses
- Must be reviewed by one peer + one adversarial LLM review (starting week 3)

**Communication:**
- GitHub Issues for technical discussion (keeps it with the code)
- Short standup at start of each group session: "What I shipped, what's blocking me, what I filed"

**Branch strategy:**
- `main` is stable (deployed)
- `dev` is integration
- Feature branches off `dev`, named `feature/issue-NUMBER-short-desc`
- PRs merge to `dev`; `dev` merges to `main` at end of week 6

---

## What Success Looks Like After 6 Weeks

**For the tool:**
- Linting and CI in place (#24)
- Type hints across the codebase (#18, #19, #20)
- First test suite (household pure functions + API endpoints)
- Bug fix for store counting (#47)
- Optimized step function (#74)
- Improved MFAI algorithm (#91)
- Reporting API + metrics display (backend #94, frontend #36, backend #79)
- Cleaner logging (#50)
- Security basics (input validation, configurable CORS, consolidated entry point)
- Spatial data handling improvements (#67)
- Cleaned up redundant code and entry points (#27)
- Frontend API URL moved to env var (frontend #10)

**For the students:**
- Can read and understand unfamiliar code without LLM help
- Know how to write specs and ADRs before implementing
- Can write meaningful tests (not just happy-path)
- Use LLM tools to accelerate work they understand, not replace understanding
- Have shipped real features through a real PR workflow
- Can do adversarial code review (with and without LLM assistance)
- Have filed, triaged, and prioritized real issues on a real project
- Can self-direct: identify what needs doing, scope it, and ship it
- Have a portfolio-worthy open source contribution
- Left a roadmap that makes the next cohort's onboarding faster

---

## Appendix A: Scaffolded Guide Template

Each guide follows this structure:

```
## [Issue Title] (#NUMBER)

### Context
What the issue is about and why it matters. 2-3 sentences.

### Before You Start
- [ ] Read these files: [list]
- [ ] Understand: [specific concept]
- [ ] Branch: feature/issue-NUMBER-short-desc

### Steps
1. First step (with expected output)
2. Second step
   - Sub-detail if needed
3. ...

### LLM Usage
What you CAN ask the LLM for this task.
What you should NOT ask the LLM for this task.

### Definition of Done
- [ ] Tests pass
- [ ] Flake8 clean
- [ ] PR opened with summary and test plan
- [ ] Peer review requested

### While You're In There
Things to look for while working in these files that could
become new issues (file them!):
- Missing type hints on adjacent functions
- Hardcoded values that should be constants
- Dead code or unused imports
- Missing error handling
- Anything that confused you (if it confused you, it'll confuse
  the next person -- file an issue to improve it)

### Stretch Goals (if you finish early)
Optional harder extensions of the same work.
```

Guides live in `docs/guides/` in the repo so future cohorts can reuse and improve them.

## Appendix B: The Solo Work Progression

The solo work sections are designed to ramp from "apply what you just learned" to "find and drive your own work":

| Week | Solo Work Mode | Decision Authority | Issue Creation |
|------|---------------|-------------------|----------------|
| 1 | **Observe + report**: File issues for everything found during traces | None (reporting only) | Required: 3+ issues per student |
| 2 | **Repeat the pattern**: Apply the same skill (type hints, tests, linting) to new files | Choose which files to work on | Encouraged: file anything you notice |
| 3 | **Pick from backlog**: Choose an issue, write a plan, implement it | Choose what to work on; plan must be posted before coding | Expected: file issues found during bug investigation |
| 4 | **Propose + execute**: File new issues based on what you discover, then work them | Full: choose what to build, write the spec | Required: 1+ new issue filed |
| 5 | **Full autonomy**: Ship the highest-impact thing you can identify | Full: prioritize, scope, implement, review | Expected: tag issues for next cohort |
| 6 | **Final push + handoff**: Close everything you can, document everything you can't | Full | Required: contribute to ROADMAP.md |

The transition from "assigned work with scaffolding" to "self-directed work with full autonomy" should feel gradual. If a student is struggling with solo work in weeks 3-4, pair them with someone more experienced. If a student is racing ahead, point them at the harder backlog issues (#42, #44, #51) and let them scope an approach even if implementation happens next cohort.
