"""
Feature engineering module for AutoDS.

This module contains the FeatureEngineer class responsible for
preparing the dataset for machine learning.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
)

from src.logger import logger


class FeatureEngineer:
    """
    Performs feature engineering operations on a dataset.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the FeatureEngineer.

        Parameters
        ----------
        dataframe : pandas.DataFrame
            Cleaned dataset.
        """

        self.dataframe = dataframe.copy()

        self.X = None
        self.y = None

        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        self.target_column = None
        self.scaler = None
        self.encoders = {}

        logger.info("FeatureEngineer initialized.")

    def select_target(self, target_column: str):
        """
        Separate the dataset into features (X) and target (y).
        """

        logger.info(f"Selecting '{target_column}' as the target column.")

        if target_column not in self.dataframe.columns:
            logger.error(f"Target column '{target_column}' does not exist.")
            raise ValueError(f"Column '{target_column}' not found.")

        self.target_column = target_column

        self.X = self.dataframe.drop(columns=[target_column])
        self.y = self.dataframe[target_column]

        logger.info("Target column selected successfully.")

        return self.X, self.y

    def remove_high_cardinality_columns(
        self,
        threshold=0.5,
    ):
        """
        Remove high-cardinality categorical columns.
        """

        logger.info(
            f"Detecting high-cardinality columns with threshold={threshold}"
        )

        categorical_columns = (
            self.X.select_dtypes(
                include=["object", "category"]
            ).columns
        )

        high_cardinality_columns = []

        total_rows = len(self.X)

        for column in categorical_columns:

            unique_values = self.X[column].nunique()

            unique_ratio = (
                unique_values / total_rows
            )

            if (unique_ratio >0.1 or unique_values>50):
                high_cardinality_columns.append(column)

        if high_cardinality_columns:

            logger.info(
                f"Removing high-cardinality columns: "
                f"{high_cardinality_columns}"
            )

            print(
                "\nHigh Cardinality Columns Removed:"
            )

            for column in high_cardinality_columns:
                print(f"- {column}")

            self.X = self.X.drop(
                columns=high_cardinality_columns
            )

        else:

            logger.info(
                "No high-cardinality columns found."
            )

        return self.X

    def encode_categorical(self, method):
        """
        Encode categorical columns in X.
        """

        logger.info(
            f"Encoding categorical columns using '{method}'."
        )

        self.remove_high_cardinality_columns()

        categorical_columns = (
            self.X.select_dtypes(
                include=["object", "category"]
            ).columns
        )

        if len(categorical_columns) == 0:
            logger.info("No categorical columns found.")
            return self.X

        if method == "label":

            

            for column in categorical_columns:
                encoder = LabelEncoder()
                self.X[column] = encoder.fit_transform(
                    self.X[column].astype(str)
                )
                self.encoders[column] = encoder

            logger.info(
                "Label encoding completed successfully."
            )

        elif method == "onehot":

            self.X = pd.get_dummies(
                self.X,
                columns=categorical_columns,
                drop_first=False,
            )

            logger.info(
                "One-Hot encoding completed successfully."
            )

        else:

            logger.error(
                f"Unsupported encoding method: {method}"
            )
            raise ValueError(
                f"Unsupported encoding method: {method}"
            )

        return self.X

    def train_test_split_data(
        self,
        test_size=0.2,
        random_state=42,
    ):
        """
        Split X and y into training and testing sets.
        """

        logger.info(
            f"Splitting dataset with test_size={test_size}"
        )

        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        ) = train_test_split(
            self.X,
            self.y,
            test_size=test_size,
            random_state=random_state,
        )

        logger.info(
            "Train/Test split completed successfully."
        )

        return (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        )

    def scale_features(self, method):
        """
        Scale numeric features in the training and testing sets.
        """

        logger.info(
            f"Scaling features using '{method}'."
        )

        if method == "standard":
            self.scaler = StandardScaler()

        elif method == "minmax":
            self.scaler = MinMaxScaler()

        elif method == "robust":
            self.scaler = RobustScaler()

        else:
            logger.error(
                f"Unsupported scaling method: {method}"
            )
            raise ValueError(
                f"Unsupported scaling method: {method}"
            )

        numeric_columns = self.X_train.select_dtypes(
            include=["number"]
        ).columns

        self.X_train[numeric_columns] = (
            self.scaler.fit_transform(
                self.X_train[numeric_columns]
            )
        )

        self.X_test[numeric_columns] = (
            self.scaler.transform(
                self.X_test[numeric_columns]
            )
        )

        logger.info(
            "Feature scaling completed successfully."
        )

        return self.X_train, self.X_test