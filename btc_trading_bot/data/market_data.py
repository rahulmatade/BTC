import yfinance as yf
import pandas as pd

def fetch_btc_data(period="60d", interval="30m"):
    df = yf.download("BTC-USD", period=period, interval=interval, auto_adjust=False)
    
    if df.empty:
        raise ValueError("No BTC data returned from yfinance. Try shorter period or different interval.")

    #Ensure required columns exist (done as a check for the multiindex issue from yfinance)
    required_cols = ["Open", "High", "Low", "Close", "Volume"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column from yfinance: {col}")

    df.dropna(inplace=True)
    return df