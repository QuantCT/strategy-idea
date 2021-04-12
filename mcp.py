
import numpy as np
import pandas as pd

import backtester
import util
import viz

def perform_mcp(idea_name, random_signals=False):        
    
    df_rets = backtester.perform_backtest(idea_name)
    
    df_signals = util.get_signals_dataframe(df_rets)
    
    test_mean = round(df_signals['Return'].mean() * 100, 2)        
    
    sample_means = []
    for i in range(1, 10000):
        df_sample = df_signals.copy()    
        if random_signals:
            df_sample['Signal'] = np.random.choice([0,1], df_signals['Signal'].shape[0], True)
        else:
            df_sample['Signal'] = np.random.permutation(df_signals['Signal'].values)
        
        df_sample['Return'] = df_sample['MarketReturn'] * df_sample['Signal']
        
        sample_mean = round(df_sample['Return'].mean() * 100, 2) 
        sample_means.append(sample_mean)
    
    viz.plot_histogram(sample_means, 
                           nBins=50, 
                           title='MCP Sample Means', 
                           test_mean=test_mean)

