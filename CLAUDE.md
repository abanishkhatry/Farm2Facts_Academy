# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

F2F Academy is the instructional materials and program management repository for student developers joining the Farm2Facts project at UW-Madison. It contains scaffolded workflow guides, sprint task lists, study material references, and onboarding documentation for running LLM-assisted development cohorts.

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
index.md                       # Site home: program materials cards and points of contact
STUDENT_ONBOARDING_PLAN.md     # Entry point for new interns: Git/GitLab concepts, repo links, environment setup
taskList/
  mainTaskList.md              # Central sprint table: task breakdowns, guide links, status, related classes
  task1.md                     # Sprint 1 guide: onboarding, Claude Code 101, F2F article, PR creation
references/
  curriculum.md                # Study Materials index: sprint-mapped resource links and completion status
docs/guides/                   # Scaffolded workflow guides (04 through 13 + FRONTEND_GUIDE, BACKEND_GUIDE)
templates/                     # Files to copy into Farm2Facts repos (CLAUDE.md, CONTRIBUTING.md, ADR template)
.github/                       # Issue and PR templates
assets/css/                    # design-system.css (tokens, components) + site.css (layout)
_layouts/default.html          # Single Jekyll layout wrapping all pages
_config.yml                    # Jekyll config: baseurl, title, exclude list
```

## Branch Workflow

- `main`: stable materials ready for use with a cohort
- `dev`: integration branch for in-progress work
- Feature branches off `dev`, named descriptively (e.g., `feature/sprint2-tasks`, `fix/guide-typos`)

After completing a discrete unit of work, follow the checkpoint-review-refine cycle: commit, re-read from a student's perspective, fix gaps, commit refinements separately.

## Content Conventions

- All written materials are Markdown.
- No em dashes in any output.
- Keep language direct and concrete. Avoid jargon not defined in `STUDENT_ONBOARDING_PLAN.md`.
- When referencing Farm2Facts application code, include file paths and line numbers so students can verify against the actual codebase.
- Code examples should be minimal and self-contained.
- `templates/` files are excluded from the Jekyll build (see `_config.yml`) and are meant to be copied into the application repos, not rendered as site pages.
