# BTC Hybrid Trading Strategy

### DCA + ATR Risk Management + ML Forecasting + Rule-Based Decision Engine

## Project Overview

This project implements a hybrid cryptocurrency trading system for Bitcoin (BTC-USD) that combines:

- Dollar Cost Averaging (DCA) for long-term accumulation
- ATR-based dynamic risk management for volatility-aware stop-losses
- Machine Learning forecasting using classical time-series models
- Rule-based strategy logic for swing trade decisions (LLM-inspired but deterministic)

The system is designed for clarity, modularity, and explainability, making it suitable for academic evaluation and real-world prototyping.

## System Architecture
Market Data (yfinance)  
        ↓  
Technical Indicators (ATR, RSI)  
        ↓  
ML Forecasting (ARIMA + Exponential Smoothing)  
        ↓  
Forecast Ensemble  
        ↓  
Hybrid Strategy Engine  
   ├── DCA Engine  
   ├── ATR Risk Manager  
   └── Rule-Based Strategy Advisor  
        ↓  
Portfolio Execution  

## Project Structure
btc_trading_bot/  
│  
├── data/  
│   └── market_data.py        # Fetches BTC price data  
│  
├── features/  
│   └── technicals.py         # ATR & RSI calculation  
│  
├── ml/  
│   ├── arima_model.py  
│   ├── exp_smoothing.py  
│   └── forecast_ensemble.py  
│  
├── strategies/  
│   ├── dca_engine.py  
│   ├── atr_risk.py  
│   ├── hybrid_strategy.py  
│  
├── llm/  
│   └── strategy_advisor.py   # Rule-based strategy decider  
│  
├── execution/  
│   └── portfolio.py          # Capital & asset management  
│  
├── config/  
│   └── strategy_config.json  
│  
└── main.py                   # Entry point  

## Configuration

Strategy behavior is controlled via strategy_config.json:

{  
  "budget_usd": 10000,  
  "dca": {  
    "amount": 500,  
    "price_drop_pct": 0.03  
  },  
  "atr": {  
    "period": 14,  
    "multiplier": 1.5  
  },  
  "ml": {  
    "forecast_horizon": 5  
  },  
  "strategy_mode": "hybrid"  
}

## Key Components Explained
### Market Data (market_data.py)

- Fetches BTC-USD OHLCV data using yfinance
- Uses 30-minute candles over 60 days
- Handles yfinance MultiIndex issues safely

### Technical Indicators (technicals.py)
- Average True Range (ATR)
- Measures volatility, not price direction
- Used to dynamically size stop-loss levels
- Relative Strength Index (RSI)
- Identifies overbought (>70) and oversold (<30) conditions

### ML Forecasting (ml/)

- Two classical time-series models:
- ARIMA (2,1,2)
- Exponential Smoothing (additive trend)
- Forecasts are combined using an ensemble mean, reducing single-model bias.

### DCA Engine (dca_engine.py)

- Buys a fixed USD amount after price drops by a configured percentage
- First price is recorded before any purchase (prevents immediate buy)

### Rule-Based Strategy Advisor (strategy_advisor.py)

- Replaces external LLM APIs with deterministic, explainable logic.
- Rules consider:
-- RSI levels
  Volume spikes
  ATR-based volatility
  ML forecasted return

- Returns:

{
  "open_swing_trade": bool,
  "stop_loss_multiplier_adjustment": float,
  "reasoning": str
}

### ATR Risk Management (atr_risk.py)

- Stop-loss calculation:
Stop Price = Entry Price − (ATR × Multiplier)

- Adapts automatically to market volatility.

### Hybrid Strategy Engine (hybrid_strategy.py)

Combines:

- DCA accumulation
- Rule-based swing trades
- ATR-scaled stop-losses
- Produces human-readable action logs for evaluation.

### Portfolio Management (portfolio.py)

- Tracks USD and BTC balances
- Prevents over-spending
- Calculates portfolio value in real time.
