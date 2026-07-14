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

---

# Step 2.4 – Environment Variables

### Status

✅ Completed

---

## Learning Objectives

After completing this step, you should understand:

- What Environment Variables are.
- Why they are used in professional software.
- The difference between Configuration and Environment Variables.
- What a `.env` file is.
- How to load Environment Variables in Python.
- How AutoDS uses Environment Variables.

---

## Part 2.4.1 – What are Environment Variables?

### Definition

Environment Variables are values stored outside the application's source code that are made available to the application at runtime.

They are primarily used to store sensitive or machine-specific information that should not be hardcoded into the project's source code.

---

### Why are Environment Variables Needed?

If sensitive information such as API keys, passwords, or database credentials are written directly into source code, anyone with access to the repository can view them.

This creates serious security risks, especially when projects are hosted on GitHub.

Environment Variables separate sensitive information from the application's source code.

---

### Common Examples

- OpenAI API Keys
- Gemini API Keys
- Database URLs
- Database Passwords
- JWT Secrets
- Email Credentials
- AWS Credentials

---

## Part 2.4.2 – Why Environment Variables Matter

Professional applications are often deployed in multiple environments such as:

- Development
- Testing
- Production

Each environment may require different credentials or configuration values.

Instead of modifying the source code for each environment, Environment Variables allow the application to use different values while keeping the same codebase.

This improves:

- Security
- Maintainability
- Portability
- Deployment

---

## Part 2.4.3 – Configuration vs Environment Variables

### Configuration (`config.py`)

Configuration stores project settings that define how the application behaves.

Examples:

- Project Name
- Version
- Random State
- Test Size
- Supported File Types
- Logging Level

Configuration values are generally safe to store inside the repository.

---

### Environment Variables

Environment Variables store sensitive or machine-specific information.

Examples:

- API Keys
- Database Passwords
- Database URLs
- Secret Keys
- Email Passwords

These values should never be committed to GitHub.

---

### Decision Rule

When deciding where a value belongs, ask:

> "Is it safe if this value becomes public on GitHub?"

If the answer is **Yes**, it belongs in `config.py`.

If the answer is **No**, it belongs in an Environment Variable.

---

## Part 2.4.4 – `.env` Files

A `.env` file is a simple text file used to store Environment Variables during development.

Example:

```env
APP_ENV=development
DEBUG=True
```

The `.env` file should always be added to `.gitignore` so that sensitive information is never uploaded to GitHub.

---

## Part 2.4.5 – Implementing Environment Variables in AutoDS

AutoDS uses the `python-dotenv` package to load Environment Variables.

Implementation steps:

1. Install `python-dotenv`.
2. Create a `.env` file.
3. Load the file using:

```python
from dotenv import load_dotenv

load_dotenv()
```

4. Read variables using:

```python
import os

APP_ENV = os.getenv("APP_ENV")
DEBUG = os.getenv("DEBUG")
```

---

## Best Practices

- Never hardcode API keys.
- Never commit `.env` files.
- Store secrets outside the source code.
- Keep configuration and secrets separate.
- Use `.gitignore` to exclude `.env`.

---

## Key Takeaways

- Environment Variables improve application security.
- `.env` files simplify local development.
- `python-dotenv` loads Environment Variables into Python.
- Configuration and Environment Variables serve different purposes.


---

# Step 2.5 – Logging System

### Status

✅ Completed

---

## Learning Objectives

After completing this step, you should understand:

- What logging is.
- Why logging is preferred over `print()` in professional applications.
- The different logging levels.
- How to configure Python's logging module.
- How AutoDS implements logging.

---

## Part 2.5.1 – Introduction to Logging

### Definition

Logging is the process of recording important events that occur while an application is running.

Instead of displaying information only on the terminal, logging stores these events in log files, making debugging and monitoring much easier.

---

### Why Logging is Important

As software grows, applications become too large to debug using `print()` statements alone.

Logging provides:

- Timestamps
- Severity levels
- Permanent records
- Easier debugging
- Production monitoring

---

## Logging vs Print

| Print | Logging |
|--------|---------|
| Displays messages on the terminal | Displays messages and stores them in log files |
| Temporary debugging | Long-term monitoring |
| No timestamps | Includes timestamps |
| No severity levels | Supports multiple log levels |
| Not suitable for production | Standard practice in production |

---

## Logging Levels

Python provides several logging levels.

### DEBUG

Detailed information used while debugging.

### INFO

Normal application events.

Example:

- Dataset loaded
- Model training started

### WARNING

Something unexpected happened, but the application can continue.

### ERROR

An operation failed.

Example:

- Unable to read a CSV file.

### CRITICAL

A serious failure that may stop the application.

---

## AutoDS Logging Architecture

AutoDS centralizes logging inside:

```
src/logger.py
```

The logger is configured once and reused throughout the application.

Logs are stored inside:

```
logs/
    autods.log
```

---

## Configuration

The logging system uses:

- `LOG_FILE_NAME`
- `LOG_LEVEL`

These values are stored inside `config.py` instead of being hardcoded.

This follows the principle of separating configuration from implementation.

---

## Implementation

The logging system uses Python's built-in `logging` module.

Major components include:

- `logging.basicConfig()`
- `FileHandler`
- `StreamHandler`
- `logger.info()`

---

## Best Practices

- Configure logging only once.
- Reuse the same logger across the project.
- Keep log configuration centralized.
- Store log configuration inside `config.py`.
- Use meaningful log messages.

---

## Key Takeaways

- Logging is essential for professional software.
- `print()` is useful during learning but should not replace logging.
- Logging records application events permanently.
- Configuration should remain separate from implementation.

---

# Step 2.6 – Error Handling

### Status

✅ Completed

---

## Learning Objectives

After completing this step, you should understand:

- What exceptions are.
- Why applications require proper error handling.
- The difference between built-in and custom exceptions.
- How AutoDS implements centralized exception handling.

---

## Part 2.6.1 – Introduction to Error Handling

### Definition

Error handling is the process of detecting, managing, and responding to unexpected situations that occur while an application is running.

Without proper error handling, applications terminate abruptly and provide confusing error messages.

---

### Why Error Handling is Important

Professional software should fail gracefully.

Instead of allowing Python to display a long traceback, applications should:

- Detect the error
- Log the error
- Display a meaningful message
- Continue execution whenever possible

This improves debugging, maintainability, and user experience.

---

## Python Exceptions

Python raises exceptions whenever an unexpected event occurs.

Examples include:

- FileNotFoundError
- ValueError
- TypeError
- ZeroDivisionError

These exceptions help identify the exact cause of a failure.

---

## Custom Exceptions

Professional applications often define their own exceptions instead of relying entirely on Python's built-in exceptions.

Example:

```python
class AutoDSError(Exception):
    pass
```

Specific exceptions can then inherit from this base class.

Example:

```python
class DatasetNotFoundError(AutoDSError):
    pass
```

This makes error messages more meaningful and keeps the project organized.

---

## AutoDS Implementation

AutoDS centralizes custom exceptions inside:

```
src/exceptions.py
```

The project defines:

- AutoDSError
- DatasetNotFoundError

Future project-specific exceptions will inherit from `AutoDSError`.

---

## Benefits of Custom Exceptions

- Better readability
- Easier debugging
- Centralized error management
- More meaningful error messages
- Improved maintainability

---

## Best Practices

- Create custom exceptions for project-specific errors.
- Inherit from a common base exception.
- Log exceptions whenever appropriate.
- Keep exception classes focused on a single purpose.

---

## Key Takeaways

- Exceptions represent unexpected situations.
- Custom exceptions improve software quality.
- Centralized exception handling makes large projects easier to maintain.

---

# Step 2.7 – Utility Modules

### Status

✅ Completed

---

## Learning Objectives

After completing this step, you should understand:

- What utility modules are.
- Why helper functions should be centralized.
- Why AutoDS includes a utility module.

---

## What is a Utility Module?

A utility module stores reusable helper functions that may be required by multiple parts of an application.

Instead of duplicating code across several files, common functionality is implemented once and reused.

---

## AutoDS Utility Module

AutoDS contains:

```
src/utils.py
```

Initially, the file contains only a module docstring.

Helper functions will be added only when they become necessary.

Examples include:

- Reading JSON files
- Saving JSON files
- Creating directories
- Loading models
- Saving models
- Reading configuration files

---

## Why Create It Now?

Creating the utility module early establishes a dedicated location for reusable helper functions.

As the project grows, new utilities can be added without reorganizing the project structure.

---

## YAGNI Principle

AutoDS follows the software engineering principle:

**YAGNI (You Aren't Gonna Need It).**

Instead of creating helper functions in advance, utilities are implemented only when a real requirement exists.

This keeps the codebase clean and avoids unnecessary complexity.

---

## Best Practices

- Keep utility functions generic.
- Avoid placing business logic inside utility modules.
- Reuse utilities instead of duplicating code.
- Create utilities only when required.

---

## Key Takeaways

- Utility modules reduce code duplication.
- They improve maintainability.
- Following YAGNI prevents unnecessary development.

---

# Phase 3 – Data Ingestion

### Status

✅ Completed

---

# Phase Objectives

The objective of this phase was to build the first functional module of AutoDS capable of loading datasets into the application.

By the end of this phase, AutoDS can:

- Load CSV datasets.
- Validate file existence.
- Validate supported file types.
- Read datasets into Pandas DataFrames.
- Generate dataset summaries.
- Log all major operations.
- Raise custom exceptions when errors occur.

---

# Step 3.1 – Data Ingestion Overview

## What is Data Ingestion?

Data Ingestion is the process of collecting and importing data from external sources into an application for further processing.

In Version 1 of AutoDS, the supported source is:

- CSV Files

Future versions may support:

- Excel
- JSON
- SQL Databases
- APIs
- Cloud Storage

---

# Step 3.2 – Installing Pandas

## Why Pandas?

Pandas is the most widely used Python library for working with structured datasets.

It provides:

- DataFrame
- Data Cleaning
- Data Filtering
- Data Aggregation
- Statistical Analysis

Installation:

```bash
pip install pandas
```

---

# Step 3.3 – DataLoader Class

## Why create a DataLoader?

Instead of reading datasets directly throughout the project using:

```python
pd.read_csv(...)
```

AutoDS centralizes dataset loading inside a dedicated class.

Advantages:

- Reusable
- Easier to maintain
- Easier to test
- Centralized validation
- Cleaner architecture

---

# Step 3.4 – File Validation

Before loading any dataset, AutoDS validates:

- File existence
- Supported file extension

If validation fails:

- Logs the error
- Raises an appropriate custom exception

Current supported extension:

```python
SUPPORTED_FILE_TYPES = ["csv"]
```

---

# Step 3.5 – Loading CSV Files

The `load()` method performs the following sequence:

1. Validate the file.
2. Log the operation.
3. Read the dataset using `pandas.read_csv()`.
4. Log successful loading.
5. Return the DataFrame.

The DataFrame becomes the primary object used throughout the remainder of the project.

---

# Step 3.6 – Dataset Summary

AutoDS generates a simple dataset summary immediately after loading.

Current summary includes:

- Number of rows
- Number of columns
- Column names

This provides a quick overview of the dataset before preprocessing begins.

---

# Step 3.7 – Production Cleanup

Two improvements were made:

### Configuration Improvement

The default dataset path was moved into `config.py`.

```python
DEFAULT_DATASET_PATH = "data/sample.csv"
```

This follows the principle of separating configuration from implementation.

---

### Application Entry Point

The project now follows the standard Python application structure.

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

This makes the project easier to maintain and aligns with professional Python development practices.

---

# Files Created During Phase 3

```
src/
│
├── data/
│   ├── __init__.py
│   └── data_loader.py
```

---

# Best Practices Learned

- Validate data before processing.
- Separate configuration from implementation.
- Keep data loading centralized.
- Use logging for important operations.
- Raise meaningful exceptions.
- Build reusable modules instead of duplicating code.

---

# Key Takeaways

- Data Ingestion is the first stage of every Machine Learning pipeline.
- AutoDS now has a reusable data loading system.
- The project architecture became more modular.
- Future phases will build directly on the DataLoader.