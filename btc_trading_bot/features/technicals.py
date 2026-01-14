import pandas as pd
import ta

def add_indicators(df, atr_period=14, rsi_period=14):

    df = df.copy()
    
    #Ensure numeric types
    for col in ["High", "Low", "Close"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    df["ATR"] = ta.volatility.average_true_range(
        high=df["High"], low=df["Low"], close=df["Close"], window=atr_period
    )
    
    df["RSI"] = ta.momentum.rsi(df["Close"], window=rsi_period)
    
    df.dropna(inplace=True)
    return df
