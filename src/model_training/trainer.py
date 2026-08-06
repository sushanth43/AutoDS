"""
Model training module for AutoDS.

This module contains the Trainer class responsible for
detecting the machine learning problem type, preparing
models, training them, and evaluating their performance.
"""

import json
from pathlib import Path
import numpy as np
import joblib
import pandas as pd

from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression,
)

from sklearn.tree import (
    DecisionTreeClassifier,
    DecisionTreeRegressor,
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
)

from sklearn.neighbors import (
    KNeighborsClassifier,
    KNeighborsRegressor,
)

from sklearn.svm import (
    SVC,
    SVR,
)

from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


from src.logger import logger


class Trainer:
    """
    Handles model training operations.
    """

    def __init__(
        self,
        X_train,
        X_test,
        y_train,
        y_test,
        metadata=None,
        scaler=None,
        encoders=None,
    ):
        """
        Initialize the Trainer.
        """

        self.X_train = X_train
        self.X_test = X_test

        self.y_train = y_train
        self.y_test = y_test
        self.metadata = metadata or {}
        self.scaler = scaler
        self.encoders = encoders or {}

        self.problem_type = None

        self.model_registry = {}

        self.results = {}

        self.results_dataframe = None

        self.best_model_name = None
        self.best_model = None
        self.best_score = None
        self.best_model_path = None

        logger.info("Trainer initialized.")

    def detect_problem_type(self):
        """
        Detect whether the task is Classification or Regression.
        """

        logger.info("Detecting problem type.")

        if self.y_train.dtype == "object":

            self.problem_type = "Classification"

        elif pd.api.types.is_bool_dtype(self.y_train):

            self.problem_type = "Classification"

        elif self.y_train.nunique() <= 20:

            self.problem_type = "Classification"

        else:

            self.problem_type = "Regression"

        logger.info(
            f"Problem type detected: {self.problem_type}"
        )

        return self.problem_type

    def build_model_registry(self):
        """
        Build the model registry based on the detected
        machine learning problem.
        """

        logger.info("Building model registry.")

        if self.problem_type is None:

            raise ValueError(
                "Detect the problem type before building the model registry."
            )

        if self.problem_type == "Classification":

            self.model_registry = {
                "Logistic Regression": LogisticRegression(),
                "Decision Tree": DecisionTreeClassifier(
                    random_state=42
                ),
                "Random Forest": RandomForestClassifier(
                    random_state=42
                ),
                "K-Nearest Neighbors": KNeighborsClassifier(),
                "Support Vector Machine": SVC(),
                "Naive Bayes": GaussianNB(),
            }

        else:

            self.model_registry = {
                "Linear Regression": LinearRegression(),
                "Decision Tree Regressor": DecisionTreeRegressor(
                    random_state=42
                ),
                "Random Forest Regressor": RandomForestRegressor(
                    random_state=42
                ),
                "K-Nearest Neighbors Regressor": KNeighborsRegressor(),
                "Support Vector Regressor": SVR(),
            }

        logger.info(
            f"{len(self.model_registry)} models added to the registry."
        )

        return self.model_registry

    def train_models(self):
        """
        Train all models in the registry.
        """

        logger.info("Training all models.")

        if not self.model_registry:

            raise ValueError(
                "Build the model registry before training."
            )

        self.results = {}

        for model_name, model in self.model_registry.items():

            logger.info(
                f"Training {model_name}..."
            )

            model.fit(
                self.X_train,
                self.y_train,
            )

            predictions = model.predict(
                self.X_test,
            )

            self.results[model_name] = {
                "model": model,
                "predictions": predictions,
            }

            logger.info(
                f"{model_name} trained successfully."
            )

        logger.info(
            "All models trained successfully."
        )

        return self.results

    def evaluate_models(self):
        """
        Evaluate all trained models.
        """

        logger.info("Evaluating trained models.")

        if not self.results:

            raise ValueError(
                "Train the models before evaluation."
            )

        for model_name, result in self.results.items():

            predictions = result["predictions"]

            logger.info(
                f"Evaluating {model_name}..."
            )

            if self.problem_type == "Classification":

                accuracy = accuracy_score(
                    self.y_test,
                    predictions,
                )

                precision = precision_score(
                    self.y_test,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )

                recall = recall_score(
                    self.y_test,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )

                f1 = f1_score(
                    self.y_test,
                    predictions,
                    average="weighted",
                    zero_division=0,
                )

                self.results[model_name]["metrics"] = {
                    "Accuracy": round(accuracy, 4),
                    "Precision": round(precision, 4),
                    "Recall": round(recall, 4),
                    "F1 Score": round(f1, 4),
                }

            else:

                mae = mean_absolute_error(
                    self.y_test,
                    predictions,
                )

                mse = mean_squared_error(
                    self.y_test,
                    predictions,
                )


                rmse = np.sqrt(mean_squared_error(
                    self.y_test,
                    predictions,
                ))

                r2 = r2_score(
                    self.y_test,
                    predictions,
                )

                self.results[model_name]["metrics"] = {
                    "MAE": round(mae, 4),
                    "MSE": round(mse, 4),
                    "RMSE": round(rmse, 4),
                    "R2 Score": round(r2, 4),
                }

            logger.info(
                f"{model_name} evaluated successfully."
            )

        logger.info(
            "All models evaluated successfully."
        )

        return self.results

    def build_results_dataframe(self):
        """
        Build a pandas DataFrame containing the
        evaluation metrics of all models.
        """

        logger.info(
            "Building results dataframe."
        )

        if not self.results:

            raise ValueError(
                "Evaluate the models before building the results dataframe."
            )

        rows = []

        for model_name, result in self.results.items():

            metrics = result["metrics"]

            if self.problem_type == "Classification":

                row = {
                    "Model": model_name,
                    "Accuracy": metrics["Accuracy"],
                    "Precision": metrics["Precision"],
                    "Recall": metrics["Recall"],
                    "F1 Score": metrics["F1 Score"],
                }

            else:

                row = {
                    "Model": model_name,
                    "MAE": metrics["MAE"],
                    "MSE": metrics["MSE"],
                    "RMSE": metrics["RMSE"],
                    "R2 Score": metrics["R2 Score"],
                }

            rows.append(row)

        self.results_dataframe = pd.DataFrame(
            rows
        )

        if self.problem_type == "Classification":

            self.results_dataframe.sort_values(
                by="Accuracy",
                ascending=False,
                inplace=True,
            )

        else:

            self.results_dataframe.sort_values(
                by="R2 Score",
                ascending=False,
                inplace=True,
            )

        self.results_dataframe.reset_index(
            drop=True,
            inplace=True,
        )

        logger.info(
            "Results dataframe built successfully."
        )

        return self.results_dataframe

    def identify_best_model(self):
        """
        Identify the best performing model from the
        results dataframe.
        """

        logger.info(
            "Identifying best model."
        )

        if (
            self.results_dataframe is None
            or self.results_dataframe.empty
        ):

            raise ValueError(
                "Build the results dataframe before identifying the best model."
            )

        metric = (
            "Accuracy"
            if self.problem_type == "Classification"
            else "R2 Score"
        )

        best_row = self.results_dataframe.iloc[0]

        self.best_model_name = best_row["Model"]
        self.best_score = best_row[metric]
        self.best_model = self.results[self.best_model_name]["model"]

        logger.info(
            f"Best model identified: {self.best_model_name}"
        )

        return self.best_model_name, self.best_model, self.best_score

    def save_best_model(self):
        """
        Save the best trained model to disk.
        """

        logger.info(
            "Saving best model."
        )

        if self.best_model is None:

            raise ValueError(
                "Identify the best model before saving."
            )

        models_dir = Path("models")
        models_dir.mkdir(parents=True, exist_ok=True)

        self.best_model_path = models_dir / "best_model.pkl"

        joblib.dump(
            self.best_model,
            self.best_model_path,
        )

        logger.info(
            f"Best model saved to {self.best_model_path}"
        )

        return self.best_model_path

    def save_scaler(self):
        """
        Save the fitted scaler to disk.
        """

        logger.info(
            "Saving scaler."
        )

        if self.scaler is None:

            logger.info(
                "No scaler available to save."
            )

            return None

        models_dir = Path("models")
        models_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        scaler_path = (
            models_dir / "scaler.pkl"
        )

        joblib.dump(
            self.scaler,
            scaler_path,
        )

        logger.info(
            f"Scaler saved to {scaler_path}"
        )

        return scaler_path

    def save_metadata(self):
        """
        Save training metadata to disk.
        """

        logger.info(
            "Saving metadata."
        )

        models_dir = Path("models")
        models_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        metadata_path = (
            models_dir / "metadata.json"
        )

        metadata = {
            **self.metadata,
            "problem_type": self.problem_type,
            "best_model_name": self.best_model_name,
            "best_score": (
                float(self.best_score)
                if self.best_score is not None
                else None
            ),
            "feature_names": (
                list(self.X_train.columns)
                if hasattr(self.X_train, "columns")
                else []
            ),
        }

        with open(
            metadata_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        logger.info(
            f"Metadata saved to {metadata_path}"
        )

        return metadata_path
    def save_encoders(self):
        """
        Save fitted encoders to disk.
        """

        logger.info(
            "Saving encoders."
        )

        if not self.encoders:

            logger.info(
                "No encoders available to save."
            )

            return None

        models_dir = Path("models")
        models_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        encoders_path = (
            models_dir / "encoders.pkl"
        )

        joblib.dump(
            self.encoders,
            encoders_path,
        )

        logger.info(
            f"Encoders saved to {encoders_path}"
        )

        return encoders_path