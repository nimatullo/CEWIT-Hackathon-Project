import numpy as np
import pandas as pd 
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot


features = ['pts_per_g', 'ast_per_g', 'trb_per_g', 'stl_per_g',
            'mp_per_g', 'ws', 'ts_pct', 'win_pct', 'usg_pct', 'bpm']

df = (pd.read_csv("mvp_votings.csv"))
currentplayers = (pd.read_csv("test_data.csv"))


x = df[features]
y = df['award_share']

X_test = currentplayers[features]


lm = linear_model.LinearRegression()
model = lm.fit(x,y)
predictions = lm.predict(X_test)
formated_pred = {}

index = 0
for award_share in predictions:
    formated_pred[award_share] = currentplayers['player'][index]
    index = index + 1

index = 1
for player in sorted(formated_pred.keys(), reverse=True):
    print(f'{index}. {formated_pred[player]}: {player}')
    index = index + 1



# plot.scatter(X_test, predictions, color = 'green')

# plot.show()

# print(df.head(10))

