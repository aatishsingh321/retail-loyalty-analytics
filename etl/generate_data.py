from faker import Faker
import pandas as pd
import os

# Create fake data generator
fake = Faker()

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create raw data directory path
raw_data_dir = os.path.join(BASE_DIR, "data", "raw")

# Create directory if it does not exist
os.makedirs(raw_data_dir, exist_ok=True)

# Output file path
output_path = os.path.join(raw_data_dir, "customers.csv")

customers = []

# Create 100 fake customers
for i in range(1, 101):
    customers.append([
        i,
        fake.name()
    ])

df = pd.DataFrame(customers, columns=["customer_id", "name"])

# Save CSV
df.to_csv(output_path, index=False)

print("✅ Customers data created successfully")


import random

# -----------------------------
# Generate Sales Data
# -----------------------------

sales = []

# Create 500 fake sales records
for sale_id in range(1, 501):
    sales.append([
        sale_id,                       # sale_id
        random.randint(1, 100),        # customer_id
        random.randint(1, 5),          # quantity
        random.choice([True, False])   # promotion_applied
    ])

sales_df = pd.DataFrame(
    sales,
    columns=["sale_id", "customer_id", "quantity", "promotion"]
)

sales_output_path = os.path.join(raw_data_dir, "sales.csv")
sales_df.to_csv(sales_output_path, index=False)

print("✅ Sales data created successfully")
