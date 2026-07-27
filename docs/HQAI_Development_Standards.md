# HQAI Development Standards

Version : 1.0

Project : Hanaka Quant AI

Author : Ravi Varma

---

# 1. Objective

This document defines the coding, testing, documentation and release standards for HQAI.

Every contributor must follow these standards.

---

# 2. Python Version

Python 3.12+

---

# 3. Code Formatting

PEP8

Black

isort

ruff

---

# 4. Naming Standards

## Classes

PascalCase

Example

HistoryAgent

FeatureBuilder

IndicatorRepository

---

## Functions

snake_case

Example

build_features()

load_history()

save_metadata()

---

## Variables

snake_case

history_file

feature_directory

indicator_count

---

## Constants

UPPER_CASE

DEFAULT_WINDOW

DATABASE_VERSION

MAX_RETRY

---

# 5. File Header

Every file begins with

Module Name

Purpose

Author

Version

---

# 6. Type Hints

Every public function uses type hints.

Example

def load(symbol: str) -> pd.DataFrame:

---

# 7. Logging

Never use print()

Always use

log.info()

log.warning()

log.error()

log.success()

---

# 8. Error Handling

Never ignore exceptions.

Catch expected exceptions.

Log all failures.

Raise custom exceptions.

---

# 9. Repository Pattern

Repositories never calculate.

Repositories only access DuckDB.

---

# 10. Storage Pattern

Storage classes only read/write Parquet.

No calculations.

---

# 11. Builder Pattern

Builders perform calculations.

No database access.

No file access.

---

# 12. Agent Pattern

Agents orchestrate workflows.

Download

Load

Build

Save

Update Index

Report

---

# 13. CLI Pattern

CLI only invokes agents.

CLI contains no business logic.

---

# 14. Testing

Every module requires

Unit Tests

Integration Tests

Regression Tests

Performance Tests

---

# 15. Documentation

Every public class

Every public function

Every CLI command

must have documentation.

---

# 16. Git Workflow

Feature Branch

↓

Commit

↓

Push

↓

Review

↓

Merge

---

# 17. Commit Message Format

Release X.Y.Z - Module Description

Example

Release 1.2.0 - History Engine

---

# 18. Versioning

Semantic Versioning

Major.Minor.Patch

---

# 19. Definition of Done

A task is complete only when

✔ Code

✔ Tests

✔ Documentation

✔ CLI

✔ Logging

✔ Storage

✔ Database

✔ Verification

✔ Git Commit

✔ Release Notes

---

# 20. Code Review Checklist

Architecture follows SDS

Database follows DDD

Logging implemented

Type hints complete

Tests passing

Documentation complete

Performance acceptable

No duplicated code

No hardcoded paths

No placeholder code

---

# 21. Release Checklist

Build succeeds

CLI succeeds

Database verified

Storage verified

Tests pass

Documentation updated

Git tagged

Release published