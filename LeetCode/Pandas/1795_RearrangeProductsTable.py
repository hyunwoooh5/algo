import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melted = pd.melt(products, id_vars=['product_id'], value_vars=[
                     'store1', 'store2', 'store3'])

    return melted.dropna().rename(columns={'variable': 'store', 'value': 'price'})
