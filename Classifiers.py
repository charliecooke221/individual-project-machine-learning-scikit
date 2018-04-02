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

    dataset = pd.DataFrame
    feature_columns = ""

    def __init__(self, dataset, feature_columns):
        self.dataset = dataset
        feature_columns = feature_columns

    def predict(self):





        dependent_var_bool = self.dataset["Winner"]
        independent_vars = self.dataset[self.feature_columns]


    def splitDataset(self,trainingDateStart,trainingDateEnd,testDateStart,testDateEnd):

        #get index at each date then trim


        self.trainingSet = self.dataset.loc[trainingDateStart:trainingDateEnd]


        print(self.trainingSet.head())

        self.testSet = self.dataset.loc[testDateStart:testDateEnd]



    def get_date_index(self, df, date, date_range, search_forward):
        print('get index for ' + str(date))
        start_index_found = False
        days_searched = 0

        if search_forward:
            day_direction = 1
        else:
            day_direction = -1

        while not start_index_found:
            if days_searched <= date_range:
                index = df.index.get_loc(str(date))
                print(type(index))

                if type(index) == slice:
                    if search_forward:
                        return index.start
                    else:
                        return index.stop

                elif not index.any():

                    print('no matches on specified date')
                    date += pd.Timedelta('%d days' % day_direction)
                    print('new date ' + str(date))
                    days_searched += 1

                else:
                    print('match found on date ' + str(date))

                    if search_forward:
                        return index.item(0)
                    else:
                        return index.item(-1)
            else:
                print("No matches in date range") # make exception
                return 0
