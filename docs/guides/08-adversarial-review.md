---
layout: default
title: "Guide: Adversarial Code Review"
---

# Guide: Adversarial LLM Code Review

## Context

Starting in week 3, every PR gets both a human peer review and an adversarial LLM review. The LLM review must be done by a different student than the author, in a fresh session (no context from the author's work). This breaks confirmation bias and builds critical evaluation skills.

## Before You Start

- [ ] You have a PR to review (assigned by the team)
- [ ] You've read the PR description and linked issue
- [ ] You have the diff (either via GitHub or `git diff`)

## Steps

### 1. Open a FRESH Claude Code session

Do not use the same session that helped write the code. Start clean.

### 2. Provide context

Give the LLM:
- The diff (paste it or point to the files)
- The spec or issue description
- Any relevant ADR

### 3. Use this prompt structure

```
Review this change against the following spec:

[paste the issue description or spec]

Here is the diff:

[paste the diff]

Be skeptical. Your job is to find:
- Spec violations: Does this actually do what it claims?
- Edge cases that aren't handled
- Security issues (injection, auth bypass, data exposure)
- Performance concerns: What happens at 10x scale?
- Maintainability issues: Would this confuse a new developer in 3 months?

Favor false positives over false negatives. I'd rather investigate
a concern that turns out to be fine than miss a real issue.
```

### 4. Evaluate each finding

For each issue the LLM raises, you (the reviewer) must decide:

**Valid**: The LLM found a real problem. Post it as a PR comment with your explanation of why it matters. Request changes.

**False positive**: The LLM raised something that isn't actually a problem. Post it as a PR comment explaining why it's not an issue. This is where the learning happens. Examples:
- "The LLM flagged SQL injection risk, but this query uses parameterized queries ($1, $2), so it's safe."
- "The LLM suggested adding null checks, but this value is guaranteed non-null by the caller (see line X)."

> **Beyond this project:** Notice you can't just say "false positive." You have to explain why, citing specific evidence. This is how professional feedback works: articulate not just what you think, but why you think it. The skill of explaining your reasoning with evidence transfers to every collaborative setting.

### 5. Post your findings on the PR

Format each finding as:

```markdown
**[Valid/False Positive]** - [One-line summary]

LLM finding: [what the LLM said]

My evaluation: [why this is or isn't a real issue]
```

## Rotating Review Perspectives

Different PRs benefit from different review lenses. Try a different one each time:

| Perspective | Prompt Addition |
|-------------|----------------|
| **Correctness** | "Focus on logic errors and spec violations. What inputs could produce wrong results?" |
| **Security** | "Focus on OWASP Top 10 risks. Check for injection, missing validation, data exposure." |
| **Performance** | "Focus on time/space complexity. What happens with 50k households and 500 stores?" |
| **Maintainability** | "Focus on readability. If a new developer read this in 3 months, what would confuse them?" |

## LLM Usage

This guide IS about using the LLM. The key discipline is:
- Fresh session (no context from the author's work)
- YOU evaluate every finding (don't just forward the LLM's output as your review)
- Document your reasoning for both valid and false positive findings

## Common Pitfalls

- **Rubber-stamping LLM output**: Don't just copy-paste LLM findings into the PR. Evaluate each one.
- **Dismissing everything**: If you mark everything as false positive, you're not engaging critically.
- **Using the author's session**: The whole point is independent review. Start fresh.
