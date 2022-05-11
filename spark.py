from pyspark.sql import SparkSession
import json
from pyspark.sql.functions import to_json, col
import os

spark_version = '3.2.1'
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka0-10_2.12:{}'.format(spark_version, spark_version)

def foreach_batch_function(dff, epoch_id):
    print("******************************************")
    new_df = dff.select("value")
    new_df.show()
    val = new_df.collect()
    info = []
    for i in val:
        data = json.loads(i[0])
        info.append(data)

    final_df = spark.createDataFrame(info)
    final_df.show()
    final_df.write.format("mongo").mode("append").option("database", "twitter_data").option("collection", "info").save()
    print("******************************************")


spark = SparkSession.builder.appName("Kafka_Tweet_app").config("spark.mongodb.input.uri", "mongodb://localhost:27017").config("spark.mongodb.output.uri", "mongodb://localhost:27017") .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1").master('local').getOrCreate()

df = spark.readStream.format("kafka").option("startingOffsets", "earliest").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "Topic_1").load()

events = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

events.writeStream.foreachBatch(foreach_batch_function).start().awaitTermination()

# ssc.start() ssc.awaitTermination() will start the streaming jon, which will continually run it until you kill it with (control-)(-c-).
