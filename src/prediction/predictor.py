"""
Prediction module for AutoDS.
"""

import json
import joblib
import pandas as pd
from pathlib import Path

from src.logger import logger


class Predictor:

    def __init__(self):

        self.model = None
        self.metadata = None
        self.scaler = None
        self.encoders = None

        logger.info(
            "Predictor initialized."
        )

    def load_model(
        self,
        model_path="models/best_model.pkl",
    ):

        model_path = Path(model_path)

        if not model_path.exists():

            raise FileNotFoundError(
                f"Model not found: {model_path}"
            )

        self.model = joblib.load(
            model_path
        )

        logger.info(
            f"Model loaded from {model_path}"
        )

        return self.model

    def load_metadata(
        self,
        metadata_path="models/metadata.json",
    ):

        metadata_path = Path(metadata_path)

        if not metadata_path.exists():

            raise FileNotFoundError(
                f"Metadata not found: {metadata_path}"
            )

        with open(
            metadata_path,
            "r",
        ) as file:

            self.metadata = json.load(
                file
            )

        logger.info(
            f"Metadata loaded from {metadata_path}"
        )

        return self.metadata

    def load_scaler(
        self,
        scaler_path="models/scaler.pkl",
    ):

        scaler_path = Path(
            scaler_path
        )

        if not scaler_path.exists():

            raise FileNotFoundError(
                f"Scaler not found: {scaler_path}"
            )

        self.scaler = joblib.load(
            scaler_path
        )

        logger.info(
            f"Scaler loaded from {scaler_path}"
        )

        return self.scaler

    def load_encoders(
        self,
        encoders_path="models/encoders.pkl",
    ):

        encoders_path = Path(
            encoders_path
        )

        if not encoders_path.exists():

            logger.warning(
                "Encoders file not found."
            )

            self.encoders = {}

            return self.encoders

        self.encoders = joblib.load(
            encoders_path
        )

        logger.info(
            f"Encoders loaded from {encoders_path}"
        )

        return self.encoders

    def preprocess_data(
        self,
        dataframe,
    ):

        if self.metadata is None:

            raise ValueError(
                "Metadata must be loaded first."
            )

        encoding_method = (
            self.metadata[
                "encoding_method"
            ]
        )

        feature_names = (
            self.metadata[
                "feature_names"
            ]
        )

        df = dataframe.copy()

        numeric_columns = df.select_dtypes(
            include=["number"]
        ).columns

        for column in numeric_columns:
            df[column] = (
                df[column]
                .fillna(
                    df[column].median()
                )
            )

        if encoding_method in ["label", "Label Encoding"]:

            for (
                column,
                encoder,
            ) in self.encoders.items():

                if column in df.columns:

                    fallback_value = (
                        encoder.classes_[0]
                    )

                    df[column] = (
                        df[column]
                        .fillna(
                            fallback_value
                        )
                        .astype(str)
                    )

                    df[column] = (
                        df[column].apply(
                            lambda x:
                            x
                            if x in encoder.classes_
                            else fallback_value
                        )
                    )

                    df[column] = (
                        encoder.transform(
                            df[column]
                        )
                    )

            df = df[
                feature_names
            ]

        elif encoding_method in ["onehot", "One-Hot Encoding"]:

            categorical_columns = (
                df.select_dtypes(
                    include=[
                        "object",
                        "category",
                    ]
                ).columns
            )

            df = pd.get_dummies(
                df,
                columns=categorical_columns,
                drop_first=False,
            )

            for column in feature_names:

                if column not in df.columns:

                    df[column] = 0

            df = df[
                feature_names
            ]


        

        if self.scaler is not None:

            df = pd.DataFrame(
                self.scaler.transform(
                    df
                ),
                columns=df.columns,
            )

        logger.info(
            "Prediction preprocessing completed."
        )

        return df

    def predict(
        self,
        dataframe,
    ):

        if self.model is None:

            raise ValueError(
                "Load a model before prediction."
            )

        predictions = self.model.predict(
            dataframe
        )

        logger.info(
            "Predictions generated successfully."
        )

        return predictions

    def save_predictions(
        self,
        predictions,
        output_path="predictions.csv",
    ):

        prediction_df = pd.DataFrame(
            {
                "Prediction": predictions
            }
        )

        prediction_df.to_csv(
            output_path,
            index=False,
        )

        logger.info(
            f"Predictions saved to {output_path}"
        )

        return output_path