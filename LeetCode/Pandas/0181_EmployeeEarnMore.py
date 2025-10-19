import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(employee, left_on='managerId',
                            right_on='id', suffixes=('', '_manager'))

    filtered = merged[merged['salary'] > merged['salary_manager']]
    result = filtered[['name']]

    return result.rename(columns={'name': 'Employee'})
