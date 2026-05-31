---
layout: default
title: "Frontend Onboarding Guide"
---

# Farm2Facts Frontend Onboarding Guide

This guide covers what the frontend is, how to clone it, and how to run it locally.

---

## About this Repo

A Vue 3 data collection and reporting platform for farmers markets. Producers, market organizations, and researchers each see a different interface based on their role. It handles data entry, CSV uploads, analysis, and report generation across a set of instruments (vendor applications, attendance, sales slips, visitor surveys, and others).

**Key technologies:**
- Vue 3 (Options API) + Vue Router 4 + Pinia 2
- Axios (HTTP requests to the backend)
- MDB Vue UI Kit -- Material Design Bootstrap, registered globally in `main.js`
- Chart.js 4 (graphs and analysis views)
- LESS (scoped per-component styles)

**Key architecture notes:**
- Single Pinia store (`useUserInfoStore` in `src/stores/userInfo.js`) persisted to `localStorage` -- holds auth token, role, and session state
- Role-based routing: the `beforeEach` guard redirects to different landing pages based on `orgType` (Individual Producer, Market Organization, Researcher)
- Three-file view pattern: each view has a `.vue` template, a `_ViewName.js` logic file, and a `_ViewName.less` style file co-located in its own folder
- API base URL configured via `VUE_APP_API_DOMAIN` in `.env`

---

## Cloning the Repository

Inside the repository page:

- Click the **Code** button.
- Choose either **SSH** or **HTTPS**.

Git supports two authentication methods:

- **SSH** (Recommended for long-term development)
- **HTTPS** (Best for restricted networks or quick setup)

Both methods use Git. The difference is how authentication is handled.

### Why Both SSH and HTTPS Exist

Git supports multiple authentication methods because:

- Developers work across different networks (home, campus, corporate).
- Some networks block SSH (port 22).
- Some environments require token-based authentication.

| Method | Authentication | Best For |
| --- | --- | --- |
| SSH | Public/Private Key | Long-term development |
| HTTPS | Personal Access Token (PAT) | Restricted networks |

---

### Option 1: Cloning Using SSH (Recommended)

SSH authenticates your machine using a public/private key pair.

**Why Use SSH?**
- No repeated credential prompts
- More secure long-term
- Ideal for active contributors

**Requirements**
- Generate an SSH key
- Add the public key to your GitLab profile

#### Step 1: Generate an SSH Key (if needed)

From your terminal:

```bash
ssh-keygen -t ed25519 -C "your_wisc_email@wisc.edu"
```

Press Enter to accept the default location.

#### Step 2: Add the Key to GitLab

Copy your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Then:
1. Go to [https://git.doit.wisc.edu](https://git.doit.wisc.edu)
2. Profile -- Preferences -- SSH Keys
3. Paste the key
4. Add a descriptive title (e.g., `Home Desktop 2026`)

#### Step 3: Clone the Repository

Navigate to your desired project directory:

```bash
git clone git@git.doit.wisc.edu:at-trad/farm2facts-frontend.git
```

If configured correctly, no password will be required.

**If SSH Fails**

If you see:

```
ssh: connect to host git.doit.wisc.edu port 22: Operation timed out
```

Your network likely blocks port 22. Use HTTPS instead.

---

### Option 2: Cloning Using HTTPS

HTTPS uses a Personal Access Token (PAT) instead of SSH keys.

**Why Use HTTPS?**
- Works when SSH is blocked
- No SSH key setup required
- Simpler for occasional contributors

**Requirements**
- UW GitLab account
- Personal Access Token (PAT)

#### Step 1: Create a PAT

1. Go to GitLab -- Profile -- Preferences -- Access Tokens
2. Create a new token with these settings:
   - **Name:** `Farm2Facts Frontend PAT`
   - **Scopes:** `read_repository`, `write_repository`
   - Set a reasonable expiration date
3. Copy the token immediately -- it will not be shown again.

#### Step 2: Clone via HTTPS

```bash
git clone https://git.doit.wisc.edu/at-trad/farm2facts-frontend.git
```

When prompted:
- **Username:** Your NetID
- **Password:** Paste your PAT (not your actual password)

---

### Which Method Should You Use?

Use **SSH** if:
- You are contributing long-term
- Port 22 is not blocked

Use **HTTPS** if:
- You are on a restrictive network
- SSH times out

---

## Running Locally

### Step 1: Install dependencies

```bash
npm install
```

### Step 2: Set up your `.env` file

Create a `.env` file at the root of the repo. Set these four variables to point at the backend you want to use:

| Variable | Purpose | Example |
| --- | --- | --- |
| `VUE_APP_API_DOMAIN` | Full API base URL | `http://localhost:3000/api/v1` |
| `VUE_APP_API_ROOT` | API root without path | `http://localhost:3000/` |
| `VUE_APP_BASE_URL` | Frontend origin | `http://localhost:8080` |
| `VUE_APP_BASE_PATH` | Route prefix | `` (empty for local) |

### Step 3: Start the dev server

```bash
npm run serve
```

This proxies `/api/v1` requests to `localhost:3000`. Open `http://localhost:8080` in your browser.

### Step 4: Verify it works

Log in with a test account. If the nav menu loads and you can reach a data entry form, the frontend is connected to the backend correctly.

---

## Other Commands

```bash
# Production build (output to dist/)
npm run build

# Lint
npm run lint
```

There is no test suite in this project.
