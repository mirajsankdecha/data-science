# Databricks Notebook

# COMMAND ----------

# MAGIC %md
# MAGIC # Apache Spark DataFrame Operations with Detailed Explanation
# MAGIC 
# MAGIC This notebook demonstrates various DataFrame operations in Apache Spark using Databricks. It includes explanations of how each operation works and its significance in data processing.

# COMMAND ----------

# Loading DataFrame from CSV File
df = spark.read.csv('dbfs:/FileStore/SS_Orders.csv', header="True", inferSchema="True")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Displaying Schema
# MAGIC **What is happening?**
# MAGIC - `printSchema()` displays the structure of the DataFrame, including column names and data types.

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Displaying Data
# MAGIC **What is happening?**
# MAGIC - `show()` displays the first few rows of the DataFrame for quick inspection.

# COMMAND ----------

df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Getting Column Names
# MAGIC **What is happening?**
# MAGIC - `columns` returns a list of column names in the DataFrame.

# COMMAND ----------

df.columns

# COMMAND ----------

# MAGIC %md
# MAGIC ## Counting Rows
# MAGIC **What is happening?**
# MAGIC - `count()` returns the total number of rows in the DataFrame.

# COMMAND ----------

df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary Statistics
# MAGIC **What is happening?**
# MAGIC - `describe()` provides basic statistics such as count, mean, min, and max for numeric columns.

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Displaying Summary Statistics
# MAGIC **What is happening?**
# MAGIC - `show()` is used to display the summary statistics.

# COMMAND ----------

df.describe().show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Selecting Specific Columns
# MAGIC **What is happening?**
# MAGIC - `select()` is used to fetch specific columns from the DataFrame.
# MAGIC - `show(5)` limits the output to 5 rows.

# COMMAND ----------

df.select("Order ID", "Customer Name", "Sales").show(5)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Getting Distinct Values of a Column
# MAGIC **What is happening?**
# MAGIC - `distinct()` removes duplicate values from the selected column.
# MAGIC - `show()` displays the unique values.

# COMMAND ----------

df.select("Category").distinct().show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Finding Duplicate Values in Customer Name Column
# MAGIC **What is happening?**
# MAGIC - We group by "Customer Name" and count occurrences.
# MAGIC - We filter where the count is greater than 1 to get duplicate values.
# MAGIC - `show()` displays the duplicate customer names.

# COMMAND ----------

df.groupBy("Customer Name").count().filter("count > 1").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Finding Maximum and Minimum Profit
# MAGIC **What is happening?**
# MAGIC - `agg()` is used to perform aggregate functions.
# MAGIC - `max("Profit")` finds the highest profit value.
# MAGIC - `min("Profit")` finds the lowest profit value.
# MAGIC - `show()` displays the results.

# COMMAND ----------

df.agg({'Profit': 'max'}).show()
df.agg({'Profit': 'min'}).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Filtering Orders by a Specific Date
# MAGIC **What is happening?**
# MAGIC - We define a specific date as a string.
# MAGIC - `filter()` is used to select only the rows where the "Order Date" matches the specified date.
# MAGIC - `show()` displays the filtered results.

# COMMAND ----------

# Replace '2024-03-01' with the specific date you want to filter
specific_date = "2024-03-01"

# Filtering orders by a specific date
df.filter(df["Order Date"] == specific_date).show()


emp = [(1,"AAA","dept1",1000),
         (2,"BBB","dept2",2000),
         (3,"CCC","dept3",3000),
         (4,"DDD","dept4",4000),
         (5,"EEE","dept5",5000)
  (6,"FFF","dept6",6000),

    
    ]
