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