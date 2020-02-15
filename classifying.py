import pandas as pd

features = ['pts_per_g', 'ast_per_g', 'trb_per_g', 'stl_per_g',
            'mp_per_g', 'ws', 'ts', 'win_pct', 'usg_pct', 'bpm']

df = (pd.read_csv("mvp_votings.csv"))[features]
