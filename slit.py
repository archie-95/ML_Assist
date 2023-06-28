import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu



with st.sidebar:
    choose = option_menu("Menu", ["About", "Data Check", "AutoML", "Contact"],
                         icons=['house', 'clipboard2-data', 'cpu','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose=="Data Check":
    st.title("Hello world!")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        target_var = st.text_input("Target_Column", "target")
        if target_var:
            st.write("The Target column chosen is :",target_var)
            st.write(df[target_var].value_counts())