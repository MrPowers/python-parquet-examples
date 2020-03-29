import databricks.koalas as ks

def write_parquet_file():
    df = ks.read_csv('data/us_presidents.csv')
    df.to_parquet('tmp/koala_us_presidents')

def display_parquet_data():
    df = ks.read_parquet('tmp/koala_us_presidents')
    print(df)

write_parquet_file()
display_parquet_data()

