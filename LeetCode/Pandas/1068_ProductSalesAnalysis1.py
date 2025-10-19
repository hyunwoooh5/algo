import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(sales, product, left_on='product_id',
                      right_on='product_id')

    return merged[['product_name', 'year', 'price']]
