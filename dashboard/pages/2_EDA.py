import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Exploratory Data Analysis")

if "dataframe" not in st.session_state:

    st.warning(
        "Please upload a dataset first."
    )

else:

    dataframe = (
        st.session_state["dataframe"]
    )

    st.success(
        "Dataset loaded successfully."
    )

    # -------------------------
    # Dataset Shape
    # -------------------------
    st.subheader(
        "Dataset Shape"
    )

    st.write(
        dataframe.shape
    )

    # -------------------------
    # Data Types
    # -------------------------
    st.subheader(
        "Data Types"
    )

    st.dataframe(
        dataframe.dtypes.astype(str)
    )

    # -------------------------
    # Missing Values
    # -------------------------
    st.subheader(
        "Missing Values"
    )

    missing_values = (
        dataframe.isnull().sum()
    )

    missing_df = pd.DataFrame(
        {
            "Column": missing_values.index,
            "Missing Values": missing_values.values,
        }
    )

    st.dataframe(
        missing_df
    )

    # -------------------------
    # Missing Values Chart
    # -------------------------
    st.subheader(
        "Missing Values Chart"
    )

    missing_chart = (
        dataframe.isnull().sum()
    )

    missing_chart = (
        missing_chart[
            missing_chart > 0
        ]
    )

    if len(missing_chart) > 0:

        fig, ax = plt.subplots(
            figsize=(8, 4)
        )

        missing_chart.sort_values(
            ascending=False
        ).plot(
            kind="bar",
            ax=ax
        )

        ax.set_ylabel(
            "Missing Values"
        )

        st.pyplot(fig)

    else:

        st.success(
            "No missing values found."
        )

    # -------------------------
    # Statistical Summary
    # -------------------------
    st.subheader(
        "Statistical Summary"
    )

    st.dataframe(
        dataframe.describe()
    )

    # -------------------------
    # Correlation Heatmap
    # -------------------------
    st.subheader(
        "Correlation Heatmap"
    )

    numerical_dataframe = (
        dataframe.select_dtypes(
            include=["number"]
        )
    )

    if len(
        numerical_dataframe.columns
    ) > 1:

        correlation_matrix = (
            numerical_dataframe.corr()
        )

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            ax=ax,
        )

        st.pyplot(fig)

    else:

        st.info(
            "Not enough numerical columns for correlation analysis."
        )

    # -------------------------
    # Feature Distributions
    # -------------------------
    st.subheader(
        "Feature Distributions"
    )

    numerical_columns = (
        dataframe
        .select_dtypes(
            include=["number"]
        )
        .columns
    )

    selected_column = st.selectbox(
        "Select Numerical Feature",
        numerical_columns,
        key="histogram_column"
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.hist(
        dataframe[
            selected_column
        ].dropna(),
        bins=30
    )

    ax.set_title(
        selected_column
    )

    st.pyplot(fig)

    # -------------------------
    # Outlier Detection
    # -------------------------
    st.subheader(
        "Outlier Detection"
    )

    boxplot_column = st.selectbox(
        "Select Feature for Boxplot",
        numerical_columns,
        key="boxplot_column"
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.boxplot(
        dataframe[
            boxplot_column
        ].dropna()
    )

    ax.set_title(
        boxplot_column
    )

    st.pyplot(fig)

    # -------------------------
    # Numerical Columns
    # -------------------------
    st.subheader(
        "Numerical Columns"
    )

    numerical_columns_list = (
        dataframe
        .select_dtypes(
            include=["number"]
        )
        .columns
        .tolist()
    )

    st.write(
        numerical_columns_list
    )

    # -------------------------
    # Categorical Columns
    # -------------------------
    st.subheader(
        "Categorical Columns"
    )

    categorical_columns = (
        dataframe
        .select_dtypes(
            exclude=["number"]
        )
        .columns
        .tolist()
    )

    st.write(
        categorical_columns
    )