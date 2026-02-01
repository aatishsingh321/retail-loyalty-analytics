import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
raw_data_dir = os.path.join(BASE_DIR, "data", "raw")
sales_file = os.path.join(raw_data_dir, "sales.csv")
output_file = os.path.join(raw_data_dir, "sales_with_points.csv")

# Read sales data
sales_df = pd.read_csv(sales_file)

# Loyalty points calculation rule
def calculate_points(row):
    points = row["quantity"] * 10
    if row["promotion"]:
        points += 20
    return points

# Apply rule
sales_df["loyalty_points"] = sales_df.apply(calculate_points, axis=1)

# Save transformed data
sales_df.to_csv(output_file, index=False)

print("✅ Loyalty points calculated and saved successfully")
