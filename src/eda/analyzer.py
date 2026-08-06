"""
Exploratory Data Analysis module for AutoDS.

This module contains the EDAAnalyzer class responsible for
performing exploratory data analysis on datasets.
"""

import pandas as pd

from src.logger import logger


class EDAAnalyzer:
    """
    Performs exploratory data analysis on datasets.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def statistical_summary(self):
        logger.info("Generating statistical summary.")
        return self.dataframe.describe()

    def numerical_feature_analysis(self):
        logger.info("Analyzing numerical features.")

        return self.dataframe.select_dtypes(
            include=["number"]
        ).columns

    def categorical_feature_analysis(self):
        logger.info("Analyzing categorical features.")

        return self.dataframe.select_dtypes(
            exclude=["number"]
        ).columns

    def correlation_analysis(self):
        logger.info("Generating correlation matrix.")

        return self.dataframe.corr(numeric_only=True)

    def detect_outliers(self):
        """
        Detect outliers using the IQR method.

        Returns
        -------
        dict
            Dictionary containing outlier count for each
            numerical column.
        """

        logger.info("Detecting outliers.")

        report = {}

        numerical_columns = self.dataframe.select_dtypes(
            include=["number"]
        ).columns

        for column in numerical_columns:

            q1 = self.dataframe[column].quantile(0.25)
            q3 = self.dataframe[column].quantile(0.75)

            iqr = q3 - q1

            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            outliers = self.dataframe[
                (self.dataframe[column] < lower_bound)
                | (self.dataframe[column] > upper_bound)
            ]

            report[column] = len(outliers)

        return report