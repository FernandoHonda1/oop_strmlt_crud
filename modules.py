import streamlit as st
import numpy as np

def year_range(data):

        min, max = st.sidebar.slider('year range', min_value = int(data['ano'].min()), max_value = int(data['ano'].max()), value = (2000, 2020), step = 1)
        
        data = data.loc[(data['ano'] >= min) & (data['ano'] <= max)]
        
        return data