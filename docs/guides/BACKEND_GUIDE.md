---
layout: default
title: "Backend Onboarding Guide"
---

# Farm2Facts Backend Onboarding Guide

This guide covers what the backend is, how to clone it, and how to run it locally.

---

## About this Repo

A Rails 6.1 metrics platform for farmers' markets and individual producers. It tracks sales, visitors, vendors, and ecosystem services. The backend exposes both a Grape REST API (consumed by the frontend) and a traditional Rails web interface.

**Key technologies:**
- Ruby on Rails 6.1
- MySQL (Homebrew install recommended)
- Grape (REST API framework, mounted at `/`)
- DeviseTokenAuth (token-based API authentication)

**Key architecture notes:**
- **Dual routing:** A Grape REST API (`app/controllers/api/v1/`) handles all frontend requests. 300+ traditional Rails routes (`config/routes.rb`) handle the web interface.
- **Authentication:** Web routes use session-based auth (`session[:user_id]` via `ApplicationController`). API routes use DeviseTokenAuth token headers, mounted at `/auth`.
- **Metric engine:** `ApplicationController` contains a generic `calculate_metric()` method driven by `Metric` model config. Complex metrics use named formula methods (e.g., `metric2_formula` for total sales, `metric16_formula` for vendors per day).
- **Metric selections** are stored as two integers representing a 37-bit bitmask. Do not manipulate metric selections without understanding this encoding.

---

## Cloning the Repository

Follow the same SSH or HTTPS steps described in the [Frontend Guide](FRONTEND_GUIDE.md#cloning-the-repository), substituting the backend repo URL:

**SSH:**
```bash
git clone git@git.doit.wisc.edu:at-trad/farmers-coalition.git
```

**HTTPS:**
```bash
git clone https://git.doit.wisc.edu/at-trad/farmers-coalition.git
```

---

## Running Locally

### Step 1: Start MySQL

MySQL must be running before you start the app. With Homebrew:

```bash
brew services start mysql
```

**Database config note:** `config/database.yml` uses socket `/tmp/mysql.sock` (Homebrew MySQL). If you use MAMP, update the socket path to `/Applications/MAMP/tmp/mysql/mysql.sock`.

### Step 2: Install dependencies

```bash
bundle install
```

### Step 3: Set up the database

For a fresh local setup, use `db:schema:load` -- do not use `db:migrate` for a fresh setup, as some migrations have ordering bugs:

```bash
bundle exec rails db:create db:schema:load
```

When adding new migrations on top of an existing database:

```bash
bundle exec rails db:migrate
```

### Step 4: Start the server

```bash
bundle exec rails server
```

### Step 5: Verify it works

Open `http://localhost:3000` in your browser. The Rails app should load.

---

## Known Issues

- `ApplicationController` contains SQL string concatenation in metric calculation loops. Treat changes there carefully to avoid injection vulnerabilities.
- The `market_entry_point_dates` table was never created via migrations. Always use `db:schema:load` for fresh local setup, not `db:migrate`.
- Geocoding (`Geocoder.search`) fires on every profile save when address fields change.
