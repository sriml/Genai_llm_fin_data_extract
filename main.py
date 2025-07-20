import streamlit as st
import pandas as pd
from data_extractor import extract

st.title("Financial Data Extractor")

paragraph = st.text_area("Enter financial paragraph:")

if st.button("Extract"):
    if paragraph:
        extracted_data = extract(paragraph)
        data = {
            "Measure" : ["Revenue", "EPS"],
            "Estimated" : [extracted_data["revenue_expected"], extracted_data["eps_expected"]],
            "Actual" : [extracted_data["revenue_actual"], extracted_data["eps_actual"]]
        }
        df = pd.DataFrame(data)
        st.table(df)
    else:
        st.warning("Please enter a paragraph to extract data from.")
