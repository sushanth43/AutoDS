from configs.config import APP_ENV, DEBUG
from src.logger import logger

from configs.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    TEST_SIZE,
    RANDOM_STATE,
    SUPPORTED_FILE_TYPES,
)

from src.logger import logger

logger.info("Project Started")

logger.info(f"Project Name      : {PROJECT_NAME}")
logger.info(f"Project Version   : {PROJECT_VERSION}")
logger.info(f"Test Size         : {TEST_SIZE}")
logger.info(f"Random State      : {RANDOM_STATE}")
logger.info(f"Supported Files   : {SUPPORTED_FILE_TYPES}")
logger.info(f"Environment       : {APP_ENV}")
logger.info(f"Debug Mode        : {DEBUG}")

print(f"Project Name      : {PROJECT_NAME}")
print(f"Project Version   : {PROJECT_VERSION}")
print(f"Test Size         : {TEST_SIZE}")
print(f"Random State      : {RANDOM_STATE}")
print(f"Supported Files   : {SUPPORTED_FILE_TYPES}")
print(f"Environment       : {APP_ENV}")
print(f"Debug Mode        : {DEBUG}")

