# Refactoring Backlog

---

## Purpose

This document tracks architectural improvements, refactoring ideas, and technical debt identified during the development of AutoDS.

These items are **not bugs** and **do not block development**. Instead of interrupting progress, they are documented here and will be reviewed at major project milestones or before the Version 1 release.

---

# Status Legend

- Deferred
- In Progress
- Completed
- Cancelled

---

# Priority Levels

- High
- Medium
- Low

---

# R001 – Configuration-Driven Dataset Path

**Phase Found:** Phase 3

**Category:** Future Enhancement

**Priority:** Medium

### Current Design

The dataset path is defined in `config.py`.

### Improvement

Allow users to upload datasets through the dashboard instead of relying on a fixed dataset path.

### Status

Deferred

---

# R002 – Separate Validation Logic from Validation Reporting

**Phase Found:** Phase 4

**Category:** Architecture

**Priority:** Medium

### Current Design

`DataValidator` performs validation and prints the validation report.

### Improvement

Return structured validation results and delegate report generation to a dedicated `ValidationReport` class.

### Benefits

- Better separation of responsibilities
- Easier testing
- Consistent architecture with EDA reporting

### Status

Deferred

---

# R003 – Improve Missing Value Strategy Selection

**Phase Found:** Phase 6

**Category:** Code Quality

**Priority:** Medium

### Current Design

```python
if strategy == "mean":
    ...
elif strategy == "median":
    ...
elif strategy == "mode":
    ...
elif strategy == "constant":
    ...
```

### Improvement

Replace the conditional chain with a strategy mapping or Strategy Design Pattern to simplify future extensions.

### Status

Deferred

---

# R004 – Separate Strategy Selection from Cleaning Logic

**Phase Found:** Phase 6

**Category:** Architecture

**Priority:** Medium

### Current Design

`handle_missing_values()` both selects the strategy and performs the cleaning.

### Improvement

Split strategy selection and cleaning into separate methods to improve readability and maintainability.

### Status

Deferred

---

# R005 – Validate Strategy and Column Compatibility

**Phase Found:** Phase 6

**Category:** Robustness

**Priority:** High

### Current Design

Users can explicitly select incompatible columns for a strategy.

Example:

```python
columns=["Name"]
strategy="mean"
```

### Improvement

Validate compatibility between selected columns and the chosen strategy before applying any cleaning operation.

### Benefits

- Better error handling
- Prevents runtime exceptions
- Improves user experience

### Status

Deferred

---

# Review Schedule

The refactoring backlog will be reviewed at the following milestones:

- After Phase 8 (Feature Engineering)
- Before Phase 15 (Documentation & Optimization)
- Before Version 1 Release

---

# Development Rule

If an improvement does not affect correctness or block progress, it should be documented in this backlog instead of interrupting the current phase of development.

---

# R006 – Cleaning Summary Report

**Phase Found:** Phase 6

**Category:** Maintainability

**Priority:** Medium

### Current Design

Each cleaning method logs its actions independently.

### Improvement

Maintain a cleaning history inside `DataCleaner` and generate a consolidated cleaning summary report after all cleaning operations are completed.

### Benefits

- Centralized cleaning summary
- Easier debugging
- Better transparency
- Can later be exported to HTML/PDF

### Status

Deferred