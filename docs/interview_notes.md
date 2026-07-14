# AutoDS - Interview Notes

---

# Table of Contents

## Phase 0 – Product Design
- Step 0.5 – Project Vision

## Phase 2 – Configuration & Logging
- Step 2.1 – Configuration Management
- Step 2.2 – Configuration Module
- Step 2.3 – Python Modules & Packages
    - Part 2.3.1 – Python Modules
    - Part 2.3.2 – Python Packages
    - Part 2.3.3 – Understanding __init__.py
    - Part 2.3.4 – Python Imports

---

# PHASE 0 – PRODUCT DESIGN

---

## Step 0.5 – Project Vision

---

### Question 1

**What is AutoDS?**

### Answer

AutoDS (Autonomous Data Scientist) is an end-to-end machine learning platform that automates the complete data science workflow. It allows users to upload a dataset, automatically preprocess it, perform exploratory data analysis, engineer features, train multiple machine learning models, compare their performance, explain predictions, and generate reports through an interactive dashboard.

---

### Question 2

**Why did you choose to build AutoDS?**

### Answer

I wanted to build a project that combines Machine Learning, Software Engineering, Data Engineering, Explainable AI, API Development, and Deployment into one production-style application.

Instead of creating isolated machine learning notebooks, AutoDS demonstrates the complete lifecycle of an ML application.

---

### Question 3

**Who are the target users of AutoDS?**

### Answer

The primary target users are:

- Data Scientists
- Machine Learning Engineers

However, the interface is designed to remain simple enough for students and beginners.

---

### Question 4

**Why are advanced AI features not included in Version 1?**

### Answer

Version 1 focuses on building a strong and stable machine learning engine first.

Features like conversational AI, multi-agent systems, and enterprise capabilities can be built on top of this foundation in future versions without redesigning the core architecture.

---

### Interview Tip

Interviewers often ask project-related questions to evaluate:

- Problem-solving ability
- Software architecture thinking
- Decision-making skills
- Long-term planning

---

# PHASE 2 – CONFIGURATION & LOGGING

---

# Step 2.1 – Configuration Management

---

### Question 1

**What is Configuration Management?**

### Answer

Configuration Management is the practice of storing project-wide settings in a centralized location instead of hardcoding them throughout the application.

It separates configuration from business logic, making software easier to maintain and update.

---

### Question 2

**What is the difference between Configuration and Business Logic?**

### Answer

Configuration defines how the application behaves.

Examples:

- Test Size
- Random Seed
- Project Name

Business Logic defines what the application does.

Examples:

- Data Cleaning
- Feature Engineering
- Model Training
- Report Generation

---

### Question 3

**Why should configuration be centralized?**

### Answer

Centralizing configuration:

- Eliminates duplicate values.
- Simplifies maintenance.
- Prevents inconsistent behavior.
- Improves scalability.
- Makes future modifications easier.

---

### Question 4

**Can you give examples of configuration values?**

### Answer

Examples include:

- Project Name
- Version Number
- Random Seed
- Test Size
- Logging Level
- Supported File Types

---

### Interview Tip

A common mistake is confusing configuration with application logic.

Configuration controls behavior.

Business Logic performs operations.

---

# Step 2.2 – Configuration Module

---

### Question 1

**Why did you create a separate `config.py` file?**

### Answer

The configuration module provides a single source of truth for project-wide settings.

Instead of redefining configuration values throughout the project, every module imports them from `config.py`.

---

### Question 2

**Why should Python modules begin with a docstring?**

### Answer

Module docstrings explain:

- Purpose
- Responsibility
- Contents

They improve readability and make large projects easier to maintain.

---

# Step 2.3 – Python Modules & Packages

---

## Part 2.3.1 – Python Modules

---

### Question 1

**What is a Python Module?**

### Answer

A Python module is a Python file (`.py`) containing related code such as variables, functions, classes, and constants.

Modules help organize software into smaller, manageable units.

---

### Question 2

**Why do we use modules?**

### Answer

Modules improve:

- Code organization
- Reusability
- Readability
- Debugging
- Maintainability

---

### Question 3

**Can a module contain classes and functions together?**

### Answer

Yes.

A module can contain:

- Variables
- Constants
- Functions
- Classes
- Documentation

---

## Part 2.3.2 – Python Packages

---

### Question 1

**What is a Python Package?**

### Answer

A Python package is a folder containing one or more Python modules.

Packages organize related modules into logical groups.

---

### Question 2

**What is the difference between a Module and a Package?**

### Answer

| Module | Package |
|---------|----------|
| Python file | Folder |
| Contains code | Contains modules |
| Performs tasks | Organizes related functionality |

---

### Question 3

**Can a package contain another package?**

### Answer

Yes.

Packages can contain sub-packages, allowing large applications to maintain a clean and scalable structure.

---

## Part 2.3.3 – Understanding `__init__.py`

---

### Question 1

**What is `__init__.py`?**

### Answer

`__init__.py` is a special Python file placed inside a package.

Historically, it identified the folder as a package.

Today, although Python supports namespace packages, it is still commonly used for clarity, compatibility, and package initialization.

---

### Question 2

**Is `__init__.py` mandatory in modern Python?**

### Answer

No.

Modern Python (3.3+) supports namespace packages.

However, professional projects still commonly include `__init__.py`.

---

### Question 3

**What else can `__init__.py` do besides marking a package?**

### Answer

It can:

- Execute initialization code.
- Re-export modules.
- Simplify imports.
- Control package behavior.

---

## Part 2.3.4 – Python Imports

---

### Question 1

**How does Python find imported modules?**

### Answer

Python searches for modules using directories listed in `sys.path`.

It does not search the entire computer.

---

### Question 2

**What causes `ModuleNotFoundError`?**

### Answer

Common causes include:

- Incorrect project structure.
- Wrong execution location.
- Missing modules.
- Incorrect import statements.
- Python not searching the correct directory.

---

### Question 3

**Why did `python src/main.py` fail but `python -m src.main` work?**

### Answer

`python src/main.py` executes the file as an isolated script.

`python -m src.main` executes the module as part of the project package, allowing Python to correctly resolve imports using the project structure.

---

### Question 4

**What is `sys.path`?**

### Answer

`sys.path` is a list of directories that Python searches when resolving import statements.

---

# Common Interview Questions (Quick Revision)

- What is a Python module?
- What is a Python package?
- Difference between a module and a package?
- What is `__init__.py`?
- Is `__init__.py` mandatory?
- What is Configuration Management?
- Difference between Configuration and Business Logic?
- What is `sys.path`?
- Why do we use `python -m`?
- What causes `ModuleNotFoundError`?

---

# Phase 2 – Configuration & Logging

# Step 2.4 – Environment Variables

---

## Question 1

**What are Environment Variables?**

### Answer

Environment Variables are values stored outside the application's source code that are made available to the application at runtime.

They are commonly used to store sensitive information such as API keys, passwords, and database credentials.

---

## Question 2

**Why should API keys not be hardcoded?**

### Answer

Hardcoding API keys exposes sensitive credentials if the source code is uploaded to GitHub.

This can lead to unauthorized access, quota exhaustion, and security risks.

---

## Question 3

**What is the difference between Configuration and Environment Variables?**

### Answer

Configuration controls how the application behaves and is generally safe to commit to the repository.

Environment Variables store secrets or machine-specific information and should never be committed to version control.

---

## Question 4

**What is a `.env` file?**

### Answer

A `.env` file stores Environment Variables during development.

It allows developers to keep sensitive values outside the application's source code.

---

## Question 5

**Why is `.env` added to `.gitignore`?**

### Answer

The `.env` file often contains sensitive credentials.

Adding it to `.gitignore` prevents accidental commits to GitHub.

---

## Question 6

**How do you access Environment Variables in Python?**

### Answer

Using the `os` module.

Example:

```python
import os

API_KEY = os.getenv("API_KEY")
```

---

## Question 7

**What is `python-dotenv`?**

### Answer

`python-dotenv` is a Python package that loads Environment Variables from a `.env` file into the application's runtime environment.

---

## Interview Tip

A common interview question is:

> "Where would you store an API key?"

The expected answer is:

> "In an Environment Variable, not inside the source code."

---

# Phase 2 – Configuration & Logging

# Step 2.5 – Logging System

---

## Question 1

**What is logging?**

### Answer

Logging is the process of recording application events while a program is running.

It helps developers monitor, debug, and maintain software.

---

## Question 2

**Why is logging preferred over `print()`?**

### Answer

Logging provides:

- Timestamps
- Severity levels
- Permanent log files
- Better debugging
- Production monitoring

Unlike `print()`, logs can be stored and reviewed later.

---

## Question 3

**What are the main logging levels?**

### Answer

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Each level represents a different severity of application events.

---

## Question 4

**Why should logging be configured only once?**

### Answer

Centralizing logging ensures consistent formatting, avoids duplicate configuration, and allows every module to reuse the same logger.

---

## Question 5

**Why was the log file name stored in `config.py`?**

### Answer

The log file name is a configuration value.

Keeping it inside `config.py` follows the principle of separating configuration from implementation and makes future changes easier.

---

## Interview Tip

A common interview question is:

> "When would you use logging instead of `print()`?"

A good answer is:

> "`print()` is useful for quick debugging during development, whereas logging is the standard solution for recording application events in production software."


---

# Phase 2 – Configuration & Logging

# Step 2.6 – Error Handling

---

## Question 1

**What is an exception?**

### Answer

An exception is an event that interrupts the normal execution of a program due to an unexpected error or condition.

---

## Question 2

**Why do we use custom exceptions?**

### Answer

Custom exceptions make project-specific errors easier to understand, improve debugging, and provide meaningful error messages.

---

## Question 3

**Why create a base exception class?**

### Answer

A base exception provides a common parent for all project-specific exceptions, making error handling consistent across the application.

---

## Question 4

**What is the difference between built-in and custom exceptions?**

### Answer

Built-in exceptions are provided by Python.

Custom exceptions are created by developers to represent application-specific errors.

---

## Interview Tip

Interviewers often ask:

> "Why not just use Exception everywhere?"

A good answer is:

> "Custom exceptions improve readability, debugging, maintainability, and make project-specific failures easier to identify."

---

# Step 2.7 – Utility Modules

---

## Question 1

**What is a utility module?**

### Answer

A utility module contains reusable helper functions that can be shared across multiple parts of an application.

---

## Question 2

**Why shouldn't business logic be placed inside utility modules?**

### Answer

Business logic belongs in feature-specific modules.

Utility modules should contain only generic helper functions that are reusable throughout the application.

---

## Question 3

**What is the YAGNI principle?**

### Answer

YAGNI stands for "You Aren't Gonna Need It."

It encourages developers to implement functionality only when it is actually required rather than anticipating future needs.

---

## Interview Tip

Using the YAGNI principle demonstrates an understanding of clean software design and helps avoid unnecessary complexity.

---

# Phase 3 – Data Ingestion

---

## Question 1

**What is Data Ingestion?**

### Answer

Data Ingestion is the process of importing data from external sources into an application for further processing.

---

## Question 2

**Why create a DataLoader class instead of directly using `pd.read_csv()`?**

### Answer

Using a DataLoader centralizes data loading, validation, logging, and error handling, making the application easier to maintain and extend.

---

## Question 3

**Why should datasets be validated before loading?**

### Answer

Validation ensures that:

- The file exists.
- The file type is supported.

This prevents unnecessary runtime errors.

---

## Question 4

**Why return a Pandas DataFrame?**

### Answer

The DataFrame is Pandas' primary data structure and provides powerful functionality for data manipulation, cleaning, visualization, and machine learning.

---

## Question 5

**What responsibilities should a DataLoader have?**

### Answer

A DataLoader should:

- Validate input files.
- Read datasets.
- Handle errors.
- Log operations.
- Return structured data.

---

## Interview Tip

A common interview discussion is:

> "Why design a DataLoader class when Pandas already provides `read_csv()`?"

A strong answer is:

> "Because the DataLoader encapsulates validation, logging, configuration, and error handling, keeping the rest of the application independent of file-loading details."