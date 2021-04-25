import streamlit as st
from connect import babies_params, connect
import psycopg2
import pandas as pd
import page


pg = page.Page(connect(babies_params))

st.title('app')

pg.chart_data['1']