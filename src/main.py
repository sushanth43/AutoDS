from configs.config import APP_ENV, DEBUG

from configs.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    TEST_SIZE,
    RANDOM_STATE,
    SUPPORTED_FILE_TYPES,
)

print(f"Project Name      : {PROJECT_NAME}")
print(f"Project Version   : {PROJECT_VERSION}")
print(f"Test Size         : {TEST_SIZE}")
print(f"Random State      : {RANDOM_STATE}")
print(f"Supported Files   : {SUPPORTED_FILE_TYPES}")

print(f"Environment      : {APP_ENV}")
print(f"Debug Mode      : {DEBUG}")