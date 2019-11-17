import pandas as pd
import numpy as np


def playground():
    dataFrame = pd.read_csv("train.csv")
    modDataFrame = dataFrame.drop(
        ["Orientation", "DisplayName", "JerseyNumber", "VisitorScoreBeforePlay", "HomeScoreBeforePlay", "PlayerBirthDate", "VisitorTeamAbbr", "HomeTeamAbbr","Stadium"], axis=1)
    print(modDataFrame.columns)
    matrix = modDataFrame.values
    print(matrix)
    # print(modDataFrame["DisplayName"])



if __name__ == "__main__":
    playground()
