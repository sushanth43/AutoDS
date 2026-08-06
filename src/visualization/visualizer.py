"""
Visualization module for AutoDS.

This module contains the Visualizer class responsible for
creating and saving visualizations.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.logger import logger


class Visualizer:
    """
    Generates visualizations for datasets.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the Visualizer.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Dataset to visualize.
        """
        self.dataframe = dataframe

    def generate_histograms(self):
        """
        Generate histograms for all numerical columns.
        """

        logger.info("Generating histograms for numerical features.")

        output_dir = Path("reports/plots")
        output_dir.mkdir(parents=True, exist_ok=True)

        numerical_columns = self.dataframe.select_dtypes(
            include=["number"]
        ).columns

        for column in numerical_columns:

            plt.figure(figsize=(8, 5))

            sns.histplot(
                self.dataframe[column],
                kde=True
            )

            plt.title(f"{column} Distribution")
            plt.xlabel(column)
            plt.ylabel("Frequency")

            output_path = output_dir / f"{column}_histogram.png"

            plt.savefig(output_path, dpi=300, bbox_inches="tight")
            plt.close()

            logger.info(f"Histogram saved: {output_path}")

        print("\nHistograms generated successfully.")