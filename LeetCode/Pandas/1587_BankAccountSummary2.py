import pandas as pd


def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    count = transactions.groupby('account', as_index=False)['amount'].sum()

    merged = pd.merge(users, count, on='account', how='left')

    return merged[merged['amount'] > 10000][['name', 'amount']].rename(columns={'amount': 'balance'})
