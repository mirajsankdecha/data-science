# Databricks Notebook

# COMMAND ----------

# MAGIC %md
# MAGIC # Fundamentals of Spark SQL DataFrame
# MAGIC 
# MAGIC This notebook demonstrates key concepts of Spark SQL DataFrames, including creation, transformation, and querying using DataFrame operations.

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize Spark Session
spark = SparkSession.builder.appName("SparkSQLDataFrameFundamentals").getOrCreate()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Creating Employee DataFrame
# MAGIC **What is happening?**
# MAGIC - Creating a DataFrame from a list of tuples.
# MAGIC - Defining schema for better structure.
# MAGIC - Converting into a Spark DataFrame.

# COMMAND ----------

# Creating Employee DataFrame
emp = [
    (1, "AAA", "dept1", 1000),
    (2, "BBB", "dept1", 1100),
    (3, "CCC", "dept1", 3000),
    (4, "DDD", "dept1", 1500),
    (5, "EEE", "dept2", 8000),
    (6, "FFF", "dept2", 7200),
    (7, "GGG", "dept3", 7100),
    (8, "HHH", "dept3", 3700),
    (9, "III", "dept3", 4500),
    (10, "JJJ", "dept3", 3400)
]

# Creating Employee DataFrame
df = spark.createDataFrame(emp, ["id", "name", "dept", "salary"])

# Show DataFrame
df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Creating Department DataFrame
# MAGIC **What is happening?**
# MAGIC - Creating a DataFrame for department information.
# MAGIC - Converting the list into a DataFrame.

# COMMAND ----------

# Creating Department DataFrame
dept = [
    ("dept1", "Department - 1"),
    ("dept2", "Department - 2"),
    ("dept3", "Department - 3"),
    ("dept4", "Department - 4")
]

deptdf = spark.createDataFrame(dept, ["id", "name"])

# Show DataFrame
deptdf.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Joining Employee and Department DataFrames
# MAGIC **What is happening?**
# MAGIC - Performing an inner join on `dept` column to combine employee and department data.
# MAGIC - `join()` is used for merging DataFrames on a common key.

# COMMAND ----------

joined_df = df.join(deptdf, df.dept == deptdf.id, "inner").select(df.id, df.name, df.salary, deptdf.name.alias("department"))

# Show Joined DataFrame
joined_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Filtering Employees with Salary Greater than 5000
# MAGIC **What is happening?**
# MAGIC - Using `filter()` to fetch employees earning more than 5000.

# COMMAND ----------

high_salary_df = df.filter(df.salary > 5000)

# Show Filtered DataFrame
high_salary_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Grouping Employees by Department and Calculating Average Salary
# MAGIC **What is happening?**
# MAGIC - Using `groupBy()` to aggregate employees based on departments.
# MAGIC - Applying `avg()` to calculate the average salary per department.

# COMMAND ----------

from pyspark.sql.functions import avg

avg_salary_df = df.groupBy("dept").agg(avg("salary").alias("average_salary"))

# Show Average Salary per Department
avg_salary_df.show()
