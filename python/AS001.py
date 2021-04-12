
import backtrader as bt

from python.base_strategy import BaseStrategy

class AS001Strategy(BaseStrategy):

    params = (
        ('fast_period', None),
        ('slow_period', None),
    )

    def __init__(self):        
        self.close = self.datas[0].close

        self.fast_mom = bt.indicators.Momentum(self.close, period=self.params.fast_period, plot=False)
        self.slow_mom = bt.indicators.Momentum(self.close, period=self.params.slow_period, plot=False)
        
        self.order = None    

    def next(self):                        

        # Check if an order is pending
        if self.order:
            return
        
        buy_condition = (self.slow_mom[0] > 0) and (self.fast_mom[0] > 0)
        sell_condition = (self.slow_mom[0] < 0) or (self.fast_mom[0] < 0)

        # Check if we are in the market
        if not self.position:
            
            if buy_condition:
                self.order = self.buy()
                
        else:                       
            
            if sell_condition:
                self.order = self.sell()                                

