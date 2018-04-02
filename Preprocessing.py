import pandas as pd
import numpy as np
import os
import scipy
import sklearn
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn import metrics


class Preprocessing:

    features_dataframe = pd.DataFrame

    def __init__(self,feature_columns):
        self.feature_columns = feature_columns
        self.using_columns = ['Date', 'End Score Diff', 'Map', 'Match ID', 'Team 1 ID', 'Team 2 ID', 'Winner'] + feature_columns

        filename ='feature'
        for file in os.listdir(): # find feature file if date is appended to name
            if file.startswith('feature') & file.endswith('.csv'):
                filename = file

        # remove overlapping rows
        self.features_dataframe = pd.read_csv(filename, error_bad_lines=False)

        # use only desired columns
        self.features_dataframe = self.features_dataframe[self.using_columns]

        # remove rows containing empty values
        self.features_dataframe = self.features_dataframe.dropna(axis=0, how='any')


    def scale(self):


        #print(self.features_dataframe.head())
        self.features_dataframe[self.feature_columns] = preprocessing.scale(self.features_dataframe[self.feature_columns])
        #print(self.features_dataframe.head())


        #old_columns = ['Match ID', 'Date', 'Map', 'Team 1 ID', 'Team 2 ID', 'End Score Diff', 'Winner']
        #using_columns = ['Winner','End Score Diff','Team 1 ID', 'Team 2 ID', 'Recent Matches Score Difference', 'Past Encounters Score Difference','Common Opponents Average Score difference','Map Score Difference']

        #dependent_var_bool = self.features_dataframe.ix[:,0].values
        #dependant_var_ordinal = self.features_dataframe.ix[:,1].values

        #independant_vars = self.features_dataframe.ix[:,(4,5,6,7)].values

        #independant_vars_scaled = preprocessing.scale(independant_vars)

        #
        # LogReg_bool = LogisticRegression()
        # LogReg_bool.fit(independant_vars_scaled,dependent_var_bool)
        # print(LogReg_bool.score(independant_vars_scaled,dependent_var_bool))
        #
        #
        # y_pred = LogReg_bool.predict(independant_vars_scaled)
        #
        #
        # print(metrics.classification_report(dependent_var_bool, y_pred))
        # print(metrics.confusion_matrix(dependent_var_bool,y_pred))
        #
        #
        #
        # LogReg_ordinal = LogisticRegression()
        # LogReg_ordinal.fit(independant_vars_scaled, dependant_var_ordinal)
        # ordinal_pred = LogReg_ordinal.predict(independant_vars_scaled)

        # print(independant_vars_scaled[15,:])
        # print(ordinal_pred[15])

        # print(LogReg_ordinal.score(independant_vars_scaled, dependant_var_ordinal))




# if __name__ == "__main__":
#     x = Preprocessing()
#     x.main()