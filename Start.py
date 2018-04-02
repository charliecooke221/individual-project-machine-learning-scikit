import Preprocessing
import Classifiers

import Betting

class Start:

    features_to_consider = ['Recent Matches Score Difference', 'Past Encounters Score Difference','Common Opponents Average Score difference','Map Score Difference']
    normalise = True
    classification_model = 'logisticRegression' # options: logisticRegression, ordinalLogisticRegression

    splitByDate = True
    trainingDateStart = '2017-01-01'
    trainingDateEnd = '2017-12-31'
    testDateStart = '2018-01-1'
    testDateEnd = '20118-02-30'


    def __init__(self):
        self.columns_to_consider = ['Date','End Score Diff','Map','Match ID','Team 1 ID', 'Team 2 ID','Winner',]

    def main(self):

        pre = Preprocessing.Preprocessing(self.features_to_consider)

        if self.normalise :
            pre.scale()  # TODO different scaling options

        if self.classification_model == 'logisticRegression':
            predict = Classifiers.Classifiers(pre.features_dataframe,self.features_to_consider)

            if self.splitByDate:
                predict.splitDataset(self.trainingDateStart,self.trainingDateEnd,self.testDateStart,self.testDateEnd)

        else:
            print("other model")






if __name__ == "__main__":
    x = Start()
    x.main()
