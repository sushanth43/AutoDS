import streamlit as st
import pandas as pd

st.title("📂 Dataset Upload")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    dataframe = pd.read_csv(
        uploaded_file
    )
    st.session_state["dataframe"] = dataframe

    st.success(
        "Dataset uploaded successfully!"
    )

    st.subheader(
        "Dataset Preview"
    )

    st.dataframe(
        dataframe.head()
    )

    st.subheader(
        "Dataset Information"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Rows",
            dataframe.shape[0]
        )

    with col2:

        st.metric(
            "Columns",
            dataframe.shape[1]
        )

    st.subheader(
        "Column Names"
    )

    st.write(
        list(dataframe.columns)
    )