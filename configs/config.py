"""
Configuration settings for AutoDS.
"""

import logging
import os

from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Project Information
# ==========================================

PROJECT_NAME = "AutoDS"
PROJECT_VERSION = "1.0.0"

# ==========================================
# Machine Learning Configuration
# ==========================================

TEST_SIZE = 0.2
RANDOM_STATE = 42

# ==========================================
# Supported File Types
# ==========================================

SUPPORTED_FILE_TYPES = ["csv"]

# ==========================================
# Default Dataset
# ==========================================

DEFAULT_DATASET_PATH = "data/sample.csv"

# ==========================================
# Logging Configuration
# ==========================================

LOG_FILE_NAME = "autods.log"
LOG_LEVEL = logging.INFO

# ==========================================
# Environment Variables
# ==========================================

APP_ENV = os.getenv("APP_ENV")
DEBUG = os.getenv("DEBUG")