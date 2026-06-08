---
layout: default
title: "README"
---

# F2F Academy

Instructional materials for the F2F (Farm2Facts) student developer onboarding program. An eight-week curriculum that teaches LLM-assisted development practices while students make real contributions to a farmers' market metrics platform.

**Live site:** [F2F Academy](https://abanishkhatry.github.io/Farm2Facts_Academy/)

## What this is

This repo contains everything an instructor needs to run a cohort of student developers through the F2F onboarding program: a master curriculum, scaffolded guides, repo templates, and reference materials. It contains no application code.

The Farm2Facts application lives in two separate repos:
- **Backend:** [git.doit.wisc.edu/at-trad/farmers-coalition](https://git.doit.wisc.edu/at-trad/farmers-coalition) (Rails 6.1 + MySQL + Grape API)
- **Frontend:** [git.doit.wisc.edu/at-trad/farm2facts-frontend](https://git.doit.wisc.edu/at-trad/farm2facts-frontend) (Vue 3 + Pinia + MDB Vue UI Kit)

Students do not need direct database access -- all data flows through the backend API.

## How the program works

Students progress from "run the project and understand what it does" to "independently plan and ship improvements." The journey follows four repeating steps each week:

1. **Onboard.** Start with [STUDENT_ONBOARDING_PLAN.md](STUDENT_ONBOARDING_PLAN.md) to set up your environment, understand the Farm2Facts codebase, and configure your LLM tooling. This is the entry point for every new cohort member.

2. **Follow the curriculum.** Each week's scope -- group session topics and solo work -- is outlined in [references/curriculum.md](references/curriculum.md). The curriculum tells you what to do and in what order across all eight weeks.

3. **Get task details.** Before starting any task, read the relevant entry in [taskList/mainTaskList.md](taskList/mainTaskList.md). Each entry has acceptance criteria, context, and pointers to the right files in the codebase.

4. **Use the workflow.** Create a feature branch off the right base, complete the task, open a pull request, and work through the three-layer review pipeline before merging: CI checks, peer review, and LLM adversarial review. The guides in [docs/guides/](docs/guides/) explain each step.

**Key design decisions:**

- **Progressive LLM access.** Weeks 1-2: LLM as explainer only. Weeks 3-4: spec review, edge case brainstorming, adversarial PR review. Weeks 5-8: full LLM workflow including guided code generation. The constant rule: you must be able to explain every line without looking at your chat history.
- **Three-layer review pipeline.** CI checks (from Week 2), peer review (from Week 2), and LLM adversarial review (from Week 3) build incrementally so students never submit PRs without structured feedback.
- **ADR progression.** Students write Architecture Decision Records manually in Weeks 2-3, then learn to generate them from diffs/PRs with LLM tools in Week 4, and choose the right approach for each situation in Weeks 5-8.
- **Agentic tools from day one.** A CLI agent (Claude Code if available, Gemini CLI as a free alternative) is installed in Week 1. Students create a project context file for their repo as part of their first solo work.

See [DECISIONS.md](DECISIONS.md) for the full rationale behind these and other curriculum choices.

## Repo structure

```
STUDENT_ONBOARDING_PLAN.md    Entry point: environment setup, Git concepts, repo links
DECISIONS.md                   Curriculum design decisions with rationale
docs/
  guides/                      Scaffolded student guides (used alongside taskList entries)
    index.md                   How We Work, Git Workflow Reference, Pull Requests
    FRONTEND_GUIDE.md          Frontend repo overview and run-locally walkthrough
    BACKEND_GUIDE.md           Backend repo overview and run-locally walkthrough
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
  mainTaskList.md              Central task index: acceptance criteria and file pointers per task
references/
  curriculum.md                Week-by-week curriculum (Weeks 1-8) with jump-link nav
assets/
  css/
    design-system.css          Shared design tokens
    site.css                   Site-wide styles
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

## Deployment

The site is built with Jekyll and deployed to GitHub Pages via GitHub Actions. Pushing to `main` triggers a rebuild automatically. To run locally:

```bash
bundle exec jekyll serve --baseurl "" --port 4001
```

Always use `--baseurl ""` locally -- `_config.yml` sets the GitHub Pages baseurl which breaks asset loading without the override.

