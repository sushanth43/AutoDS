from configs.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    TEST_SIZE,
    RANDOM_STATE,
    SUPPORTED_FILE_TYPES,
    APP_ENV,
    DEBUG,
    DEFAULT_DATASET_PATH,
)

from src.logger import logger
from src.data.data_loader import DataLoader


def main():
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

    loader = DataLoader(DEFAULT_DATASET_PATH)

    try:
        dataframe = loader.load()

        loader.get_summary(dataframe)

        print("Dataset Preview:\n")
        print(dataframe)

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()