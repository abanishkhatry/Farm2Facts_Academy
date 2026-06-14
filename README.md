---
layout: default
title: "README"
---

# F2F Academy

Instructional materials for the F2F (Farm2Facts) student developer onboarding program. Students work through sprint-based task guides using LLM-assisted development while making real contributions to a farmers' market metrics platform.

**Live site:** [F2F Academy](https://abanishkhatry.github.io/Farm2Facts_Academy/)

## What this is

This repo contains everything needed to run a cohort of student developers through the F2F onboarding program: sprint task guides, workflow references, study materials, and onboarding documentation. It contains no application code.

The Farm2Facts application lives in two separate repos:
- **Backend:** [git.doit.wisc.edu/at-trad/farmers-coalition](https://git.doit.wisc.edu/at-trad/farmers-coalition) (Rails 6.1 + MySQL + Grape API)
- **Frontend:** [git.doit.wisc.edu/at-trad/farm2facts-frontend](https://git.doit.wisc.edu/at-trad/farm2facts-frontend) (Vue 3 + Pinia + MDB Vue UI Kit)

Students do not need direct database access -- all data flows through the backend API.

## How the program works

Each sprint has a soft deadline and a dedicated task guide. Students work through the guide, commit each deliverable separately, and submit a Merge Request on GitLab when complete.

1. **Onboard.** Read [STUDENT_ONBOARDING_PLAN.md](STUDENT_ONBOARDING_PLAN.md) to understand the two repos, Git and GitLab concepts, and database access details.
2. **Review study materials.** Check [references/study-materials.md](references/study-materials.md) for readings and resources mapped to the current sprint.
3. **Follow the task guide.** Open the relevant sprint entry in [taskList/curriculum-task-list.md](taskList/curriculum-task-list.md) and work through each task in order.
4. **Use the workflow guides.** The [docs/guides/](docs/guides/) index covers branching strategy, commit conventions, and how to open a Merge Request on GitLab.

## Repo structure

```
index.md                          Site home: program materials cards and points of contact
STUDENT_ONBOARDING_PLAN.md        Onboarding: Git/GitLab concepts, repo links, database access
taskList/
  curriculum-task-list.md         Sprint table: sprint names, full task guide links, related classes
  task1.md                        Sprint 1 -- Welcome to the Barn: onboarding, Claude Code 101,
                                  F2F article, personal Claude.md, codebase overview, MR submission
references/
  study-materials.md              Study materials index: sprint-mapped readings and resource links
docs/guides/
  index.md                        Workflow guides: How We Work, Git Workflow Reference, Pull Requests
  FRONTEND_GUIDE.md               Frontend repo overview and run-locally walkthrough
  BACKEND_GUIDE.md                Backend repo overview and run-locally walkthrough
assets/
  css/
    design-system.css             Design tokens: colors, type, spacing, shadows
    site.css                      Site-wide layout and component styles
  J6_Ledesma_Sustainability_2_2021.pdf  F2F research article (Sprint 1 reading)
templates/
  CLAUDE.md                       CLAUDE.md template for Farm2Facts repos
  CONTRIBUTING.md                 Contributing guide template
  adr-template.md                 ADR template
.github/
  ISSUE_TEMPLATE/                 Bug report, enhancement, refactor templates
  pull_request_template.md        PR template
  workflows/pages.yml             GitHub Pages deployment
```

## Deployment

The site is built with Jekyll and deployed to GitHub Pages via GitHub Actions. Pushing to `main` triggers a rebuild automatically. To run locally:

```bash
bundle exec jekyll serve
```

The site is served at `http://localhost:4000/Farm2Facts_Academy`.
