import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Market Reaper AI",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        color: #1f77b4;
        text-align: center;
        padding: 20px;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">📈 Market Reaper AI</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666;">Advanced AI-Powered Market Analysis & Trading Insights</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔧 Configuration")
st.sidebar.markdown("---")

# Navigation
page = st.sidebar.radio(
    "Select Page",
    ["Dashboard", "Market Analysis", "Trading Signals", "Portfolio", "Settings"]
)

# Dashboard Page
if page == "Dashboard":
    st.header("📊 Dashboard Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Current Portfolio Value", "$125,400", "+2.5%", delta_color="normal")
    
    with col2:
        st.metric("Today's P&L", "$3,150", "+1.8%", delta_color="normal")
    
    with col3:
        st.metric("Win Rate", "68%", "+5%", delta_color="normal")
    
    with col4:
        st.metric("Active Positions", "12", "0", delta_color="off")
    
    st.markdown("---")
    
    # Charts
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("Portfolio Performance (7 Days)")
        dates = pd.date_range(end=datetime.now(), periods=7)
        values = [100000, 102000, 101500, 103200, 104100, 123900, 125400]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=values, mode='lines+markers', name='Portfolio Value'))
        fig.update_layout(height=300, showlegend=False, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.subheader("Asset Allocation")
        assets = ['Tech Stocks', 'Crypto', 'Commodities', 'Forex', 'Options']
        allocation = [35, 25, 20, 12, 8]
        
        fig = go.Figure(data=[go.Pie(labels=assets, values=allocation)])
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)

# Market Analysis Page
elif page == "Market Analysis":
    st.header("📈 Market Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        symbol = st.text_input("Enter Stock Symbol", "AAPL")
    
    with col2:
        timeframe = st.selectbox("Timeframe", ["1D", "1W", "1M", "3M", "1Y"])
    
    st.markdown("---")
    
    # Generate sample data
    dates = pd.date_range(end=datetime.now(), periods=100)
    prices = 100 + np.cumsum(np.random.randn(100) * 2)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"{symbol} Price Movement")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='Price'))
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Technical Indicators")
        sma_20 = pd.Series(prices).rolling(20).mean()
        sma_50 = pd.Series(prices).rolling(50).mean()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=prices, mode='lines', name='Price'))
        fig.add_trace(go.Scatter(x=dates, y=sma_20, mode='lines', name='SMA 20'))
        fig.add_trace(go.Scatter(x=dates, y=sma_50, mode='lines', name='SMA 50'))
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)

# Trading Signals Page
elif page == "Trading Signals":
    st.header("🎯 AI Trading Signals")
    
    signal_data = {
        'Symbol': ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN'],
        'Signal': ['BUY', 'SELL', 'HOLD', 'BUY', 'HOLD'],
        'Confidence': [92, 78, 65, 88, 72],
        'Entry Price': [150.25, 380.50, 140.75, 245.30, 175.50],
        'Target Price': [155.50, 375.00, 142.00, 255.80, 178.25],
        'Stop Loss': [148.00, 385.00, 139.50, 242.50, 173.75]
    }
    
    df_signals = pd.DataFrame(signal_data)
    
    st.markdown("### Current Trading Signals")
    
    # Color code signals
    def signal_color(signal):
        if signal == 'BUY':
            return 'background-color: #90EE90'
        elif signal == 'SELL':
            return 'background-color: #FFB6C6'
        else:
            return 'background-color: #FFFFE0'
    
    styled_df = df_signals.style.applymap(signal_color, subset=['Signal'])
    st.dataframe(styled_df, use_container_width=True)
    
    st.markdown("---")
    st.subheader("Signal Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Signals", len(df_signals), "")
    with col2:
        buy_signals = len(df_signals[df_signals['Signal'] == 'BUY'])
        st.metric("Buy Signals", buy_signals, "")
    with col3:
        avg_confidence = df_signals['Confidence'].mean()
        st.metric("Avg Confidence", f"{avg_confidence:.1f}%", "")

# Portfolio Page
elif page == "Portfolio":
    st.header("💼 Portfolio Management")
    
    portfolio_data = {
        'Asset': ['AAPL', 'MSFT', 'BTC', 'ETH', 'SPY'],
        'Quantity': [50, 30, 0.5, 5, 25],
        'Entry Price': [145.00, 375.50, 42000, 2200, 420.30],
        'Current Price': [150.25, 380.50, 43500, 2350, 425.15],
        'Value': [7512.50, 11415.00, 21750, 11750, 10628.75]
    }
    
    df_portfolio = pd.DataFrame(portfolio_data)
    
    st.markdown("### Current Holdings")
    st.dataframe(df_portfolio, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Portfolio Value Breakdown")
        fig = go.Figure(data=[go.Pie(labels=df_portfolio['Asset'], values=df_portfolio['Value'])])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Gain/Loss per Asset")
        df_portfolio['Gain/Loss %'] = ((df_portfolio['Current Price'] - df_portfolio['Entry Price']) / df_portfolio['Entry Price'] * 100)
        
        fig = go.Figure(data=[
            go.Bar(x=df_portfolio['Asset'], y=df_portfolio['Gain/Loss %'],
                   marker_color=['green' if x > 0 else 'red' for x in df_portfolio['Gain/Loss %']])
        ])
        fig.update_layout(height=400, yaxis_title="Gain/Loss %")
        st.plotly_chart(fig, use_container_width=True)

# Settings Page
elif page == "Settings":
    st.header("⚙️ Settings")
    
    st.subheader("API Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        api_key = st.text_input("API Key", type="password")
        api_endpoint = st.text_input("API Endpoint", "https://api.example.com")
    
    with col2:
        refresh_rate = st.slider("Refresh Rate (seconds)", 5, 300, 30)
        max_positions = st.number_input("Max Positions", 1, 100, 20)
    
    st.markdown("---")
    
    st.subheader("Risk Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        max_loss = st.slider("Max Daily Loss %", 1, 10, 5)
        position_size = st.slider("Position Size %", 1, 10, 2)
    
    with col2:
        stop_loss_pct = st.slider("Stop Loss %", 1, 10, 2)
        take_profit_pct = st.slider("Take Profit %", 1, 20, 5)
    
    st.markdown("---")
    
    if st.button("Save Settings", key="save_settings"):
        st.success("✅ Settings saved successfully!")
    
    if st.button("Reset to Defaults", key="reset_settings"):
        st.warning("⚠️ Settings reset to defaults")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #999; font-size: 12px;'>Market Reaper AI © 2026 | Last Updated: " + 
    datetime.now().strftime("%Y-%m-%d %H:%M:%S") + 
    "</p>",
    unsafe_allow_html=True
)
