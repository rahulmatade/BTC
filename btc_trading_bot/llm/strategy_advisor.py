#PS: This is a rule-based strategy adviser as I was having issues with API connections
#for both OpenAI and Gemini.

def llm_strategy_advice(context: dict):
    #Conext is a dict with keys: price, atr, rsi, volume_change_pct, forecast_return_pct (from ML predictor)
    #Function returns: dict: open_swing_trade, stop_loss_multiplier_adjustment, reasoning

    price = context["price"]
    atr = context["atr"]
    rsi = context["rsi"]
    vol_change = context["volume_change_pct"]
    forecast_return = context["forecast_return_pct"]

    advice = {
        "open_swing_trade": False,
        "stop_loss_multiplier_adjustment": 0.0,
        "reasoning": ""
    }

    #Rule 1: RSI-based swing trade
    if rsi < 30:
        advice["open_swing_trade"] = True
        advice["reasoning"] += "RSI below 30 indicates oversold, potential buy opportunity. "
    elif rsi > 70:
        advice["open_swing_trade"] = False
        advice["reasoning"] += "RSI above 70 indicates overbought, avoid buying. "

    #Rule 2: Volume breakout
    if vol_change > 50:  # 50% increase in 30m volume
        advice["open_swing_trade"] = True
        advice["reasoning"] += "Volume spike detected, indicating momentum. "

    #Rule 3: ATR-based stop adjustment
    # Increase stop distance if volatility is high
    if atr > 0.02 * price:  # 2% of price
        advice["stop_loss_multiplier_adjustment"] = 0.5  # more room for stop
        advice["reasoning"] += "ATR high, widening stop-loss. "
    else:
        advice["stop_loss_multiplier_adjustment"] = -0.2  # tighter stop
        advice["reasoning"] += "ATR low, can tighten stop-loss. "

    #Rule 4: ML forecast influence
    if forecast_return > 3:  # ML predicts >3% gain
        advice["open_swing_trade"] = True
        advice["reasoning"] += "Forecast predicts positive return, consider buying. "
    elif forecast_return < -2:
        advice["open_swing_trade"] = False
        advice["reasoning"] += "Forecast predicts negative return, avoid buying. "

    return advice
