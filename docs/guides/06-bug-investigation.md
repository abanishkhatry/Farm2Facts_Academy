# Guide: Investigating and Fixing a Bug

**Related issue**: #47 (Stores within 1 Mile logic)

## Context

Issue #47 reports that after running a simulation step, all households appear to have the same number of stores within 1 mile. This guide walks through how to investigate and fix a bug using a test-first approach.

## Before You Start

- [ ] Read `food_access_model/abm/household.py`, especially `stores_with_1_miles()` (line 131), `calculate_distances()` (line 246), and `step()` (line 259)
- [ ] Understand how `distances_map` is populated and used
- [ ] Branch: `feature/issue-47-stores-within-mile`

## Steps

### 1. Understand before you fix

Read `stores_with_1_miles()`:
```python
def stores_with_1_miles(self) -> int:
    total = 0
    for store in self.model.stores_list:
        distance = self.distances_map[store.unique_id]
        if distance <= 1.0:
            total += 1
    self.rating_evaluation(total)
    return total
```

It iterates all stores, checks `distances_map` for each, counts those within 1.0 mile.

### 2. Form a hypothesis

When is `distances_map` populated? Look at `calculate_distances()` (line 246) and where it's called in `step()` (line 263):

```python
def step(self) -> None:
    if self.distances_map is None:
        self.calculate_distances()
```

`distances_map` is only calculated if it's `None`. After step 0, it's never `None` again, so distances are never recalculated even if stores change between steps.

Is this the bug? Or is there something else going on? Think about:
- Are all households getting the same `distances_map`?
- Is there a shared mutable state issue?
- What happens when a store is added or removed between steps?

### 3. Write a test that reproduces the bug BEFORE fixing it

```python
def test_stores_within_1_mile_returns_different_counts_for_different_households():
    """Two households at different locations should see different store counts."""
    # Set up two households with different distances_map values
    # Assert they return different counts from stores_with_1_miles()
    ...
```

This test should FAIL with the current code if the bug is real. If it passes, your hypothesis is wrong and you need to dig deeper.

### 4. Investigate further if needed

Ask yourself:
- Does `distances_map` need to be recalculated when stores are added or removed between steps?
- Is the `step()` function re-using a stale `distances_map`?
- Are all households sharing the same `distances_map` instance somehow?

### 5. Write the fix

Once you understand the root cause, fix it. Your reproducing test should now pass.

### 6. Write additional tests

- Different households at different distances from stores -> different counts
- A household with all stores beyond 1 mile -> count of 0
- A household with all stores within 1 mile -> count equals total stores
- Exact boundary: store at exactly 1.0 miles (is it `<=` or `<`?)

## LLM Usage

- You CAN describe the bug and your hypothesis to the LLM and ask: "What else could cause all households to report the same store count?"
- You CAN ask: "How would I set up a minimal test fixture for a Household with a known distances_map?"
- You should NOT ask: "Fix this bug for me"

## Definition of Done

- [ ] Root cause identified and documented in the issue
- [ ] Reproducing test written (fails before fix, passes after)
- [ ] Fix implemented
- [ ] Additional edge case tests written
- [ ] PR opened with explanation of root cause in description

## While You're In There

- Is the distance comparison correct? `<= 1.0` miles, but `calculate_distances()` divides by `METERS_IN_MILE = 1609.34`. Is that right?
- File issues for any other suspicious logic you find in the step flow
