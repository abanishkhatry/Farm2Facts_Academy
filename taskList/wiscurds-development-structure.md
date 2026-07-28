---
layout: default
title: "Development Structure Overview"
---

# Farm2Facts Development Structure Overview

How the Farm2Facts project is put together and how work moves through it. Read this before your first task so you know where the code lives, how the pieces talk to each other, and what happens between being assigned an issue and having your work merged.

- [The Two Repositories](#the-two-repositories)
- [How the Pieces Fit Together](#how-the-pieces-fit-together)
- [Branches and Environments](#branches-and-environments)
- [How Work Moves](#how-work-moves)
- [Working Locally](#working-locally)
- [Who to Ask](#who-to-ask)

---

<details id="the-two-repositories" class="section-card" markdown="1">
<summary>The Two Repositories</summary>

Farm2Facts is not one codebase. It is two applications that are developed, reviewed, and run separately, and you will work in both.

| | Frontend | Backend |
| --- | --- | --- |
| **Repo** | <a href="https://git.doit.wisc.edu/at-trad/farm2facts-frontend" target="_blank" rel="noopener noreferrer">farm2facts-frontend</a> | <a href="https://git.doit.wisc.edu/at-trad/farmers-coalition" target="_blank" rel="noopener noreferrer">farmers-coalition</a> |
| **Stack** | Vue 3, Vue Router, Pinia, Chart.js, LESS | Ruby on Rails 6.1, MySQL, Grape, DeviseTokenAuth |
| **What it is** | The interface market organizations, producers, and researchers use to enter and review data | The API and data layer, plus a traditional Rails web interface |
| **Runs locally on** | `localhost:8080` | `localhost:3000` |
| **Setup guide** | [Frontend guide]({{ site.baseurl }}/docs/guides/FRONTEND_GUIDE) | [Backend guide]({{ site.baseurl }}/docs/guides/BACKEND_GUIDE) |

Both are hosted on **GitLab** at `git.doit.wisc.edu`, not GitHub. You need a GitLab account on your `@wisc.edu` email and permissions granted on both repos before you can clone or push.

Each repo also contains an **ADR (Architecture Decision Record)**. When you want to know why something is built the way it is, read the ADR before reading the code.

</details>

<details id="how-the-pieces-fit-together" class="section-card" markdown="1">
<summary>How the Pieces Fit Together</summary>

The frontend holds no data of its own. Every screen you see is the result of a request to the backend.

1. A user acts in the Vue app, for example opening a market profile.
2. The frontend sends an HTTP request through Axios to the backend's API, under `/api/v1`.
3. The backend's **Grape API** (`app/controllers/api/v1/`) handles that request, reads or writes MySQL, and returns JSON.
4. The frontend stores what it needs and renders it.

A few consequences worth knowing early:

- **Two auth systems exist.** The API uses DeviseTokenAuth token headers, mounted at `/auth`. The older Rails web interface uses session-based auth. They are separate, and which one applies depends on which part of the backend you are touching.
- **The frontend has to be told where the backend is.** `VUE_APP_API_DOMAIN` in the frontend's `.env` points at an API. If it points at production, you are working against live market data. Check it before you start.
- **A frontend feature usually needs backend work too.** If the data you want is not already exposed by an endpoint, the change starts in the backend, not the Vue component.
- **The backend serves more than the API.** There are 300+ traditional Rails routes in `config/routes.rb` alongside the API. Not all backend code paths are reachable from the Vue app.

### Where things are hosted

| Thing | Where |
| --- | --- |
| Source code, issues, merge requests | GitLab (`git.doit.wisc.edu`) |
| Live application and its MySQL database | DoIT web hosting (`account.farm2facts.org`) |
| Public-facing WordPress site | `farm2facts.org` |

Database access goes through phpMyAdmin in the DoIT hosting panel. The steps are in the [Database section of the Student Onboarding Plan]({{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#database).

</details>

<details id="branches-and-environments" class="section-card" markdown="1">
<summary>Branches and Environments</summary>

Both repos use the same four-level branch structure. Code moves up one level at a time.

| Branch | What it holds | How code gets in |
| --- | --- | --- |
| `main` | Stable, production-ready code | Merged from `staging` after full review |
| `staging` | Pre-production integration, tested before release | Merged from `dev` |
| `dev` | The active integration branch | Your merge requests land here |
| `feature/*` | Your work on one issue | You create it from `dev` |

Two rules that matter more than the rest:

- **Never commit directly to `main` or `dev`.** All changes arrive by merge request.
- **Always branch from an up-to-date `dev`.** Pull first, then branch, or you will be resolving avoidable conflicts later.

```bash
git checkout dev
git pull
git checkout -b feature/issue-NUMBER-short-desc
```

Name the branch after the issue it addresses, for example `feature/issue-24-linting`.

</details>

<details id="how-work-moves" class="section-card" markdown="1">
<summary>How Work Moves</summary>

Work is not something you pick up informally. It follows a fixed path, so that everyone can see what is in progress and nothing lands unreviewed.

1. **An issue is created** on the GitLab issue board and assigned to you. It describes the task and carries a checklist.
2. **You branch from `dev`**, named after the issue.
3. **You commit as you go**, one logical change per commit, in imperative mood, referencing the issue number. `Fix store count bug (#6)`, not `fixed stuff`.
4. **You open a merge request into `dev`** when the issue's checklist is complete. Assign Abanish as reviewer and yourself as assignee, and fill out every field of the description template.
5. **Review happens on the merge request.** Expect feedback and further commits on the same branch.
6. **It merges into `dev`**, and later moves up through `staging` to `main` as part of a release.

The full rules for each step, including the commit message conventions and the merge request description template, are in the [Workflow Guides]({{ site.baseurl }}/docs/guides/).

Your work is not submitted until the merge request is open, fully filled out, and assigned. A finished branch that nobody has been asked to review is not finished.

</details>

<details id="working-locally" class="section-card" markdown="1">
<summary>Working Locally</summary>

To see a change end to end you generally need three things running: MySQL, the backend, and the frontend.

| Order | What | Command | Result |
| --- | --- | --- | --- |
| 1 | MySQL | varies by machine and OS | Database reachable |
| 2 | Backend | `bundle exec rails server` | API on `localhost:3000` |
| 3 | Frontend | `npm run serve` | App on `localhost:8080` |

The frontend proxies `/api/v1` to `localhost:3000`, so the backend needs to be up first or the app will load with no data.

Where to go for the details:

- [Frontend guide]({{ site.baseurl }}/docs/guides/FRONTEND_GUIDE) and [Backend guide]({{ site.baseurl }}/docs/guides/BACKEND_GUIDE) for setting up your own machine. Both cover macOS and Windows; use the switch at the top of each guide.
- [Running Lab Machines]({{ site.baseurl }}/STUDENT_ONBOARDING_PLAN#running-lab-machines) if you are working on a Kaufman Lab machine, where everything is already installed.

**Before you start working, confirm you are pointed at local data.** The backend's `config/database.yml` should point at your local MySQL, and the frontend's `.env` should point at `localhost:3000`. Getting this wrong means editing production market data.

</details>

<details id="who-to-ask" class="section-card" markdown="1">
<summary>Who to Ask</summary>

Ask early. A question that takes someone five minutes to answer is not worth two days of being stuck.

| Topic | Person |
| --- | --- |
| Code, tasks, issues, merge requests | Abanish Khatry -- [akhatry@wisc.edu](mailto:akhatry@wisc.edu) |
| Professional guidance | Garrett Smith -- [garrett.smith@wisc.edu](mailto:garrett.smith@wisc.edu) |
| Administrative matters | Alfonso Morales -- [morales1@wisc.edu](mailto:morales1@wisc.edu) |

Day-to-day questions go in the project's Slack channel. Use email for anything that needs a lasting record.

</details>
