# Spotify ETL Data Pipeline Project

## Project Overview

This project is an end-to-end Spotify ETL Data Engineering Pipeline built using AWS cloud services, Python, SQL, and Power BI.

The pipeline extracts Spotify streaming data using the Spotify API, stores the data in Amazon S3, performs SQL analysis using Athena, and visualizes insights using Power BI dashboards.

---

# Pipeline Architecture

Spotify API → AWS Lambda → Amazon S3 → Amazon Athena → Power BI

---

# Tech Stack

- Python
- AWS Lambda
- Amazon S3
- Amazon Athena
- SQL
- Power BI

---

# Features

- Serverless ETL pipeline using AWS services
- Spotify API data extraction
- Cloud-based data storage using Amazon S3
- SQL analysis using Athena
- Interactive Power BI dashboard
- KPI cards and trend analysis
- Top artists and tracks analysis

---

# Project Workflow

## 1. Data Extraction
Spotify API data is extracted using Python scripts running inside AWS Lambda.

## 2. Data Storage
Raw Spotify data is stored inside Amazon S3 buckets.

## 3. Data Processing
The extracted data is cleaned and prepared for analytics.

## 4. Data Querying
Amazon Athena is used to run SQL queries on Spotify datasets stored in Amazon S3.

## 5. Data Visualization
Power BI dashboard is used to visualize trends and insights from the processed data.

---

# Dashboard Insights

The Power BI dashboard includes:

- Total Streams
- Active Users
- Top Artists
- Top Tracks
- Listening Trends
- KPI Cards
- Interactive Filters

---

# Folder Structure

```bash
spotify-etl-pipeline/
│
├── extraction/
│   └── spotify_api_data_extract.py
│
├── transformation/
│   └── spotify_transformation_load_function.py
│
├── queries/
│   └── athena_queries.sql
│
├── screenshot/
│   └── dashboard.png
│
├── powerbi/
│   └── spotify_dashboard.pbix
│
└── README.md
```

---

# SQL Queries

All Athena SQL queries used for analysis are stored in:

```bash
queries/athena_queries.sql
```

---

# AWS Services Used

## AWS Lambda
Used for serverless execution of ETL scripts.

## Amazon S3
Stores Spotify datasets and processed files.

## Amazon Athena
Used to perform SQL analysis directly on data stored in Amazon S3.

---

# Sample SQL Query

```sql
SELECT artist_name,
       COUNT(*) AS total_streams
FROM spotify_data
GROUP BY artist_name
ORDER BY total_streams DESC;
```

---

# Future Improvements

- Add automated scheduling using EventBridge
- Build real-time streaming pipeline
- Add Spark-based transformations
- Implement orchestration tools like Airflow
- Add advanced analytics and machine learning

---

# Dashboard Preview

![Dashboard](screenshot/dashboard.png)


---

# Author

Raunak  
Aspiring Data Engineer

---

# Connect

LinkedIn: https://www.linkedin.com/in/raunak-nirali
GitHub: https://github.com/raunak1908