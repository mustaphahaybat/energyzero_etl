# ⚡ EnergyZero ETL Pipeline

## 🧩 Project Overview
This project fetches energy price data from the **EnergyZero API**, processes it with **Apache Airflow**, and converts it to **Parquet** format. All components run in **Docker**, making the pipeline portable and reproducible.

## 🚀 Project Structure
energyzero_etl/
│
├── docker-compose.yml
├── requirements.txt
├── dags/
│ └── energyzero_etl.py # Airflow DAG
├── scripts/
│ ├── extract_energyzero.py # Fetch JSON from API
│ └── transform_pandas.py # Transform JSON to Parquet
├── data/
│ ├── raw/ # Raw JSON files
│ └── processed/ # Transformed Parquet files
└── README.md

markdown
Kodu kopyala

## ⚙️ Running the Project
1. **Start Docker Environment**  
```bash
docker-compose up -d
This launches:

Airflow webserver & scheduler

PostgreSQL database

Airflow UI: http://localhost:8080
Username: airflow | Password: airflow

Run the DAG
Turn on the energyzero_etl DAG in the Airflow UI and trigger it manually or wait for the schedule.

Outputs

Raw data: data/raw/

Processed data: data/processed/energy_transformed.parquet

🧠 Key Learnings
Build multi-component ETL pipelines in Docker

Schedule tasks using Apache Airflow

Transform JSON to Parquet using Pandas

💡 Next Steps / Improvements
Load Parquet into PostgreSQL or DuckDB

Add logging or error notifications to Airflow DAG

Extend API date ranges

Create visualization scripts with Matplotlib or Plotly

👨‍💻 Developer
Mustapha Haybat | Netherlands
🔗 LinkedIn Profile https://www.linkedin.com/in/mustafa-haybat-86725235a/
