from snowflake.connector.pandas_tools import pd_writer
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

def loading_csv():
    
    engine = create_engine(URL(
    account = 'ieb90279.us-east-1',
    user = 'xxxxxx',#type ur username
    password = 'xxxxx',#type ur pass word
    database  = 'FLIGHTS',
    schema='PUBLIC',
    warehouse = 'compute'
))
    file_path = '/home/sivachandan/Flight_Prediction_Delay/data/final_data.csv'
    table_name = 'data'
    with engine.connect() as conn:
        df = pd.read_csv('/home/sivachandan/Flight_Prediction_Delay/data/final_data.csv')
        df.columns = map(lambda x: str(x).upper(), df.columns)
        df.to_sql(name='data', con=conn, if_exists='replace', method=pd_writer,index =False)
        conn.execute(f"put file://{file_path} @%{table_name} ")
        conn.execute(f"copy into {table_name} FILE_FORMAT = (FORMAT_NAME = my_csv_format)") 
    return True
def insert_data():
    engine = create_engine(URL(
    account = 'ieb90279.us-east-1',
    user = 'sivachandan',
    password = 'Sivaking1@',
    database  = 'FLIGHTS',
    schema='PUBLIC',
    warehouse = 'compute'
)) 
    with engine.connect() as conn:
        file_path = '/home/sivachandan/Flight_Prediction_Delay/input.csv'
        table_name = 'data'
        df = pd.read_csv('/home/sivachandan/Flight_Prediction_Delay/input.csv')
        df.columns = map(lambda x: str(x).upper(), df.columns)
        print(df)
        df.to_sql('data', con=conn, index=False, method=pd_writer,if_exists='append')
        print("Added data")
            
if __name__=='__main__':
    insert_data()