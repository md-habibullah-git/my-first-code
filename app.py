import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# 1. Web Page Configurations and Title
st.set_page_config(page_title="Crypto Dashboard", page_icon="📈", layout="wide")
st.title("📈 Real-Time Crypto & Stock Market Dashboard")
st.write("Your first advanced web application powered by Python!")

# 2. Sidebar Control Panel Settings
st.sidebar.header("🔧 Control Panel")

# User inputs for Crypto/Stock ticker symbol
ticker = st.sidebar.text_input("Enter Crypto or Stock Ticker:", "BTC-USD")

# User selection for data time period
time_period = st.sidebar.selectbox("Select Time Period:", ["1mo", "1wk", "3mo", "1y"])

# 3. Fetching live financial data from the internet
st.subheader(f"📊 {ticker} - Current Market Status")

with st.spinner("Loading live data from the market..."):
    # Fixed data loading issues by adding auto_adjust=False
    data = yf.download(ticker, period=time_period, interval="1d", auto_adjust=False)

# Check if data is fetched successfully (Debugging)
if not data.empty:
    # Flatten multi-index columns if yfinance returns tuple names
    data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]
    
    # 4. Creating an interactive Candlestick chart
    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )])
    
    # Customizing chart layout for dark mode
    fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark")
    st.plotly_chart(fig, width='stretch')
    
    # 5. Displaying raw data in a clean data table
    st.write("📋 Detailed Data Table:")
    st.dataframe(data.tail(10), width='stretch')
else:
    st.error("Sorry! No data found or connection issue. Please check your internet or entry.")
