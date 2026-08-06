from configs.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    TEST_SIZE,
    RANDOM_STATE,
    SUPPORTED_FILE_TYPES,
    APP_ENV,
    DEBUG,
    DEFAULT_DATASET_PATH,
)

from src.logger import logger
from src.data.data_loader import DataLoader
from src.data.data_validator import DataValidator
from src.eda.analyzer import EDAAnalyzer
from src.eda.report import EDAReport
from src.visualization.visualizer import Visualizer
from src.cleaning.cleaning_workflow import CleaningWorkflow
from src.feature_engineering.feature_workflow import FeatureWorkflow
from src.model_training.training_workflow import TrainingWorkflow
from src.prediction.prediction_workflow import (
    PredictionWorkflow,
)


def run_training():

    logger.info("Training Workflow Started")

    try:

        # -----------------------------
        # Data Loading
        # -----------------------------
        loader = DataLoader(
            DEFAULT_DATASET_PATH
        )

        dataframe = loader.load()

        loader.get_summary(
            dataframe
        )

        # -----------------------------
        # Data Validation
        # -----------------------------
        validator = DataValidator(
            dataframe
        )

        validator.validate_empty_dataset()

        validator.check_missing_values()

        validator.check_duplicate_rows()

        validator.generate_validation_report()

        validation_results = (
            validator.get_validation_results()
        )

        # -----------------------------
        # Exploratory Data Analysis
        # -----------------------------
        analyzer = EDAAnalyzer(
            dataframe
        )

        analyzer.statistical_summary()

        numerical_columns = (
            analyzer.numerical_feature_analysis()
        )

        categorical_columns = (
            analyzer.categorical_feature_analysis()
        )

        analyzer.correlation_analysis()

        outlier_report = (
            analyzer.detect_outliers()
        )

        # -----------------------------
        # Visualization
        # -----------------------------
        visualizer = Visualizer(
            dataframe
        )

        visualizer.generate_histograms()

        # -----------------------------
        # EDA Report
        # -----------------------------
        report = EDAReport()

        report.generate_report(
            dataframe,
            numerical_columns,
            categorical_columns,
            outlier_report,
        )

        # -----------------------------
        # Data Cleaning
        # -----------------------------
        cleaning_workflow = (
            CleaningWorkflow(
                dataframe,
                validation_results,
            )
        )

        cleaned_dataframe = (
            cleaning_workflow.start_cleaning()
        )

        # -----------------------------
        # Feature Engineering
        # -----------------------------
        feature_workflow = (
            FeatureWorkflow(
                cleaned_dataframe
            )
        )

        (
            X_train,
            X_test,
            y_train,
            y_test,
        ) = (
            feature_workflow
            .start_feature_engineering()
        )

        metadata = {
            "target_column": (
                feature_workflow
                .engineer
                .target_column
            ),
            "encoding_method": (
                feature_workflow
                .encoding_method
            ),
            "scaling_method": (
                feature_workflow
                .scaling_method
            ),
        }

        # -----------------------------
        # Model Training
        # -----------------------------
        training_workflow = (
            TrainingWorkflow(
                X_train,
                X_test,
                y_train,
                y_test,
                metadata=metadata,
                scaler=feature_workflow.scaler,
                encoders=(
                    feature_workflow
                    .engineer
                    .encoders
                ),
            )
        )

        training_workflow.start_training()

    except Exception as e:

        logger.error(e)

        print(
            f"\nError: {e}"
        )


def run_prediction():

    try:

        workflow = (
            PredictionWorkflow()
        )

        workflow.start_prediction()

    except Exception as e:

        logger.error(e)

        print(
            f"\nError: {e}"
        )


def main():

    logger.info(
        "Project Started"
    )

    print(
        f"\nProject Name      : {PROJECT_NAME}"
    )

    print(
        f"Project Version   : {PROJECT_VERSION}"
    )

    print(
        f"Environment       : {APP_ENV}"
    )

    print(
        f"Debug Mode        : {DEBUG}"
    )

    print(
        "\n========== AutoDS =========="
    )

    print(
        "1. Train Model"
    )

    print(
        "2. Predict"
    )

    print(
        "3. Exit"
    )

    choice = input(
        "\nEnter choice: "
    )

    if choice == "1":

        run_training()

    elif choice == "2":

        run_prediction()

    elif choice == "3":

        print(
            "\nThank you for using AutoDS."
        )

    else:

        print(
            "\nInvalid choice."
        )


if __name__ == "__main__":

    main()