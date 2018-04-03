import pandas as pd
import numpy as np
import os
import scipy
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn import metrics


# train model, predict test dataset, perform standard evaluation


class Classifiers:

    feature_columns = ""
    dataset = pd.DataFrame
    trainingSet = pd.DataFrame
    testSet = pd.DataFrame
    logReg = LogisticRegression()


    def __init__(self, dataset, feature_columns):
        self.dataset = dataset
        self.feature_columns = feature_columns

    def LogRegTrainModel(self):

        train_label_var_bool = self.trainingSet["Winner"]
        train_feature_vars = self.trainingSet[self.feature_columns]
        #print(independent_vars.head())

        self.logReg = LogisticRegression()
        self.logReg.fit(train_feature_vars,train_label_var_bool)

    def LogRegTestModel(self):

        test_feature_vars = self.testSet[self.feature_columns]
        test_label_vars =  self.testSet["Winner"]
        predicted_values = self.logReg.predict(test_feature_vars)
        #print(predicted_values.shape)

        probability_values = self.logReg.predict_proba(test_feature_vars)
        #print(probability_values.shape)
        #print(self.testSet.shape)

        decisionFunc_values = self.logReg.decision_function(test_feature_vars)
        #print(decisionFunc_values[6])

        self.testSet.loc[:,'Winner(predicted)'] = predicted_values
        self.testSet.loc[:,'Predicted Probability 0'] = probability_values[:,0]
        self.testSet.loc[:,'Predicted Probability 1'] = probability_values[:,1]
        self.testSet.to_csv('testPredictions.csv')

        print("Prediction Complete. Output written to testPredictions.csv \n")

        #print(self.testSet.head(5))

        # Performance Metrics
        accuracy_score = self.logReg.score(test_feature_vars,test_label_vars)
        print("Mean accuracy of logreg on testset = " + str(accuracy_score))
        print("Confusion Matrix")
        print( metrics.confusion_matrix(test_label_vars,predicted_values))
        print("Additional Metrics")
        print(metrics.classification_report(test_label_vars, predicted_values))

    def splitDataset(self,trainingDateStart,trainingDateEnd,testDateStart,testDateEnd):

        # get index at each date then trim
        training_start_index = self.get_date_index(self.dataset,trainingDateStart,30,True)
        training_end_index = self.get_date_index(self.dataset,trainingDateEnd,30,False)

        self.trainingSet = self.dataset.loc[training_start_index:training_end_index].copy()

        test_start_index = self.get_date_index(self.dataset,testDateStart,30,True)
        test_end_index  = self.get_date_index(self.dataset,testDateEnd,30,False)

        self.testSet = self.dataset.loc[test_start_index:test_end_index].copy()

        #print(self.trainingSet.head())
        #print(self.testSet.head())


    def get_date_index(self, df, date, date_range, search_forward):

        # print('get index for ' + str(date))
        start_index_found = False
        days_searched = 0

        if search_forward:
            day_direction = 1
        else:
            day_direction = -1

        while not start_index_found:
            if days_searched <= date_range:
                index = df.index[df['Date'] == str(date)].tolist()
                #print(type(index))

                if type(index) == slice:
                    if search_forward:
                        return index.start
                    else:
                        return index.stop

                elif not index:

                    # print('no matches on specified date')
                    date += pd.Timedelta('%d days' % day_direction)
                    # print('new date ' + str(date))
                    days_searched += 1

                else:
                    # print('match found on date ' + str(date))
                    # print(index)

                    if search_forward:
                        return index[0]
                    else:
                        return index[-1]
            else:
                print("No matches in date range") # make exception
                return 0
