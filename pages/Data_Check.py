import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


st.write(st.session_state)
st.markdown("<h1 style='text-align: center;'>Data Check</h1>", unsafe_allow_html=True)


## initializing the session_state variables ###

if 'df' not in st.session_state:
    st.session_state.df=None

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file=None

if 'target_var' not in st.session_state:
    st.session_state.target_var=None

if 'genre' not in st.session_state:
    st.session_state.genre=None

uploaded_file = st.file_uploader("Choose a file")
submit =st.button("Submit")

if submit :
    st.session_state.df = pd.read_csv(uploaded_file)
    st.session_state.uploaded_file=uploaded_file

if st.session_state.df is not None:
    st.write("File Uploaded is :",st.session_state.uploaded_file.name)
    st.write(st.session_state.df.head(5))
    l_col,r_col=st.columns(2)
    with l_col:
        target_var = st.selectbox("Target Column",tuple(st.session_state.df.columns))

    with r_col:
        genre = st.selectbox("Type of Problem",('Classification', 'Regression'))

    if st.button("Target Analysis"):
        st.session_state.target_var=target_var
        st.session_state.genre=genre

    if st.session_state.target_var is not None and st.session_state.genre is not None:
        st.write("target Column Selected : ",st.session_state.target_var)
        st.write("Type of Problem : ",st.session_state.genre)
    if st.session_state.genre=='Classification' and st.session_state.genre is not None:
        if 'fig' not in st.session_state:
            st.session_state.fig = plt.figure(figsize=(10, 4))
        sns.countplot(x=target_var,data=st.session_state.df)
        st.pyplot(st.session_state.fig)

    if st.session_state.genre == "Regression" and st.session_state.genre is not None:
        fig = plt.figure(figsize=(10, 4))
        sns.distplot(st.session_state.df[st.session_state.target_var])
        st.pyplot(fig)
            
    if st.button("Generate Data Profile"):
        pr = ProfileReport(st.session_state.df)
        st_profile_report(pr)
