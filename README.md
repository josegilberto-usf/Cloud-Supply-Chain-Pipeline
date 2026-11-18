# Cloud-Based Supply Chain Analytics Pipeline

## Overview
Warehouses need to know which products are about to run out so they can reorder in time. This project builds a small end-to-end pipeline that loads inventory data into a cloud database and uses SQL to flag and rank the most urgent restocks at each warehouse.

The inventory data is simulated, so the project can be run by anyone without access to real company data.

## How It Works
1. **Generate and load the data (`data_pipeline.py`)**
   - Creates 10,000 simulated inventory records using Python and the Faker library.
   - Each record includes an item ID, product name, category, warehouse location, current stock level, reorder point and unit price.
   - Covers five warehouses: Tampa, Orlando, Miami, Jacksonville and Atlanta.
   - Loads the records into a cloud-hosted PostgreSQL database (Neon) as an `inventory` table using pandas and SQLAlchemy.

2. **Analyze stock-out risk (`analyze_inventory.py`)**
   - Runs a SQL query that finds every item whose stock level is below its reorder point and calculates how far short it is (the deficit).
   - Ranks those shortages within each warehouse, so the largest shortage at each location is ranked #1.
   - Prints the most critical shortages (deficit over 100 units) and the top-priority restock for each warehouse.

## Tech Stack
- **Python:** pandas, SQLAlchemy, Faker
- **Database:** PostgreSQL (hosted on Neon)
- **SQL techniques:** a Common Table Expression (CTE) to isolate low-stock items, and the `RANK()` window function to rank shortages within each warehouse

## Example Business Question Answered
> "For each of our warehouses, which product should we reorder first?"

## How to Run Locally
1. Clone this repository.
2. Install the dependencies:
   ```bash
   pip install pandas sqlalchemy psycopg2-binary faker
   ```
3. Create a free PostgreSQL database (for example on [Neon](https://neon.tech)) and copy its connection string.
4. In both `data_pipeline.py` and `analyze_inventory.py`, replace `DB_URL_HERE` with your connection string. Don't commit your real connection string to GitHub.
5. Load the data, then run the analysis:
   ```bash
   python data_pipeline.py
   python analyze_inventory.py
   ```

## Possible Next Steps
- Read the source data from a real cloud storage bucket (such as AWS S3) instead of generating it.
- Add a dashboard (Tableau or Power BI) on top of the `inventory` table.
- Estimate the dollar value of each shortage using `unit_price`.
