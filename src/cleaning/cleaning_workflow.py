"""
Cleaning workflow module for AutoDS.
"""

from src.logger import logger
from src.cleaning.cleaner import DataCleaner


class CleaningWorkflow:

    def __init__(self, dataframe, validation_results):
        self.dataframe = dataframe
        self.validation_results = validation_results
        self.cleaner = DataCleaner(dataframe)
        logger.info("CleaningWorkflow initialized.")

    def start_cleaning(self):
        logger.info("Starting cleaning workflow.")

        print("\n========== CLEANING WORKFLOW ==========\n")

        self.handle_missing_values()
        self.handle_duplicate_rows()

        print("Text Cleaning")
        print("-------------")
        print("Coming Soon...\n")

        print("=======================================\n")

        logger.info("Cleaning workflow completed.")

        return self.dataframe

    def handle_missing_values(self):
        missing_info = self.validation_results["missing_values"]

        if not missing_info["exists"]:
            print("Missing Value Handling")
            print("----------------------")
            print("No missing values found.\n")
            return

        print("========== MISSING VALUE HANDLING ==========\n")

        numerical_columns = []
        categorical_columns = []

        for column in missing_info["columns"]:
            if self.dataframe[column].dtype.kind in "biufc":
                numerical_columns.append(column)
            else:
                categorical_columns.append(column)

        if numerical_columns:
            print("Numerical Columns with Missing Values\n")
            for column in numerical_columns:
                print(f"{column} ({missing_info['columns'][column]})")

            print("\nChoose Strategy")
            print("1. Mean")
            print("2. Median")
            print("3. Constant")
            print("4. Skip")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.dataframe = self.cleaner.handle_missing_values(
                    strategy="mean",
                    columns=numerical_columns,
                )
            elif choice == "2":
                self.dataframe = self.cleaner.handle_missing_values(
                    strategy="median",
                    columns=numerical_columns,
                )
            elif choice == "3":
                value = input("Enter constant value: ")
                self.dataframe = self.cleaner.handle_missing_values(
                    strategy="constant",
                    columns=numerical_columns,
                    fill_value=value,
                )
            elif choice == "4":
                print("Skipping numerical columns.")
            else:
                print("Invalid choice. Skipping numerical columns.")

        if categorical_columns:
            print("\nCategorical Columns with Missing Values\n")
            for column in categorical_columns:
                print(f"{column} ({missing_info['columns'][column]})")

            print("\nChoose Strategy")
            print("1. Mode")
            print("2. Constant")
            print("3. Skip")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.dataframe = self.cleaner.handle_missing_values(
                    strategy="mode",
                    columns=categorical_columns,
                )
            elif choice == "2":
                value = input("Enter constant value: ")
                self.dataframe = self.cleaner.handle_missing_values(
                    strategy="constant",
                    columns=categorical_columns,
                    fill_value=value,
                )
            elif choice == "3":
                print("Skipping categorical columns.")
            else:
                print("Invalid choice. Skipping categorical columns.")

        print("\n✓ Missing Value Handling Completed.\n")

    def handle_duplicate_rows(self):
        duplicate_info = self.validation_results["duplicates"]

        print("========== DUPLICATE ROW HANDLING ==========\n")

        if not duplicate_info["exists"]:
            print("No duplicate rows found.\n")
            return

        print(f"{duplicate_info['count']} duplicate row(s) found.\n")

        print("Choose Strategy")
        print("1. Remove Duplicates (Keep First)")
        print("2. Remove Duplicates (Keep Last)")
        print("3. Skip")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            self.dataframe = self.cleaner.remove_duplicates(keep="first")
            print("Duplicate rows removed (keeping first occurrence).\n")
        elif choice == "2":
            self.dataframe = self.cleaner.remove_duplicates(keep="last")
            print("Duplicate rows removed (keeping last occurrence).\n")
        elif choice == "3":
            print("Skipping duplicate removal.\n")
        else:
            print("Invalid choice. Skipping duplicate removal.\n")