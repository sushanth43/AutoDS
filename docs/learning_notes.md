# AutoDS - Learning Notes

---

# Table of Contents

## Phase 0 – Product Design
- Step 0.5 – Project Vision

## Phase 2 – Configuration & Logging
- Step 2.1 – Configuration Management
- Step 2.2 – Implementing the Configuration Module
- Step 2.3 – Python Modules & Packages
    - Part 2.3.1 – Python Modules
    - Part 2.3.2 – Python Packages
    - Part 2.3.3 – Understanding __init__.py
    - Part 2.3.4 – How Python Imports Work

---

# PHASE 0 – PRODUCT DESIGN

---

## Step 0.5 – Project Vision

### Status

✅ Completed

---

## Learning Objectives

After completing this step, you should understand:

- Why AutoDS is being developed.
- The long-term vision of the project.
- The difference between Version 1 and future versions.
- The target users of the application.
- The technology stack chosen for development.
- The overall workflow of the application.

---

## Project Vision

AutoDS (Autonomous Data Scientist) is a professional machine learning application designed to automate the complete data science workflow.

Instead of requiring users to manually perform every machine learning task, AutoDS will automatically perform each stage of the workflow and generate useful insights.

The project is being built with two major goals:

1. To serve as a production-quality portfolio project demonstrating software engineering and machine learning skills.
2. To simulate the workflow followed by professional Data Scientists and Machine Learning Engineers.

---

## Version 1 Scope

Version 1 focuses entirely on building a complete autonomous data science platform.

Major capabilities include:

- CSV Upload
- Dataset Validation
- Data Profiling
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Automatic Machine Learning
- Model Comparison
- Explainable AI (SHAP)
- Interactive Dashboard
- PDF Report Generation
- FastAPI Prediction API

The objective is to create a stable and professional foundation before introducing advanced AI features.

---

## Future Vision

After Version 1 is completed, future versions of AutoDS will introduce:

- AI Chat Assistant
- Multi-Agent Architecture
- Docker Deployment
- MLflow Integration
- Authentication System
- Enterprise Features

These additions will extend the platform without requiring changes to the core machine learning engine.

---

## Target Users

AutoDS is primarily designed for:

- Data Scientists
- Machine Learning Engineers

However, the interface will remain simple and intuitive so that students and beginners can also use the platform effectively.

---

## Technology Stack

Version 1 will use:

- Python
- Pandas
- NumPy
- Plotly
- Scikit-learn
- SHAP
- Streamlit
- FastAPI
- Pytest
- Git
- GitHub

These technologies are widely used in the data science industry and are free, mature, and well supported.

---

## High-Level Workflow

The overall workflow of AutoDS is:

User
↓
Upload Dataset
↓
Data Validation
↓
Data Profiling
↓
Data Cleaning
↓
Feature Engineering
↓
Automatic Model Training
↓
Model Evaluation
↓
Explainability
↓
Dashboard
↓
Prediction API

This modular workflow ensures that each stage performs one well-defined responsibility.

---

## Key Takeaways

- AutoDS is being built as a professional autonomous data science platform.
- Version 1 focuses on the complete machine learning pipeline.
- Future versions will introduce conversational AI and advanced engineering features.
- The project follows a modular architecture to improve maintainability and scalability.

---

# PHASE 2 – CONFIGURATION & LOGGING

---

# Step 2.1 – Configuration Management

### Status

✅ Completed

---

## Learning Objectives

After completing this step, you should understand:

- What Configuration Management is.
- Why configuration should be separated from business logic.
- How professional software stores project settings.
- How AutoDS implements configuration management.

---

## What is Configuration Management?

Configuration Management is the practice of storing all project settings in one central location instead of hardcoding them throughout the application's source code.

Configuration defines **how the application behaves**, while business logic defines **what the application does**.

---

## Why is Configuration Management Important?

Imagine a project containing hundreds of Python files.

Suppose every file contains:

```python
test_size = 0.2
```

Later, the testing ratio changes to 30%.

Every file would need to be edited manually.

This creates several problems:

- Duplicate values
- Higher maintenance effort
- Increased possibility of mistakes
- Difficult debugging

Professional software avoids this by storing configuration in one dedicated module.

---

## Real-Life Analogy

Think of your smartphone.

The Settings application contains:

- Brightness
- Language
- Wallpaper
- Wi-Fi
- Notifications

Changing these settings changes how the phone behaves without changing the operating system itself.

Configuration files serve the same purpose in software projects.

---

## Configuration vs Business Logic

### Configuration

Defines settings such as:

- Project Name
- Version
- Random Seed
- Test Size
- Supported File Types

These values control the behaviour of the application.

---

### Business Logic

Defines operations performed by the application.

Examples:

- Cleaning data
- Training machine learning models
- Generating reports
- Creating visualizations

---

## Practical Implementation in AutoDS

AutoDS maintains a dedicated configuration module:

configs/
└── config.py

Initially it stores:

- PROJECT_NAME
- PROJECT_VERSION
- TEST_SIZE
- RANDOM_STATE
- SUPPORTED_FILE_TYPES

Every module imports these values instead of redefining them.

---

## Advantages

- Centralized settings
- Easier maintenance
- Better scalability
- Reduced duplication
- Improved readability
- Professional architecture

---

## Key Takeaways

- Configuration controls behaviour.
- Business logic performs tasks.
- Configuration should always be centralized.

---

# Step 2.2 – Implementing the Configuration Module

### Status

✅ Completed

---

## Objective

Implement the first centralized configuration module for AutoDS.

---

## Module Created

configs/
└── config.py

The module contains project-wide settings such as:

- PROJECT_NAME
- PROJECT_VERSION
- RANDOM_STATE
- TEST_SIZE
- SUPPORTED_FILE_TYPES

---

## Module Docstring

Every Python module should begin with a module docstring describing:

- Purpose
- Responsibility
- Contents

This improves readability and maintainability.

---

## Key Takeaways

- Configuration values are stored only once.
- Every module imports configuration instead of redefining it.
- Professional projects begin modules with descriptive docstrings.

---

# Step 2.3 – Python Modules & Packages

---

## Part 2.3.1 – Python Modules

### Status

✅ Completed

---

### Definition

A Python module is simply a Python file (`.py`) containing related code.

Modules may contain:

- Variables
- Functions
- Classes
- Constants
- Documentation

---

### Purpose

Modules divide large software projects into smaller, manageable components.

Each module should ideally perform one well-defined responsibility.

---

### Real-Life Analogy

A book is divided into chapters.

Similarly, a software project is divided into modules.

Each module focuses on a specific task.

---

### Examples in AutoDS

config.py

Stores configuration.

trainer.py

Trains machine learning models.

dashboard.py

Creates the user interface.

---

### Advantages

- Better organization
- Easier maintenance
- Code reuse
- Improved readability
- Easier debugging

---

### Key Takeaways

- Every `.py` file is a module.
- Modules organize code.
- Modules should have a single responsibility.

---

## Part 2.3.2 – Python Packages

### Status

✅ Completed

---

### Definition

A Python package is a folder containing one or more Python modules.

Packages help organize related modules into logical groups.

---

### Examples

configs/

contains:

- config.py

models/

contains:

- trainer.py
- predictor.py
- evaluator.py

---

### Module vs Package

| Module | Package |
|---------|----------|
| Python file | Folder |
| Contains code | Contains modules |
| Performs tasks | Organizes modules |

---

### Advantages

- Better organization
- Logical grouping
- Easier navigation
- Improved scalability

---

### Key Takeaways

- Modules perform tasks.
- Packages organize modules.

---

## Part 2.3.3 – Understanding __init__.py

### Status

✅ Completed

---

### Definition

`__init__.py` is a special Python file placed inside a package.

Historically, it identified folders as Python packages.

Although modern Python supports namespace packages, professional projects still commonly include it.

---

### Uses

- Marks a package.
- Executes initialization code.
- Simplifies imports.
- Controls package behaviour.

---

### AutoDS Implementation

Every package inside AutoDS will contain an `__init__.py` file.

---

### Key Takeaways

- `__init__.py` is a special module.
- It improves clarity and compatibility.
- Professional Python projects continue to use it.

---

## Part 2.3.4 – How Python Imports Work

### Status

✅ Completed

---

### How Python Finds Modules

Python searches for imported modules using a list of directories called:

sys.path

Python searches only these locations rather than the entire computer.

---

### Why ModuleNotFoundError Occurred

Initially, AutoDS was executed using:

python src/main.py

Python treated `src` as the starting point and could not locate the sibling `configs` package.

The issue was resolved by executing:

python -m src.main

This runs the application as a module within the project structure, allowing imports to resolve correctly.

---

### Key Takeaways

- Python searches modules using `sys.path`.
- The execution method affects imports.
- `python -m` is the recommended approach for structured projects.