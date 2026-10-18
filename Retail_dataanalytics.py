import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load data
df = pd.read_excel("Retail_Sales_data.xlsx")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

df.head()

# Check column names and data types
df.info()

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Check inconsistent text
print("\nRegions:")
print(df["Region"].unique())

print("\nCategories:")
print(df["Category"].unique())

# Keep the original data unchanged
cleaned_df = df.copy()

# Remove duplicate rows
cleaned_df = cleaned_df.drop_duplicates()

# Standardize text columns
cleaned_df["Region"] = (
    cleaned_df["Region"].str.strip().str.title()
)

cleaned_df["Category"] = (
    cleaned_df["Category"].str.strip().str.title()
)

# Handle missing values
cleaned_df["State"] = cleaned_df["State"].fillna("Unknown")
cleaned_df["Customer_ID"] = cleaned_df["Customer_ID"].fillna("Unknown")
cleaned_df["Payment_Mode"] = cleaned_df["Payment_Mode"].fillna("Unknown")

# Convert order date to datetime
cleaned_df["Order_Date"] = pd.to_datetime(
    cleaned_df["Order_Date"], errors="coerce"
)

# Save cleaned dataset
cleaned_df.to_csv("retail_sales_cleaned.csv", index=False)

print("Data cleaning completed!")
print("Cleaned shape:", cleaned_df.shape)
print("Remaining duplicates:", cleaned_df.duplicated().sum())
print("Saved as retail_sales_cleaned.csv")

# 1. Category-wise sales and profit
category_analysis = cleaned_df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)

print(category_analysis.round(2))

import matplotlib.pyplot as plt

# Sales by category
category_analysis["Total_Sales"].plot(
    kind="bar", figsize=(9, 5), title="Total Sales by Category"
)
plt.ylabel("Sales (₹)")
plt.xlabel("Product Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=300)
plt.show()

# Profit by category
category_analysis["Total_Profit"].plot(
    kind="bar", figsize=(9, 5), title="Total Profit by Category"
)
plt.ylabel("Profit (₹)")
plt.xlabel("Product Category")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("profit_by_category.png", dpi=300)
plt.show()


monthly_sales = (
    cleaned_df.set_index("Order_Date")
    .resample("MS")["Sales"]
    .sum()
)

monthly_sales.plot(
    figsize=(10, 5),
    marker="o",
    title="Monthly Sales Trend"
)

plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
plt.show()