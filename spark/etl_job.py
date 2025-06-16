from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("IrisETLJob").getOrCreate()

spark._jsc.hadoopConfiguration().set("fs.s3a.access.key", "minioadmin")
spark._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "minioadmin")
spark._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://minio:9000")
spark._jsc.hadoopConfiguration().set("fs.s3a.path.style.access", "true")
spark._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

df = spark.read.option("header", True).csv("s3a://ml-data/raw/iris.csv")

filtered_df = df.filter(df["petal_length"] > 1.5)

filtered_df.write.mode("overwrite").option("header", True).csv("s3a://ml-data/processed/iris_cleaned.csv")

spark.stop()