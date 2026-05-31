---
layout: default
title: "Student Onboarding Plan"
---

# F2F Student Developer Onboarding

Welcome to the Farm2Facts student developer program. This document is your starting point. It covers the tools, repositories, and systems you will be working with. Each repository also has its own dedicated Markdown guide with deeper technical details, workflow rules, and issue scaffolding specific to that codebase.

---

## Git, GitHub, and GitLab

**Git** is a version control system that tracks changes to files over time. Every change you make to code is recorded as a commit -- a snapshot with a message explaining what changed and why. Git runs locally on your machine.

**GitHub** is a cloud platform that hosts Git repositories. It adds collaboration features on top of Git: pull requests, code review, issue tracking, and CI/CD automation. This is where your team's repos live and where all code review happens.

**GitLab** is an alternative to GitHub with similar features. Farm2Facts uses GitLab, but the concepts transfer directly if you encounter Github elsewhere.

### Key concepts you need before touching any code

| Concept           | What it means                                                                      |
| ----------------- | ---------------------------------------------------------------------------------- |
| Repository (repo) | A project folder tracked by Git, with full history of every change                 |
| Branch            | A parallel version of the codebase where you do your work without affecting others |
| Commit            | A saved snapshot of your changes, with a message explaining what and why           |
| Pull Request (PR) | A proposal to merge your branch into the main codebase, open for review            |
| Clone             | Download a copy of a remote repo to your local machine                             |
| Push / Pull       | Send your commits to GitHub / download others' commits to your machine             |
| Fork              | A personal copy of someone else's repo, used to propose changes                    |

---

## The Repos

Farm2Facts is split across two repositories. Each has a dedicated guide with setup instructions, architecture details, and issue scaffolding.

### Frontend: Farm2Facts Frontend

**Repo:** [Farm2Facts Frontend](https://git.doit.wisc.edu/at-trad/farm2facts-frontend)

**Guide To Run It Locally:** [FRONTEND_GUIDE.md]({{ site.baseurl }}/docs/guides/FRONTEND_GUIDE)

---

### Backend: Farm2Facts Backend

**Repo:** [Farm2Facts Backend](https://git.doit.wisc.edu/at-trad/farmers-coalition)

**Guide To Run It Locally:** [BACKEND_GUIDE.md]({{ site.baseurl }}/docs/guides/BACKEND_GUIDE)

---

## Database

Farm2Facts uses a **MySQL** relational database hosted through the Department of Information Technology (DoIT) at UW-Madison. As a student developer, you will not interact with the database directly -- all data flows through the backend API, which exposes farmers market data as JSON endpoints that the frontend consumes. The access details below are for reference and instructor use.

**Hosting panel:** [webhosting.doit.wisc.edu/panel](https://webhosting.doit.wisc.edu/panel/)

For login credentials, contact **Garrett Smith** at garrett.smith@wisc.edu.

### Domain layout

After logging in you will see four domains. Two are associated with Farm2Facts:

| Domain | Purpose |
| ------ | ------- |
| `farm2facts.org` | Hosts the WordPress instance |
| `account.farm2facts.org` | Hosts the main application and the database |

### Accessing the database

1. Select **account.farm2facts.org** from the hosting dashboard.
2. Navigate to **Files & Databases** → **Databases**.
3. Click **phpMyAdmin** to open the graphical interface.

From phpMyAdmin you can view and manipulate live data entries from markets and market organizations using the GUI or raw SQL queries.

---
