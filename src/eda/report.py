"""
EDA reporting module for AutoDS.

This module contains the EDAReport class responsible for
displaying and saving EDA reports.
"""

from pathlib import Path

from src.logger import logger


class EDAReport:
    """
    Displays and saves EDA reports.
    """

    def __init__(self):
        logger.info("EDA Report initialized.")

    def generate_report(
        self,
        dataframe,
        numerical_columns,
        categorical_columns,
        outlier_report,
    ):
        """
        Generate a complete EDA report.
        """

        report_lines = []

        report_lines.append("=" * 60)
        report_lines.append("AUTO DS - EDA REPORT".center(60))
        report_lines.append("=" * 60)
        report_lines.append("")

        report_lines.append("DATASET INFORMATION")
        report_lines.append("-" * 60)
        report_lines.append(f"Rows                 : {dataframe.shape[0]}")
        report_lines.append(f"Columns              : {dataframe.shape[1]}")
        report_lines.append("")

        report_lines.append("FEATURE SUMMARY")
        report_lines.append("-" * 60)
        report_lines.append(
            f"Numerical Features   : {len(numerical_columns)}"
        )
        report_lines.append(
            f"Categorical Features : {len(categorical_columns)}"
        )
        report_lines.append("")

        report_lines.append("OUTLIER SUMMARY")
        report_lines.append("-" * 60)

        for column, count in outlier_report.items():
            report_lines.append(f"{column:<20}: {count}")

        report_lines.append("")
        report_lines.append("VISUALIZATIONS")
        report_lines.append("-" * 60)
        report_lines.append(
            f"Histograms Generated : {len(numerical_columns)}"
        )
        report_lines.append("Location             : reports/plots/")
        report_lines.append("")
        report_lines.append("=" * 60)

        report = "\n".join(report_lines)

        print("\n")
        print(report)
        print("\n")

        output_dir = Path("reports")
        output_dir.mkdir(exist_ok=True)

        output_file = output_dir / "eda_report.txt"

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(report)

        logger.info(f"EDA report saved to {output_file}")