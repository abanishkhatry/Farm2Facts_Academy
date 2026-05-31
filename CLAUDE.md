# CLAUDE.md

## Project Overview

FEAST_edu is the instructional materials repository for the FEAST (Food Equity Access Simulation Technology) student developer onboarding program. It contains the 8-week curriculum, scaffolded guides, templates, and reference materials that instructors use to run LLM-assisted development cohorts.

This repo contains no application code. The Farm2Facts application lives in two separate repos:
- Backend: `git.doit.wisc.edu/at-trad/farmers-coalition` (Rails 6.1 + MySQL + Grape API)
- Frontend: `git.doit.wisc.edu/at-trad/farm2facts-frontend` (Vue 3 + Pinia + MDB Vue UI Kit)

Templates in `templates/` are designed to be copied into those repos when setting up a new cohort.

This repo is also a demonstration of a lightweight, repo-local project management pattern (CLAUDE.md + DECISIONS.md) intended to be replicable for other subjects and domains.

## Repo Structure

```
STUDENT_ONBOARDING_PLAN.md    # Entry point: environment setup, Git concepts, repo links
DECISIONS.md                   # Architectural decision log for curriculum design choices
docs/
  guides/                      # Scaffolded student guides (index through 13)
taskList/
  mainTaskList.md              # Central task index: acceptance criteria and file pointers per task
references/
  curriculum.md                # Week-by-week curriculum (8 weeks, 4 sprints) with jump-link nav
assets/
  css/                         # Shared design system (design-system.css) + site styles (site.css)
templates/                     # Files to copy into FEAST repos (CLAUDE.md, CONTRIBUTING.md, ADR template)
.github/                       # Issue and PR templates (for copying into FEAST repos)
```

## Development Workflow

This repo uses main/dev/feature branch workflow:
- `main`: stable, reviewed materials ready for use with a cohort
- `dev`: integration branch for in-progress work
- Feature branches off `dev`, named descriptively (e.g., `feature/week1-slides`, `fix/guide-typos`)

### Checkpoint-Review-Refine Cycle

After completing a discrete unit of work (a guide, a template, a curriculum section):

1. **Checkpoint**: Commit the work.
2. **Review**: Re-read the material from a student's perspective. Does it stand alone? Are scaffolding levels appropriate for the target tier (J vs S)?
3. **Refine**: Fix gaps, adjust difficulty, ensure consistency with adjacent materials. Commit refinements separately.

This cycle applies to every deliverable, not just at milestone boundaries. Small, frequent checkpoints keep the materials internally consistent as the curriculum evolves.

## Content Conventions

- All written materials are Markdown.
- Keep language direct and concrete. Avoid jargon not defined in the domain section of `STUDENT_ONBOARDING_PLAN.md`.
- When referencing FEAST code, include file and line numbers so students can verify against the actual codebase.
- Code examples should be minimal and self-contained.
- No em dashes in any output.
