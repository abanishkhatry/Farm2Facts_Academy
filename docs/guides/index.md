---
layout: default
title: "Student Guides"
---

# Workflow Guides

Scaffolded guides that walk you through increasingly complex contributions to the Farm2Facts codebase. Each guide pairs with a week of the [onboarding curriculum]({{ site.baseurl }}/STUDENT_ONBOARDING_PLAN).

- [How We Work](#how-we-work)
- [Git Workflow Reference](#git-workflow-reference)
- [Pull Requests](#pull-requests)

---

<details id="how-we-work" class="section-card" markdown="1">
<summary>How We Work</summary>

1. A task will be created in the Gitlab Issue Boards and assigned to you.
2. Follow the [branching strategy](#git-workflow-reference) to create a feature branch for that issue.
3. Read the issue description and complete each step listed there.
4. When the final checklist in the issue is checked off, open a [Pull Request](#pull-requests).

</details>

<details id="git-workflow-reference" class="section-card" markdown="1">
<summary>Git Workflow Reference</summary>

### Branch strategy

The Farm2Facts repos use a four-level branch structure:

- `main` -- stable, production-ready code. Only merged from staging after full review.
- `staging` -- pre-production integration. Tested here before going to main.
- `dev` -- the active integration branch. Your feature branches merge here via PR.
- Feature branches -- where you do your work. Always create them from an up-to-date `dev`:

```bash
git checkout dev
git pull
git checkout -b feature/issue-NUMBER-short-desc
```

Name branches after the issue they address: `feature/issue-24-linting`, `feature/issue-6-store-count-fix`.

### Commit message rules

1. Use imperative mood: "Add linting config" not "Added linting" or "linting stuff"
2. Reference the issue number: "Fix store count bug (#6)"
3. One logical change per commit -- if you did two things, make two commits

Good: `Add flake8 configuration and pre-commit hook (#4)`

Bad: `fixed stuff`, `updates`, `WIP`

</details>

<details id="pull-requests" class="section-card" markdown="1">
<summary>Pull Requests</summary>

A Pull Request (PR) is a proposal to merge your feature branch into `dev`. It stays open for review before anything is merged, giving your instructor a chance to leave feedback and approve the work.

**Reviewer:** Assign Abanish.

**Assignee:** Assign yourself.

### PR Title Format

Write the title in imperative mood and reference the issue number.

Good: `Add linting configuration (#4)`

Bad: `linting stuff`, `WIP`, `updates`

### Description Template

Use this template for every PR description:

```
**What this PR does:**
[1-2 sentences describing the change]

**Issue reference:**
Closes #N

**How to test it:**
1.
2.
3.

**Checklist:**
- [ ] Self-reviewed the diff
- [ ] All checklist items in the issue are complete
- [ ] No unrelated changes included
```

Fill out every field before requesting review. An incomplete description delays the review cycle for everyone on the team.

</details>

