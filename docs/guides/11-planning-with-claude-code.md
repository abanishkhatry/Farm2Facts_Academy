---
layout: default
title: "Guide: Structured Planning with CLI Agents"
---

# Guide: Structured Planning with CLI Agents

## Context

CLI agents have structured planning capabilities that complement the hand-written specs and ADRs you've been writing since Week 2. This guide covers when to use planning tools and how they fit into the spec-first workflow. Examples use Claude Code commands, but the concepts apply to any agent.

## The Planning Capabilities

Most CLI agents support three levels of structured planning. The names differ by tool, but the concepts are the same.

### Single-feature planning

**What it does:** Given a description of what you want to accomplish, the agent explores the codebase and produces a structured plan: which files to change, in what order, what dependencies exist, and how to verify the changes.

**In Claude Code,** this is the `/plan` command. In other tools, you can achieve the same result by prompting the agent to "plan the implementation" of a feature before writing any code.

**When to use it:**
- You know *what* you want to build and need to map the *how*
- The change touches multiple files and you want to make sure you don't miss any
- You've written a hand-written spec and want a cross-check on your implementation plan

**When NOT to use it:**
- You're still deciding *whether* to do something (write an ADR instead)
- You're exploring or understanding code (just ask the agent questions)
- The change is trivial (one file, obvious what to do)

**Example workflow:**
```
1. Write a hand-written spec in the issue comment (the what and why)
2. Ask the agent to plan the implementation with your spec as context (the how)
3. Review the plan critically:
   - Did it identify files you missed?
   - Did it over-scope the change?
   - Does the order make sense?
4. Revise your plan based on what you learned
5. Implement
```

### Multi-issue / project-phase planning

**What it does:** Plans across multiple related issues or an entire project phase. Identifies dependencies between issues, proposes implementation ordering, and maps the work across the codebase.

**In Claude Code,** this is the `/ultraplan` command. In other tools, you can prompt for multi-issue planning by providing all related issue descriptions and asking the agent to sequence and identify dependencies across them.

**When to use it:**
- You have a cluster of related issues (e.g., backend API + frontend view + metrics)
- You're starting a new project phase and need to sequence the work
- You want to identify the dependency chain between tasks

**When NOT to use it:**
- Single-feature work (use single-feature planning instead)
- Prioritization decisions (that's a human/team judgment call)
- You haven't written specs for the individual issues yet

**Example workflow:**
```
1. Gather the related issues (e.g., #94, #79, frontend #36)
2. Ask the agent to plan across all of them (in Claude Code: /ultraplan)
3. Review: Does the dependency ordering make sense?
   Did it identify the API contract that connects the pieces?
4. Use the output to coordinate work across team members
5. Each team member uses single-feature planning for their individual piece
```

### Branch-level review

**What it does:** Reviews an entire branch's accumulated changes (not just a single PR's diff). Looks for cross-cutting issues that per-PR reviews might miss.

**In Claude Code,** this is the `/ultrareview` command. In other tools, you can achieve this by providing the full branch diff and asking the agent to review for cross-cutting concerns.

**When to use it:**
- Before merging a long-lived branch to dev or main
- As a complement to the per-PR adversarial review rotation
- When you want a comprehensive check after multiple PRs have landed

**When NOT to use it:**
- For individual PR review (use a fresh LLM session with the diff instead)
- As a replacement for human review (it's a supplement, not a substitute)

## How These Fit Together

| Stage | Tool | Purpose |
|-------|------|---------|
| Deciding what to build | Hand-written ADR | Capture the *why* and *what*, document alternatives |
| Planning how to build it | Single-feature planning | Map files, order, dependencies for one feature |
| Coordinating across features | Multi-issue planning | Sequence multiple issues, find API contracts |
| Implementing | CLI agent (interactive) | Write code with the iterative refinement pattern |
| Reviewing one PR | Fresh LLM session | Adversarial review of a single diff |
| Reviewing accumulated work | Branch-level review | Cross-cutting review of a branch |

## The Key Principle

Structured planning maps *how* to implement something. It does not decide *what* to implement or *whether* it's worth doing. Those decisions belong to you, your team, and your ADRs.

The best workflow pairs human judgment with tool precision:
- **You** write the spec (what and why)
- **The tool** maps the implementation (how and where)
- **You** review the plan (does the how match the what?)
- **You** implement (the tool assists, you own the result)

## LLM Usage by Week

| Week | What's available |
|------|-----------------|
| 2 | Single-feature planning previewed in demo. Not yet used independently. |
| 3 | Single-feature planning for cross-checking hand-written specs on assigned issues. |
| 4 | Single-feature planning independently. Multi-issue planning for cross-feature work. Branch-level review introduced. |
| 5-6 | Full access. Choose manual specs vs. structured planning based on scope and complexity. |
