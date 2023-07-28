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
if 'target_var_aml' not in st.session_state:
    st.session_state.target_var_aml=None
if 'genre_aml' not in st.session_state:
    st.session_state.genre_aml=None


def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

uploaded_file_aml = st.file_uploader("Choose a file")
submit =st.button("Submit")

if submit:
    st.session_state.df_aml = pd.read_csv(uploaded_file_aml)
    st.session_state.uploaded_file_aml=uploaded_file_aml

if st.session_state.df_aml is not None:
    st.write("File Uploaded is :",st.session_state.uploaded_file_aml.name)
    st.write(st.session_state.df_aml.head(5))

    l_col,r_col=st.columns(2)
    with l_col:
        target_var_aml=st.selectbox ("Target",tuple(st.session_state.df_aml.columns))
        genre_aml = st.selectbox("Type of Problem",('Classification', 'Regression'))

    with r_col:
        grid=make_grid(5,3)
        # grid[0][0].write('00')
        # grid[1][1].write('11')
        # grid[2][2].write('22')
        # grid[3][3].write('22')
        with grid[4][1]:
            begin_automl=st.button("Begin AutoML")
    if begin_automl:
        st.session_state.target_var_aml=target_var_aml
        st.session_state.genre_aml=genre_aml
    
    if st.session_state.target_var_aml is not None and st.session_state.genre_aml is not None:
        st.write("target Column Selected : ",st.session_state.target_var_aml)
        st.write("Type of Problem : ",st.session_state.genre_aml)


    
