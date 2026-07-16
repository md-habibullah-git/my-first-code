# 📈 Real-Time Crypto & Stock Market Dashboard

![Dashboard Demo](https://unsplash.com)

An advanced, interactive web application built entirely with **Python** and **Streamlit** to track live prices of cryptocurrencies and stock markets around the world. It fetches real-time market data dynamically using the Yahoo Finance API and visualizes it with professional candlestick charts.

## ✨ Features
- **Real-Time Data Fetching:** Automatically downloads the latest financial data using `yfinance`.
- **Interactive Candlestick Charts:** Powered by `Plotly` with professional dark mode layout.
- **Customized Controls:** Users can enter any ticker symbol (e.g., BTC-USD, AAPL, GOOG) and adjust the time period (1 week, 1 month, 3 months, 1 year).
- **Detailed Data Tables:** Displays the exact raw numbers for the last 10 days of market activity.
- **Error Handling:** Built-in validation system to catch invalid tickers or network drops gracefully.

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Web Interface:** Streamlit
- **Data Analysis:** Pandas
- **Financial API:** Yahoo Finance (`yfinance`)
- **Data Visualization:** Plotly

## 💻 How to Run Locally

Follow these steps to run the application on your computer:

### 1. Install Required Dependencies
Make sure you have Python installed, then run:
```bash
pip install streamlit yfinance plotly pandas
```

### 2. Run the Application
Execute the following command in your terminal:
```bash
python -m streamlit run app.py
```
The application will automatically open in your local browser at `http://localhost:8501`.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
