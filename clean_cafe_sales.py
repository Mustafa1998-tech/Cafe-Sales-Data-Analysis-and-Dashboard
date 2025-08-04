import pandas as pd
import numpy as np
from datetime import datetime

# Load the data
df = pd.read_csv('dirty_cafe_sales.csv')

# 1. Replace placeholder values with NaN
placeholders = ['ERROR', 'UNKNOWN', '']
df = df.replace(placeholders, np.nan)

# 2. Clean Item column
valid_items = ['Coffee', 'Tea', 'Cake', 'Cookie', 'Sandwich', 'Salad', 'Smoothie', 'Juice']
df['Item'] = df['Item'].where(df['Item'].isin(valid_items), other=np.nan)

# 3. Clean numeric columns
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price Per Unit'] = pd.to_numeric(df['Price Per Unit'], errors='coerce')

def clean_currency(x):
    if pd.isna(x):
        return np.nan
    try:
        return float(x)
    except:
        return np.nan

df['Total Spent'] = df['Total Spent'].apply(clean_currency)

# 4. Recalculate Total Spent where possible
def calculate_total_spent(row):
    if pd.notna(row['Quantity']) and pd.notna(row['Price Per Unit']):
        calculated = row['Quantity'] * row['Price Per Unit']
        if pd.isna(row['Total Spent']) or (row['Total Spent'] != calculated):
            return calculated
    return row['Total Spent']

df['Total Spent'] = df.apply(calculate_total_spent, axis=1)

# 5. Clean Payment Method
valid_payments = ['Credit Card', 'Cash', 'Digital Wallet']
df['Payment Method'] = df['Payment Method'].where(df['Payment Method'].isin(valid_payments), other=np.nan)

# 6. Clean Location
df['Location'] = df['Location'].where(df['Location'].isin(['In-store', 'Takeaway']), other=np.nan)

# 7. Clean Transaction Date
def clean_date(date_str):
    if pd.isna(date_str):
        return np.nan
    try:
        # Try to parse the date in YYYY-MM-DD format
        return pd.to_datetime(date_str, format='%Y-%m-%d')
    except:
        return np.nan

df['Transaction Date'] = df['Transaction Date'].apply(clean_date)

# 8. Remove rows where essential information is missing
essential_columns = ['Item', 'Quantity', 'Price Per Unit', 'Total Spent']
df = df.dropna(subset=essential_columns, how='all')

# 9. Ensure Transaction ID is unique and not missing
df = df.drop_duplicates('Transaction ID')
df = df[df['Transaction ID'].notna()]

# 10. Convert data types
df['Transaction ID'] = df['Transaction ID'].astype(str)

# Save the cleaned data
df.to_csv('cleaned_cafe_sales.csv', index=False)
print("Data cleaning complete. Cleaned data saved as 'cleaned_cafe_sales.csv'")

# Print summary of cleaning
print("\nCleaning Summary:")
print(f"Original number of rows: {len(pd.read_csv('dirty_cafe_sales.csv'))}")
print(f"Number of rows after cleaning: {len(df)}")
print(f"Number of rows removed: {len(pd.read_csv('dirty_cafe_sales.csv')) - len(df)}")
print("\nSample of cleaned data:")
print(df.head())
