
#Sidebar with styling , icons are from bootstrap
# with st.sidebar:
#     choose = option_menu("Menu", ["About", "Data Check", "AutoML", "Contact"],
#                          icons=['house', 'clipboard2-data', 'cpu','person lines fill'],
#                          menu_icon="app-indicator", default_index=0,
#                          styles={
#         "container": {"padding": "5!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "#02ab21"},
#     }
#     )

# Data check file 

import streamlit as st 
st.markdown(
    """
    <style>

    [data-testid="stSidebarNav"] {
                background-image: url("C:\Work\Project\logo.png");
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }

    </style>
    """,
    unsafe_allow_html=True,
)

