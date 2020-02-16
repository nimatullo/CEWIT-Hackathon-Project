import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
df = pd.read_csv("data/mvp_votings.csv")
features = ['fga', 'fg3a', 'fta', 'per', 'ts_pct', 'usg_pct', 'bpm',
            'mp_per_g', 'pts_per_g', 'trb_per_g', 'ast_per_g',
            'stl_per_g', 'blk_per_g', 'fg_pct', 'fg3_pct', 'ft_pct', 'ws',
            'ws_per_48', 'win_pct']
data_frame = df[features]
cmap = sn.cm.rocket_r
corr = data_frame.corr()
sn.heatmap(corr, annot=True,cmap=cmap)
plt.show()