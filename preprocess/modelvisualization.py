import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
tips = pd.read_csv("data/mvp_votings.csv")
# sns.jointplot(x="award_share", y="stl_per_g", data=tips,kind="reg",color="m")
sns.jointplot(x="award_share", y="ws", data=tips,kind="reg",color="m")

# Grid Graphs=========================================================
# features = ['pts_per_g', 'ast_per_g', 'trb_per_g', 'stl_per_g',
#             'mp_per_g', 'blk_per_g', 'ws', 'ts_pct', 'win_pct']
# x_data = ['award_share','ws']
# sns.pairplot(tips,x_vars=x_data,y_vars=features,kind="reg")
#=====================================================================
plt.show()