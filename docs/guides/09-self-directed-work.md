---
layout: default
title: "Guide: Self-Directed Work"
---

# Guide: Self-Directed Work

## Context

Starting in week 3, you'll have solo time to pick issues from the backlog and work them independently. This guide explains how to choose work, plan it, and ship it.

## How to Pick an Issue

### 1. Go to the GitHub project board

Look at issues by priority: must-fix > should-fix > nice-to-have.

### 2. Match to your comfort level

**If you're newer to the codebase:**
- Type hint additions in files nobody's touched yet
- Documentation gaps (missing docstrings, confusing comments)
- Small flake8 fixes in excluded files
- Frontend: missing error handling, loading states

**If you're comfortable:**
- Bug fixes with clear reproduction steps
- Refactoring (extract functions, remove duplication)
- New tests for untested functions
- Logging improvements

**If you want a challenge:**
- Cross-cutting refactors (spatial data handling, database access patterns)
- Algorithm improvements (MFAI scoring, distance optimization)
- New features (reporting API, metrics display)

### 3. Claim it

Comment on the issue: "I'm picking this up." If someone else is already working on it, pick a different one.

## How to Plan It

Before coding, write a one-paragraph plan in the issue comments:

```markdown
**Plan**: I'm going to [what you'll change] in [which files].
The approach is [how]. I'll test it by [test plan].
This should take about [time estimate].
```

This takes 5 minutes and saves you from going down the wrong path. It also lets others give you feedback before you invest time coding.

## How to Ship It

1. Implement on your feature branch
2. Make sure tests pass and flake8 is clean
3. Open a PR using the template
4. Self-review: run adversarial LLM review on your own PR in a fresh session before requesting peer review
5. Request review from a teammate

## What If You Get Stuck?

- Comment on the issue describing where you're stuck
- Move on to something else. Someone (or you next week) can pick it up.
- Getting stuck is information. File a new issue if you discovered the problem is bigger than expected.

## What If You Finish Early?

- Pick another issue
- Write tests for code that doesn't have them
- Look for new issues to file
- Improve a scaffolded guide based on your experience (what was confusing? what was missing?)

## Filing New Issues

As you work, you'll notice things. File issues for:
- Anything that confused you (if it confused you, it'll confuse others)
- Patterns you see repeated (e.g., "store type classification is hardcoded in 5 places")
- Things that are harder than they should be (e.g., "testing Household requires a full Mesa model")
- Ideas for improvements you don't have time for right now

For S students: If you see a systemic pattern, file a single issue that captures the whole problem and proposes a solution. This is how you move from contributor to maintainer.

## The Progression

| Week | Your Authority | What You're Expected to Do |
|------|---------------|---------------------------|
| 3 | Choose from existing backlog | Pick 1 issue, write a plan, ship it |
| 4 | Create + choose | File 1+ new issues, pick and ship from backlog |
| 5 | Full autonomy | Ship the highest-impact thing you can identify |
| 6 | Handoff | Close or document everything in progress |
