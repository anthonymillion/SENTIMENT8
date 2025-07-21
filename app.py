import streamlit as st
import pandas as pd
import datetime

# Define asset groups
assets = {
    "📈 Stocks": ["NVDA", "MSFT", "AAPL", "AMZN", "GOOGL", "GOOG", "META", "TSLA", "AVGO", "COST", "AMD", "NFLX"],
    "🌐 Indices": ["SP500", "QQQ", "USTECH100", "RUSSELL", "NIKKEI"],
    "💰 Commodities": ["GOLD", "USOIL", "BRENT", "COPPER", "SILVER", "NATGAS"],
    "💱 Currencies": ["USDJPY", "EURUSD", "DXY", "BTCUSD"],
    "⚡ Volatility": ["VIX", "BONDYIELDS"]
}

# Timeframes
timeframes = ["1s", "5s", "15s", "30s", "M1", "M2", "M3", "M4", "M10", "M15", "M30", "H6", "H7", "H8", "1H", "4H", "Daily", "Weekly", "Monthly"]

# App config
st.set_page_config(page_title="AI EdgeFinder – Horizontal Clean Layout", layout="wide")
st.markdown("## ✨ AI EdgeFinder – Horizontal Layout")
st.markdown("Easily view all assets across categories in a clean, horizontal format.")

# Timeframe selection
main_tf = st.selectbox("Select Main Timeframe", timeframes, index=10, key="main_tf")
top_tf = st.selectbox("Select Top Mover Timeframe", timeframes, index=10, key="top_tf")

# Scoring logic
def simulate_score(symbol, tf):
    base = (hash(symbol + tf + str(datetime.date.today())) % 9) - 4
    return round(base + (hash(tf) % 3 - 1), 2)

def classify_sentiment(score):
    if score > 1.5:
        return "🟢 Bullish"
    elif score < -1.5:
        return "🔴 Bearish"
    return "🟡 Neutral"

def generate_table(symbols, tf):
    return pd.DataFrame([{
        "Symbol": sym,
        "Score": (s := simulate_score(sym, tf)),
        "Sentiment": classify_sentiment(s)
    } for sym in symbols])

# Prepare columns
cols = st.columns(len(assets))

# Render each group
for i, (title, symbols) in enumerate(assets.items()):
    with cols[i]:
        st.markdown(f"### {title}")
        st.dataframe(generate_table(symbols, main_tf), use_container_width=True)
