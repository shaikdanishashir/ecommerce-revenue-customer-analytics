# Databricks notebook source
from pyspark.sql.functions import *

customers = spark.table("workspace.default.bronze_customers")

silver_customers = (
    customers
    .dropDuplicates(["customer_id"])
)

print("Bronze:", customers.count())
print("Silver:", silver_customers.count())

display(silver_customers.limit(10))

# COMMAND ----------

silver_customers.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_customers")

# COMMAND ----------

spark.table("workspace.default.silver_customers").count()

# COMMAND ----------

from pyspark.sql.functions import to_timestamp

orders = spark.table("workspace.default.bronze_orders")

silver_orders = (
    orders
    .withColumn(
        "order_purchase_timestamp",
        to_timestamp("order_purchase_timestamp")
    )
    .withColumn(
        "order_approved_at",
        to_timestamp("order_approved_at")
    )
    .withColumn(
        "order_delivered_carrier_date",
        to_timestamp("order_delivered_carrier_date")
    )
    .withColumn(
        "order_delivered_customer_date",
        to_timestamp("order_delivered_customer_date")
    )
    .withColumn(
        "order_estimated_delivery_date",
        to_timestamp("order_estimated_delivery_date")
    )
    .dropDuplicates(["order_id"])
)

display(silver_orders.limit(10))

# COMMAND ----------

silver_orders.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_orders")

# COMMAND ----------

spark.table("workspace.default.silver_orders").count()

# COMMAND ----------

spark.sql("SHOW TABLES IN workspace.default").show(truncate=False)

# COMMAND ----------

products = spark.table("workspace.default.bronze_products")

silver_products = (
    products
    .dropDuplicates(["product_id"])
)

silver_products.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_products")

# COMMAND ----------

sellers = spark.table("workspace.default.bronze_sellers")

silver_sellers = (
    sellers
    .dropDuplicates(["seller_id"])
)

silver_sellers.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_sellers")

# COMMAND ----------

payments = spark.table("workspace.default.bronze_payments")

silver_payments = (
    payments
    .dropDuplicates()
)

silver_payments.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_payments")

# COMMAND ----------

reviews = spark.table("workspace.default.bronze_reviews")

silver_reviews = (
    reviews
    .dropDuplicates(["review_id"])
)

silver_reviews.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_reviews")

# COMMAND ----------

order_items = spark.table("workspace.default.bronze_order_items")

silver_order_items = (
    order_items
    .dropDuplicates()
)

silver_order_items.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.silver_order_items")

# COMMAND ----------

spark.sql("SHOW TABLES IN workspace.default").show(truncate=False)