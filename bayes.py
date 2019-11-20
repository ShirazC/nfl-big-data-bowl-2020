from sklearn.naive_bayes import BernoulliNB
import preprocess
import pandas as pd
import numpy as np




class NaiveBayes():
    #Constructor
    def __init__(self,trainPath, testPath):
        self.preprocessUtil = preprocess.PreprocessUtil()
        self.trainPath = trainPath
        self.testPath = testPath
        self.dataFrame = pd.read_csv(self.trainPath)
        self.model = BernoulliNB()
        # print(self.dataFrame["Down"])
        self.parseData()
        # self.dataFrame = self.dataFrame.head(n=500)
        # for index, value in enumerate(list(set(self.dataFrame["WindDirection"]))):
        #     print(index,value)
        # print(len(set(self.dataFrame["OffensePersonnel"])))
        # print(self.dataFrame["WindDirection"])
        
    #Parse Data
    def parseData(self):
        self.dataFrame = self.preprocessUtil.dropColumns(self.dataFrame, [
                                                         "Orientation", "DisplayName", "JerseyNumber", "VisitorScoreBeforePlay", 
                                                         "HomeScoreBeforePlay", "PlayerBirthDate", "VisitorTeamAbbr", "HomeTeamAbbr", 
                                                         "Stadium", "Team", "TimeHandoff", "TimeSnap","GameClock","PossessionTeam",
                                                         "PlayerCollegeName", "Location", "FieldPosition","DefensePersonnel", 
                                                         "PlayDirection", "PlayerBirthDate","Position"])
        #Offense Formation
        self.dataFrame = self.preprocessUtil.discretizeValues(self.dataFrame, "OffenseFormation")
        #Offense Personnel
        self.dataFrame = self.preprocessUtil.discretizeValues(self.dataFrame, "OffensePersonnel")
        #Wind Direction
        self.dataFrame = self.preprocessUtil.discretizeValues(self.dataFrame, "WindDirection")
        #Turf
        self.dataFrame = self.preprocessUtil.discretizeValues(self.dataFrame, "Turf")
        #Player Height
        self.dataFrame = self.preprocessUtil.discretizeValues(self.dataFrame, "PlayerHeight")
        #Stadium Type
        self.dataFrame = self.preprocessUtil.discretizeValues(self.dataFrame, "StadiumType")
        #Game Weather
        self.dataFrame = self.preprocessUtil.discretizeValues(self.dataFrame, "GameWeather")
        
        
        
        
        
    
    #Train model
    def trainModel(self):
        trainLabels = self.dataFrame["Yards"].values
        self.dataFrame = self.dataFrame.drop(["Yards"],axis=1)
        self.dataFrame = self.dataFrame[self.dataFrame["NflIdRusher"] == self.dataFrame["NflId"]]
        trainVectors = self.dataFrame.values
        # print(len(self.dataFrame.columns))
        for col in self.dataFrame:
            print(self.dataFrame[col].dtype)
        # self.model.fit(trainVectors,trainLabels)
        
    
    #Predict
    def predict(self):
        pass   
        
        
if __name__ == "__main__":
    bayesianModel = NaiveBayes("train.csv", None)
    bayesianModel.trainModel()
        
        
        
    
