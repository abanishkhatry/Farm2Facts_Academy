# Decisions Log

Curriculum and structural design decisions for the FEAST_edu repository. Each entry documents a choice that shapes how the onboarding program works and why we made it. Future adapters should read these before modifying the pattern.

For the ADR template used in the FEAST application repos, see `templates/adr-template.md`.

---

## DEC-001: Dedicated Repo for Instructional Materials

**Date:** 2026-05-06
**Status:** Accepted

**Context:** The FEAST project has two application repos (backend, frontend). Instructional materials could live in one of those repos, in a shared wiki, in external docs, or in a dedicated repo. We need a home for the 6-week curriculum, guides, slides, and templates that doesn't interfere with student development workflows in the code repos.

**Decision:** Use a dedicated `FEAST_edu` repo for all instructional materials, separate from the application code.

**Alternatives considered:**
- *Docs folder in the backend repo.* Ties instructional materials to one side of the stack. Clutters the dev workflow with non-code changes.
- *GitHub wiki.* Not versionable through normal git workflows, no PR review process, harder to track changes over time.
- *Notion/Google Docs.* Easy to collaborate on but not versionable, not portable, can't demonstrate the project management pattern we're teaching.

**Consequences:**
- (+) Instructional materials have their own commit history, branches, and review cycle
- (+) The repo itself demonstrates the project management workflow that students will use
- (+) Cleanly separable from application repos, making reuse for other domains straightforward
- (-) Templates must be manually copied into the FEAST repos for each cohort
- (-) Code references (file paths, line numbers) in guides can drift as the FEAST codebase evolves and must be re-verified before each cohort

---

## DEC-002: Progressive LLM Usage Model

**Date:** 2026-05-06
**Status:** Accepted

**Context:** Students range from freshmen to seniors. LLM code generation tools can shortcut the learning process. Anthropic's 2026 RCT with 52 junior engineers found that students who delegated code generation early scored 17% lower on comprehension. We need a policy that lets students benefit from LLMs without skipping skill-building.

**Decision:** Restrict LLM usage in early weeks and progressively unlock capabilities:
- Weeks 1-2: LLM as explainer only (ask questions about existing code, not for code generation)
- Weeks 3-4: LLM for spec review, edge case brainstorming, adversarial PR review
- Weeks 5-6: Full LLM workflow including design discussion and guided code generation

The constant across all weeks: "You must be able to explain every line in your PR without looking at your chat history."

**Alternatives considered:**
- *Full access from day one.* Faster output, but freshmen skip developing code-reading skills entirely. Supported by the Anthropic research showing comprehension gaps.
- *No LLM tools at all.* Misses the pedagogical goal of teaching LLM-assisted development as a professional skill. Students will use these tools regardless; better to teach good habits.
- *Honor system with full access.* Unenforceable and creates social pressure on students who want to follow the rules but see peers bypassing them.

**Consequences:**
- (+) Students build code-reading and reasoning skills before getting code-generation power
- (+) Each week's unlock feels earned, maintaining engagement
- (+) Adversarial review skills (week 3) are established before full generation access (week 5)
- (-) Experienced students may feel held back in weeks 1-2 (mitigated by assigning harder analysis tasks to S-tier students)
- (-) Requires instructor attention to enforce, since LLM usage is difficult to monitor directly

---

## DEC-003: Built-in Project Management as Pedagogical Pattern

**Date:** 2026-05-06
**Status:** Accepted

**Context:** We want this curriculum to be adaptable for other projects and domains. Beyond the content itself, the repo structure and development workflow should be something others can copy. We also want to practice what we preach: if we tell students to use CLAUDE.md and track decisions, the repo that teaches them should do the same.

**Decision:** Use CLAUDE.md, ROADMAP.md, DECISIONS.md, and a post-commit hook in this repo. Track the development of the instructional materials using the same lightweight workflow we teach students to use in the FEAST repos.

**Alternatives considered:**
- *GitHub Issues/Projects only.* Standard tooling but doesn't demonstrate anything specific to LLM-assisted development workflows. Issues live outside the repo, making the pattern less self-contained.
- *External project management (Linear, Notion).* Adds a dependency, login barrier, and separates planning from the materials they describe. Reduces portability.

**Consequences:**
- (+) The repo is a self-contained example of the pattern it teaches
- (+) Future adapters can fork the repo structure, not just the content
- (+) Decisions are tracked in version control alongside the materials they affect
- (-) Adds maintenance overhead to keep ROADMAP.md current (mitigated by the post-commit hook nudge)
- (-) Small team (primarily one instructor) means the overhead must stay genuinely lightweight or it won't stick
