import pandas as pd


def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    grouped = user_activity.groupby('user_id').agg(
        trial_avg_duration=('activity_duration', lambda x: (
            x[user_activity['activity_type'] == 'free_trial'] + 1e-4).mean()),
        paid_avg_duration=('activity_duration', lambda x: (
            x[user_activity['activity_type'] == 'paid'] + 1e-4).mean())
    ).dropna().round(2).sort_values(by='user_id', ascending=True)

    return grouped.reset_index()[['user_id', 'trial_avg_duration', 'paid_avg_duration']]
