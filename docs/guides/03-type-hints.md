---
layout: default
title: "Guide: Adding Type Hints"
---

# Guide: Adding Type Hints and Docstrings

**Related issues**: #18, #19, #20

## Context

The FEAST codebase has inconsistent type hints. Some files use modern syntax, some use older `typing` imports, and some have no hints at all. Adding type hints improves readability, catches bugs via static analysis, and helps the next developer understand each function's contract.

## Before You Start

- [ ] Read the files you're assigned to annotate
- [ ] Understand what each function takes and returns (read the callers too)
- [ ] Branch: `feature/issue-NUMBER-type-hints-MODULE`

## Steps

### 1. Read the function. Understand it before annotating it.

Don't just look at the signature. Read the body. Read who calls it. What types actually flow through?

### 2. Add parameter and return type hints

Use modern Python syntax (3.10+):

```python
# Before
def has_resources(self):
    if self.income < 10000:
        return False

# After
def has_resources(self) -> bool:
    if self.income < 10000:
        return False
```

### 3. Use modern syntax consistently

| Old Style | Modern Style |
|-----------|-------------|
| `Optional[str]` | `str \| None` |
| `List[Dict]` | `list[dict]` |
| `Tuple[int, str]` | `tuple[int, str]` |
| `Dict[str, Any]` | `dict[str, Any]` |

Remove `from typing import List, Dict, Optional, Tuple` imports when no longer needed. Keep `Any`, `TypedDict`, `Callable` if used.

### 4. Use TypedDict for known dict structures

If a dict always has the same keys, define a TypedDict:

```python
from typing import TypedDict

class HouseholdData(TypedDict):
    id: int
    Geometry: str
    Income: float
    Household_Size: int
    Vehicles: int
```

### 5. Add docstrings only when the function name isn't self-explanatory

Skip docstrings for obvious functions like getters. Add one-line docstrings for functions with non-obvious behavior:

```python
def stores_with_1_miles(self) -> int:
    """Count stores within 1 mile using pre-computed distances_map."""
```

Don't write multi-paragraph docstrings. One line is almost always enough.

## LLM Usage

- You CAN ask: "What type does this function return?" (then verify by reading callers)
- You CAN ask: "What's the modern Python syntax for Optional[List[str]]?"
- You should NOT ask: "Add type hints to all functions in this file"

## Definition of Done

- [ ] All functions in your assigned files have parameter and return type hints
- [ ] Modern syntax used consistently (no `Optional`, `List`, `Dict` imports)
- [ ] Flake8 passes
- [ ] PR opened linking to the relevant issue

## While You're In There

Look for these and file issues:
- Functions that take `Any` but could be more specific
- Parameters with misleading names
- Dead code or unused imports
- Hardcoded values that should be constants

## Stretch Goals

- Add mypy to CI and get your assigned files to pass strict mode
- Create TypedDict definitions for the household and store data structures used throughout the codebase
