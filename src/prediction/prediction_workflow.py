"""
Prediction workflow module for AutoDS.
"""

from src.logger import logger
from src.data.data_loader import DataLoader
from src.prediction.predictor import Predictor


class PredictionWorkflow:
    """
    Controls the prediction workflow.
    """

    def __init__(self):
        """
        Initialize the workflow.
        """

        self.predictor = Predictor()

        self.dataframe = None
        self.predictions = None

        logger.info(
            "PredictionWorkflow initialized."
        )

    def start_prediction(self):
        """
        Start the prediction workflow.
        """

        logger.info(
            "Starting prediction workflow."
        )

        print("\n========== PREDICTION ==========\n")

        self.handle_dataset_loading()

        self.handle_model_loading()

        self.handle_prediction()

        self.handle_save_predictions()

        print("\n================================\n")

        logger.info(
            "Prediction workflow completed."
        )

    def handle_dataset_loading(self):
        """
        Load prediction dataset.
        """

        print(
            "========== LOAD DATASET ==========\n"
        )

        dataset_path = input(
            "Enter dataset path: "
        )

        loader = DataLoader(
            dataset_path
        )

        self.dataframe = loader.load()

        print(
            "\nDataset Loaded Successfully"
        )

        print(
            f"Shape: {self.dataframe.shape}"
        )

        print()

    def handle_model_loading(self):
        """
        Load trained artifacts.
        """

        print(
            "========== LOAD ARTIFACTS ==========\n"
        )

        self.predictor.load_model()

        self.predictor.load_metadata()

        self.predictor.load_scaler()

        self.predictor.load_encoders()

        

        print(
            "✓ Model loaded successfully."
        )

        print(
            "✓ Metadata loaded successfully."
        )

        print(
            "✓ Scaler loaded successfully."
        )

        print(
            "✓ Encoders loaded successfully.\n"
        )

    def handle_prediction(self):
        """
        Generate predictions.
        """

        print(
            "========== GENERATE PREDICTIONS ==========\n"
        )

        processed_df = (
            self.predictor.preprocess_data(
                self.dataframe
            )
        )

        self.predictions = (
            self.predictor.predict(
                processed_df
            )
        )

        print(
            f"Generated {len(self.predictions)} predictions.\n"
        )

    def handle_save_predictions(self):
        """
        Save predictions to CSV.
        """

        print(
            "========== SAVE PREDICTIONS ==========\n"
        )

        output_file = (
            self.predictor.save_predictions(
                self.predictions
            )
        )

        print(
            f"Saved to: {output_file}\n"
        )