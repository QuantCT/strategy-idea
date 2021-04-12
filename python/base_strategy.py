
import backtrader as bt


class BaseStrategy(bt.Strategy):
    
    def __init__(self):
        super().__init__()
        
    def log(self, txt, dt=None):        
        dt = dt or self.datas[0].datetime.date(0)
        print('%s | %s' % (dt.isoformat(), txt))    
                        
    def notify_order(self, order):        
        if order.status in [order.Submitted, order.Accepted]:            
            return
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY @ %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL @ %.2f' % order.executed.price)
                
            self.order = None
    
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Rejected - trying again ...')
            if order.isbuy():
                self.order = self.buy()
            if order.issell():
                self.order = self.sell                    

