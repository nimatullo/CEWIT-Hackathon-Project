import statistics
from randomforest import forest_prediction
from linearreg import linear_regression_prediction
from gradientboost import gradient_prediction

import pandas as pd

results_average = []
current_players = pd.read_csv("test_data.csv")

for i, prediction in enumerate(gradient_prediction):
    results_average.append(
        ((forest_prediction[i] + linear_regression_prediction[i] + gradient_prediction[i]) / 3))

formated_pred = {}

index = 0
for award_share in results_average:
    formated_pred[award_share] = current_players['player'][index]
    index = index + 1

index = 1
for player in sorted(formated_pred.keys(), reverse=True):
    print(f'{index}. {formated_pred[player]}: {player}')
    index = index + 1
