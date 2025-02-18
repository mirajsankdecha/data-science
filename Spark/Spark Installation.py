# Databricks notebook source
sc = spark.sparkContext

# COMMAND ----------

num = [1,2,3,4,5]
num_rdd = sc.parallelize(num)
num_rdd.collect()

# COMMAND ----------

def eve_function(x):
    return x*2
n_rdd = sc.parallelize([1,2,3,4,5])
final_res = n_rdd.map(eve_function).collect()
print(final_res)

# COMMAND ----------

def eve_function(x):
    return x * 2
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Example").getOrCreate()

# COMMAND ----------

from pyspark import SparkContext

# Create an RDD from the list
listt = [1, 2, 3, 4, 5]
rdd = sc.parallelize(listt)

# Filter even numbers
even_rdd = rdd.filter(lambda x: x % 2 == 0)

# Collect and print the even numbers
even_numbers = even_rdd.collect()
print(even_numbers)

# COMMAND ----------
# FlatMap Example
num_rdd = sc.parallelize([1,2,3,4,5])
final_res = num_rdd.map(lambda x: range(1,x)).collect()
print(final_res)

# COMMAND ----------
# Distinct Example
num_rdd = sc.parallelize([1,2,3,4,5,1,2,3,4,5])
final_res = num_rdd.distinct().collect()
print(final_res)