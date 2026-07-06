# E-Commerce Revenue & Customer Analytics

## Project Overview

This project demonstrates an end-to-end Data Engineering and Analytics pipeline built using Databricks, PySpark, SQL, and Data Warehousing concepts. The project processes Brazilian E-Commerce data, transforms it through Medallion Architecture (Bronze, Silver, and Gold layers), and delivers business insights through interactive dashboards.

The goal is to simulate a real-world analytics platform that supports business decision-making through data modeling, KPI reporting, and visualization.

---

## Architecture

Raw Data → Bronze Layer → Silver Layer → Gold Layer → SQL Analytics → Dashboard

### Bronze Layer
- Ingest raw e-commerce datasets
- Preserve source data structure
- Store data for downstream processing

### Silver Layer
- Data cleaning and validation
- Remove duplicates
- Standardize schemas
- Apply business transformations

### Gold Layer
- Build analytics-ready data models
- Create Fact and Dimension tables
- Implement Star Schema for reporting

---

## Data Model

### Fact Tables

#### fact_orders
Stores transactional order-level information.

#### fact_payments
Stores payment details and revenue metrics.

### Dimension Tables

#### dim_customer
Customer demographics and location details.

#### dim_product
Product and category information.

#### dim_seller
Seller information.

#### dim_date
Date dimension for time-based analytics.

---

## Technologies Used

- Databricks
- PySpark
- SQL
- Delta Tables
- Data Warehousing
- Star Schema Modeling
- Data Analytics
- Dashboarding

---

## Project Files

### 01_Bronze_Layer.py
Raw data ingestion and Bronze Layer creation.

### 02_Silver_Layer.py
Data cleansing, transformation, and Silver Layer processing.

### 03_Gold_Layer.py
Fact and Dimension table creation for analytical reporting.

### 04_SQL_Analytics.sql
Business KPI calculations and analytical SQL queries.

### Dashboard.png
Interactive analytics dashboard created in Databricks.

---

## Key Performance Indicators (KPIs)

The dashboard includes:

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value (AOV)

---

## Dashboard Visualizations

### Revenue Distribution by Payment Method
Analyzes revenue contribution from different payment methods.

### Monthly Revenue Trend
Tracks revenue growth over time.

### Top 10 Cities by Customer Count
Identifies cities with the highest customer concentration.

### Top Product Categories by Revenue
Highlights best-performing product categories.

### Revenue by State
Shows regional revenue distribution.

### Top Sellers by Revenue
Ranks sellers based on generated revenue.

---

## Business Insights

- Credit Card is the dominant payment method.
- Revenue is concentrated in a few major states and cities.
- Certain product categories contribute significantly more revenue than others.
- Revenue trends reveal seasonal fluctuations and growth patterns.
- A small number of sellers generate a large share of total revenue.

---

## Dashboard Preview

<img width="1577" height="721" alt="Dashboard" src="https://github.com/user-attachments/assets/641dca10-98d6-4555-a1ec-0ef0e8dd9964" />


---
## Dashboard Files

This repository includes the exported Databricks dashboard file:

- E-Commerce Analytics Dashboard.lvdash.json

### How to View the Dashboard

The dashboard was developed using Databricks Dashboards and can be imported into a Databricks workspace for interactive exploration.

Steps:

1. Download `E-Commerce Analytics Dashboard.lvdash.json` from this repository.
2. Log in to your Databricks workspace.
3. Navigate to **Dashboards**.
4. Click **Create** → **Import Dashboard**.
5. Upload the `.lvdash.json` file.
6. Connect the dashboard to the corresponding tables and warehouse.
7. Open the dashboard to interact with all KPIs and visualizations.

## Skills Demonstrated

- Data Engineering
- ETL Development
- PySpark Transformations
- SQL Analytics
- Data Warehousing
- Star Schema Design
- Dashboard Development
- Business Intelligence
- Databricks Platform

---

## Dataset

Brazilian E-Commerce Public Dataset by Olist

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---
