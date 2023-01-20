import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Title
st.markdown('''
# **Exploratory Data Analysis Web Application**
This app is developed by **Mohammad Wasiq** called EDA App 
''')

# How to upload a file from pc
with st.sidebar.header("Upload Your Dataset File (.csv)"):
    uploaded_file= st.sidebar.file_uploader("Upload your File", type=['csv'])
    df= sns.load_dataset('titanic')
    st.sidebar.markdown("[Example .csv file](https://www.kaggle.com/datasets/senapatirajesh/netflix-tv-shows-and-movies?select=NetFlix.csv)")

# Profiling Report for Pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv= pd.read_csv(uploaded_file)
        return csv
    df= load_csv()
    pr= ProfileReport(df, explorative=True)
    st.header('**Input DF**')
    st.write(df)
    st.write('----')
    st.header('**Profiling Report with Pandas**')
    st_profile_report(pr)

else:
    st.info("Awaiting for csv file, upload the file otherwise you can't complete EDA")
    if st.button("Press to use Example Data"):
         # Example dataset
        @st.cache
        def load_data():
            a= pd.DataFrame(np.random.rand(100, 5),
                            columns=['age', 'height', 'weight', 'height1', 'weight1'])
            return a
        df= load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DF**')
        st.write(df)
        st.write('----')
        st.header('**Profiling Report with Pandas**')
        st_profile_report(pr)
