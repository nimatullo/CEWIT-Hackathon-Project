import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy

df = pd.read_csv('mvp_votings.csv')

orig_features = ['fga', 'fg3a', 'fta', 'per', 'ts_pct', 'usg_pct', 'bpm',
                 'mp_per_g', 'pts_per_g', 'trb_per_g', 'ast_per_g',
                 'stl_per_g', 'blk_per_g', 'fg_pct', 'fg3_pct', 'ft_pct', 'ws',
                 'ws_per_48', 'win_pct']

X_train = df[orig_features].to_numpy()
y_data = df[['award_share']].to_numpy()
y_data = y_data.reshape(y_data.shape[0], )

regress = RandomForestRegressor(n_estimators=200)

regress.fit(X_train, y_data)

indices = numpy.argsort(regress.feature_importances_)[::-1]

for index in indices:
    print(f"{orig_features[index]}: {regress.feature_importances_[index]}")
