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