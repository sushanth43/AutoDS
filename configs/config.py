from dotenv import load_dotenv
import os
import logging

load_dotenv()

APP_ENV = os.getenv("APP_ENV")
DEBUG = os.getenv("DEBUG")
"""
Configuration file for the AutoDS project.

This file contains all project-wide settings.
Any configurable value should be defined here instead of being
hardcoded throughout the project.
"""

PROJECT_NAME = "AutoDS"

PROJECT_VERSION = "1.0.0"

SUPPORTED_FILE_TYPES = ["csv"]

RANDOM_STATE = 42

TEST_SIZE = 0.2

LOG_FILE_NAME = "autods.log"

LOG_LEVEL = logging.INFO