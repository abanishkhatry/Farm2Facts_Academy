---
layout: default
title: "Backend Onboarding Guide"
---

# Farm2Facts Backend Onboarding Guide

This guide covers what the backend is, how to clone it, and how to run it locally.

Pick your operating system below. Every step that differs between macOS and Windows will switch to match your choice, and your choice is remembered on the other guides too.

<div class="os-picker">
  <p class="os-picker-label">Your operating system</p>
  <div class="os-switch" role="group" aria-label="Choose your operating system">
    <button type="button" data-os="mac" aria-pressed="true">macOS</button>
    <button type="button" data-os="win" aria-pressed="false">Windows</button>
  </div>
</div>

---

## About this Repo

A Rails 6.1 metrics platform for farmers' markets and individual producers. It tracks sales, visitors, vendors, and ecosystem services. The backend exposes both a Grape REST API (consumed by the frontend) and a traditional Rails web interface.

**Key technologies:**
- Ruby on Rails 6.1
- MySQL
- Grape (REST API framework, mounted at `/`)
- DeviseTokenAuth (token-based API authentication)

**Key architecture notes:**
- **Dual routing:** A Grape REST API (`app/controllers/api/v1/`) handles all frontend requests. 300+ traditional Rails routes (`config/routes.rb`) handle the web interface.
- **Authentication:** Web routes use session-based auth (`session[:user_id]` via `ApplicationController`). API routes use DeviseTokenAuth token headers, mounted at `/auth`.
- **Metric engine:** `ApplicationController` contains a generic `calculate_metric()` method driven by `Metric` model config. Complex metrics use named formula methods (e.g., `metric2_formula` for total sales, `metric16_formula` for vendors per day).
- **Metric selections** are stored as two integers representing a 37-bit bitmask. Do not manipulate metric selections without understanding this encoding.

---

## Prerequisites

The backend needs Ruby, Bundler, and MySQL. This is the harder of the two repos to set up, so work through this section before cloning.

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

**1. Install the Command Line Tools and Homebrew** if you have not already. Both are covered in the [Frontend Guide prerequisites](FRONTEND_GUIDE#prerequisites).

**2. Install MySQL:**

```bash
brew install mysql
```

**3. Install a Ruby version manager.** Do not use the Ruby that ships with macOS -- it is old and system-owned. Use `rbenv`:

```bash
brew install rbenv ruby-build
rbenv init
```

Follow the line `rbenv init` prints to add it to your shell profile, then open a new Terminal window.

**4. Install the Ruby version this project expects.** Check the repo for a `.ruby-version` file or the `ruby` line at the top of the `Gemfile`, and install that exact version:

```bash
rbenv install <version-from-repo>
rbenv local <version-from-repo>
```

**5. Install Bundler:**

```bash
gem install bundler
```

**6. Verify:**

```bash
ruby --version
bundler --version
mysql --version
```

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

Rails is built around Unix tooling, and several gems this project depends on compile native extensions that assume a Unix environment. On Windows you have two paths. **Use WSL2** unless you have a specific reason not to.

#### Recommended: WSL2 (Windows Subsystem for Linux)

WSL2 runs a real Ubuntu system inside Windows. You get the same commands as your teammates on macOS and Linux, and the Rails setup behaves the way the documentation expects.

**1. Install WSL2.** Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

Restart when prompted. On first launch Ubuntu asks you to create a username and password. That password is for Ubuntu, not Windows, and you will need it for `sudo`.

**2. Open Ubuntu** from the Start menu. Every command from here on runs inside that Ubuntu terminal, not PowerShell.

**3. Update the package list and install the build tools, Git, and MySQL:**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl build-essential libssl-dev libreadline-dev \
  zlib1g-dev libmysqlclient-dev mysql-server
```

`libmysqlclient-dev` is required for the `mysql2` gem to compile. Installing it now saves you a confusing error later.

**4. Install `rbenv` and the Ruby version this project expects.** Check the repo for a `.ruby-version` file or the `ruby` line at the top of the `Gemfile`, and install that exact version:

```bash
curl -fsSL https://rbenv.org/install.sh | bash
```

Follow the shell configuration lines the installer prints, close the terminal, open a new one, then:

```bash
rbenv install <version-from-repo>
rbenv global <version-from-repo>
gem install bundler
```

**5. Install VS Code on Windows** and add the **WSL** extension. You can then run `code .` from inside the Ubuntu terminal and edit the code in a normal Windows window while it runs under Linux.

**6. Keep the repo inside the Linux file system.** Clone into your Ubuntu home directory (`~/dev/`, which is `\\wsl$\Ubuntu\home\<you>\dev` from File Explorer). Cloning into `/mnt/c/Users/...` works but is significantly slower, and file watching is unreliable there.

**7. Verify:**

```bash
ruby --version
bundler --version
mysql --version
```

#### Alternative: native Windows

Only take this path if WSL2 is unavailable to you, for example on a managed machine where you cannot enable virtualization.

**1. Install Ruby+Devkit** from <a href="https://rubyinstaller.org/downloads/" target="_blank" rel="noopener noreferrer">rubyinstaller.org</a>. Pick the **Ruby+Devkit** package matching the version in the repo's `.ruby-version` or `Gemfile`. At the end of the installer, let it run `ridk install` and choose option **3** (MSYS2 and MINGW development toolchain). Without the Devkit, the `mysql2` gem cannot build.

**2. Install MySQL Community Server** from <a href="https://dev.mysql.com/downloads/installer/" target="_blank" rel="noopener noreferrer">dev.mysql.com/downloads/installer</a>. During setup, choose to run MySQL as a **Windows Service** and note the root password you set.

**3. Point the `mysql2` gem at the MySQL libraries.** Native Windows cannot find them on its own:

```powershell
gem install mysql2 -- --with-mysql-dir="C:\Program Files\MySQL\MySQL Server 8.0"
```

Adjust the path if you installed a different version.

**4. Install Bundler:**

```powershell
gem install bundler
```

Expect more friction on this path than your teammates have. If you hit a wall on a gem that will not build, that is the signal to switch to WSL2.

</div>

---

## Cloning the Repository

Follow the same SSH or HTTPS steps described in the [Frontend Guide](FRONTEND_GUIDE#cloning-the-repository), substituting the backend repo URL:

**SSH:**
```bash
git clone git@git.doit.wisc.edu:at-trad/farmers-coalition.git
```

**HTTPS:**
```bash
git clone https://git.doit.wisc.edu/at-trad/farmers-coalition.git
```

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

If you are using WSL2, run the clone from the **Ubuntu** terminal and set up your SSH key there. WSL2 has its own home directory, so a key you generated in Git Bash on Windows does not exist inside Ubuntu.

</div>

---

## Running Locally

### Step 1: Start MySQL

MySQL must be running before you start the app.

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

```bash
brew services start mysql
```

To confirm it is up:

```bash
brew services list
```

**Database config note:** `config/database.yml` uses socket `/tmp/mysql.sock` (Homebrew MySQL). If you use MAMP, update the socket path to `/Applications/MAMP/tmp/mysql/mysql.sock`.

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

**On WSL2:**

```bash
sudo service mysql start
```

You have to run this after every reboot, since WSL2 does not start services automatically.

**On native Windows,** MySQL runs as a service and starts with the machine. To start or stop it manually, open PowerShell as Administrator:

```powershell
net start MySQL80
```

The service name depends on the version you installed. Check it under **Services** in the Start menu if `MySQL80` is not found.

**Database config note:** `config/database.yml` uses socket `/tmp/mysql.sock`, which is a macOS Homebrew path. You need to change it locally:

- **On WSL2,** Ubuntu's MySQL socket is at `/var/run/mysqld/mysqld.sock`. Update the socket line to match.
- **On native Windows,** Unix sockets do not exist at all. Remove the `socket:` line and connect over TCP instead:

```yaml
default: &default
  adapter: mysql2
  encoding: utf8
  host: 127.0.0.1
  port: 3306
  username: root
  password: <your-mysql-root-password>
```

Do not commit your local `database.yml` changes. If Git tracks the file, keep your edits out of your commits so you do not break everyone else's setup.

</div>

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

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

On WSL2, open that URL in your normal Windows browser. WSL2 forwards `localhost` to Windows, so the Rails server running inside Ubuntu is reachable at the same address.

</div>

---

## Known Issues

- `ApplicationController` contains SQL string concatenation in metric calculation loops. Treat changes there carefully to avoid injection vulnerabilities.
- The `market_entry_point_dates` table was never created via migrations. Always use `db:schema:load` for fresh local setup, not `db:migrate`.
- Geocoding (`Geocoder.search`) fires on every profile save when address fields change.

---

## Troubleshooting

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

| Problem | Fix |
| --- | --- |
| `Can't connect to local MySQL server through socket '/tmp/mysql.sock'` | MySQL is not running. Run `brew services start mysql`. If it is running, your socket path in `config/database.yml` does not match your MySQL install. |
| `mysql2` gem fails to build during `bundle install` | Run `brew install mysql` first, then `bundle install` again. |
| `rbenv: version not installed` | You are in a directory with a `.ruby-version` for a Ruby you have not installed. Run `rbenv install <version>`. |
| Port 3000 already in use | Find the process with `lsof -i :3000` and stop it, or run `bundle exec rails server -p 3001`. |

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

| Problem | Fix |
| --- | --- |
| `Can't connect to local MySQL server through socket '/tmp/mysql.sock'` | The socket path in `config/database.yml` is the macOS default. Change it to `/var/run/mysqld/mysqld.sock` on WSL2, or switch to `host`/`port` on native Windows. |
| `mysql2` gem fails to build (WSL2) | `libmysqlclient-dev` is missing. Run `sudo apt install libmysqlclient-dev`, then `bundle install` again. |
| `mysql2` gem fails to build (native Windows) | You are missing the MSYS2 toolchain or the MySQL library path. Run `ridk install` and choose option 3, then reinstall the gem with `--with-mysql-dev`. If it still fails, switch to WSL2. |
| MySQL connection refused after a reboot (WSL2) | The service does not auto-start. Run `sudo service mysql start`. |
| Rails starts but the browser cannot reach it (WSL2) | Bind to all interfaces: `bundle exec rails server -b 0.0.0.0`. |
| Everything is very slow, or file changes are not picked up (WSL2) | The repo is on `/mnt/c/`. Move it into your Ubuntu home directory (`~/dev/`). |
| Port 3000 already in use | On WSL2, `lsof -i :3000`. On native Windows, `Get-NetTCPConnection -LocalPort 3000` in PowerShell, then stop the process in Task Manager. |

</div>
