import pandas as pd


def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks['capital_gain_loss'] = np.where(
        stocks['operation'] == 'Buy', -stocks['price'], stocks['price'])

    return stocks.groupby('stock_name', as_index=False)['capital_gain_loss'].sum()
