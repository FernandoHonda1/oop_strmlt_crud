import psycopg2

babies_params = {'database': 'strmlt_crud_db',
                 'user': 'postgres',
                 'password': '5432',
                 'host': 'localhost'}

def connect(prms):
    connection = psycopg2.connect(database = prms['database'],
                                 user = prms['user'],
                                 password = prms['password'],
                                 host = prms['host'])

    return connection

