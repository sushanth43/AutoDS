"""
Data loading module for AutoDS.

This module contains the DataLoader class responsible for
loading datasets into the application.
"""

from pathlib import Path
import pandas as pd

from configs.config import SUPPORTED_FILE_TYPES
from src.exceptions import DatasetNotFoundError
from src.logger import logger


class DataLoader:
    """
    Loads datasets into AutoDS.
    """

    def __init__(self, file_path: str):
        """
        Initialize the DataLoader.

        Parameters
        ----------
        file_path : str
            Path to the dataset.
        """
        self.file_path = Path(file_path)

    def validate_file(self):
        """
        Validate the dataset before loading.
        """

        # Check if the file exists
        if not self.file_path.exists():
            logger.error(f"Dataset not found: {self.file_path}")
            raise DatasetNotFoundError(
                f"Dataset '{self.file_path}' does not exist."
            )

        # Check if the file extension is supported
        extension = self.file_path.suffix.lower().replace(".", "")

        if extension not in SUPPORTED_FILE_TYPES:
            logger.error(f"Unsupported file type: {extension}")
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        logger.info("Dataset validation successful.")

    def load(self):
        """
        Load the dataset into a Pandas DataFrame.

        Returns
        -------
        pandas.DataFrame
            Loaded dataset.
        """

        self.validate_file()

        logger.info(f"Loading dataset: {self.file_path}")

        try:
            dataframe = pd.read_csv(self.file_path)

            logger.info(
                f"Dataset loaded successfully. Shape: {dataframe.shape}"
            )

            return dataframe

        except Exception as e:
            logger.error(f"Failed to load dataset: {e}")
            raise

    def get_summary(self, dataframe):
        """
        Display a basic summary of the dataset.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Dataset to summarize.
        """

        logger.info("Generating dataset summary.")

        print("\n========== DATASET SUMMARY ==========")
        print(f"Rows            : {dataframe.shape[0]}")
        print(f"Columns         : {dataframe.shape[1]}")

        print("\nColumn Names:")
        for column in dataframe.columns:
            print(f"- {column}")

        print("=====================================\n")