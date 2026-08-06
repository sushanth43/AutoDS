import streamlit as st
import sys
from pathlib import Path

project_root = (
    Path(__file__).resolve().parents[2]
)

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.model_training.trainer import (
    Trainer,
)

st.title("🤖 Model Training")

required_keys = [
    "X_train",
    "X_test",
    "y_train",
    "y_test",
]

missing_keys = [
    key
    for key in required_keys
    if key not in st.session_state
]

if missing_keys:

    st.warning(
        "Please complete Feature Engineering first."
    )

else:

    X_train = st.session_state["X_train"]
    X_test = st.session_state["X_test"]

    y_train = st.session_state["y_train"]
    y_test = st.session_state["y_test"]

    scaler = st.session_state.get(
        "scaler"
    )

    encoders = st.session_state.get(
        "encoders"
    )

    st.success(
        "Feature engineered data loaded successfully."
    )

    st.subheader(
        "Dataset Summary"
    )

    st.write(
        f"X_train Shape: {X_train.shape}"
    )

    st.write(
        f"X_test Shape: {X_test.shape}"
    )

    st.write(
        f"y_train Shape: {y_train.shape}"
    )

    st.write(
        f"y_test Shape: {y_test.shape}"
    )

    if st.button(
        "Train Models"
    ):

        with st.spinner(
            "Training models..."
        ):
            print("\nSCALER:")
            print(scaler)

            print("\nENCODERS:")
            print(encoders)
            trainer = Trainer(
                X_train,
                X_test,
                y_train,
                y_test,
                
                metadata={
                    "encoding_method":st.session_state.get( "encoding_method"),
                    "scaling_method":st.session_state.get( "scaling_method"),
                    "target_column":st.session_state.get( "target_column"),
                },
                scaler=scaler,
                encoders=encoders,
            )

            problem_type = (
                trainer.detect_problem_type()
            )

            trainer.build_model_registry()

            trainer.train_models()

            trainer.evaluate_models()

            results_dataframe = (
                trainer.build_results_dataframe()
            )

            (
                best_model_name,
                best_model,
                best_score,
            ) = trainer.identify_best_model()

            trainer.save_best_model()

            trainer.save_scaler()

            trainer.save_encoders()

            trainer.save_metadata()

            st.session_state[
                "trainer"
            ] = trainer

            st.session_state[
                "results_dataframe"
            ] = results_dataframe

            st.session_state[
                "best_model_name"
            ] = best_model_name

            st.session_state[
                "best_score"
            ] = best_score

            st.session_state[
                "problem_type"
            ] = problem_type

        st.success(
            "Model Training Completed Successfully."
        )

        st.subheader(
            "Problem Type"
        )

        st.write(
            problem_type
        )

        st.subheader(
            "Model Leaderboard"
        )

        st.dataframe(
            results_dataframe,
            use_container_width=True,
        )

        st.subheader(
            "🏆 Best Model"
        )

        st.write(
            f"Model: {best_model_name}"
        )

        if (
            problem_type
            == "Classification"
        ):

            st.write(
                f"Accuracy: {best_score}"
            )

        else:

            st.write(
                f"R2 Score: {best_score}"
            )

        st.subheader(
            "Saved Artifacts"
        )

        st.write(
            "✓ best_model.pkl"
        )

        st.write(
            "✓ metadata.json"
        )

        if scaler is not None:

            st.write(
                "✓ scaler.pkl"
            )

        if encoders:

            st.write(
                "✓ encoders.pkl"
            )