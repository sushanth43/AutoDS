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

---

# PHASE 4 – DATA VALIDATION

---

# Engineering Decision 015

## Phase

Phase 4 – Data Validation

## Topic

Separate Data Validation from Data Cleaning

## Decision

Implement Data Validation as a completely independent module before introducing Data Cleaning.

The validation module is responsible only for identifying data quality issues and reporting them.

---

## Alternatives Considered

### Option A

Perform validation and cleaning together inside a single module.

### Option B ✅ (Selected)

Separate validation and cleaning into two independent phases.

---

## Reason

Validation and cleaning solve different problems.

Validation identifies issues within the dataset, whereas cleaning modifies the dataset to resolve those issues.

Separating these responsibilities follows the Single Responsibility Principle (SRP) and produces a cleaner, more maintainable architecture.

---

## Advantages

- Clear separation of responsibilities
- Easier debugging
- Better maintainability
- Reusable validation module
- Easier testing

---

## Future Impact

Future validation checks can be added without affecting the Data Cleaning module.

Likewise, new cleaning techniques can be introduced without modifying the validation logic.

---

# Engineering Decision 016

## Phase

Phase 4 – Data Validation

## Topic

Dedicated DataValidator Class

## Decision

Create a dedicated `DataValidator` class responsible for performing all dataset validation operations.

---

## Alternatives Considered

### Option A

Perform validation directly inside `main.py`.

### Option B

Merge validation logic into the `DataLoader`.

### Option C ✅ (Selected)

Implement a dedicated `DataValidator` class.

---

## Reason

The DataLoader is responsible only for loading datasets.

Adding validation responsibilities would violate the Single Responsibility Principle.

Creating a dedicated validator produces a cleaner and more modular architecture.

---

## Advantages

- Single Responsibility Principle
- Better modularity
- Easier maintenance
- Reusable validation component
- Improved scalability

---

## Future Impact

Future validation rules such as schema validation, constraint validation, and business rule validation can be implemented inside the `DataValidator` without affecting other modules.

---

# Engineering Decision 017

## Phase

Phase 4 – Data Validation

## Topic

Validation Before Processing

## Decision

Ensure every dataset passes through the validation pipeline before any further analysis or preprocessing.

---

## Alternatives Considered

### Option A

Begin EDA immediately after loading the dataset.

### Option B ✅ (Selected)

Validate the dataset before allowing it to proceed to the next stage.

---

## Reason

Processing invalid datasets may produce incorrect statistics, misleading visualizations, and unreliable Machine Learning models.

Validating data first guarantees that later modules receive datasets whose quality has already been assessed.

---

## Advantages

- Improved reliability
- Better data quality
- Reduced downstream errors
- Cleaner workflow

---

## Future Impact

Every future module in AutoDS will receive datasets that have already passed the validation stage.

This establishes Data Validation as a permanent quality checkpoint within the pipeline.

---

# Engineering Decision 018

## Phase

Phase 4 – Data Validation

## Topic

Generate Validation Reports Instead of Individual Console Messages

## Decision

Combine all validation results into a structured validation report instead of displaying unrelated console messages.

---

## Alternatives Considered

### Option A

Print each validation result individually.

### Option B ✅ (Selected)

Generate a single structured validation summary.

---

## Reason

A consolidated report is easier to read, easier to maintain, and provides users with a complete overview of dataset quality.

It also allows validation results to be reused by future reporting modules.

---

## Advantages

- Better readability
- Professional output
- Easier debugging
- Centralized reporting
- Improved user experience

---

## Future Impact

Future versions of AutoDS can export validation reports as PDF, HTML, or dashboard components without modifying the validation logic.

---

# Engineering Decision 019

## Phase

Phase 4 – Data Validation

## Topic

Non-Destructive Validation

## Decision

Ensure that the validation module never modifies the dataset.

Its responsibility is limited to identifying and reporting data quality issues.

---

## Alternatives Considered

### Option A

Automatically fix problems during validation.

### Option B ✅ (Selected)

Keep validation completely non-destructive.

---

## Reason

Automatically modifying datasets during validation makes it difficult to distinguish between identifying problems and correcting them.

Keeping validation non-destructive improves transparency and makes debugging easier.

---

## Advantages

- Predictable behaviour
- Easier debugging
- Clear separation of responsibilities
- Better software design
- Improved maintainability

---

## Future Impact

Future cleaning strategies can evolve independently while the validation module remains stable and reusable.

---

# Engineering Decision 020

## Phase

Phase 4 – Data Validation

## Topic

Modular Validation Checks

## Decision

Implement each validation check as an independent method inside the `DataValidator` class.

Examples include:

- Empty Dataset Validation
- Missing Value Detection
- Duplicate Detection
- Data Type Analysis

---

## Alternatives Considered

### Option A

Write one large validation function.

### Option B ✅ (Selected)

Create separate methods for every validation task.

---

## Reason

Smaller methods are easier to understand, maintain, debug, and test.

They also allow new validation rules to be added without modifying existing functionality.

---

## Advantages

- Cleaner architecture
- Better readability
- Easier testing
- Improved maintainability
- Better extensibility

---

## Future Impact

Future validation methods such as:

- Range Validation
- Schema Validation
- Date Validation
- Constraint Validation

can be added as independent methods without changing the existing implementation.

---

---

# PHASE 5 – EXPLORATORY DATA ANALYSIS (EDA)

---

# Engineering Decision 021

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Separate Exploratory Data Analysis from Data Validation

## Decision

Implement Exploratory Data Analysis (EDA) as an independent phase that executes only after Data Validation has been completed successfully.

---

## Alternatives Considered

### Option A

Merge Data Validation and EDA into a single module.

### Option B ✅ (Selected)

Keep Data Validation and Exploratory Data Analysis as separate phases.

---

## Reason

Validation focuses on verifying dataset quality, whereas EDA focuses on understanding the dataset.

Separating these responsibilities keeps the architecture modular and follows the Single Responsibility Principle.

---

## Advantages

- Clear separation of concerns
- Easier maintenance
- Better scalability
- Improved readability
- Cleaner project architecture

---

## Future Impact

Future EDA techniques can be added without affecting the validation module.

---

# Engineering Decision 022

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Dedicated EDAAnalyzer Class

## Decision

Create a dedicated `EDAAnalyzer` class responsible for performing all exploratory data analysis operations.

---

## Alternatives Considered

### Option A

Perform EDA directly inside `main.py`.

### Option B

Add EDA functionality inside the `DataValidator`.

### Option C ✅ (Selected)

Create a dedicated `EDAAnalyzer` class.

---

## Reason

EDA involves multiple independent analyses such as descriptive statistics, correlation analysis, categorical analysis, and outlier detection.

Keeping these operations inside a dedicated class improves modularity and keeps other components focused on their own responsibilities.

---

## Advantages

- Modular design
- Easier maintenance
- Reusable analysis component
- Better testing
- Improved scalability

---

## Future Impact

Future EDA techniques can be implemented without modifying the rest of the pipeline.

---

# Engineering Decision 023

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Separate Visualization from Analysis

## Decision

Move all visualization logic into a dedicated `Visualizer` class.

---

## Alternatives Considered

### Option A

Generate plots directly inside the EDA analysis methods.

### Option B ✅ (Selected)

Separate visualization into its own module.

---

## Reason

Creating visualizations and performing statistical analysis are two different responsibilities.

Separating them follows the Single Responsibility Principle and keeps both components simpler.

---

## Advantages

- Cleaner architecture
- Easier maintenance
- Better code organization
- Independent visualization module
- Easier future expansion

---

## Future Impact

Additional visualizations such as box plots, scatter plots, heatmaps, and pair plots can be added without changing the analysis logic.

---

# Engineering Decision 024

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Dedicated EDA Report Generator

## Decision

Create a dedicated `EDAReport` class responsible for formatting and generating the final EDA report.

---

## Alternatives Considered

### Option A

Print analysis results directly from the analyzer.

### Option B ✅ (Selected)

Generate a structured report using a dedicated reporting module.

---

## Reason

Separating reporting from analysis keeps the EDAAnalyzer focused solely on computing results.

It also allows reports to be generated in multiple formats without modifying the analysis code.

---

## Advantages

- Better separation of responsibilities
- Cleaner implementation
- Easier report customization
- Improved maintainability

---

## Future Impact

Future versions can export reports as PDF, HTML, or dashboard widgets using the same reporting component.

---

# Engineering Decision 025

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Automatic Histogram Generation

## Decision

Automatically generate histogram plots for every numerical feature during EDA.

---

## Alternatives Considered

### Option A

Require users to manually generate plots.

### Option B ✅ (Selected)

Automatically generate histogram visualizations.

---

## Reason

Histograms provide immediate insight into feature distributions and help identify skewness, multimodal distributions, and potential outliers.

Automating this process improves usability and saves users from repetitive tasks.

---

## Advantages

- Better data understanding
- Improved user experience
- Consistent analysis
- Reduced manual effort

---

## Future Impact

Additional automatic visualizations can be generated using the same visualization framework.

---

# Engineering Decision 026

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Use the IQR Method for Outlier Detection

## Decision

Adopt the Interquartile Range (IQR) method as the default approach for detecting outliers.

---

## Alternatives Considered

### Option A

Z-Score Method

### Option B

Isolation Forest

### Option C ✅ (Selected)

Interquartile Range (IQR)

---

## Reason

The IQR method is simple, interpretable, computationally efficient, and performs well for many tabular datasets.

It also does not assume that the data follows a normal distribution.

---

## Advantages

- Easy to understand
- Fast computation
- Robust for many datasets
- Widely accepted statistical technique

---

## Future Impact

Future versions may support multiple outlier detection techniques while retaining IQR as the default implementation.

---

# Engineering Decision 027

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Generate Persistent EDA Reports

## Decision

Save the EDA report to disk in addition to displaying it in the terminal.

---

## Alternatives Considered

### Option A

Display results only in the console.

### Option B ✅ (Selected)

Generate a persistent report file.

---

## Reason

Console output disappears after the application terminates.

Saving reports allows users to review results later and provides a permanent record of the analysis.

---

## Advantages

- Persistent analysis results
- Better reproducibility
- Improved user experience
- Easier documentation

---

## Future Impact

The reporting system can later support PDF, HTML, Markdown, and dashboard-based report generation without changing the analysis workflow.

---

# Engineering Decision 028

## Phase

Phase 5 – Exploratory Data Analysis (EDA)

## Topic

Refactor the EDA Module Using the Single Responsibility Principle

## Decision

Refactor the original EDA implementation into three independent components:

- `EDAAnalyzer`
- `Visualizer`
- `EDAReport`

Each component performs one well-defined responsibility.

---

## Alternatives Considered

### Option A

Maintain one large EDA class containing analysis, visualization, and reporting.

### Option B ✅ (Selected)

Split the functionality into dedicated classes.

---

## Reason

As the EDA module expanded, combining multiple responsibilities into a single class made the code harder to understand and maintain.

Applying the Single Responsibility Principle resulted in a cleaner and more extensible architecture.

---

## Advantages

- Better modularity
- Improved maintainability
- Easier testing
- Better readability
- Simpler future extensions

---

## Future Impact

Future EDA features can be implemented by extending the appropriate component without affecting the others.

This architecture provides a scalable foundation for future versions of AutoDS.

---
