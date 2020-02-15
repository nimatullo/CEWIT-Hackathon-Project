import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
tips = pd.read_csv("mvp_votings.csv")
#sns.relplot(x="award_share", y="stl_per_g", data=tips)
#sns.relplot(x="award_share", y="ws", data=tips)
# sns.regplot(x="award_share", y="stl_per_g", data=tips)
sns.jointplot(x="award_share", y="ws", data=tips,kind="reg")

plt.show()