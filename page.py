import pandas as pd

class Page:
    def __init__(self, con):
        
        self.base_queries = {'all': 'SELECT * FROM babies'}
        self.con = con
        self.base_data = None
        self.chart_data = None
        
        self.get_base_data()
        self.get_avg_score1_by_classe()
        
    def get_base_data(self):

        con = self.con
        self.base_data = {key: pd.read_sql(self.base_queries[key], con) for key in self.base_queries}

    def get_avg_score1_by_classe(self):
        data = self.base_data['all']
        self.chart_data = {'1': data.groupby('classe')['nota1'].mean().to_frame()}