# Databricks notebook source
customers = spark.table("workspace.default.silver_customers")

dim_customer = customers.select(
    "customer_id",
    "customer_unique_id",
    "customer_zip_code_prefix",
    "customer_city",
    "customer_state"
)

dim_customer.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.dim_customer")

# COMMAND ----------

products = spark.table("workspace.default.silver_products")

dim_product = products.select(
    "product_id",
    "product_category_name",
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g"
)

dim_product.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.dim_product")

# COMMAND ----------

sellers = spark.table("workspace.default.silver_sellers")

dim_seller = sellers.select(
    "seller_id",
    "seller_zip_code_prefix",
    "seller_city",
    "seller_state"
)

dim_seller.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.dim_seller")

# COMMAND ----------

orders = spark.table("workspace.default.silver_orders")
order_items = spark.table("workspace.default.silver_order_items")

fact_orders = (
    orders.alias("o")
    .join(
        order_items.alias("oi"),
        "order_id",
        "inner"
    )
    .select(
        "order_id",
        "customer_id",
        "product_id",
        "seller_id",
        "price",
        "freight_value",
        "order_status",
        "order_purchase_timestamp"
    )
)

fact_orders.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.fact_orders")

# COMMAND ----------

payments = spark.table("workspace.default.silver_payments")

fact_payments = payments.select(
    "order_id",
    "payment_type",
    "payment_installments",
    "payment_value"
)

fact_payments.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.fact_payments")

# COMMAND ----------

spark.sql("SHOW TABLES IN workspace.default").show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import *

orders = spark.table("workspace.default.silver_orders")

dim_date = (
    orders
    .select(
        col("order_purchase_timestamp").alias("date")
    )
    .dropDuplicates()
    .withColumn("year", year("date"))
    .withColumn("month", month("date"))
    .withColumn("day", dayofmonth("date"))
)

dim_date.write \
    .mode("overwrite") \
    .saveAsTable("workspace.default.dim_date")