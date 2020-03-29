import pandas as pd

def write_parquet_file():
    df = pd.read_csv('data/us_presidents.csv')
    df.to_parquet('tmp/us_presidents.parquet')

def display_parquet_data():
    df = pd.read_parquet('tmp/us_presidents.parquet')
    print(df)

