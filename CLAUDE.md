# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

F2F Academy is the instructional materials repository for student developers joining the Farm2Facts project at UW-Madison. It contains sprint task guides, workflow references, study materials, and onboarding documentation for running LLM-assisted development cohorts.

This repo contains no application code. The Farm2Facts application lives in two separate repos:
- Backend: `git.doit.wisc.edu/at-trad/farmers-coalition` (Rails 6.1 + MySQL + Grape API)
- Frontend: `git.doit.wisc.edu/at-trad/farm2facts-frontend` (Vue 3 + Pinia + MDB Vue UI Kit)

The site is built with Jekyll and deployed to GitHub Pages at `/Farm2Facts_Academy`.

## Local Development

```bash
bundle exec jekyll serve   # serve site locally at http://localhost:4000/Farm2Facts_Academy
bundle exec jekyll build   # build to _site/
```

The `_site/` directory is the build output -- do not edit files there directly.

## Repo Structure

```
index.md                          # Site home: program materials cards and points of contact
STUDENT_ONBOARDING_PLAN.md        # Onboarding: Git/GitLab concepts, repo links, database access
taskList/
  curriculum-task-list.md         # Sprint table: sprint names, guide links, related classes
  task1.md                        # Sprint 1 guide: onboarding, Claude Code 101, F2F article,
                                  # personal Claude.md, codebase overview, MR submission
references/
  study-materials.md              # Study materials index: sprint-mapped resource links
docs/guides/
  index.md                        # Workflow guides: How We Work, Git Workflow Reference, Pull Requests
  FRONTEND_GUIDE.md               # Frontend repo setup and run-locally walkthrough
  BACKEND_GUIDE.md                # Backend repo setup and run-locally walkthrough
assets/
  css/
    design-system.css             # Design tokens: colors, type, spacing, shadows
    site.css                      # Site-wide layout and component styles
  J6_Ledesma_Sustainability_2_2021.pdf  # F2F research article (Sprint 1 reading)
templates/                        # Files to copy into Farm2Facts repos -- excluded from Jekyll build
.github/                          # Issue and PR templates
_layouts/default.html             # Single Jekyll layout wrapping all pages
_config.yml                       # Jekyll config: baseurl, title, exclude list
```

## Branch Workflow

- `main`: stable materials ready for use with a cohort
- `dev`: integration branch for in-progress work
- Feature branches off `dev`, named descriptively (e.g., `feature/sprint2-tasks`, `fix/guide-typos`)

After completing a discrete unit of work, commit, re-read from a student's perspective, fix gaps, and commit refinements separately.

## Content Conventions

- All written materials are Markdown.
- No em dashes in any output.
- Keep language direct and concrete. Avoid jargon not defined in `STUDENT_ONBOARDING_PLAN.md`.
- When referencing Farm2Facts application code, include file paths and line numbers so students can verify against the actual codebase.
- Code examples should be minimal and self-contained.
- `templates/` files are excluded from the Jekyll build (see `_config.yml`) and are meant to be copied into the application repos, not rendered as site pages.
- Sprints are added to `curriculum-task-list.md` and `study-materials.md` as they are defined -- do not add placeholder rows for future sprints.
