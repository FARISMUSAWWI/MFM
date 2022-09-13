import streamlit as st
import pandas as pd

st.header("My first Streamlit App")

st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))