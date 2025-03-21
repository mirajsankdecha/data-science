# Databricks Notebook

# COMMAND ----------
# MAGIC %md
# MAGIC # Apache Spark RDD Operations with Detailed Explanation
# MAGIC 
# MAGIC This notebook demonstrates various RDD (Resilient Distributed Dataset) operations in Apache Spark using Databricks. It includes explanations of how each operation works and its significance in distributed data processing.

# COMMAND ----------
# Initializing SparkContext
sc = spark.sparkContext

# COMMAND ----------
# MAGIC %md
# MAGIC ## Creating an RDD
# MAGIC **What is happening?**
# MAGIC - We use `parallelize()` to create an RDD from a Python list.
# MAGIC - RDD (Resilient Distributed Dataset) is a fundamental data structure in Spark, representing an immutable distributed collection of objects.

# COMMAND ----------
num = [1, 2, 3, 4, 5]
num_rdd = sc.parallelize(num)
print("RDD Contents:", num_rdd.collect())

# COMMAND ----------
# MAGIC %md
# MAGIC ## Finding Maximum Value
# MAGIC **What is happening?**
# MAGIC - We use the `reduce()` function to find the maximum value in the RDD.
# MAGIC - `reduce()` works by applying a binary function cumulatively to the elements of the RDD.

# COMMAND ----------
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num_rdd = sc.parallelize(num_list)
max_value = num_rdd.reduce(lambda x, y: x if x > y else y)
print("Maximum Value:", max_value)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Applying `map()` Transformation
# MAGIC **What is happening?**
# MAGIC - `map()` is a transformation that applies a given function to each element of the RDD.
# MAGIC - Here, we multiply each element by 2.
# MAGIC - The output is a new RDD containing the transformed values.

# COMMAND ----------
n_rdd = sc.parallelize([1, 2, 3, 4, 5])
final_res = n_rdd.map(lambda y: y * 2).collect()
print("Doubled Values:", final_res)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Filtering Even Numbers
# MAGIC **What is happening?**
# MAGIC - `filter()` is used to keep only elements that satisfy a given condition.
# MAGIC - We filter out even numbers by checking if each element is divisible by 2.

# COMMAND ----------
rdd = sc.parallelize(range(1, 21))  # RDD from 1 to 20
final_res = rdd.filter(lambda x: x % 2 == 0).collect()
print("Even Numbers:", final_res)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Sorting RDD Based on Elements
# MAGIC **What is happening?**
# MAGIC - We use `sortBy()` to sort elements based on a specific index in a tuple.
# MAGIC - Sorting can be done in ascending or descending order.
# MAGIC - Here, we sort by the third and second values in the tuple.

# COMMAND ----------
pairs = [("a", 5, 10), ("d", 3, 9), ("c", 2, 11), ("b", 3, 9)]
rdd = sc.parallelize(pairs)

sorted_by_third_asc = rdd.sortBy(lambda x: x[2])
print("Sorted by Third Element Ascending:", sorted_by_third_asc.collect())

sorted_by_third_desc = rdd.sortBy(lambda x: x[2], ascending=False)
print("Sorted by Third Element Descending:", sorted_by_third_desc.collect())

sorted_by_second_asc = rdd.sortBy(lambda x: x[1])
print("Sorted by Second Element Ascending:", sorted_by_second_asc.collect())

# COMMAND ----------
# MAGIC %md
# MAGIC ## Sorting RDD Using `sortByKey()`
# MAGIC **What is happening?**
# MAGIC - `sortByKey()` sorts an RDD based on the key in (key, value) pairs.
# MAGIC - Sorting can be in ascending or descending order.

# COMMAND ----------
key_value_pairs = sc.parallelize([(3, "apple"), (1, "banana"), (2, "cherry"), (4, "date")])

sorted_asc = key_value_pairs.sortByKey()
print("Sorted by Key Ascending:", sorted_asc.collect())

sorted_desc = key_value_pairs.sortByKey(ascending=False)
print("Sorted by Key Descending:", sorted_desc.collect())

# COMMAND ----------
# MAGIC %md
# MAGIC ## Using a Function with `map()`
# MAGIC **What is happening?**
# MAGIC - Instead of using a lambda function, we define a function `eve_function()` that doubles a value.
# MAGIC - We pass this function to `map()` to transform the RDD.

# COMMAND ----------
def eve_function(x):
    return x * 2

n_rdd = sc.parallelize([1, 2, 3, 4, 5])
final_res = n_rdd.map(eve_function).collect()
print("Function-based Mapping Result:", final_res)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Filtering Even Numbers with `filter()`
# MAGIC **What is happening?**
# MAGIC - We use `filter()` to keep only even numbers from the RDD.

# COMMAND ----------
listt = [1, 2, 3, 4, 5]
rdd = sc.parallelize(listt)
even_rdd = rdd.filter(lambda x: x % 2 == 0)
print("Filtered Even Numbers:", even_rdd.collect())

# COMMAND ----------
# MAGIC %md
# MAGIC ## `flatMap()` Transformation
# MAGIC **What is happening?**
# MAGIC - Unlike `map()`, `flatMap()` flattens the output.
# MAGIC - Each element produces multiple values, and they are returned as a single list.

# COMMAND ----------
num_rdd = sc.parallelize([1, 2, 3, 4, 5])
final_res = num_rdd.flatMap(lambda x: range(1, x)).collect()
print("Flattened Values:", final_res)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Removing Duplicates with `distinct()`
# MAGIC **What is happening?**
# MAGIC - `distinct()` removes duplicate elements from an RDD.

# COMMAND ----------
num_rdd = sc.parallelize([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
final_res = num_rdd.distinct().collect()
print("Distinct Elements:", final_res)
