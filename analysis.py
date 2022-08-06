from pyspark.sql import SparkSession
from pyspark.sql.functions import trim

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

sc = spark.sparkContext

def get_sorted_price_data():
    sorted_price_df = spark.sql("SELECT year, substring(type, 0, 2) as type_id,substring(type, 4, length(type) - 2) as type, year, grade  from coins_raw") 

    return sorted_price_df


def get_sort_coin_df():

    sorted_df = spark.sql("SELECT id, substring(type, 0, 2) as type_id,substring(type, 4, length(type) - 2) as type, year, grade  from coins_raw") 

    return sorted_df


path = "./database/coins.csv"

df = spark.read.option("header",True) \
     .csv("./database/coins.csv")    

df.registerTempTable("coins_raw")

sorted_df = get_sort_coin_df()

price_data_df = spark.read.option("header",True) \
     .csv("./database/penny_prices.csv")    
price_data_df.registerTempTable("price_data")

coin_data_with_price = sorted_df.join(price_data_df, trim(sorted_df['year']) == trim(price_data_df['Year  ']), 'left').where(sorted_df['type_id'] == 0)

coin_data_with_price.write.csv('coin_price_data.csv', header=True)
