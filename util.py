
import pandas as pd


def get_data_frame(filePath = "data\\BTCUSDT_1d.csv"):
    
    df = pd.read_csv(filePath,
                    parse_dates=['Date Time'],
                    usecols=['Date Time', 'Open', 'High', 'Low', 'Close'],
                    index_col='Date Time',
                    sep=',',
                    na_values=['NaN'])

    return df

def get_signals_dataframe(df_rets):

    filename = 'data\\BTCUSDT_1d.csv'
    df_data = get_data_frame(filename)

    df_data = df_data.head(df_rets.shape[0]+1)  
    
    df_rets = df_rets.dropna()
    df_signals = df_rets.where(df_rets == 0, 1)
    df_signals.columns = ['Signal']
    df_signals['MarketReturn'] = df_data['Close'].pct_change().dropna()
    df_signals['Return'] = df_signals['MarketReturn'] * df_signals['Signal']
    df_signals.to_excel('df_signals.xlsx')
    return df_signals