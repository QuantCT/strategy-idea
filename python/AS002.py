
import backtrader as bt

from python.base_strategy import BaseStrategy

class AS002Strategy(BaseStrategy):

    params = (
        ('high_period', None),
        ('low_period', None),
    )

    def __init__(self):        
        self.close = self.datas[0].close
        self.high = self.datas[0].high
        self.low = self.datas[0].low

        self.highest_high = bt.indicators.Highest(self.high, period=self.params.high_period, plot=False)
        self.lowest_low = bt.indicators.Lowest(self.low, period=self.params.low_period, plot=False)
        self.macd_hist = bt.indicators.MACDHisto(self.close, plot=False).histo
        
        self.order = None    

    def next(self):                        

        # Check if an order is pending
        if self.order:
            return
        
        buy_condition = (self.macd_hist[0] > 0) and (self.close[0] > self.highest_high[-1])
        sell_condition = (self.macd_hist[0] < 0) or (self.close[0] < self.lowest_low[-1])

        # Check if we are in the market
        if not self.position:
            
            if buy_condition:
                self.order = self.buy()
                
        else:                       
            
            if sell_condition:
                self.order = self.sell()                                

