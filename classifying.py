import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import numpy as np

features = ['pts_per_g', 'ast_per_g', 'trb_per_g', 'stl_per_g',
            'mp_per_g', 'blk_per_g', 'ws', 'ts_pct', 'win_pct']

df = (pd.read_csv("mvp_votings.csv"))
current_players = pd.read_csv("test_data.csv")
df = df[features + ['award_share']]


X_train = df[features].to_numpy()
y_train = df['award_share'].to_numpy()

X_train, y_train = shuffle(X_train, y_train)

forest = GradientBoostingRegressor()
forest.fit(X_train, y_train)

prediction = forest.predict(current_players[features])
formated_pred = {}

index = 0
for award_share in prediction:
    formated_pred[award_share] = current_players['player'][index]
    index = index + 1

index = 1
for player in sorted(formated_pred, reverse=True):
    print(f'{index}. {formated_pred[player]}: {player}')
    index = index + 1
