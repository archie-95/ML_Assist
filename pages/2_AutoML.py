import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
import dtale as dt


st.write(st.session_state)
st.markdown("<h1 style='text-align: center;'>Auto ML</h1>", unsafe_allow_html=True)

if 'df_aml' not in st.session_state:
    st.session_state.df_aml=None
if 'uploaded_file_aml' not in st.session_state:
    st.session_state.uploaded_file_aml=None


uploaded_file_aml = st.file_uploader("Choose a file")
submit =st.button("Submit")

if submit:
    st.session_state.df_aml = pd.read_csv(uploaded_file_aml)
    st.session_state.uploaded_file_aml=uploaded_file_aml

if st.session_state.df_aml is not None:
    st.write("File Uploaded is :",st.session_state.uploaded_file_aml.name)
    st.write(st.session_state.df_aml.head(5))