import pandas as pd

features = ['pts_per_g', 'ast_per_g', 'trb_per_g', 'stl_per_g',
            'mp_per_g', 'ws', 'fg_pct', 'win_pct', 'usg_pct']

df = (pd.read_csv("mvp_votings.csv"))[features]
