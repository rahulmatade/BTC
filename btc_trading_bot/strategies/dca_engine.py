class DCAEngine:
    def __init__(self, drop_pct, amount):
        self.last_buy_price = None
        self.drop_pct = drop_pct
        self.amount = amount

    '''def should_buy(self, price):
        if self.last_buy_price is None:
            return True
        return price <= self.last_buy_price * (1 - self.drop_pct)'''

    def should_buy(self, price):
        if self.last_buy_price is None:
            self.last_buy_price = price #waits for a price drop before first buy
            return False
        return price <= self.last_buy_price * (1 - self.drop_pct)


    def record_buy(self, price):
        self.last_buy_price = price
