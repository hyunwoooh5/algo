import pandas as pd


def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    grouped = logins[(logins['time_stamp'] >= pd.Timestamp('2020-01-01 00:00:00')) & (logins['time_stamp'] <
                                                                                      pd.Timestamp('2021-01-01 00:00:00'))].groupby('user_id', as_index=False)['time_stamp'].agg([('last_stamp', 'max')])
    return grouped
