import streamlit as st
from connect import babies_params, connect
import psycopg2
import pandas as pd
import page
import modules

pg = page.Page(connect(babies_params))

task = st.sidebar.selectbox('task', ['read', 'create', 'update', 'delete', 'groupby'])

if task == 'read':

    filtro = st.sidebar.selectbox('filter', ['none', 'ano'], index = 0)
    
    if filtro == 'none':

        data = pg.base_data['all']
        data

    elif filtro == 'ano':
        
        ret = pg.year_range()
        ret

if task == 'groupby':

    filtro = st.selectbox('filter', ['ano/score'], index = 0)

    if filtro == 'ano/score':
        ret = pg.groupby_year_and_class()
        ret