import pandas as pd


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    def fm(x):
        if x == 'm':
            return 'f'
        elif x == 'f':
            return 'm'

    salary['sex'] = salary['sex'].apply(fm)

    return salary
