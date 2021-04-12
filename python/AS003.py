
import backtrader as bt

from python.base_strategy import BaseStrategy

class AS003Strategy(BaseStrategy):

    params = (
        ('ema1_period', None),
        ('ema2_period', None),
        ('ema3_period', None),
    )

    def __init__(self):    
        self.high = self.datas[0].high    
        self.low = self.datas[0].low
        self.close = self.datas[0].close
        self.hlc3 = (self.high + self.low + self.close) / 3

        self.ema1 = bt.indicators.ExponentialMovingAverage(self.hlc3, period=self.params.ema1_period, plot=False)
        self.ema2 = bt.indicators.ExponentialMovingAverage(self.hlc3, period=self.params.ema2_period, plot=False)
        self.ema3 = bt.indicators.ExponentialMovingAverage(self.hlc3, period=self.params.ema3_period, plot=False)
        
        self.order = None    

    def next(self):                        

        # Check if an order is pending
        if self.order:
            return
        
        buy_condition = self.is_rising(self.ema1, 1) and self.is_rising(self.ema2, 1) and self.is_rising(self.ema3, 1)
        sell_condition = not (self.is_rising(self.ema1, 1) or self.is_rising(self.ema2, 1) or self.is_rising(self.ema3, 1))

        # Check if we are in the market
        if not self.position:
            
            if buy_condition:
                self.order = self.buy()
                
        else:                       
            
            if sell_condition:
                self.order = self.sell()     

    def is_rising(self, ds, count):
        index = count+1 if count >= 1 else 2
        if (len(ds) >= index):
            for i in range(1, index):
                if ds[1-i] <= ds[-i]:
                    return False

            return True
        else:
            return False 

