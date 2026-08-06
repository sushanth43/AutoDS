"""
Feature engineering workflow module for AutoDS.
"""

from src.logger import logger
from src.feature_engineering.engineer import FeatureEngineer


class FeatureWorkflow:
    """
    Controls the feature engineering workflow.
    """

    def __init__(self, dataframe):
        """
        Initialize the workflow.
        """

        self.dataframe = dataframe

        self.engineer = FeatureEngineer(dataframe)

        self.X = None
        self.y = None

        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        # Store user selections
        self.encoding_method = "Skipped"
        self.scaling_method = "Skipped"
        self.scaler = None
        self.test_size = None

        logger.info("FeatureWorkflow initialized.")

    def start_feature_engineering(self):
        """
        Start the feature engineering workflow.
        """

        logger.info("Starting feature engineering workflow.")

        print("\n========== FEATURE ENGINEERING ==========\n")

        self.handle_target_selection()
        self.handle_categorical_encoding()
        self.handle_train_test_split()
        self.handle_feature_scaling()

        # Display summary
        self.show_summary()

        print("\n=========================================\n")

        logger.info("Feature engineering workflow completed.")

        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        )

    def handle_target_selection(self):
        """
        Allow the user to select the target column.
        """

        print("========== TARGET SELECTION ==========\n")

        columns = list(self.dataframe.columns)

        print("Available Columns\n")

        for index, column in enumerate(columns, start=1):
            print(f"{index}. {column}")

        while True:

            choice = input("\nSelect Target Column: ")

            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(columns):
                break

            print("Invalid choice. Try again.")

        target_column = columns[choice - 1]

        self.X, self.y = self.engineer.select_target(target_column)

        print(f"\nTarget Column : {target_column}")
        print("\n✓ Target selected successfully.\n")

    def handle_categorical_encoding(self):
        """
        Allow the user to choose a categorical encoding method.
        """

        print("========== CATEGORICAL ENCODING ==========\n")
        categorical_columns = (
            self.X
            .select_dtypes(include=["object", "category"])
            .columns
        )

        if len(categorical_columns) == 0:
            print("No categorical columns found.\n")
            self.encoding_method = "Skipped"
            return

        print("Categorical Columns\n")

        for column in categorical_columns:
            print(f"- {column}")

        print("\nChoose Encoding Method")
        print("1. Label Encoding")
        print("2. One-Hot Encoding")
        print("3. Skip")

        while True:

            choice = input("\nEnter your choice: ")

            if choice in ["1", "2", "3"]:
                break

            print("Invalid choice. Please try again.")

        if choice == "1":

            self.X = self.engineer.encode_categorical("label")
            self.encoding_method = "Label Encoding"

            print("\n✓ Label Encoding Completed.\n")

        elif choice == "2":

            self.X = self.engineer.encode_categorical("onehot")
            self.encoding_method = "One-Hot Encoding"

            print("\n✓ One-Hot Encoding Completed.\n")

        else:

            self.encoding_method = "Skipped"

            print("\nSkipping categorical encoding.\n")

    def handle_train_test_split(self):
        """
        Split the dataset into training and testing sets.
        """

        print("========== TRAIN / TEST SPLIT ==========\n")

        print("Choose Test Size")
        print("1. 20%")
        print("2. 25%")
        print("3. 30%")

        while True:

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.test_size = 0.20
                break

            elif choice == "2":
                self.test_size = 0.25
                break

            elif choice == "3":
                self.test_size = 0.30
                break

            print("Invalid choice. Please try again.")

        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        ) = self.engineer.train_test_split_data(
            test_size=self.test_size
        )

        print("\n✓ Train/Test Split Completed Successfully.\n")

        print("Dataset Shapes")
        print("--------------------------")
        print(f"X_train : {self.X_train.shape}")
        print(f"X_test  : {self.X_test.shape}")
        print(f"y_train : {self.y_train.shape}")
        print(f"y_test  : {self.y_test.shape}")
        print()

    def handle_feature_scaling(self):
        """
        Allow the user to choose a feature scaling method.
        """

        print("========== FEATURE SCALING ==========\n")

        print("Choose Scaling Method")
        print("1. StandardScaler")
        print("2. MinMaxScaler")
        print("3. RobustScaler")
        print("4. Skip")

        while True:

            choice = input("\nEnter your choice: ")

            if choice in ["1", "2", "3", "4"]:
                break

            print("Invalid choice. Please try again.")

        if choice == "1":

            self.X_train, self.X_test = (
                self.engineer.scale_features("standard")
            )

            self.scaling_method = "StandardScaler"
            self.scaler = self.engineer.scaler

            print("\n✓ Standard Scaling Completed.\n")

        elif choice == "2":

            self.X_train, self.X_test = (
                self.engineer.scale_features("minmax")
            )

            self.scaling_method = "MinMaxScaler"
            self.scaler = self.engineer.scaler

            print("\n✓ MinMax Scaling Completed.\n")

        elif choice == "3":

            self.X_train, self.X_test = (
                self.engineer.scale_features("robust")
            )

            self.scaling_method = "RobustScaler"
            self.scaler = self.engineer.scaler

            print("\n✓ Robust Scaling Completed.\n")

        else:

            self.scaling_method = "Skipped"

            print("\nSkipping Feature Scaling.\n")

    def show_summary(self):
        """
        Display a summary of the feature engineering process.
        """

        print("\n========== FEATURE ENGINEERING SUMMARY ==========\n")

        print(f"Target Column      : {self.engineer.target_column}")
        print(f"Encoding Method    : {self.encoding_method}")
        print(f"Test Size          : {int(self.test_size * 100)}%")
        print(f"Scaling Method     : {self.scaling_method}")

        print("\nDataset Summary")
        print("--------------------------")
        print(f"Training Samples   : {len(self.X_train)}")
        print(f"Testing Samples    : {len(self.X_test)}")
        print(f"Number of Features : {self.X_train.shape[1]}")

        print("\nFinal Dataset Shapes")
        print("--------------------------")
        print(f"X_train : {self.X_train.shape}")
        print(f"X_test  : {self.X_test.shape}")
        print(f"y_train : {self.y_train.shape}")
        print(f"y_test  : {self.y_test.shape}")

        print("\n===============================================\n")