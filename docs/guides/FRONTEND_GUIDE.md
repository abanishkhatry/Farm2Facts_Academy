---
layout: default
title: "Frontend Onboarding Guide"
---

# Farm2Facts Frontend Onboarding Guide

This guide covers what the frontend is, how to clone it, and how to run it locally.

Pick your operating system below. Every step that differs between macOS and Windows will switch to match your choice, and your choice is remembered on the other guides too.

<div class="os-picker">
  <p class="os-picker-label">Your operating system</p>
  <div class="os-switch" role="group" aria-label="Choose your operating system">
    <button type="button" data-os="mac" aria-pressed="true">macOS</button>
    <button type="button" data-os="win" aria-pressed="false">Windows</button>
  </div>
</div>

<details id="about-this-repo" class="section-card" markdown="1">
<summary>About this Repo</summary>

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

</details>

<details id="prerequisites" class="section-card" markdown="1">
<summary>Prerequisites</summary>

You need Git and Node.js installed before anything else. Install them once, then verify.

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

**1. Install the Xcode Command Line Tools.** This gives you `git` and the compilers some npm packages need:

```bash
xcode-select --install
```

**2. Install Homebrew** if you do not already have it. Homebrew is the package manager we use to install everything else:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the "Next steps" it prints at the end -- on Apple Silicon Macs you have to add Homebrew to your `PATH` yourself.

**3. Install Node.js:**

```bash
brew install node
```

**4. Verify.** Run each of these in Terminal:

```bash
git --version
node --version
npm --version
```

All three should print a version number. Use the built-in **Terminal** app (or iTerm) for every command in this guide.

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

**1. Install Git for Windows** from <a href="https://git-scm.com/download/win" target="_blank" rel="noopener noreferrer">git-scm.com/download/win</a>. Accept the defaults. This also installs **Git Bash**, a terminal that understands the same commands as macOS and Linux.

**2. Install Node.js LTS** from <a href="https://nodejs.org" target="_blank" rel="noopener noreferrer">nodejs.org</a>. Choose the **LTS** installer, not Current. When the installer offers to install "Tools for Native Modules", check the box -- some npm packages compile native code.

**3. Restart your terminal** after both installers finish. New programs are not on your `PATH` until you open a fresh window.

**4. Verify.** Open **Git Bash** from the Start menu and run:

```bash
git --version
node --version
npm --version
```

All three should print a version number.

**Which terminal should you use?** Use **Git Bash** for everything in this guide. PowerShell and Command Prompt work for most commands, but they use different syntax for paths, environment variables, and file creation. Git Bash matches what this guide shows, so you can copy commands as written.

**One Windows-specific setting.** Git on Windows rewrites line endings by default, which can show up as every line in a file being changed. Set this once, before you clone:

```bash
git config --global core.autocrlf input
```

</div>

</details>

<details id="cloning-the-repository" class="section-card" markdown="1">
<summary>Cloning the Repository</summary>

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

#### Step 2: Copy your public key

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

Print the key and copy it, or send it straight to your clipboard:

```bash
cat ~/.ssh/id_ed25519.pub

# or copy it directly
pbcopy < ~/.ssh/id_ed25519.pub
```

Your keys live in `~/.ssh/`. Copy the contents of the `.pub` file only. Never share `id_ed25519` (the file without `.pub`) -- that is your private key.

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

In **Git Bash**, print the key or send it straight to your clipboard:

```bash
cat ~/.ssh/id_ed25519.pub

# or copy it directly
clip < ~/.ssh/id_ed25519.pub
```

Your keys live in `C:\Users\<YourName>\.ssh\`, which Git Bash calls `~/.ssh/`. Copy the contents of the `.pub` file only. Never share `id_ed25519` (the file without `.pub`) -- that is your private key.

**Start the SSH agent** so Windows remembers your key instead of asking for the passphrase every time. In Git Bash:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

</div>

#### Step 3: Add the Key to GitLab

1. Go to [https://git.doit.wisc.edu](https://git.doit.wisc.edu)
2. Profile -- Preferences -- SSH Keys
3. Paste the key
4. Add a descriptive title (e.g., `Home Desktop 2026`)

#### Step 4: Clone the Repository

Navigate to your desired project directory:

```bash
git clone git@git.doit.wisc.edu:at-trad/farm2facts-frontend.git
```

If configured correctly, no password will be required.

**If SSH Fails**

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

If you see:

```
ssh: connect to host git.doit.wisc.edu port 22: Operation timed out
```

Your network likely blocks port 22. Use HTTPS instead.

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

If you see either of these:

```
ssh: connect to host git.doit.wisc.edu port 22: Connection timed out
ssh: connect to host git.doit.wisc.edu port 22: Network is unreachable
```

Your network likely blocks port 22. Use HTTPS instead.

If instead you see `Permission denied (publickey)`, the key reached your machine but not GitLab. Re-check that you pasted the `.pub` file into GitLab, and confirm the agent has your key loaded with `ssh-add -l`.

</div>

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

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

To avoid re-entering the token on every push, store it in the macOS Keychain:

```bash
git config --global credential.helper osxkeychain
```

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

Git for Windows installs Git Credential Manager, so the prompt appears as a window rather than in the terminal and your token is saved after the first use. If you are never prompted again, that is why.

If you are prompted every time, turn the credential manager on explicitly:

```bash
git config --global credential.helper manager
```

To replace a saved token later (for example when it expires), search the Start menu for **Credential Manager**, open **Windows Credentials**, and delete the `git:https://git.doit.wisc.edu` entry.

</div>

---

### Which Method Should You Use?

Use **SSH** if:
- You are contributing long-term
- Port 22 is not blocked

Use **HTTPS** if:
- You are on a restrictive network
- SSH times out

</details>

<details id="running-locally" class="section-card" markdown="1">
<summary>Running Locally</summary>

### Step 1: Install dependencies

From inside the cloned `farm2facts-frontend` folder:

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

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

Create the file from Terminal, then open it in your editor:

```bash
touch .env
open -e .env
```

Files starting with a dot are hidden in Finder. Press `Cmd + Shift + .` to show them.

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

Create the file from Git Bash:

```bash
touch .env
```

Then open it in VS Code or another code editor.

**Do not create it with Notepad through File Explorer.** Notepad silently saves the file as `.env.txt`, and the app will not find it. If you must use Notepad, choose **Save as type: All Files** and put the name in quotes: `".env"`.

File Explorer hides these extensions by default. Turn on **View -- Show -- File name extensions** so you can confirm the file is named exactly `.env`.

</div>

### Step 3: Start the dev server

```bash
npm run serve
```

This proxies `/api/v1` requests to `localhost:3000`. Open `http://localhost:8080` in your browser.

### Step 4: Verify it works

Log in with a test account. If the nav menu loads and you can reach a data entry form, the frontend is connected to the backend correctly.

</details>

<details id="other-commands" class="section-card" markdown="1">
<summary>Other Commands</summary>

```bash
# Production build (output to dist/)
npm run build

# Lint
npm run lint
```

There is no test suite in this project.

</details>

<details id="troubleshooting" class="section-card" markdown="1">
<summary>Troubleshooting</summary>

<div class="os-block" data-os="mac" markdown="1">

<p class="os-block-label">macOS</p>

| Problem | Fix |
| --- | --- |
| `command not found: brew` after installing Homebrew | Homebrew was not added to your `PATH`. Re-run the "Next steps" lines the installer printed, then open a new Terminal window. |
| `EACCES` permission errors from `npm install` | Do not use `sudo npm`. Reinstall Node through Homebrew (`brew install node`) so npm writes to a directory you own. |
| Port 8080 already in use | Find the process with `lsof -i :8080` and stop it, or run `npm run serve -- --port 8081`. |
| `gyp` or compiler errors during `npm install` | The Command Line Tools are missing. Run `xcode-select --install`, then delete `node_modules` and run `npm install` again. |

</div>

<div class="os-block" data-os="win" markdown="1">

<p class="os-block-label">Windows</p>

| Problem | Fix |
| --- | --- |
| `'npm' is not recognized` | Node is installed but your terminal is stale. Close it and open a new Git Bash window. |
| Every line of a file shows as changed | Line endings. Run `git config --global core.autocrlf input`, then re-clone the repo. |
| `.env` values are ignored | The file is probably named `.env.txt`. Turn on file name extensions in File Explorer and rename it. |
| Port 8080 already in use | Find the process with `Get-NetTCPConnection -LocalPort 8080` in PowerShell, stop it in Task Manager, or run `npm run serve -- --port 8081`. |
| `gyp` errors during `npm install` | Native build tools are missing. Re-run the Node.js installer and check "Tools for Native Modules". |
| Paths too long, or install fails deep in `node_modules` | Clone into a short path such as `C:\dev\farm2facts-frontend` rather than a deeply nested folder under Documents. |

</div>

</details>
