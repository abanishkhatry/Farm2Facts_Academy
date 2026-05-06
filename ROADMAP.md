# ROADMAP

Last updated: 2026-05-06

## Current State

**What works:**
- Complete 6-week onboarding plan with weekly breakdowns, issue mappings, student assignment strategy, and LLM usage progression (`STUDENT_ONBOARDING_PLAN.md`)
- 9 scaffolded student guides covering environment setup through self-directed work (`docs/guides/`)
- Templates for FEAST repos: CLAUDE.md, CONTRIBUTING.md, ADR template (`templates/`)
- Annotated reference bibliography with pedagogical and domain sources (`references/`)
- GitHub issue and PR templates (`.github/`)
- Project management scaffold: CLAUDE.md, ROADMAP.md, DECISIONS.md, post-commit hook

**In progress:**
- Slide decks for weeks 2-6

**Not started:**
- README for this repo
- Consistency review across all written materials
- Packaging guidance for reuse in other domains

**Open questions:**
- How much slide content should duplicate vs. reference the onboarding plan?
- What level of FEAST-environment readiness is needed before the first cohort starts?

---

## Milestones

### M1: Core Curriculum [In Progress]
**Goal:** All written instructional materials are complete, consistent, and reviewed.

- [x] Master onboarding plan (`STUDENT_ONBOARDING_PLAN.md`)
- [x] Scaffolded student guides (`docs/guides/01` through `09`)
- [x] FEAST repo templates (`templates/`)
- [x] Reference bibliography (`references/README.md`)
- [x] GitHub issue and PR templates (`.github/`)
- [ ] Consistency review across all written materials (cross-references, terminology, scaffolding tiers)
- [ ] Verify FEAST code references (file paths, line numbers) against current codebase state

### M2: Presentation Materials [In Progress]
**Goal:** Slide decks ready for all weekly group sessions.

- [x] Week 1: Orientation, domain concepts, architecture, LLM tools intro (`slides/week-1/`)
- [ ] Week 2: Linting, type hints, edge case brainstorming with LLMs
- [ ] Week 3: Specs before code, adversarial review workflow
- [ ] Week 4: ADRs and design decision documentation
- [ ] Week 5: Security review and deployment readiness
- [ ] Week 6: Retrospective and handoff (may be discussion-driven, slides optional)

### M3: Repo Scaffold [Complete]
**Goal:** This repo demonstrates the lightweight project management pattern it teaches.

- [x] CLAUDE.md with project overview, workflow, and roadmap maintenance rules
- [x] ROADMAP.md with milestones, dependency graph, and critical path
- [x] DECISIONS.md seeded with foundational curriculum design decisions
- [x] Post-commit hook for roadmap update reminders

### M4: Pilot Readiness [Not Started]
**Goal:** Everything an instructor needs to run the first cohort, end to end.

- [ ] README.md with instructor setup instructions
- [ ] Pre-session checklist (what to prepare before each week)
- [ ] Verify FEAST backend/frontend repos are in expected state for student onboarding
- [ ] All materials reviewed by at least one other instructor or peer
- [ ] Dry-run of Week 1 session flow

### M5: Post-Pilot Iteration [Not Started]
**Goal:** Incorporate feedback from the first cohort run.

- [ ] Collect student feedback (what worked, what was confusing, what was missing)
- [ ] Collect instructor observations (pacing, scaffolding levels, actual LLM usage patterns observed)
- [ ] Update guides based on common stumbling points
- [ ] Update onboarding plan based on actual vs. planned pacing
- [ ] Document deviations from plan and rationale

### M6: Reusable Template [Not Started]
**Goal:** Package the pattern so others can adapt it for different projects and domains.

- [ ] Separate domain-specific content (FEAST, food access, Mesa) from domain-agnostic structure
- [ ] Write adaptation guide: how to create an onboarding program for a different project
- [ ] Document which pieces are FEAST-specific vs. reusable scaffolding
- [ ] Create a template branch or repo with placeholders where domain content goes

---

## Dependency Graph

```
M1 (Core Curriculum)
 |
 +------> M2 (Presentations) -------+
 |                                   |
 +------> M3 (Repo Scaffold) -------+--> M4 (Pilot Readiness)
                                              |
                                              v
                                        M5 (Post-Pilot Iteration)
                                              |
                                              v
                                        M6 (Reusable Template)
```

M1 feeds M2 (slides reference the written curriculum) and M3 (repo scaffold needs to know the scope).
M2 and M3 both feed M4 (pilot needs slides and a functioning repo pattern).
M4 blocks M5 (must run the pilot to get feedback).
M5 blocks M6 (must iterate before packaging as a template).

## Critical Path to MVP (Pilot-Ready)

**M1** (finish consistency review) -> **M2** (at minimum, Week 1 slides) -> **M4** (instructor prep + dry-run)

The minimum viable pilot requires: the onboarding plan, guides, Week 1 slides, and a working FEAST environment for students. Weeks 2-6 slides can be created just-in-time during the pilot if needed, but Week 1 must be complete before students arrive. M3 is already done.
