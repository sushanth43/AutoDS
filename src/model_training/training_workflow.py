"""
Model training workflow module for AutoDS.
"""

from src.logger import logger
from src.model_training.trainer import Trainer


class TrainingWorkflow:
    """
    Controls the model training workflow.
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
        Initialize the workflow.
        """

        self.X_train = X_train
        self.X_test = X_test

        self.y_train = y_train
        self.y_test = y_test
        self.metadata = metadata or {}
        self.scaler = scaler
        self.encoders = encoders or {}

        self.trainer = Trainer(
            X_train,
            X_test,
            y_train,
            y_test,
            metadata=self.metadata,
            scaler=self.scaler,
            encoders=self.encoders,
        )

        self.problem_type = None
        self.model_registry = None
        self.results = None
        self.results_dataframe = None

        self.best_model_name = None
        self.best_model = None
        self.best_score = None
        self.best_model_path = None

        self.metric = None

        logger.info("TrainingWorkflow initialized.")

    def start_training(self):
        """
        Start the model training workflow.
        """

        logger.info("Starting model training workflow.")

        print("\n========== MODEL TRAINING ==========\n")

        self.handle_problem_detection()
        self.handle_model_registry()
        self.handle_model_training()
        self.handle_model_evaluation()
        self.handle_results_dataframe()
        self.handle_best_model()
        self.handle_model_persistence()
        self.handle_training_summary()

        print("\n====================================\n")

        logger.info("Model training workflow completed.")

    def handle_problem_detection(self):
        """
        Detect the machine learning problem type.
        """

        print("========== PROBLEM TYPE DETECTION ==========\n")

        self.problem_type = (
            self.trainer.detect_problem_type()
        )

        print(f"Target Column : {self.y_train.name}")

        print("\nDetected Problem Type")
        print("-------------------------")
        print(self.problem_type)

        print("\n✓ Problem type detected successfully.\n")

    def handle_model_registry(self):
        """
        Build the model registry automatically.
        """

        print("========== MODEL REGISTRY ==========\n")

        self.model_registry = (
            self.trainer.build_model_registry()
        )

        print("Models Selected Automatically\n")

        for index, model_name in enumerate(
            self.model_registry.keys(),
            start=1,
        ):
            print(f"{index}. {model_name}")

        print(
            f"\n✓ {len(self.model_registry)} models added successfully.\n"
        )

    def handle_model_training(self):
        """
        Train all models.
        """

        print("========== MODEL TRAINING ==========\n")

        self.results = self.trainer.train_models()

        print("Training Status\n")

        for model_name in self.results.keys():
            print(f"✓ {model_name}")

        print(
            f"\n✓ Successfully trained {len(self.results)} models.\n"
        )

    def handle_model_evaluation(self):
        """
        Evaluate all trained models.
        """

        print("========== MODEL EVALUATION ==========\n")

        self.results = self.trainer.evaluate_models()

        print("Evaluation Status\n")

        for model_name in self.results.keys():
            print(f"✓ {model_name}")

        print(
            f"\n✓ Successfully evaluated {len(self.results)} models.\n"
        )

    def handle_results_dataframe(self):
        """
        Build and display the model comparison table.
        """

        print("========== MODEL COMPARISON ==========\n")

        self.results_dataframe = (
            self.trainer.build_results_dataframe()
        )

        print(
            self.results_dataframe.to_string(
                index=False
            )
        )

        print(
            "\n✓ Model comparison generated successfully.\n"
        )

    def handle_best_model(self):
        """
        Identify and display the best model.
        """

        print("========== BEST MODEL ==========\n")

        (
            self.best_model_name,
            self.best_model,
            self.best_score,
        ) = self.trainer.identify_best_model()

        self.metric = (
            "Accuracy"
            if self.problem_type == "Classification"
            else "R2 Score"
        )

        print("Best Model")
        print("--------------------------")
        print(self.best_model_name)

        print(f"\nBest {self.metric}")
        print("--------------------------")
        print(self.best_score)

        print(
            "\n✓ Best model identified successfully.\n"
        )

    def handle_model_persistence(self):
        """
        Save the best model, scaler and metadata to disk.
        """

        print("========== MODEL PERSISTENCE ==========\n")

        self.best_model_path = (
            self.trainer.save_best_model()
        )

        scaler_path = (
            self.trainer.save_scaler()
        )

        encoders_path = (
            self.trainer.save_encoders()
        )

        metadata_path = (
            self.trainer.save_metadata()
        )

        print("Best Model")
        print("--------------------------")
        print(self.best_model_name)

        print("\nModel Save Location")
        print("--------------------------")
        print(self.best_model_path)

        print("\nScaler Save Location")
        print("--------------------------")
        print(scaler_path)

        print("\nEncoders Save Location")
        print("--------------------------")
        print(encoders_path)

        print("\nMetadata Save Location")
        print("--------------------------")
        print(metadata_path)

        print(
            "\n✓ Best model, scaler and metadata saved successfully.\n"
        )

    def handle_training_summary(self):
        """
        Display a summary of the completed
        model training workflow.
        """

        print("========== TRAINING SUMMARY ==========\n")

        print(
            f"Problem Type      : {self.problem_type}"
        )

        print(
            f"Target Column     : {self.y_train.name}"
        )

        print(
            f"Models Trained    : {len(self.model_registry)}"
        )

        print(
            f"Evaluation Metric : {self.metric}"
        )

        print(
            f"Best Model        : {self.best_model_name}"
        )

        print(
            f"Best Score        : {self.best_score}"
        )

        print(
            f"Model Saved At    : {self.best_model_path}"
        )

        print(
            "Scaler Saved At   : models/scaler.pkl"
        )

        print("\n======================================")