import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="🚆 Data Sweeper By Abdul Waheed", layout='wide')
st.title("🚆 Data Sweeper - Transform Your Files")

st.write("Transform your files between CSV and Excel with options for data cleaning, visualization, and summary statistics. You can also view summary statistics of your data and download the cleaned data after processing.")


uploaded_file = st.file_uploader("Upload a file (CSV or Excel)", type=['csv', 'xlsx'], accept_multiple_files=True, label_visibility="visible")

if uploaded_file: 
    st.success("File uploaded successfully!")

    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == '.csv':
            try:
                df = pd.read_csv(file)
                st.write("Summary Statistics:")
                st.write(df.describe())  # Display summary statistics
            except Exception as e:
                st.error(f"Error reading CSV file: {e}. Please ensure the file is not corrupted and is in the correct format. If the issue persists, try a different file or reach out for support.")
                continue

        elif file_ext == '.xlsx':
            try:
                df = pd.read_excel(file)
                st.write("Summary Statistics:")
                st.write(df.describe())  # Display summary statistics
            except Exception as e:
                st.error(f"Error reading Excel file: {e}. Please ensure the file is not corrupted and is in the correct format. If the issue persists, try a different file or reach out for support.")
                continue
