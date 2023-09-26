from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder.appName("ReadFromKafka").getOrCreate()

# Define Schema for incoming data
kafka_schema = StructType([
    StructType().add("key", StringType()),
    StructType().add("value", StringType())
])

# Read from Kafka Topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic_name") \
    .load()

# Transform and store in HDFS Parquet - RAW Zone
df.writeStream.format("parquet").option("path", "path/to/raw_zone").start()