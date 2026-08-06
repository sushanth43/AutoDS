import streamlit as st
import pandas as pd

import sys
from pathlib import Path

project_root = (
    Path(__file__).resolve().parents[2]
)

if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.cleaning.cleaner import DataCleaner

st.title("🧹 Data Cleaning")

if "dataframe" not in st.session_state:

    st.warning(
        "Please upload a dataset first."
    )

else:

    dataframe = (
        st.session_state["dataframe"]
    )

    st.subheader(
        "Missing Values Before Cleaning"
    )

    missing_before = (
        dataframe.isnull().sum()
    )

    missing_before_df = pd.DataFrame(
        {
            "Column": missing_before.index,
            "Missing Values": missing_before.values,
        }
    )

    st.dataframe(
        missing_before_df
    )

    st.subheader(
        "Cleaning Configuration"
    )

    numerical_strategy = st.selectbox(
        "Numerical Missing Value Strategy",
        [
            "mean",
            "median",
            "skip",
        ],
    )

    categorical_strategy = st.selectbox(
        "Categorical Missing Value Strategy",
        [
            "mode",
            "skip",
        ],
    )

    duplicate_strategy = st.selectbox(
        "Duplicate Row Strategy",
        [
            "first",
            "last",
            "skip",
        ],
    )

    if st.button(
        "Run Cleaning"
    ):

        cleaned_dataframe = (
            dataframe.copy()
        )

        cleaner = DataCleaner(
            cleaned_dataframe
        )

        numerical_columns = (
            cleaned_dataframe
            .select_dtypes(
                include=["number"]
            )
            .columns
            .tolist()
        )

        categorical_columns = (
            cleaned_dataframe
            .select_dtypes(
                exclude=["number"]
            )
            .columns
            .tolist()
        )

        if numerical_strategy != "skip":

            cleaned_dataframe = (
                cleaner.handle_missing_values(
                    strategy=numerical_strategy,
                    columns=numerical_columns,
                )
            )

            cleaner.dataframe = (
                cleaned_dataframe
            )

        if categorical_strategy != "skip":

            cleaned_dataframe = (
                cleaner.handle_missing_values(
                    strategy="mode",
                    columns=categorical_columns,
                )
            )

            cleaner.dataframe = (
                cleaned_dataframe
            )

        if duplicate_strategy != "skip":

            cleaned_dataframe = (
                cleaner.remove_duplicates(
                    keep=duplicate_strategy
                )
            )

        st.session_state[
            "cleaned_dataframe"
        ] = cleaned_dataframe

        st.success(
            "Cleaning completed successfully."
        )

        st.subheader(
            "Missing Values After Cleaning"
        )

        missing_after = (
            cleaned_dataframe.isnull().sum()
        )

        missing_after_df = pd.DataFrame(
            {
                "Column": missing_after.index,
                "Missing Values": missing_after.values,
            }
        )

        st.dataframe(
            missing_after_df
        )

        st.subheader(
            "Cleaned Dataset Preview"
        )

        st.dataframe(
            cleaned_dataframe.head()
        )