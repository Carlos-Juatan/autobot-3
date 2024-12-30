class Backtester:
    def __init__(self, data):
        self.data = data.copy()  # Avoid modifying original self.self.data
        # self.indicators = indicators.copy()
        # self.initial_value = initial_value
        # self.quantity = quantity
        # self.fee = fee
