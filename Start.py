import pandas as pd
import Preprocessing
import Classifiers

import Betting

class Start:

    features_to_consider = ['Recent Matches Score Difference', 'Past Encounters Score Difference','Common Opponents Average Score difference','Map Score Difference']
    normalise = True
    classification_model = 'logisticRegression' # options: logisticRegression, ordinalLogisticRegression

    splitByDate = True
    trainingDateStart = pd.to_datetime('2017-01-01')
    trainingDateEnd = pd.to_datetime('2017-12-31')
    testDateStart = pd.to_datetime('2018-01-1')
    testDateEnd = pd.to_datetime('2018-02-18')


    def __init__(self):
        self.columns_to_consider = ['Date','End Score Diff','Map','Match ID','Team 1 ID', 'Team 2 ID','Winner',]

    def main(self):

        pre = Preprocessing.Preprocessing(self.features_to_consider)

        if self.normalise :
            pre.scale()  # TODO different scaling options

        if self.classification_model == 'logisticRegression':
            logReg_predict = Classifiers.Classifiers(pre.features_dataframe,self.features_to_consider)

            if self.splitByDate:
                logReg_predict.splitDataset(self.trainingDateStart,self.trainingDateEnd,self.testDateStart,self.testDateEnd)

            logReg_predict.LogRegTrainModel()
            logReg_predict.LogRegTestModel()

        else:
            print("other model")






if __name__ == "__main__":
    x = Start()
    x.main()
