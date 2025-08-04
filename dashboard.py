import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# Set page config
st.set_page_config(
    page_title="Cafe Sales Dashboard",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    if os.path.exists('analyzed_cafe_sales.csv'):
        df = pd.read_csv('analyzed_cafe_sales.csv', parse_dates=['Transaction Date'])
        # Ensure Month is in datetime format for proper sorting
        df['Month'] = pd.to_datetime(df['Month'])
        return df
    else:
        st.error("Error: analyzed_cafe_sales.csv not found. Please run the analysis first.")
        return None

df = load_data()

if df is not None:
    # Sidebar filters
    st.sidebar.title("Filters")
    
    # Date range filter
    min_date = df['Transaction Date'].min().date()
    max_date = df['Transaction Date'].max().date()
    date_range = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Item filter
    all_items = ['All'] + sorted(df['Item'].unique().tolist())
    selected_items = st.sidebar.multiselect('Select Items', all_items, default='All')
    if 'All' in selected_items or not selected_items:
        selected_items = all_items[1:]  # Exclude 'All' for filtering
    
    # Location filter
    locations = ['All'] + df['Location'].unique().tolist()
    selected_locations = st.sidebar.multiselect('Select Locations', locations, default='All')
    if 'All' in selected_locations or not selected_locations:
        selected_locations = locations[1:]
    
    # Apply filters
    filtered_df = df[
        (df['Transaction Date'].dt.date >= date_range[0]) & 
        (df['Transaction Date'].dt.date <= date_range[1]) &
        (df['Item'].isin(selected_items)) &
        (df['Location'].isin(selected_locations))
    ]
    
    # Calculate metrics
    total_sales = filtered_df['Total Spent'].sum()
    total_transactions = filtered_df['Transaction ID'].nunique()
    avg_sale = filtered_df['Total Spent'].mean()
    
    # Page title
    st.title("☕ Cafe Sales Dashboard")
    
    # KPI Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Sales", f"${total_sales:,.2f}")
    with col2:
        st.metric("Total Transactions", f"{total_transactions:,}")
    with col3:
        st.metric("Average Sale", f"${avg_sale:,.2f}")
    
    # Sales Trend
    st.subheader("Sales Trend")
    sales_trend = filtered_df.groupby('Month')['Total Spent'].sum().reset_index()
    fig1 = px.line(sales_trend, x='Month', y='Total Spent', 
                  title='Monthly Sales Trend',
                  labels={'Total Spent': 'Total Sales ($)', 'Month': 'Month'})
    st.plotly_chart(fig1, use_container_width=True)
    
    # Sales by Category
    st.subheader("Sales by Category")
    col1, col2 = st.columns(2)
    
    with col1:
        # Sales by Item
        sales_by_item = filtered_df.groupby('Item')['Total Spent'].sum().sort_values(ascending=False).reset_index()
        fig2 = px.bar(sales_by_item, x='Item', y='Total Spent',
                     title='Sales by Item',
                     labels={'Total Spent': 'Total Sales ($)', 'Item': 'Menu Item'})
        st.plotly_chart(fig2, use_container_width=True)
    
    with col2:
        # Payment Method Distribution
        payment_dist = filtered_df['Payment Method'].value_counts().reset_index()
        payment_dist.columns = ['Payment Method', 'Count']
        fig3 = px.pie(payment_dist, values='Count', names='Payment Method',
                     title='Payment Method Distribution')
        st.plotly_chart(fig3, use_container_width=True)
    
    # Top Selling Items Table
    st.subheader("Top Selling Items")
    top_items = filtered_df.groupby('Item').agg({
        'Total Spent': 'sum',
        'Quantity': 'sum',
        'Transaction ID': 'nunique'
    }).sort_values('Total Spent', ascending=False).reset_index()
    
    top_items.columns = ['Item', 'Total Sales ($)', 'Total Quantity', 'Number of Transactions']
    st.dataframe(top_items, use_container_width=True)
    
    # Location Analysis
    st.subheader("Location Analysis")
    location_sales = filtered_df.groupby('Location')['Total Spent'].sum().reset_index()
    fig4 = px.bar(location_sales, x='Location', y='Total Spent',
                 title='Sales by Location',
                 color='Location')
    st.plotly_chart(fig4, use_container_width=True)
    
    # Day of Week Analysis
    st.subheader("Sales by Day of Week")
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_sales = filtered_df.groupby('DayOfWeek')['Total Spent'].sum().reindex(day_order).reset_index()
    fig5 = px.line(day_sales, x='DayOfWeek', y='Total Spent',
                  title='Sales by Day of Week',
                  labels={'Total Spent': 'Total Sales ($)', 'DayOfWeek': 'Day of Week'})
    st.plotly_chart(fig5, use_container_width=True)
    
    # Raw Data
    with st.expander("View Raw Data"):
        st.dataframe(filtered_df, use_container_width=True)

# Add some styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stMetric {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .stMetric h4 {
        color: #6c757d;
        margin-bottom: 5px;
    }
    .stMetric div:first-of-type {
        font-size: 24px;
        font-weight: bold;
        color: #0d6efd;
    }
</style>
""", unsafe_allow_html=True)
