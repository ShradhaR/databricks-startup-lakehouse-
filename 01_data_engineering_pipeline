# 1. Bronze Layer: Simulate data streaming/ingestion into a Delta Table
from pyspark.sql.functions import current_timestamp, lit

# Dummy data simulating startup user activity logs
data = [
    ("user_1", "click", "2026-06-01", 10.5),
    ("user_2", "login", "2026-06-01", 0.0),
    ("user_3", "purchase", "2026-06-02", 99.9),
]
columns = ["user_id", "event_type", "event_date", "revenue"]

df_raw = spark.createDataFrame(data, columns).withColumn("ingested_at", current_timestamp())

# Write to Bronze Delta Table
df_raw.write.format("delta").mode("append").saveAsTable("bronze_user_events")

# 2. Silver Layer: Clean and enrich data
df_silver = spark.table("bronze_user_events") \
    .filter("user_id IS NOT NULL") \
    .withColumn("is_premium", lit(True))

df_silver.write.format("delta").mode("overwrite").option("overwriteSchema", "true").saveAsTable("silver_user_events")

# 3. Gold Layer: Aggregated business metrics for BI/ML
df_gold = spark.table("silver_user_events") \
    .groupBy("user_id") \
    .sum("revenue").withColumnRenamed("sum(revenue)", "total_spend")

df_gold.write.format("delta").mode("overwrite").saveAsTable("gold_user_features")
