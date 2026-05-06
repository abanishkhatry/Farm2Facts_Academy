# Guide: Optimizing the Step Function

**Related issue**: #74

## Context

Every time `household.step()` is called, the function iterates over all stores multiple times per household. With thousands of households and hundreds of stores, this adds up. The goal is to consolidate into fewer passes without changing results.

## Before You Start

- [ ] Read `household.py`: `step()`, `calculate_distances()`, `get_closest_cspm()`, `get_closest_spm()`, `stores_with_1_miles()`
- [ ] Count how many times each household iterates over all stores in a single step
- [ ] Branch: `feature/issue-74-optimize-step`

## Steps

### 1. Audit the current store iterations

In a single call to `step()`, a household iterates all stores in:
1. `calculate_distances()` - builds `distances_map` (all stores)
2. `get_closest_spm()` - iterates all stores, filters supermarkets
3. `get_closest_cspm()` (called inside `get_mfai()`) - iterates all stores, filters non-supermarkets
4. `stores_with_1_miles()` - iterates all stores via `distances_map`

That's at least 4 full passes over the store list per household per step.

### 2. Write a spec BEFORE coding

Post this in the issue comments:

"I propose consolidating store iteration into a single pass that computes:
- `distances_map` (all store distances)
- `closest_spm` and `spm_distance` (closest supermarket)
- `closest_cspm` and `cspm_distance` (closest non-supermarket)
- `stores_within_1_mile` count

This reduces from O(4*S) to O(S) per household, where S = number of stores. The `get_closest_spm()`, `get_closest_cspm()`, and `stores_with_1_miles()` functions either get merged into the single pass or rewritten to read from pre-computed values."

### 3. Write tests for CURRENT behavior first

Before changing anything, capture the current behavior in tests:
- For a known set of stores and a household at a known location, record:
  - What `get_closest_spm()` returns
  - What `get_closest_cspm()` returns
  - What `stores_with_1_miles()` returns
  - What `get_mfai()` returns (run multiple times, check range)

These tests must still pass after your optimization.

### 4. Implement the optimization

Write a single method (e.g., `_compute_store_metrics()`) that iterates stores once and computes all needed values. Then update `step()` to call it.

### 5. Verify identical results

Run your before-tests. They should pass with unchanged results.

## LLM Usage

- You CAN ask (after writing your spec): "I want to optimize a function that iterates stores 4 times per household. Ask me questions about my approach." Let the LLM push back on edge cases.
- You CAN ask: "What's the most efficient way to find the min of a filtered subset while iterating?"
- You should NOT ask: "Rewrite the step function to be faster"

## Definition of Done

- [ ] Spec posted in issue comments before coding
- [ ] Tests for current behavior written and passing
- [ ] Optimization implemented
- [ ] Tests still pass with identical results
- [ ] PR opened with before/after comparison (how many iterations saved)

## Stretch Goals

- Benchmark the before and after with `time.time()` on a real dataset
- Consider whether `distances_map` could use a spatial index (STRtree from shapely) for even faster nearest-neighbor lookups
