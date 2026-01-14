class Portfolio:
    def __init__(self, usd):
        self.usd = usd
        self.btc = 0

    def buy(self, price, amount):
        if self.usd < amount:
            return None
        btc = amount / price
        self.btc += btc
        self.usd -= amount
        return btc