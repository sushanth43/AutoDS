# AutoDS - Engineering Decisions

---

# Table of Contents

## Phase 0 – Product Design

- Engineering Decision 001 – Two-Stage Development Strategy
- Engineering Decision 002 – Target Audience
- Engineering Decision 003 – Version 1 Scope
- Engineering Decision 004 – Technology Stack
- Engineering Decision 005 – System Architecture
- Engineering Decision 006 – Professional README
- Engineering Decision 007 – Git Version Control Setup

## Phase 2 – Configuration & Logging

- Engineering Decision 008 – Separate Configuration from Business Logic

---

# PHASE 0 – PRODUCT DESIGN

---

# Engineering Decision 001

## Phase

Phase 0 – Product Design

## Topic

Two-Stage Development Strategy

## Decision

Develop AutoDS in two stages.

### Stage 1 (Current)

Build a complete autonomous data science platform capable of:

- Dataset Upload
- Dataset Validation
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Automatic Model Training
- Model Evaluation
- Explainable AI
- Dashboard
- Prediction API

### Stage 2 (Future)

Extend the platform into an AI-powered conversational assistant capable of understanding natural language and interacting intelligently with datasets.

---

## Alternatives Considered

### Option A

Build only the AI Assistant.

### Option B ✅ (Selected)

Build the core autonomous data science platform first and add AI capabilities later.

---

## Reason

The AI assistant depends on a strong machine learning engine.

By building the engine first, future AI components can reuse existing functionality instead of reimplementing it.

---

## Advantages

- Strong foundation
- Easier maintenance
- Better scalability
- Faster future development

---

## Future Impact

Future AI modules will interact with the existing platform rather than replacing it.

---

# Engineering Decision 002

## Phase

Phase 0 – Product Design

## Topic

Target Audience

## Decision

Design AutoDS primarily for professional Data Scientists and Machine Learning Engineers while keeping the interface simple enough for students and beginners.

---

## Alternatives Considered

### Option A

Target beginners only.

### Option B

Target professionals only.

### Option C ✅ (Selected)

Professional-grade functionality with a beginner-friendly interface.

---

## Reason

This approach demonstrates industry-level engineering while remaining accessible to learners.

---

## Advantages

- Professional portfolio project
- Broader usability
- Better user experience

---

## Future Impact

Future enterprise features can be added without redesigning the user interface.

---

# Engineering Decision 003

## Phase

Phase 0 – Product Design

## Topic

Version 1 Scope

## Decision

Limit Version 1 to the complete autonomous data science workflow.

---

## Included Features

- CSV Upload
- Dataset Validation
- Data Profiling
- Data Cleaning
- EDA
- Feature Engineering
- AutoML
- Model Comparison
- SHAP Explainability
- Dashboard
- PDF Report
- FastAPI Prediction API

---

## Deferred Features

- AI Assistant
- Multi-Agent System
- Docker
- MLflow
- Authentication
- Enterprise Features

---

## Reason

A stable MVP provides a solid foundation for future expansion.

---

## Advantages

- Faster completion
- Better software quality
- Easier testing
- Clear development roadmap

---

# Engineering Decision 004

## Phase

Phase 0 – Product Design

## Topic

Technology Stack

## Decision

Use the following technologies:

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

---

## Alternatives Considered

Several alternative libraries exist for visualization, web frameworks, and testing.

The selected stack prioritizes:

- Industry adoption
- Stability
- Community support
- Ease of learning
- Free and open-source tooling

---

## Reason

The selected technologies are widely used in production machine learning systems.

---

## Advantages

- Professional ecosystem
- Large community support
- Excellent documentation
- High scalability

---

# Engineering Decision 005

## Phase

Phase 0 – Product Design

## Topic

System Architecture

## Decision

Adopt a modular pipeline architecture.

---

## Pipeline

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

AutoML Engine

↓

Model Evaluation

↓

Explainability

↓

Dashboard

↓

Prediction API

---

## Reason

Each module performs one clearly defined responsibility.

This improves maintainability, testing, scalability, and future extensibility.

---

## Advantages

- Modular design
- Easy debugging
- Easier testing
- Better code organization

---

# Engineering Decision 006

## Phase

Phase 0 – Product Design

## Topic

Repository Documentation

## Decision

Create a professional README at the beginning of the project.

---

## Reason

The README is the first document viewed by recruiters, collaborators, and users.

It explains the project's purpose, features, installation process, and roadmap.

---

## Advantages

- Better first impression
- Easier onboarding
- Professional presentation

---

# Engineering Decision 007

## Phase

Phase 0 – Product Design

## Topic

Version Control

## Decision

Initialize Git and GitHub before writing application code.

---

## Reason

Version control should begin from the first commit so the complete development history is preserved.

---

## Advantages

- Safe experimentation
- Collaboration readiness
- Project history
- Easy rollback

---

# PHASE 2 – CONFIGURATION & LOGGING

---

# Engineering Decision 008

## Phase

Phase 2 – Configuration & Logging

## Topic

Configuration Management

## Decision

Separate configuration from business logic.

Create a dedicated configuration module (`config.py`) containing all project-wide settings.

---

## Alternatives Considered

### Option A

Hardcode configuration values throughout the project.

### Option B ✅ (Selected)

Store configuration values in a centralized module.

---

## Reason

Centralized configuration improves maintainability, readability, consistency, and scalability.

---

## Advantages

- Single source of truth
- Easier updates
- Reduced duplication
- Cleaner architecture

---

## Future Impact

As AutoDS grows, additional configuration values can be added without modifying existing business logic.

This keeps the project modular and easier to maintain.

---

# Engineering Decision 009

## Phase

Phase 2 – Configuration & Logging

## Topic

Environment Variable Management

## Decision

Use Environment Variables to store sensitive and environment-specific information.

During development, AutoDS will use a `.env` file together with the `python-dotenv` package to load these values.

---

## Alternatives Considered

### Option A

Hardcode secrets inside Python files.

### Option B ✅ (Selected)

Store secrets in Environment Variables and load them using `python-dotenv`.

---

## Reason

Separating secrets from source code improves security, prevents accidental exposure on GitHub, and allows different environments (development, testing, production) to use different values without modifying the application code.

---

## Advantages

- Improved security
- Cleaner source code
- Environment-specific configuration
- Easier deployment
- Follows industry best practices

---

## Future Impact

Future integrations such as OpenAI, databases, email services, and cloud deployments will use Environment Variables instead of hardcoded credentials.


---

# Engineering Decision 010

## Phase

Phase 2 – Configuration & Logging

## Topic

Centralized Logging System

## Decision

Implement a centralized logging system using Python's built-in `logging` module.

The logger is configured once inside `src/logger.py` and reused throughout the project.

---

## Alternatives Considered

### Option A

Use `print()` statements throughout the project.

### Option B ✅ (Selected)

Use a centralized logging system.

---

## Reason

A centralized logging system provides timestamps, severity levels, persistent log files, and consistent formatting across the application.

---

## Advantages

- Easier debugging
- Better monitoring
- Professional software practice
- Reusable across modules
- Consistent log formatting

---

## Additional Decision

The following logging settings are treated as configuration values:

- LOG_FILE_NAME
- LOG_LEVEL

These are stored inside `config.py` rather than hardcoded inside `logger.py`.

---

## Future Impact

As AutoDS grows, every module will use the same logging configuration without requiring additional setup.

---

# Engineering Decision 011

## Phase

Phase 2 – Configuration & Logging

## Topic

Centralized Error Handling

## Decision

Create a centralized exception module (`src/exceptions.py`) containing a common base exception (`AutoDSError`) and project-specific exceptions.

---

## Alternatives Considered

### Option A

Raise generic `Exception` throughout the project.

### Option B ✅ (Selected)

Use custom exceptions derived from a common base class.

---

## Reason

Custom exceptions make project-specific failures easier to identify, improve debugging, and simplify future maintenance.

---

## Advantages

- Cleaner error handling
- Better debugging
- Easier maintenance
- Reusable exception hierarchy

---

## Future Impact

As AutoDS grows, new exceptions will inherit from `AutoDSError`, creating a consistent error handling strategy.

---

# Engineering Decision 012

## Phase

Phase 2 – Configuration & Logging

## Topic

Centralized Utility Module

## Decision

Create a dedicated utility module (`src/utils.py`) for reusable helper functions.

---

## Alternatives Considered

### Option A

Duplicate helper functions across multiple modules.

### Option B ✅ (Selected)

Maintain a centralized utility module.

---

## Reason

Centralizing reusable helper functions reduces duplication and improves maintainability.

The module will grow only when real requirements appear, following the YAGNI principle.

---

## Advantages

- Cleaner codebase
- Better reusability
- Easier maintenance
- Reduced duplication

---

## Future Impact

Future helper functions such as JSON handling, model persistence, and file utilities will be added to this module as needed.

---

# Engineering Decision 013

## Phase

Phase 3 – Data Ingestion

## Topic

Centralized Data Loading

## Decision

Create a dedicated `DataLoader` class responsible for dataset loading.

---

## Alternatives Considered

### Option A

Call `pandas.read_csv()` directly throughout the project.

### Option B ✅ (Selected)

Create a reusable DataLoader module.

---

## Reason

Centralizing data loading provides:

- Better maintainability
- Easier testing
- Centralized validation
- Consistent logging
- Better scalability

---

## Advantages

- Single responsibility
- Reusable component
- Cleaner project architecture
- Easier future extensions

---

## Future Impact

Future support for Excel, JSON, SQL databases, and APIs can be added inside the DataLoader without changing the rest of the application.

---

# Engineering Decision 014

## Phase

Phase 3 – Data Ingestion

## Topic

Configuration-Driven Dataset Path

## Decision

Move the default dataset path into `config.py`.

---

## Reason

Dataset location is a configuration value rather than application logic.

Keeping it inside `config.py` follows the project's configuration management principles.

---

## Advantages

- Easier maintenance
- Single source of truth
- Cleaner implementation

---

## Future Impact

Future versions may allow users to change dataset paths through configuration files or a graphical interface without modifying the source code.