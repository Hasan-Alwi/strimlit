import streamlit as st
import pandas as pd 
import numpy as np

st.title('SIMPLE VEKTOR MATRIKS')

with st.sidebar:
    tipe = st.radio('pilih tipe', ['single vektor', 'double matriks'])

with st.expander('pilih ukuran'):
    with st.form('pilih ukuran'):
        if tipe == 'single vektor':
           size = st.number_input('pilih ukuran dari vektor', min_value=2)
        elif tipe == 'double matriks':
            col = st.number_input('pilih baris dari matriks pertama', min_value=2)
            row1 = st.number_input('pilih kolom dari matriks pertama', min_value=2)
            col2 = st.number_input('pilih baris dari matriks kedua', min_value=2)
            row2 = st.number_input('pilih kolom dari matriks kedua', min_value=2)
        st.form_submit_button('kirim ukuran')
