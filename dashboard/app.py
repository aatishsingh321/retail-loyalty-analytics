import streamlit as st
import pandas as pd
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Retail Loyalty Dashboard",
    layout="wide"
)

st.title("🛒 Retail Loyalty & Promotion Analytics")

# ---------------- LOAD DATA ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "raw", "sales_with_points.csv")

df = pd.read_csv(data_path)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

promo_filter = st.sidebar.selectbox(
    "Promotion Applied?",
    options=["All", "Yes", "No"]
)

# Apply filter
filtered_df = df.copy()

if promo_filter == "Yes":
    filtered_df = filtered_df[filtered_df["promotion"] == True]
elif promo_filter == "No":
    filtered_df = filtered_df[filtered_df["promotion"] == False]

# ---------------- KPI SECTION ----------------
total_sales = len(filtered_df)
total_points = int(filtered_df["loyalty_points"].sum())
avg_points = round(filtered_df["loyalty_points"].mean(), 2)

col1, col2, col3 = st.columns(3)

col1.metric("📊 Total Sales", total_sales)
col2.metric("🎁 Total Loyalty Points", total_points)
col3.metric("⭐ Avg Points / Sale", avg_points)

st.divider()

# ---------------- PROMOTION ANALYSIS ----------------
st.subheader("🏷 Promotion Impact")

promo_analysis = df.groupby("promotion")["loyalty_points"].mean().reset_index()
promo_analysis["promotion"] = promo_analysis["promotion"].map({
    True: "Promotion Applied",
    False: "No Promotion"
})

st.bar_chart(
    promo_analysis.set_index("promotion")
)

st.divider()

# ---------------- CUSTOMER INSIGHTS ----------------
st.subheader("👤 Top Customers by Loyalty Points")

customer_points = (
    df.groupby("customer_id")["loyalty_points"]
    .sum()
    .reset_index()
    .sort_values(by="loyalty_points", ascending=False)
    .head(10)
)

st.dataframe(customer_points)

st.divider()

# ---------------- RAW DATA VIEW ----------------
with st.expander("📄 View Raw Data"):
    st.dataframe(filtered_df)
