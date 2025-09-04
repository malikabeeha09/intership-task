# Task 4: Global Superstore Sales Dashboard

import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\hp\Downloads\archive (1)\train.csv", encoding="ISO-8859-1")
    return df
df = load_data()
# Standardize column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Ensure numeric columns
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

# Drop missing values
df = df.dropna(subset=['Sales','Profit'])

# 4. Sidebar Filters

st.sidebar.header("📊 Filters")

regions = st.sidebar.multiselect(
    "Select Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

categories = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

sub_categories = st.sidebar.multiselect(
    "Select Sub-Category:",
    options=df["Sub-Category"].unique(),
    default=df["Sub-Category"].unique()
)

# Apply filters
df_filtered = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories)) &
    (df["Sub-Category"].isin(sub_categories))
]


# 5. KPIs
total_sales = df_filtered["Sales"].sum()
total_profit = df_filtered["Profit"].sum()
top_customers = df_filtered.groupby("Customer_Name")["Sales"].sum().nlargest(5)

# 6. Dashboard Layout
st.title("📈 Global Superstore Dashboard")
st.markdown("Interactive analysis of **Sales, Profit, and Segment Performance**")

# KPIs
col1, col2 = st.columns(2)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📊 Total Profit", f"${total_profit:,.0f}")

# Sales by Region
fig_region = px.bar(
    df_filtered.groupby("Region")["Sales"].sum().reset_index(),
    x="Region", y="Sales", title="Sales by Region", color="Region"
)
st.plotly_chart(fig_region, use_container_width=True)

# Sales by Category
fig_category = px.pie(
    df_filtered.groupby("Category")["Sales"].sum().reset_index(),
    names="Category", values="Sales", title="Sales by Category"
)
st.plotly_chart(fig_category, use_container_width=True)

# Profit by Sub-Category
fig_subcat = px.bar(
    df_filtered.groupby("Sub-Category")["Profit"].sum().reset_index(),
    x="Sub-Category", y="Profit", title="Profit by Sub-Category", color="Profit"
)
st.plotly_chart(fig_subcat, use_container_width=True)

# Top 5 Customers by Sales
st.subheader("🏆 Top 5 Customers by Sales")
st.table(top_customers.reset_index().rename(columns={"Sales":"Total Sales"}))
