import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, bonus, how='outer', on='empId')

    return merged[(merged['bonus'] < 1000) | (pd.isna(merged['bonus']))][['name', 'bonus']]
