import os
import pandas as pd
from sqlalchemy import create_engine

# 1. CONNECT TO THE CLOUD
os.environ["DATABASE_URL"] = "DB_URL_HERE"  # Replace with your actual database URL
db_url = os.environ["DATABASE_URL"]

if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(db_url)

print("Connected to Neon Cloud. Executing Advanced SQL Analytics...")

# 2. THE ADVANCED SQL QUERY (CTE + Window Function)
sql_query = """
WITH InventoryRisk AS (
    -- This CTE (Common Table Expression) finds all items running low
    SELECT 
        item_id, 
        product_name, 
        warehouse_location, 
        stock_level, 
        reorder_point,
        (reorder_point - stock_level) AS deficit
    FROM inventory
    WHERE stock_level < reorder_point
)
SELECT 
    warehouse_location,
    product_name,
    stock_level,
    deficit,
    -- This Window Function ranks the most critical shortages per warehouse
    RANK() OVER(PARTITION BY warehouse_location ORDER BY deficit DESC) as urgency_rank
FROM InventoryRisk
WHERE deficit > 100
ORDER BY warehouse_location, urgency_rank;
"""

# 3. RUN THE QUERY AND DISPLAY RESULTS
df_results = pd.read_sql(sql_query, engine)

print(f"\n🚨 Identified {len(df_results)} critical inventory shortages across the supply chain.\n")
print("Top Priority Restocks (Rank 1 per Warehouse):")

# Filter to only show the #1 most urgent item for each warehouse
top_priorities = df_results[df_results['urgency_rank'] == 1]
print(top_priorities.to_string(index=False))

print("\n✅ Analytics complete.")