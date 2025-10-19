import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    grouped = activity.groupby('player_id')

    play = grouped['event_date'].agg('min').reset_index()

    return play[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})
