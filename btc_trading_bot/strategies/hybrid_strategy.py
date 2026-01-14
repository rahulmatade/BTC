from strategies.atr_risk import atr_stop
from strategies.dca_engine import DCAEngine
from llm.strategy_advisor import llm_strategy_advice  #rule-based, although i've named it llm

class HybridStrategy:
    #Hybrid DCA + ATR + rule-based swing strategy.

    def __init__(self, config):
        #DCA engine
        self.dca = DCAEngine(
            config["dca"]["price_drop_pct"],
            config["dca"]["amount"]
        )
        #Base ATR multiplier
        self.base_atr_mult = config["atr"]["multiplier"]

    def run(self, price, atr, forecast, rsi, volume_change, portfolio):
        #Runs one iteration of the strategy
        actions = []

        #DCA base layer
        if self.dca.should_buy(price):
            btc_bought = portfolio.buy(price, self.dca.amount)
            self.dca.record_buy(price)
            actions.append(f"DCA BUY {btc_bought:.4f} BTC @ {price}")

        #Rule-based swing logic
        context = {
            "price": price,
            "atr": atr,
            "rsi": rsi,
            "volume_change_pct": volume_change,
            "forecast_return_pct": (forecast - price) / price * 100
        }

        advice = llm_strategy_advice(context)

        if advice["open_swing_trade"]:
            adjusted_mult = self.base_atr_mult + advice["stop_loss_multiplier_adjustment"]
            stop_price = atr_stop(price, atr, adjusted_mult)
            actions.append(f"Rule-based Swing BUY @ {price} | Stop @ {stop_price:.2f}")
            actions.append(f"Reasoning: {advice['reasoning']}")

        return actions
