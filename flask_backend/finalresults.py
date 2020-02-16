import statistics
from models.randomforest import forest_prediction
from models.linearreg import linear_regression_prediction
from models.gradientboost import gradient_prediction

import pandas as pd

results_average = []
current_players = pd.read_csv("data/current_results.csv")

for i, prediction in enumerate(gradient_prediction):
    results_average.append(
        ((forest_prediction[i] + linear_regression_prediction[i] + gradient_prediction[i]) / 3))

formated_pred = {}

index = 0
for award_share in results_average:
    formated_pred[award_share] = current_players['player'][index]
    index = index + 1

index = 0
result = []
for player in sorted(formated_pred.keys(), reverse=True):
    data = {'name': formated_pred[player], 'award_share': player}
    result.append(data)
