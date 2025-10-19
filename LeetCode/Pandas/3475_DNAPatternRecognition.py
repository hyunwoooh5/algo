import pandas as pd


def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    def has_start(x):
        return x[:3] == 'ATG'

    def has_stop(x):
        return x[-3:] == 'TAA' or x[-3:] == 'TAG' or x[-3:] == 'TGA'

    def has_atat(x):
        return 'ATAT' in x

    def has_ggg(x):
        return 'GGG' in x

    samples['has_start'] = samples['dna_sequence'].apply(has_start).astype(int)
    samples['has_stop'] = samples['dna_sequence'].apply(has_stop).astype(int)
    samples['has_atat'] = samples['dna_sequence'].apply(has_atat).astype(int)
    samples['has_ggg'] = samples['dna_sequence'].apply(has_ggg).astype(int)

    return samples
