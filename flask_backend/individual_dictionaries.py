from models.randomforest import forest_prediction
from models.linearreg import linear_regression_prediction
from models.gradientboost import gradient_prediction
import pandas as pd

current_players = pd.read_csv("data/current_results.csv")


def dictionary(award_share_list):
    formatted_pred = {}

    index = 0
    for award_share in award_share_list:
        formatted_pred[award_share] = current_players['player'][index]
        index = index + 1

    index = 0
    result = []
    for player in sorted(formatted_pred.keys(), reverse=True):
        data = {'name': formatted_pred[player], 'award_share': player}
        result.append(data)

    return result


RFR = dictionary(forest_prediction)
LR = dictionary(linear_regression_prediction)
GBR = dictionary(gradient_prediction)
