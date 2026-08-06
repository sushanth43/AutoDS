import streamlit as st
import sys
from pathlib import Path

project_root = (
    Path(__file__).resolve().parents[2]
)

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.feature_engineering.engineer import (
    FeatureEngineer,
)

st.title("⚙️ Feature Engineering")

if "cleaned_dataframe" not in st.session_state:

    st.warning(
        "Please complete the cleaning step first."
    )

else:

    dataframe = (
        st.session_state["cleaned_dataframe"]
    )

    st.success(
        "Cleaned dataset loaded successfully."
    )

    st.subheader(
        "Feature Engineering Configuration"
    )

    target_column = st.selectbox(
        "Target Column",
        dataframe.columns,
    )

    encoding_method = st.selectbox(
        "Encoding Method",
        [
            "label",
            "onehot",
            "skip",
        ],
    )

    test_size_option = st.selectbox(
        "Test Size",
        [
            "20%",
            "25%",
            "30%",
        ],
    )

    scaling_method = st.selectbox(
        "Scaling Method",
        [
            "standard",
            "minmax",
            "robust",
            "skip",
        ],
    )

    if st.button(
        "Run Feature Engineering"
    ):

        engineer = FeatureEngineer(
            dataframe
        )

        engineer.select_target(
            target_column
        )

        if encoding_method != "skip":

            engineer.encode_categorical(
                encoding_method
            )

        if test_size_option == "20%":

            test_size = 0.20

        elif test_size_option == "25%":

            test_size = 0.25

        else:

            test_size = 0.30

        (
            X_train,
            X_test,
            y_train,
            y_test,
        ) = engineer.train_test_split_data(
            test_size=test_size
        )

        if scaling_method != "skip":

            X_train, X_test = (
                engineer.scale_features(
                    scaling_method
                )
            )

        st.session_state[
            "X_train"
        ] = X_train

        st.session_state[
            "X_test"
        ] = X_test

        st.session_state[
            "y_train"
        ] = y_train

        st.session_state[
            "y_test"
        ] = y_test

        st.session_state[
            "target_column"
        ] = target_column

        st.session_state[
            "encoding_method"
        ] = encoding_method

        st.session_state[
            "scaling_method"
        ] = scaling_method

        st.session_state[
            "feature_engineer"
        ] = engineer

        st.session_state[
            "scaler"
        ] = engineer.scaler

        st.session_state[
            "encoders"
        ] = engineer.encoders

        st.success(
            "Feature Engineering Completed Successfully."
        )

        st.subheader(
            "Configuration Summary"
        )

        st.write(
            f"Target Column: {target_column}"
        )

        st.write(
            f"Encoding Method: {encoding_method}"
        )

        st.write(
            f"Scaling Method: {scaling_method}"
        )

        st.write(
            f"Test Size: {int(test_size * 100)}%"
        )

        st.subheader(
            "Dataset Shapes"
        )

        st.write(
            f"X_train: {X_train.shape}"
        )

        st.write(
            f"X_test: {X_test.shape}"
        )

        st.write(
            f"y_train: {y_train.shape}"
        )

        st.write(
            f"y_test: {y_test.shape}"
        )

        st.subheader(
            "Engineered Features"
        )

        st.write(
            list(X_train.columns)
        )