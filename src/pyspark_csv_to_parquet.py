from pyspark.sql import SparkSession

spark = SparkSession.builder \
  .master("local") \
  .appName("parquet_example") \
  .getOrCreate()

def write_parquet_file():
    df = spark.read.csv('data/us_presidents.csv', header = True)
    df.repartition(1).write.mode('overwrite').parquet('tmp/pyspark_us_presidents')

def display_parquet_data():
    df = spark.read.parquet('tmp/pyspark_us_presidents')
    df.show()

