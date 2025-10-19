import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person[person.duplicated(
        subset='email', keep='first')].drop_duplicates(subset='email')

    return result[['email']].rename(columns={'email': "Email"})
