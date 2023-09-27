import findspark
findspark.init()
from pyspark.sql import *
from Industry_project1.src.main.utility.logging_config import *

def spark_session():
    spark = SparkSession.builder.master("local[*]") \
        .appName("Project_spark2")\
        .config("spark.driver.extraClassPath", "D:\\Industry_DE_project\\Industry_project2-venv\\Lib\\site-packages\\mysql-connector-java-8.0.29\\mysql-connector-java-8.0.29.jar") \
        .getOrCreate()
    logger.info("spark session %s",spark)
    return spark
