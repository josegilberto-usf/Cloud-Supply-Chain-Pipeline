# 📦 Cloud-Based Supply Chain Analytics Pipeline

## Overview
Modern supply chains generate massive amounts of data that often sit siloed in cloud storage. Without automated pipelines, businesses struggle to identify stock-out risks and procurement inefficiencies in real-time.

This project simulates an **Enterprise ETL (Extract, Transform, Load) Pipeline**. It automates the movement of inventory data from cloud storage into a relational database, where advanced SQL analytics are applied to identify critical supply chain vulnerabilities and cost-saving opportunities.

## 🛠️ Tech Stack
* **Database:** PostgreSQL (Cloud Instance)
* **Language:** Python
* **ORM & Connectivity:** SQLAlchemy
* **Cloud Storage Simulation:** AWS S3 (Simulated local-to-cloud ingestion)
* **Data Analysis:** Advanced SQL (CTEs, Window Functions)

## 🚀 Key Features
1. [cite_start]**Automated ETL Pipeline:** Architected a Python-based script to extract 10,000+ simulated inventory records and automate ingestion into a live PostgreSQL database using SQLAlchemy. [cite: 53]
2. [cite_start]**Cloud Integration:** Simulates the extraction of raw data from AWS S3 storage buckets, reflecting industry-standard data engineering workflows. [cite: 53]
3. [cite_start]**Advanced SQL Analytics:** Developed complex queries utilizing **Common Table Expressions (CTEs)** and **Window Functions** to perform multi-level ranking of stock-out risks. [cite: 54]
4. [cite_start]**Actionable Business Intelligence:** Transforms raw data into procurement metrics, identifying simulated cost-saving opportunities across multiple distribution centers. [cite: 16, 54]

## 💻 How to Run Locally
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install sqlalchemy psycopg2 pandas