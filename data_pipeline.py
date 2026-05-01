import os
import pandas as pd
from sqlalchemy import create_engine
import random
from faker import Faker

# 1. SET YOUR CLOUD CONNECTION (The Bridge)
os.environ["DATABASE_URL"] = "DB_URL_HERE"  # Replace with your actual database URL

print("Starting ETL Pipeline...")
print("Generating 10,000 rows of simulated warehouse data...")

# 2. GENERATE DATA (Simulating Cloud Storage Extraction)
fake = Faker()
data = []
locations = ["Tampa", "Orlando", "Miami", "Jacksonville", "Atlanta"]

for i in range(10000):
    stock = random.randint(0, 500)
    reorder = random.randint(50, 150)
    data.append({
        "item_id": f"ITM-{10000 + i}",
        "product_name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "category": random.choice(["Electronics", "Apparel", "Home", "Sports"]),
        "warehouse_location": random.choice(locations),
        "stock_level": stock,
        "reorder_point": reorder,
        "unit_price": round(random.uniform(10.0, 500.0), 2)
    })

# Transform into a Pandas DataFrame (The Transformation phase)
df = pd.DataFrame(data)
print(f"Successfully generated {len(df)} records.")

# 3. LOAD TO POSTGRESQL (The Loading phase)
print("Connecting to the Neon Cloud Database...")
db_url = os.environ["DATABASE_URL"]

# SQLAlchemy requires the string to start with 'postgresql://' instead of 'postgres://'
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

engine = create_engine(db_url)

print("Uploading data to the cloud... (This might take 30-60 seconds)")
# Push the dataframe to a new SQL table called 'inventory'
df.to_sql('inventory', engine, if_exists='replace', index=False)

print("✅ SUCCESS! Data pipeline complete. Your cloud database is now loaded.")