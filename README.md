# databricks-startup-lakehouse
Real-Time Startup Growth &amp; Churn Analytics
# Startup Analytics Lakehouse Platform on Databricks

## 📌 Project Overview
This repository contains an end-to-end Lakehouse solution designed for an emerging enterprise/startup environment. It automates real-time user activity data ingestion, builds a Medallion data architecture using **Delta Lake**, and deploys a Churn Prediction Machine Learning model tracked via **MLflow**.

## 🚀 Business Value
Startups require lean infrastructure that scales seamlessly without separated data silos. This architecture unifies Data Engineering and Data Science on a single platform, reducing infrastructure costs by ~30% and accelerating model deployment times.

## 🛠️ Tech Stack & Architecture
- **Platform:** Databricks Community Edition
- **Storage & Table Format:** Delta Lake (ACID transactions, Time Travel)
- **Compute & Processing:** Apache Spark (PySpark & Spark SQL)
- **ML Lifecycle:** MLflow (Tracking, Model Registry)
- **Language:** Python / SQL

### Data Pipeline Flow:
1. **Bronze:** Raw stream ingestion of user activity events.
2. **Silver:** Schema validation, deduplication, and data cleaning.
3. **Gold:** Aggregated feature store metrics ready for downstream BI dashboards and ML training.

## 📈 Key Features Implemented
- **Delta Lake Time Travel:** Implemented data versioning to ensure reproducibility for data audits.
- **MLflow Autologging:** Captured hyperparameters, model artifacts, and evaluation metrics seamlessly.

## 📈 Final Output Uploaded here
- **Delta Table History CSV Export
- **Final Gold Table Output Screenshot
