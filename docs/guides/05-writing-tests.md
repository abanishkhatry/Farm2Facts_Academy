---
layout: default
title: "Guide: Writing Tests"
---

# Guide: Writing Your First Tests

## Context

The FEAST codebase has zero test coverage. This guide walks you through setting up pytest and writing tests for the pure functions in `household.py`. These are the easiest functions to test because they have no external dependencies (no database, no network, no filesystem).

> **Beyond this project:** Writing tests forces you to think about boundaries: what inputs break the function? When does behavior change? This same edge-case thinking is how you scope any open-ended problem: a feature has edge cases, a performance problem has boundary conditions, a user complaint has special cases.

## Before You Start

- [ ] Read `food_access_model/abm/household.py` thoroughly
- [ ] Understand what `has_resources()`, `get_monthly_trip_count()`, `get_color()`, and `rating_evaluation()` do
- [ ] Branch: `feature/first-tests`

## Steps

### 1. Set up pytest

```bash
uv add --dev pytest pytest-asyncio mutmut
```

Create the test directory:
```
tests/
  __init__.py
  conftest.py
  test_household.py
```

### 2. Write tests for `has_resources()` (line 169)

This function returns `False` if the household lacks resources based on income and household size. Read it carefully:

```python
def has_resources(self) -> bool:
    if self.income < 10000:
        return False
    if self.household_size >= 2 and self.income < 15000:
        return False
    if self.household_size >= 3 and self.income < 25000:
        return False
    return True
```

Test cases to write:
- `income=5000, household_size=1` -> `False` (below 10k floor)
- `income=12000, household_size=1` -> `True` (above 10k, size 1 has no further threshold)
- `income=12000, household_size=2` -> `False` (below 15k for size 2+)
- `income=20000, household_size=3` -> `False` (below 25k for size 3+)
- `income=25001, household_size=3` -> `True` (above all thresholds)

Edge cases:
- Exact boundary: `income=10000` - is it `<` or `<=`?
- Exact boundary: `income=15000, household_size=2`
- Exact boundary: `income=25000, household_size=3`

Note: You'll need to create a Household instance to test these methods. You may need to mock or simplify the constructor since it requires a Mesa model. Figure out the minimal setup needed.

### 3. Write tests for `get_monthly_trip_count()` (line 178)

Three paths:
- Has resources + has vehicles -> 7
- Has resources + no vehicles -> 8
- No resources -> 6

### 4. Write tests for `get_color()` (line 57)

This converts an MFAI score to a hex color. Test:
- `mfai=40` -> should be reddish (low access)
- `mfai=70` -> should be greenish (high access)
- `mfai=100` -> should be very green
- Boundary at `normalized=0.5` (where red transitions to green)

Verify the hex output is a valid color string matching `#rrggbb` format.

### 5. Run the tests

```bash
uv run pytest tests/ -v
```

### 6. Run mutation testing

Mutation testing verifies your tests actually catch bugs. It makes small changes to the code (mutations) and checks if your tests fail. If a mutation survives (tests still pass), your tests have a gap.

```bash
uv run mutmut run --paths-to-mutate=food_access_model/abm/household.py
uv run mutmut results
```

If mutations survive, add test cases to kill them.

## LLM Usage

- You CAN ask (after writing your tests): "I wrote tests for a function that classifies household resources based on income and household size thresholds at 10k/15k/25k. What edge cases might I be missing?"
- You CAN ask: "How do I create a minimal Household instance for testing without a full Mesa model?"
- You should NOT ask: "Write tests for has_resources()"

## Definition of Done

- [ ] pytest runs and passes
- [ ] Tests cover `has_resources()`, `get_monthly_trip_count()`, `get_color()`
- [ ] At least one edge case per function (boundary values)
- [ ] Mutation testing run; any surviving mutants documented or killed
- [ ] PR opened with test plan in description

## While You're In There

- File issues for any behavior in household.py that seems wrong or surprising
- Note functions that are hard to test because of dependencies (these are candidates for refactoring)

## Stretch Goals

- Write tests for `chance_of_choosing_spm()` (5 return paths)
- Write tests for `stores_with_1_miles()` (requires mocking distances_map)
- Write tests for `get_mfai()` (statistical: run many times, verify score range)
- Add pytest to the CI workflow
