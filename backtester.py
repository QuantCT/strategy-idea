
import datetime

import pandas as pd
import backtrader as bt
import backtrader.feeds as btfeed

from python import AS001, AS002, AS003


def perform_backtest(idea_name):

    cer = get_cerebro(idea_name)    

    strategy = cer.run()[0]
    stats = strategy.stats
    analyzers = strategy.analyzers
        
    obs_rets = stats[2]    
    rets = obs_rets.get(size=len(obs_rets)).tolist()
    rets.insert(0, 0.0)
    df_rets = create_returns_dataframe(idea_name, '2018-01-01', '2020-12-30', rets)
    
    cer.plot(iplot=False)
    
    print_performance_results(idea_name, cer, stats, analyzers)
    
    df_rets.to_excel('df_rets.xlsx')
    return df_rets

# %% Helper methods

def get_cerebro(idea_name):
    
    strategies = {
        'AS001': AS001.AS001Strategy,
        'AS002': AS002.AS002Strategy,
        'AS003': AS003.AS003Strategy
    }
    params = {
        'AS001': {
            'slow_period':10,
            'fast_period':5
        },
        'AS002': {
            'high_period':5,
            'low_period':7
        },
        'AS003': {
            'ema1_period':10,
            'ema2_period':20,
            'ema3_period':30
        }
    }

    data = btfeed.GenericCSVData(
        dataname='data\\BTCUSDT_1d.csv',

        fromdate=datetime.datetime(2018, 1, 1),
        todate=datetime.datetime(2020, 12, 30),

        dtformat=('%Y-%m-%d %H:%M:%S'),    

        datetime=0,
        time=-1,
        open=1,
        high=2,
        low=3,
        close=4,
        volume=5,
        openinterest=-1
    )
    
    cer = bt.Cerebro(stdstats=False)
    
    cer.adddata(data)
    cer.broker.setcommission(commission=0)
    cer.broker.set_cash(100000)

    cer.addstrategy(strategies[idea_name], **params[idea_name])
    
    cer.addobserver(bt.observers.BuySell)
    cer.addobserver(bt.observers.Value)
    cer.addobserver(bt.observers.TimeReturn)
    
    cer.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cer.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    cer.addanalyzer(bt.analyzers.PositionsValue, _name='positions')
    cer.addanalyzer(bt.analyzers.PeriodStats, _name='periodstats')
    cer.addanalyzer(bt.analyzers.TimeReturn, 
                    _name='timereturn', 
                    timeframe=bt.TimeFrame.NoTimeFrame)
    cer.addanalyzer(bt.analyzers.SharpeRatio, 
                    _name='sharpe',
                    annualize=True, 
                    timeframe=bt.TimeFrame.Days, 
                    factor=365)
    
    return cer
    
def create_returns_dataframe(strategy_name, from_time, to_time, rets):
    
    date_range = pd.date_range(from_time, to_time)
    print(len(rets), len(date_range))
    df = pd.DataFrame(index=date_range, columns=[strategy_name], data=rets)

    return df

def print_performance_results(strategy_name, cerebro, stats, analyzers):
    """"""

    cum_ret_od = analyzers.timereturn.get_analysis()
    cum_ret = cum_ret_od[next(reversed(cum_ret_od))]
    
    print("")
    print('=== Performance Summary ({}) ==='.format(strategy_name))
    print("Final portfolio value: $%.2f" % cerebro.broker.getvalue())
    print("Cumulative returns: %.2f %%" % (cum_ret * 100))    
    print("Anualized Sharpe ratio: %.2f" % (analyzers.sharpe.get_analysis()['sharperatio']))
    print("Max. drawdown: %.2f %%" % (analyzers.drawdown.get_analysis()['max']['drawdown']))
    print("Max. drawdown duration: %s" % (analyzers.drawdown.get_analysis()['max']['len']))    
        
    trades = analyzers.trades.get_analysis()
    total = int(trades['total']['total'])
    wins = int(trades['won']['total'])
    losts = int(trades['lost']['total'])
    avg_profit = float(trades['won']['pnl']['average'])
    avg_loss = float(trades['lost']['pnl']['average']) * -1
    
    print("")    
    print('=== Trades Summary ({}) ==='.format(strategy_name))
    print("Total trades: %d" % (total))
    print("Winning trades: %d" % (wins))
    print("Losing trades: %d" % (losts))
    print("Max. consec. loses: %d" % (trades['streak']['lost']['longest']))
    print("Win rate: %.2f" % (wins / total))
    print("Reward/Risk ratio: %.2f" % (avg_profit / avg_loss))
        

