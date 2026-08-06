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

---

# Phase 4 – Data Validation

# Step 4.1 – Introduction to Data Validation

---

## Question 1

**What is Data Validation?**

### Answer

Data Validation is the process of checking whether a dataset satisfies predefined quality rules before it is processed further.

Its primary purpose is to identify problems in the dataset without modifying the data.

---

## Question 2

**Why is Data Validation important in Machine Learning?**

### Answer

Machine Learning models are highly dependent on data quality.

Validating data before processing helps identify issues such as missing values, duplicate records, incorrect data types, and empty datasets, reducing the chances of errors and improving model reliability.

---

## Question 3

**What is the difference between Data Validation and Data Cleaning?**

### Answer

Data Validation identifies problems within the dataset.

Examples include:

- Missing values
- Duplicate rows
- Incorrect data types

Data Cleaning corrects those problems by modifying the dataset.

Examples include:

- Filling missing values
- Removing duplicates
- Converting data types

---

## Question 4

**When should Data Validation be performed?**

### Answer

Data Validation should be performed immediately after data ingestion and before Exploratory Data Analysis or Data Cleaning.

This ensures that every downstream module works with a dataset whose quality has already been assessed.

---

## Interview Tip

Interviewers often ask:

> "Why not clean the data immediately instead of validating it first?"

A strong answer is:

> "Validation identifies data quality issues, while cleaning resolves them. Separating these responsibilities makes the application easier to maintain, debug, and extend."

---

# Step 4.2 – Empty Dataset Validation

---

## Question 1

**Why should an application check whether a dataset is empty?**

### Answer

An empty dataset contains no observations and therefore cannot be analyzed or used for Machine Learning.

Detecting this condition early prevents unnecessary computation and avoids errors in later stages of the pipeline.

---

## Question 2

**Why is the empty dataset check performed first?**

### Answer

Checking whether a dataset is empty is computationally inexpensive.

If the dataset contains no records, there is no need to perform more expensive validation operations such as duplicate detection or data type analysis.

---

## Interview Tip

Always mention that inexpensive validation checks should be performed before more computationally expensive operations.

---

# Step 4.3 – Missing Value Detection

---

## Question 1

**What are missing values?**

### Answer

Missing values represent unavailable or unknown information within a dataset.

In Pandas, they are commonly represented as `NaN` or `None`.

---

## Question 2

**Why are missing values problematic?**

### Answer

Missing values can:

- Distort statistical calculations.
- Reduce model accuracy.
- Cause some Machine Learning algorithms to fail.
- Produce misleading analytical results.

---

## Question 3

**How does AutoDS handle missing values during validation?**

### Answer

During validation, AutoDS only detects and reports missing values.

The dataset remains unchanged.

The actual handling of missing values is performed later during the Data Cleaning phase.

---

## Interview Tip

Interviewers may ask:

> "Would you remove every row containing missing values?"

A good answer is:

> "Not necessarily. The appropriate strategy depends on the amount of missing data, feature importance, and the specific Machine Learning problem."

---

# Step 4.4 – Duplicate Row Detection

---

## Question 1

**What are duplicate rows?**

### Answer

Duplicate rows are records that appear more than once in a dataset without providing any additional information.

---

## Question 2

**Why are duplicate rows harmful?**

### Answer

Duplicate records can:

- Bias Machine Learning models.
- Distort statistical analysis.
- Increase dataset size unnecessarily.
- Produce misleading insights.

---

## Question 3

**Does AutoDS remove duplicates during validation?**

### Answer

No.

The validation module only detects and reports duplicate records.

Duplicate removal is performed later during the Data Cleaning phase.

---

## Interview Tip

A common interview question is:

> "Why not remove duplicates immediately?"

A good answer is:

> "Validation should only identify issues. Cleaning is responsible for modifying the dataset."

---

# Step 4.5 – Data Type Analysis

---

## Question 1

**Why is data type analysis important?**

### Answer

Different data types require different preprocessing techniques.

Understanding feature types helps determine how each column should be handled during Feature Engineering and Machine Learning.

---

## Question 2

**What are the most common Pandas data types?**

### Answer

Common data types include:

- int64
- float64
- object
- bool
- datetime64

---

## Question 3

**Why is storing numerical data as text a problem?**

### Answer

Machine Learning algorithms expect numerical features to have numerical data types.

If numerical values are stored as text, they cannot be processed correctly until they are converted.

---

## Interview Tip

Interviewers often ask:

> "Why should data types be checked before Feature Engineering?"

The expected answer is:

> "Feature Engineering depends on correctly identifying numerical, categorical, and datetime features. Incorrect data types can lead to improper preprocessing."

---

# Step 4.6 – Validation Report Generation

---

## Question 1

**Why generate a Validation Report?**

### Answer

A Validation Report provides a centralized summary of dataset quality instead of displaying scattered console messages.

It allows users to quickly understand the condition of the dataset before preprocessing begins.

---

## Question 2

**What information does the Validation Report contain?**

### Answer

The Validation Report currently includes:

- Dataset Shape
- Empty Dataset Check
- Missing Value Summary
- Duplicate Row Count
- Column Data Types

---

## Question 3

**What are the advantages of generating structured reports?**

### Answer

Structured reports provide:

- Better readability
- Easier debugging
- Improved maintainability
- Better user experience
- Reusable outputs for future reporting systems

---

## Interview Tip

If asked why reports are important, mention that professional applications present information in a structured format rather than relying on scattered terminal output.

---

# Common Interview Questions (Quick Revision)

- What is Data Validation?
- Why is Data Validation important?
- Difference between Validation and Data Cleaning?
- Why validate data before EDA?
- What are missing values?
- Why are duplicate rows harmful?
- What are common Pandas data types?
- Why analyze data types?
- Why generate a Validation Report?
- Why should validation be non-destructive?

---

---

# Phase 5 – Exploratory Data Analysis (EDA)

# Step 5.1 – Introduction to Exploratory Data Analysis (EDA)

---

## Question 1

**What is Exploratory Data Analysis (EDA)?**

### Answer

Exploratory Data Analysis (EDA) is the process of examining and understanding a dataset before preprocessing or model training.

It uses statistical summaries and visualizations to identify patterns, relationships, anomalies, and important characteristics within the data.

---

## Question 2

**Why is EDA important in Machine Learning?**

### Answer

EDA helps data scientists understand the dataset before building models.

It helps identify:

- Data distribution
- Feature relationships
- Outliers
- Data imbalance
- Potential preprocessing requirements

A good understanding of the dataset leads to better feature engineering and model selection.

---

## Question 3

**When is EDA performed in the Machine Learning pipeline?**

### Answer

EDA is performed after Data Validation and before Data Cleaning or Feature Engineering.

This ensures that the dataset has already passed basic quality checks before analysis begins.

---

## Question 4

**Why shouldn't we train a model immediately after loading the data?**

### Answer

Without understanding the dataset, important issues such as skewed distributions, outliers, redundant features, or unusual relationships may go unnoticed.

EDA provides valuable insights that improve later stages of the Machine Learning pipeline.

---

## Interview Tip

A common interview question is:

> "Why do Data Scientists spend so much time performing EDA?"

A strong answer is:

> "Because understanding the data is often more important than choosing the Machine Learning algorithm. Good EDA leads to better preprocessing, feature engineering, and model performance."

---

# Step 5.2 – Statistical Summary

---

## Question 1

**What is a statistical summary?**

### Answer

A statistical summary provides descriptive statistics for numerical features.

It commonly includes:

- Count
- Mean
- Standard Deviation
- Minimum
- Maximum
- Quartiles

These statistics provide a quick overview of the dataset.

---

## Question 2

**Why are descriptive statistics useful?**

### Answer

Descriptive statistics help identify:

- Data distribution
- Large variations
- Possible outliers
- Overall characteristics of numerical features

They provide an efficient way to understand large datasets.

---

## Interview Tip

Interviewers often ask:

> "What information can you obtain from `describe()`?"

Mention statistics such as mean, standard deviation, minimum, maximum, and quartiles.

---

# Step 5.3 – Numerical Feature Analysis

---

## Question 1

**What are numerical features?**

### Answer

Numerical features represent measurable quantities and support mathematical operations.

Examples include:

- Age
- Salary
- Height
- Temperature

---

## Question 2

**Why are numerical features important?**

### Answer

Most Machine Learning algorithms require numerical input.

Analyzing numerical features helps understand:

- Distribution
- Range
- Variability
- Potential outliers

---

## Interview Tip

Always mention that numerical features are the primary input for many Machine Learning algorithms.

---

# Step 5.4 – Categorical Feature Analysis

---

## Question 1

**What are categorical features?**

### Answer

Categorical features represent labels or groups rather than numerical values.

Examples include:

- Gender
- Country
- Department
- Product Category

---

## Question 2

**Why analyze categorical features?**

### Answer

Categorical analysis helps understand:

- Number of categories
- Feature composition
- Cardinality
- Data distribution across categories

This information becomes useful during Feature Engineering and Encoding.

---

## Interview Tip

A common interview question is:

> "Can Machine Learning algorithms directly use categorical features?"

A good answer is:

> "Most Machine Learning algorithms require categorical variables to be converted into numerical representations using encoding techniques."

---

# Step 5.5 – Correlation Analysis

---

## Question 1

**What is correlation?**

### Answer

Correlation measures the strength and direction of the relationship between two numerical variables.

Its value ranges from:

- -1 (Strong Negative Correlation)
- 0 (No Correlation)
- +1 (Strong Positive Correlation)

---

## Question 2

**Why is correlation analysis useful?**

### Answer

Correlation analysis helps identify:

- Strong feature relationships
- Redundant variables
- Highly related features
- Potential multicollinearity

This information assists in feature selection.

---

## Question 3

**Does correlation imply causation?**

### Answer

No.

Correlation indicates that two variables move together.

It does not prove that one variable causes changes in the other.

---

## Interview Tip

This is one of the most common interview questions.

Always remember:

> **Correlation does not imply causation.**

---

# Step 5.6 – Histogram Generation

---

## Question 1

**What is a histogram?**

### Answer

A histogram is a graphical representation of the distribution of numerical data.

It groups values into intervals called bins and displays the number of observations within each interval.

---

## Question 2

**Why are histograms useful?**

### Answer

Histograms help visualize:

- Distribution
- Skewness
- Spread
- Peaks
- Potential outliers

Visualizations often reveal patterns that numerical summaries cannot.

---

## Question 3

**Why did AutoDS automatically generate histograms?**

### Answer

Automatically generating histograms saves users from manually creating visualizations and ensures every numerical feature is analyzed consistently.

---

## Interview Tip

If asked why visualization is important, explain that humans often recognize patterns much more easily through graphs than through numerical tables.

---

# Step 5.7 – Outlier Detection

---

## Question 1

**What is an outlier?**

### Answer

An outlier is an observation that lies significantly farther away from the majority of the data.

Outliers may represent genuine rare events or data quality issues.

---

## Question 2

**Why are outliers important?**

### Answer

Outliers can:

- Distort statistical summaries.
- Influence Machine Learning models.
- Affect visualizations.
- Produce misleading analysis.

---

## Question 3

**Which method does AutoDS use for outlier detection?**

### Answer

AutoDS currently uses the **Interquartile Range (IQR)** method.

The IQR method calculates lower and upper bounds based on the first and third quartiles and identifies observations outside these limits as outliers.

---

## Question 4

**Why was the IQR method selected?**

### Answer

The IQR method is:

- Simple
- Easy to interpret
- Computationally efficient
- Suitable for many tabular datasets
- Independent of normal distribution assumptions

---

## Interview Tip

Interviewers frequently ask:

> "Which outlier detection methods do you know?"

Mention:

- IQR
- Z-Score
- Isolation Forest
- DBSCAN

Then explain why IQR was selected for AutoDS.

---

# Step 5.8 – Refactoring the EDA Module

---

## Question 1

**Why was the EDA module refactored?**

### Answer

Initially, one class handled analysis, visualization, and reporting.

As the module grew, this violated the Single Responsibility Principle.

The implementation was refactored into dedicated components with clearly defined responsibilities.

---

## Question 2

**What components were created?**

### Answer

The EDA module was divided into:

- `EDAAnalyzer`
- `Visualizer`
- `EDAReport`

Each class performs one well-defined responsibility.

---

## Question 3

**What software engineering principle motivated this refactoring?**

### Answer

The refactoring was based on the **Single Responsibility Principle (SRP)**.

Each class should have one reason to change.

---

## Interview Tip

Interviewers appreciate candidates who recognize when refactoring is necessary to improve maintainability rather than simply adding more code.

---

# Step 5.9 – EDA Report Generation

---

## Question 1

**Why generate an EDA Report?**

### Answer

An EDA Report combines all analysis results into a structured and readable summary.

Instead of displaying scattered outputs, users receive a centralized overview of the dataset.

---

## Question 2

**What information does the EDA Report contain?**

### Answer

The report currently includes:

- Dataset Shape
- Statistical Summary
- Numerical Features
- Categorical Features
- Correlation Matrix
- Outlier Summary

---

## Question 3

**Why save the report instead of only displaying it?**

### Answer

Saving the report allows users to review analysis results later and provides a permanent record of the exploratory analysis.

It also supports future reporting features such as PDF and HTML export.

---

## Interview Tip

Professional software should generate reusable reports rather than relying only on console output.

---

# Common Interview Questions (Quick Revision)

- What is Exploratory Data Analysis (EDA)?
- Why is EDA important?
- What information does a statistical summary provide?
- What are numerical features?
- What are categorical features?
- What is correlation?
- Does correlation imply causation?
- What is a histogram?
- Why are histograms useful?
- What is an outlier?
- Which outlier detection methods do you know?
- Why did you choose the IQR method?
- Why separate visualization from analysis?
- What is the Single Responsibility Principle?
- Why generate an EDA Report?

---