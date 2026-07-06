# Databricks notebook source
customers = spark.table("workspace.default.bronze_customers")

print("Rows:", customers.count())
print("Columns:", len(customers.columns))

display(customers.limit(10))

# COMMAND ----------

orders = spark.table("workspace.default.bronze_orders")

print("Rows:", orders.count())
display(orders.limit(10))

# COMMAND ----------

spark.sql("SHOW TABLES IN workspace.default").show(truncate=False)

# COMMAND ----------

spark.table("workspace.default.bronze_customers").count()

# COMMAND ----------

spark.table("workspace.default.bronze_orders").count()