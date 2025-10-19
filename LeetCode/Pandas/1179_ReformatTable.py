import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    department['month'] = pd.Categorical(
        department['month'], categories=months, ordered=True
    )
    pivoted = department.pivot_table(
        index='id', columns='month', values='revenue', dropna=False).add_suffix('_Revenue')

    return pivoted.reset_index()
