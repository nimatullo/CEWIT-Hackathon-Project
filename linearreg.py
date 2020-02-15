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
model = lm.fit(x, y)
linear_regression_prediction = lm.predict(X_test)
