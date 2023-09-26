from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder.appName("StreamToKafka").getOrCreate()

# Sample XML Schema
xml_schema = StructType() \
    .add("user", StructType() \
         .add("id", StringType()) \
         .add("name", StringType()))

# Sample DataFrame (For Demonstration purposes)
data = [("1", "<user><id>123</id><name>John Doe</name></user>")]
df = spark.createDataFrame(data, ["key", "value"])

# Assuming we have a function to parse and flatten XML
# df = parse_and_flatten_xml(df, xml_schema)

query = df.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", "topic_name") \
    .option("checkpointLocation", "path/to/checkpoints") \
    .start()

query.awaitTermination()