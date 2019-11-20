class PreprocessUtil():
    
    def dropColumns(self, dataFrame, dropList):
        return dataFrame.drop(dropList, axis=1)
    
    def discretizeValues(self, dataFrame, category):
        category = str(category)
        for index, value in enumerate(list(set(dataFrame[category]))):
            dataFrame[category] = dataFrame[category].mask(dataFrame[category] == str(value), index)
        return dataFrame
    
    
