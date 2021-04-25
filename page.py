import pandas as pd
import streamlit as st
class Page:
    def __init__(self, con):
        
        self.base_queries = {'all': 'SELECT * FROM babies'}
        self.con = con
        self.base_data = None
        self.chart_data = None
        
        self.get_base_data()
       
        
    def get_base_data(self):

        con = self.con
        self.base_data = {key: pd.read_sql(self.base_queries[key], con) for key in self.base_queries}

    def year_range(self):
        
        data = self.base_data['all']

        min, max = st.sidebar.slider('year range', min_value = int(data['ano'].min()), max_value = int(data['ano'].max()), value = (2000, 2020), step = 1)
        
        data = data.loc[(data['ano'] >= min) & (data['ano'] <= max)]
        
        return data

    def groupby_year_and_class(self):

        data = self.base_data['all']

        min, max = st.slider('year range', min_value = int(data['ano'].min()), max_value = int(data['ano'].max()), value = (2000, 2020), step = 1)
        classes = st.multiselect('classes', data['classe'].unique().tolist(), data['classe'].unique().tolist())

        data = data.loc[(data['ano'] >= min) & (data['ano'] <= max)]
        data = data.loc[data['classe'].isin(classes)]
        
        if len(classes) > 0:
            return data.groupby(['classe', 'ano'])['nota1', 'nota2', 'nota3'].mean()

        else:
            return st.warning('selecione classes')
