import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from matplotlib.ticker import FuncFormatter
import os

# Create output directory if it doesn't exist
os.makedirs('analysis_results', exist_ok=True)

# Set the style for better-looking plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 12

# Helper function for currency formatting
def currency(x, pos):
    return f'${x:,.2f}'

currency_format = FuncFormatter(currency)

# 1. Load and prepare the data
print("🚀 Loading and preparing cafe sales data...")
df = pd.read_csv("cleaned_cafe_sales.csv")
original_count = len(df)

# Data cleaning
df = df.drop_duplicates()
df = df.dropna()
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
df['DayOfWeek'] = df['Transaction Date'].dt.day_name()
df['Month'] = df['Transaction Date'].dt.month_name()
df['Year'] = df['Transaction Date'].dt.year

# 2. Basic Data Exploration
print("\n📊 === Basic Data Exploration ===")
print(f"\n📈 Total records: {len(df):,}")
print(f"📅 Date range: {df['Transaction Date'].min().date()} to {df['Transaction Date'].max().date()}")
print(f"💰 Total Revenue: ${df['Total Spent'].sum():,.2f}")
print(f"🛒 Total Transactions: {df['Transaction ID'].nunique():,}")
print(f"🍽️ Unique Items Sold: {df['Item'].nunique()}")

# 3. Time-based Analysis
print("\n⏰ === Time-based Analysis ===")
monthly_revenue = df.groupby(['Year', 'Month', pd.Grouper(key='Transaction Date', freq='M')])['Total Spent'].sum().reset_index()
monthly_revenue = monthly_revenue.sort_values('Transaction Date')

# Daily patterns
daily_patterns = df.groupby('DayOfWeek')['Total Spent'].agg(['sum', 'count', 'mean']).reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])

# 4. Product Analysis
print("\n🍕 === Product Analysis ===")
product_metrics = df.groupby('Item').agg({
    'Quantity': 'sum',
    'Total Spent': 'sum',
    'Transaction ID': 'count'
}).sort_values('Total Spent', ascending=False)

product_metrics['Avg. Price'] = product_metrics['Total Spent'] / product_metrics['Quantity']
product_metrics['Avg. Transaction Value'] = product_metrics['Total Spent'] / product_metrics['Transaction ID']

# 5. Customer Behavior Analysis
print("\n👥 === Customer Behavior Analysis ===")
payment_analysis = df.groupby('Payment Method').agg({
    'Total Spent': ['sum', 'mean', 'count']
}).sort_values(('Total Spent', 'sum'), ascending=False)

location_analysis = df.groupby('Location').agg({
    'Total Spent': ['sum', 'mean', 'count']
}).sort_values(('Total Spent', 'sum'), ascending=False)

# 6. Visualization
print("\n🎨 Generating visualizations...")
plt.figure(figsize=(18, 22))

# Plot 1: Monthly Revenue Trend
plt.subplot(4, 2, 1)
sns.lineplot(x='Transaction Date', y='Total Spent', data=monthly_revenue, marker='o')
plt.title('Monthly Revenue Trend', fontweight='bold')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(currency_format)

# Plot 2: Daily Revenue by Day of Week
plt.subplot(4, 2, 2)
sns.barplot(x=daily_patterns.index, y='sum', data=daily_patterns.reset_index())
plt.title('Total Revenue by Day of Week', fontweight='bold')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(currency_format)

# Plot 3: Top Selling Items by Revenue
plt.subplot(4, 2, 3)
top_items = product_metrics.head(5)
sns.barplot(x=top_items.index, y='Total Spent', data=top_items.reset_index())
plt.title('Top 5 Items by Revenue', fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.gca().yaxis.set_major_formatter(currency_format)

# Plot 4: Payment Method Analysis
plt.subplot(4, 2, 4)
sns.barplot(x=payment_analysis.index, y=('Total Spent', 'mean'), 
            data=payment_analysis.reset_index())
plt.title('Average Transaction by Payment Method', fontweight='bold')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(currency_format)

# Plot 5: Location Analysis
plt.subplot(4, 2, 5)
sns.barplot(x=location_analysis.index, y=('Total Spent', 'count'), 
            data=location_analysis.reset_index())
plt.title('Number of Transactions by Location', fontweight='bold')
plt.xticks(rotation=45)

# Plot 6: Price Distribution by Item
plt.subplot(4, 2, 6)
sns.boxplot(x='Item', y='Price Per Unit', data=df)
plt.title('Price Distribution by Item', fontweight='bold')
plt.xticks(rotation=90)

# Plot 7: Heatmap of Sales by Day and Hour
plt.subplot(4, 2, 7)
df['Hour'] = df['Transaction Date'].dt.hour
heatmap_data = df.pivot_table(
    index='DayOfWeek', 
    columns='Hour', 
    values='Total Spent', 
    aggfunc='sum',
    fill_value=0
).reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
sns.heatmap(heatmap_data, cmap='YlGnBu', linewidths=.5)
plt.title('Sales Heatmap: Day of Week vs Hour', fontweight='bold')
plt.tight_layout()
plt.savefig('analysis_results/cafe_sales_analysis.png', dpi=300, bbox_inches='tight')

# 7. Save Detailed Analysis to CSV files
print("\n💾 Saving detailed analysis to CSV files...")

# Save summary data
summary_data = {
    'Metric': ['Total Revenue', 'Total Transactions', 'Unique Items', 'Date Range'],
    'Value': [
        f"${df['Total Spent'].sum():,.2f}",
        f"{df['Transaction ID'].nunique():,}",
        f"{df['Item'].nunique()}",
        f"{df['Transaction Date'].min().date()} to {df['Transaction Date'].max().date()}"
    ]
}
pd.DataFrame(summary_data).to_csv('analysis_results/summary.csv', index=False)

# Save other analysis results
product_metrics.to_csv('analysis_results/product_metrics.csv')
monthly_revenue.to_csv('analysis_results/monthly_revenue.csv', index=False)
daily_patterns.to_csv('analysis_results/daily_patterns.csv')
payment_analysis.to_csv('analysis_results/payment_analysis.csv')
location_analysis.to_csv('analysis_results/location_analysis.csv')

# Save the heatmap data
heatmap_data.to_csv('analysis_results/hourly_heatmap_data.csv')

# 8. Print Key Insights
print("\n🔍 === Key Insights ===")
print(f"\n💰 Highest Revenue Day: {daily_patterns['sum'].idxmax()} (${daily_patterns['sum'].max():,.2f})")
print(f"🛒 Busiest Day: {daily_patterns['count'].idxmax()} ({daily_patterns['count'].max():,} transactions)")
print(f"🏆 Top Selling Item: {product_metrics.index[0]} (${product_metrics['Total Spent'].iloc[0]:,.2f})")
print(f"💳 Most Popular Payment: {payment_analysis.index[0]} ({(payment_analysis[('Total Spent', 'count')].iloc[0] / len(df))*100:.1f}% of transactions)")
print(f"📍 Most Common Location: {location_analysis.index[0]} ({(location_analysis[('Total Spent', 'count')].iloc[0] / len(df))*100:.1f}% of transactions)")

# 9. Save key insights to a text file
with open('analysis_results/key_insights.txt', 'w') as f:
    f.write("=== Key Insights ===\n\n")
    f.write(f"• Highest Revenue Day: {daily_patterns['sum'].idxmax()} (${daily_patterns['sum'].max():,.2f})\n")
    f.write(f"• Busiest Day: {daily_patterns['count'].idxmax()} ({daily_patterns['count'].max():,} transactions)\n")
    f.write(f"• Top Selling Item: {product_metrics.index[0]} (${product_metrics['Total Spent'].iloc[0]:,.2f})\n")
    f.write(f"• Most Popular Payment: {payment_analysis.index[0]} ({(payment_analysis[('Total Spent', 'count')].iloc[0] / len(df))*100:.1f}% of transactions)\n")
    f.write(f"• Most Common Location: {location_analysis.index[0]} ({(location_analysis[('Total Spent', 'count')].iloc[0] / len(df))*100:.1f}% of transactions)\n")

print("\n✅ Analysis complete! Check the 'analysis_results' folder for all CSV files and visualizations.")
print("📂 Files created:")
print(f"   • analysis_results/summary.csv")
print(f"   • analysis_results/product_metrics.csv")
print(f"   • analysis_results/monthly_revenue.csv")
print(f"   • analysis_results/daily_patterns.csv")
print(f"   • analysis_results/payment_analysis.csv")
print(f"   • analysis_results/location_analysis.csv")
print(f"   • analysis_results/hourly_heatmap_data.csv")
print(f"   • analysis_results/key_insights.txt")
print(f"   • analysis_results/cafe_sales_analysis.png")
