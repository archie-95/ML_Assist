import pandas as pd
import evalml
import woodwork as ww
from evalml.automl import AutoMLSearch
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
if 'objective_function' not in st.session_state:
    st.session_state.objective_function=None
if 'automl' not in st.session_state:
    st.session_state.automl=None


def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


#Objectives for different Types of Problem 

binary_objective = ('MCC Binary',
 'Log Loss Binary',
 'Gini',
 'AUC',
 'Precision',
 'F1',
 'Balanced Accuracy Binary',
 'Accuracy Binary')

regression_objective = ('ExpVariance',
 'MaxError',
 'MedianAE',
 'MSE',
 'MAE',
 'R2',
 'Root Mean Squared Error')

multiclass_objective = ('MCC Multiclass',
 'Log Loss Multiclass',
 'AUC Weighted',
 'AUC Macro',
 'AUC Micro',
 'Precision Weighted',
 'Precision Macro',
 'Precision Micro',
 'F1 Weighted',
 'F1 Macro',
 'F1 Micro',
 'Balanced Accuracy Multiclass',
 'Accuracy Multiclass')

uploaded_file_aml = st.file_uploader("Choose a file")
submit =st.button("Submit")

def begin_automl_onclick():
        st.session_state.target_var_aml=target_var_aml
        st.session_state.genre_aml=genre_aml
        st.session_state.objective_function=objective_function
        st.session_state.automl=None

if submit:
    st.session_state.df_aml = pd.read_csv(uploaded_file_aml)
    st.session_state.uploaded_file_aml=uploaded_file_aml

if st.session_state.df_aml is not None:
    st.write("File Uploaded is :",st.session_state.uploaded_file_aml.name)
    st.write(st.session_state.df_aml.head(5))

    l_col,r_col=st.columns(2)
    with l_col:
        target_var_aml=st.selectbox ("Target",tuple(st.session_state.df_aml.columns))
        genre_aml = st.selectbox("Type of Problem",('Binary','Multiclass' ,'Regression'))
        if genre_aml=="Binary":
            objective_function=st.selectbox("Objective Function",binary_objective)
        if genre_aml=="Multiclass":
            objective_function=st.selectbox("Objective Function",multiclass_objective)
        if genre_aml=="Regression":
            objective_function=st.selectbox("Objective Function",regression_objective)
        

    with r_col:
        grid=make_grid(5,3)
        # grid[0][0].write('00')
        # grid[1][1].write('11')
        # grid[2][2].write('22')
        # grid[3][3].write('22')
        with grid[4][1]:
            begin_automl=st.button("Begin AutoML",on_click=begin_automl_onclick)



    
    if st.session_state.target_var_aml is not None and st.session_state.genre_aml is not None:
        st.write("target Column Selected : ",st.session_state.target_var_aml)
        st.write("Type of Problem : ",st.session_state.genre_aml)
    
    if st.session_state.target_var_aml is not None and st.session_state.genre_aml is not None and st.session_state.automl is None:
        X=st.session_state.df_aml.drop(st.session_state.target_var_aml,axis=1)
        Y=st.session_state.df_aml[st.session_state.target_var_aml]
        X.ww.init()
        Y.ww.init()
        X_train, X_test, y_train, y_test = evalml.preprocessing.split_data(X, Y, problem_type=st.session_state.genre_aml.lower(),test_size=.2)
        st.write("Split Done")
        with st.spinner("Wait for It"):
            st.session_state.automl = AutoMLSearch(X_train=X_train, y_train=y_train, problem_type=st.session_state.genre_aml.lower(), objective=st.session_state.objective_function,verbose=True,)
            st.session_state.automl.search()
        st.success('Done')

    if st.session_state.automl is not None:
        st.write(st.session_state.automl.rankings)
        st.write("Best Pipeline : ",st.session_state.automl.best_pipeline)

    
