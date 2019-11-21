from sklearn import tree
import preprocess
import pandas as pd
import numpy as np


class DecisionTree():
    #Constructor
    def __init__(self, trainPath, testPath):
        self.preprocessUtil = preprocess.PreprocessUtil()
        self.trainPath = trainPath
        self.testPath = testPath
        self.dataFrame = pd.read_csv(self.trainPath)
        self.model = tree.DecisionTreeClassifier()
        self.parseData()

    #Parse Data
    def parseData(self):
        self.dataFrame = self.dataFrame[self.dataFrame["NflIdRusher"]
                                        == self.dataFrame["NflId"]]
        self.dataFrame = self.preprocessUtil.dropColumns(self.dataFrame, [
                                                         "Orientation", "DisplayName", "JerseyNumber", "VisitorScoreBeforePlay",
                                                         "HomeScoreBeforePlay", "PlayerBirthDate", "VisitorTeamAbbr", "HomeTeamAbbr",
                                                         "Stadium", "Team", "TimeHandoff", "TimeSnap", "GameClock", "PossessionTeam",
                                                         "PlayerCollegeName", "Location", "FieldPosition", "DefensePersonnel",
                                                         "PlayDirection", "PlayerBirthDate", "Position"])
        #Offense Formation
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "OffenseFormation")
        #Offense Personnel
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "OffensePersonnel")
        #Wind Direction
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "WindDirection")
        #Turf
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "Turf")
        #Player Height
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "PlayerHeight")
        #Stadium Type
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "StadiumType")
        #Game Weather
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "GameWeather")
        #Defenders in the Box
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "DefendersInTheBox")
        #Wind Speed
        self.dataFrame = self.preprocessUtil.discretizeValues(
            self.dataFrame, "WindSpeed")

    #Train model
    def trainModel(self):
        trainFrame = self.dataFrame.head(n=20000)
        trainLabels = trainFrame["Yards"].values
        trainFrame = trainFrame.drop(["Yards"], axis=1)
        trainFrame = trainFrame.fillna(value=1.0)
        trainVectors = trainFrame.values
        self.model.fit(trainVectors, trainLabels)

    #Predict

    def predict(self):
        testFrame = self.dataFrame.tail(n=3000)
        testLabels = testFrame["Yards"].values
        testFrame = testFrame.drop(["Yards"], axis=1)
        testFrame = testFrame.fillna(value=1.0)
        testVectors = testFrame.values
        predictions = self.model.predict(testVectors)
        numCorrect = 0.0
        for prediction, trueYardage in zip(predictions, testLabels):
            if abs(trueYardage - prediction) <= 3.0:
                numCorrect += 1
        print("Test Accuracy: %.2f%%" % (numCorrect / len(predictions) * 100))


if __name__ == "__main__":
    bayesianModel = DecisionTree("train.csv", None)
    bayesianModel.trainModel()
    bayesianModel.predict()
