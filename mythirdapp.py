import streamlit as st
import numpy as np
import pandas as pd
import time

st.header("My third Streamlit App")

option = st.sidebar.selectbox(
    'Select a mini project',
     ['Long Process'])

else:
    'Starting a long computation...'
    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)

    '...and now we\'re done!'
