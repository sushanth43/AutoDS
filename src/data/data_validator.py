"""
Data validation module for AutoDS.

This module contains the DataValidator class responsible for
validating datasets before they are processed.
"""

import pandas as pd

from src.logger import logger


class DataValidator:
    """
    Performs validation checks on datasets.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the validator.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Dataset to validate.
        """

        self.dataframe = dataframe

        # Stores structured validation results
        self.validation_results = {}

    def validate_empty_dataset(self):
        """
        Validate that the dataset is not empty.
        """

        logger.info("Checking if the dataset is empty.")

        if self.dataframe.empty:
            logger.error("Dataset is empty.")
            raise ValueError("The dataset is empty.")

        logger.info("Dataset is not empty.")

    def check_missing_values(self):
        """
        Check for missing values in the dataset.
        """

        logger.info("Checking for missing values.")

        missing_values = self.dataframe.isnull().sum()

        print("\n========== MISSING VALUE REPORT ==========")

        if missing_values.sum() == 0:
            print("No missing values found.")
            logger.info("No missing values found.")
        else:
            print(missing_values)
            logger.warning("Missing values detected.")

        print("==========================================\n")

        self.validation_results["missing_values"] = {
            "exists": missing_values.sum() > 0,
            "count": int(missing_values.sum()),
            "columns": {
                column: int(count)
                for column, count in missing_values.items()
                if count > 0
            }
        }

        return missing_values

    def check_duplicate_rows(self):
        """
        Check for duplicate rows in the dataset.
        """

        logger.info("Checking for duplicate rows.")

        duplicate_count = self.dataframe.duplicated().sum()

        print("\n========== DUPLICATE ROW REPORT ==========")
        print(f"Duplicate Rows : {duplicate_count}")

        if duplicate_count == 0:
            logger.info("No duplicate rows found.")
        else:
            logger.warning(f"{duplicate_count} duplicate rows detected.")

        print("==========================================\n")

        self.validation_results["duplicates"] = {
            "exists": duplicate_count > 0,
            "count": int(duplicate_count)
        }

        return duplicate_count

    def generate_validation_report(self):
        """
        Generate a complete validation report.
        """

        logger.info("Generating validation report.")

        missing_values = self.dataframe.isnull().sum().sum()
        duplicate_rows = self.dataframe.duplicated().sum()

        print("\n========== VALIDATION REPORT ==========")
        print(f"Rows               : {self.dataframe.shape[0]}")
        print(f"Columns            : {self.dataframe.shape[1]}")
        print(f"Missing Values     : {missing_values}")
        print(f"Duplicate Rows     : {duplicate_rows}")
        print("=======================================\n")

        logger.info("Validation report generated successfully.")

    def get_validation_results(self):
        """
        Return the structured validation results.

        Returns
        -------
        dict
            Dictionary containing all validation results.
        """

        return self.validation_results