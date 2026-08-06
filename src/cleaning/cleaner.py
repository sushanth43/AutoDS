"""
Data cleaning module for AutoDS.

This module contains the DataCleaner class responsible for
cleaning datasets before feature engineering and model training.
"""

import pandas as pd

from src.logger import logger


class DataCleaner:
    """
    Performs data cleaning operations on a dataset.
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe.copy()
        logger.info("DataCleaner initialized.")

    def handle_missing_values(
        self,
        strategy="mean",
        columns=None,
        fill_value=None,
    ):
        """
        Handle missing values in the dataset.
        """

        logger.info(
            f"Handling missing values using '{strategy}' strategy."
        )

        if columns is None:

            if strategy in ["mean", "median"]:

                columns = (
                    self.dataframe
                    .select_dtypes(include="number")
                    .columns
                )

            else:

                columns = self.dataframe.columns

        for column in columns:

            if not self.dataframe[column].isnull().any():
                continue

            if strategy == "mean":

                value = self.dataframe[column].mean()

            elif strategy == "median":

                value = self.dataframe[column].median()

            elif strategy == "mode":

                value = self.dataframe[column].mode()[0]

            elif strategy == "constant":

                value = fill_value

            else:

                raise ValueError(
                    f"Unsupported strategy: {strategy}"
                )

            self.dataframe[column] = (
                self.dataframe[column].fillna(value)
            )

            logger.info(
                f"Filled missing values in '{column}' using {strategy}."
            )

        return self.dataframe

    def remove_duplicates(
        self,
        subset=None,
        keep="first",
    ):
        """
        Remove duplicate rows from the dataset.
        """

        logger.info("Removing duplicate rows.")

        initial_rows = len(self.dataframe)

        self.dataframe = self.dataframe.drop_duplicates(
            subset=subset,
            keep=keep,
        )

        final_rows = len(self.dataframe)

        removed_rows = initial_rows - final_rows

        logger.info(
            f"Duplicate removal completed. "
            f"Removed {removed_rows} duplicate row(s)."
        )

        return self.dataframe    