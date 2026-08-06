import streamlit as st
import pandas as pd
import sys
from pathlib import Path

project_root = (
    Path(__file__).resolve().parents[2]
)

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.prediction.predictor import Predictor

st.title("🔮 Prediction")

uploaded_file = st.file_uploader(
    "Upload Prediction Dataset",
    type=["csv"],
)

if uploaded_file is not None:

    dataframe = pd.read_csv(
        uploaded_file
    )

    st.success(
        "Dataset uploaded successfully."
    )

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        dataframe.head(),
        use_container_width=True,
    )

    st.write(
        f"Rows: {dataframe.shape[0]}"
    )

    st.write(
        f"Columns: {dataframe.shape[1]}"
    )

    if st.button(
        "Generate Predictions"
    ):

        with st.spinner(
            "Generating predictions..."
        ):

            predictor = Predictor()

            predictor.load_model()

            predictor.load_metadata()

            predictor.load_scaler()

            predictor.load_encoders()

            processed_df = (
                predictor.preprocess_data(
                    dataframe
                )
            )

            predictions = (
                predictor.predict(
                    processed_df
                )
            )

            output_file = (
                predictor.save_predictions(
                    predictions
                )
            )

            prediction_df = pd.DataFrame(
                {
                    "Prediction": predictions
                }
            )

            st.session_state[
                "predictions"
            ] = prediction_df

        st.success(
            "Predictions Generated Successfully."
        )

        st.subheader(
            "Prediction Results"
        )

        st.dataframe(
            prediction_df.head(20),
            use_container_width=True,
        )

        csv = (
            prediction_df
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="Download Predictions",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv",
        )