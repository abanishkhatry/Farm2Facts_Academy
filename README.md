---
layout: default
title: "README"
---

# F2F Academy

Instructional materials for the F2F (Farm2Facts) student developer onboarding program. An eight-week curriculum that teaches LLM-assisted development practices while students make real contributions to a food access simulation tool.

**Live site:** [uw-madison-dsi.github.io/FEAST_educational_materials](https://uw-madison-dsi.github.io/FEAST_educational_materials/)

## What this is

This repo contains everything an instructor needs to run a cohort of student developers through the F2F onboarding program: a master curriculum, scaffolded guides, repo templates, and reference materials. It contains no application code.

The Farm2Facts application lives in two separate repos:
- **Backend:** [git.doit.wisc.edu/at-trad/farmers-coalition](https://git.doit.wisc.edu/at-trad/farmers-coalition) (FastAPI + Mesa ABM + PostgreSQL)
- **Frontend:** [git.doit.wisc.edu/at-trad/farm2facts-frontend](https://git.doit.wisc.edu/at-trad/farm2facts-frontend) (Vue 3 + Pinia + MDB Vue UI Kit)

Students do not need direct database access -- all data flows through the backend API.

## How the program works

Students progress from "run the project and understand what it does" to "independently plan and ship improvements." Each week has a group session and async solo work.

**Key design decisions:**

- **Progressive LLM access.** Weeks 1-2: LLM as explainer only. Weeks 3-4: spec review, edge case brainstorming, adversarial PR review. Weeks 5-8: full LLM workflow including guided code generation. The constant rule: you must be able to explain every line without looking at your chat history.
- **Three-layer review pipeline.** CI checks (from Week 2), peer review (from Week 2), and LLM adversarial review (from Week 3) build incrementally so students never submit PRs without structured feedback.
- **ADR progression.** Students write Architecture Decision Records manually in Weeks 2-3, then learn to generate them from diffs/PRs with LLM tools in Week 4, and choose the right approach for each situation in Weeks 5-8.
- **Agentic tools from day one.** A CLI agent (Claude Code if available, Gemini CLI as a free alternative) is installed in Week 1. Students create a project context file for their repo as part of their first solo work.

See [DECISIONS.md](DECISIONS.md) for the full rationale behind these and other curriculum choices.

## Repo structure

```
STUDENT_ONBOARDING_PLAN.md    Focused onboarding overview (Git concepts, repo links)
docs/
  guides/                      Scaffolded student guides
    index.md                   How We Work, Git Workflow Reference, Pull Requests, all guides
    FRONTEND_GUIDE.md          Frontend repo overview, clone steps, run-locally walkthrough
    BACKEND_GUIDE.md           Backend repo overview, clone steps, run-locally walkthrough
    04-linting-setup.md
    05-writing-tests.md
    06-bug-investigation.md
    07-optimization.md
    08-adversarial-review.md
    09-self-directed-work.md
    10-deployment-configuration.md
    11-planning-with-claude-code.md
    12-agentic-engineering-concepts.md
    13-agentic-workflow-best-practices.md
taskList/
  mainTaskList.md              Central task index with week-by-week descriptions
references/
  curriculum.md                Week-by-week curriculum (Weeks 1-8) with jump-link nav
templates/
  CLAUDE.md                    CLAUDE.md template for Farm2Facts repos
  CONTRIBUTING.md              Contributing guide template
  adr-template.md              ADR template
  vision-plan-template.md      Vision and improvement plan template
.github/
  ISSUE_TEMPLATE/              Bug report, enhancement, refactor templates
  pull_request_template.md     PR template
  workflows/pages.yml          GitHub Pages deployment
```

## Using these materials

**To run a cohort:**

1. Fork or clone this repo.
2. Copy templates from `templates/` into the Farm2Facts application repos (backend and frontend).
3. Verify code references (file paths, line numbers in guides) against the current codebase state.
4. Review [STUDENT_ONBOARDING_PLAN.md](STUDENT_ONBOARDING_PLAN.md) for the onboarding overview.
5. Walk students through the week-by-week task list at [references/curriculum.md](references/curriculum.md).

**To adapt for a different project:**

This repo is designed as a replicable pattern. The curriculum structure, project management files (CLAUDE.md, ROADMAP.md, DECISIONS.md), guide scaffolding, and review pipeline progression are domain-agnostic. The Farm2Facts-specific content is in the domain sections of the curriculum and the code references in guides. See [DECISIONS.md](DECISIONS.md) to understand why the program is structured the way it is before modifying it.

## Project management

This repo uses the same lightweight project management pattern it teaches:

- **[ROADMAP.md](ROADMAP.md)** tracks milestones and progress
- **[DECISIONS.md](DECISIONS.md)** records curriculum design decisions with context and rationale
- **[CLAUDE.md](CLAUDE.md)** serves as both developer documentation and AI agent configuration
- A post-commit hook reminds about ROADMAP.md updates

## Deployment

The site is built with Jekyll and deployed to GitHub Pages via GitHub Actions. Pushing to `main` triggers a rebuild automatically. To run locally:

```bash
bundle exec jekyll serve --baseurl "" --port 4001
```

Always use `--baseurl ""` locally -- `_config.yml` sets the GitHub Pages baseurl which breaks asset loading without the override.

## Credits

Developed at the [UW-Madison Data Science Institute](https://dsi.wisc.edu).
