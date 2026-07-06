-- Databricks notebook source
/* =====================================================
   KPI 1 : Total Revenue
   ===================================================== */

SELECT
    ROUND(SUM(payment_value), 2) AS total_revenue
FROM workspace.default.fact_payments;


/* =====================================================
   KPI 2 : Total Orders
   ===================================================== */

SELECT
    COUNT(*) AS total_orders
FROM workspace.default.fact_orders;


/* =====================================================
   KPI 3 : Total Customers
   ===================================================== */

SELECT
    COUNT(*) AS total_customers
FROM workspace.default.dim_customer;


/* =====================================================
   KPI 4 : Average Order Value
   ===================================================== */

SELECT
    ROUND(AVG(payment_value), 2) AS avg_order_value
FROM workspace.default.fact_payments;


/* =====================================================
   Revenue Distribution by Payment Method
   ===================================================== */

SELECT
    payment_type,
    ROUND(SUM(payment_value), 2) AS revenue
FROM workspace.default.fact_payments
GROUP BY payment_type
ORDER BY revenue DESC;


/* =====================================================
   Monthly Revenue Trend
   ===================================================== */

SELECT
    CONCAT(dd.year,'-',LPAD(dd.month,2,'0')) AS year_month,
    ROUND(SUM(fp.payment_value),2) AS revenue
FROM workspace.default.fact_payments fp
JOIN workspace.default.fact_orders fo
    ON fp.order_id = fo.order_id
JOIN workspace.default.dim_date dd
    ON CAST(fo.order_purchase_timestamp AS DATE)
       = CAST(dd.date AS DATE)
GROUP BY dd.year, dd.month
ORDER BY dd.year, dd.month;


/* =====================================================
   Top 10 Cities by Customer Count
   ===================================================== */

SELECT
    customer_city,
    COUNT(*) AS customers
FROM workspace.default.dim_customer
GROUP BY customer_city
ORDER BY customers DESC
LIMIT 10;


/* =====================================================
   Seller Orders vs Revenue Analysis
   ===================================================== */

SELECT
    seller_id,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(price),2) AS revenue
FROM workspace.default.fact_orders
GROUP BY seller_id
ORDER BY revenue DESC
LIMIT 100;


/* =====================================================
   Top Product Categories by Revenue
   ===================================================== */

SELECT
    p.product_category_name,
    ROUND(SUM(f.price),2) AS revenue
FROM workspace.default.fact_orders f
JOIN workspace.default.dim_product p
    ON f.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;


/* =====================================================
   Average Order Value by State
   ===================================================== */

SELECT
    c.customer_state,
    ROUND(AVG(f.price),2) AS avg_order_value
FROM workspace.default.fact_orders f
JOIN workspace.default.dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY avg_order_value DESC;


/* =====================================================
   Revenue by State
   ===================================================== */

SELECT
    c.customer_state,
    ROUND(SUM(f.price),2) AS revenue
FROM workspace.default.fact_orders f
JOIN workspace.default.dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY revenue DESC;


/* =====================================================
   Top 10 Sellers by Revenue
   ===================================================== */

SELECT
    seller_id,
    ROUND(SUM(price),2) AS revenue
FROM workspace.default.fact_orders
GROUP BY seller_id
ORDER BY revenue DESC
LIMIT 10;


/* =====================================================
   Orders by Status
   ===================================================== */

SELECT
    order_status,
    COUNT(*) AS total_orders
FROM workspace.default.fact_orders
GROUP BY order_status
ORDER BY total_orders DESC;


/* =====================================================
   Top Product Categories by Orders
   ===================================================== */

SELECT
    p.product_category_name,
    COUNT(*) AS total_orders
FROM workspace.default.fact_orders f
JOIN workspace.default.dim_product p
    ON f.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY total_orders DESC
LIMIT 10;


/* =====================================================
   Revenue by Seller State
   ===================================================== */

SELECT
    s.seller_state,
    ROUND(SUM(f.price),2) AS revenue
FROM workspace.default.fact_orders f
JOIN workspace.default.dim_seller s
    ON f.seller_id = s.seller_id
GROUP BY s.seller_state
ORDER BY revenue DESC;


/* =====================================================
   Average Freight Cost by State
   ===================================================== */

SELECT
    c.customer_state,
    ROUND(AVG(f.freight_value),2) AS avg_freight_cost
FROM workspace.default.fact_orders f
JOIN workspace.default.dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY avg_freight_cost DESC;


/* =====================================================
   Top Customers by Spending
   ===================================================== */

SELECT
    customer_id,
    ROUND(SUM(price),2) AS total_spent
FROM workspace.default.fact_orders
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;