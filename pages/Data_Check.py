import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


st.write(st.session_state)
st.markdown("<h1 style='text-align: center;'>Data Check</h1>", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    if 'df' not in st.session_state:
        st.session_state.df = pd.read_csv(uploaded_file)
    st.write(st.session_state.df)
    l_col,r_col=st.columns(2)
    with l_col:
        target_var = st.selectbox("Target Column",tuple(st.session_state.df.columns))

    with r_col:
        genre = st.radio("Classification or Regression",('Classification', 'Regression'))

    if st.button("Target Analysis"):
        if target_var not in st.session_state.df.columns:
            st.write ("Target variable not found")
        else :
            if genre=='Classification':
                if 'fig' not in st.session_state:
                    st.session_state.fig = plt.figure(figsize=(10, 4))
                sns.countplot(x=target_var,data=st.session_state.df)
                st.pyplot(st.session_state.fig)

            if genre == "Regression":
                fig = plt.figure(figsize=(10, 4))
                sns.distplot(st.session_state.df[target_var])
                st.pyplot(fig)
            
    if st.button("Generate Data Profile"):
        pr = ProfileReport(st.session_state.df)
        st_profile_report(pr)
