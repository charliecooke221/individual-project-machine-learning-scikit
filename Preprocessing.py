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

    def __init__(self):

        filename ='feature'
        for file in os.listdir():
            if file.startswith('feat') & file.endswith('.csv'):
                filename = file

        self.features_dataframe = pd.read_csv(filename, error_bad_lines=False)

    def main(self):
        old_columns = ['Match ID', 'Date', 'Map', 'Team 1 ID', 'Team 2 ID', 'End Score Diff', 'Winner']
        using_columns = ['Winner','End Score Diff','Team 1 ID', 'Team 2 ID', 'Recent Matches Score Difference', 'Past Encounters Score Difference','Common Opponents Average Score difference','Map Score Difference']

        self.features_dataframe = self.features_dataframe[using_columns]

        # remove rows containing empty values
        self.features_dataframe = self.features_dataframe.dropna(axis=0, how='any')


        dependent_var_bool = self.features_dataframe.ix[:,0].values
        dependant_var_ordinal = self.features_dataframe.ix[:,1].values



        independant_vars = self.features_dataframe.ix[:,(4,5,6,7)].values

        independant_vars_scaled = preprocessing.scale(independant_vars)


        LogReg_bool = LogisticRegression()
        LogReg_bool.fit(independant_vars_scaled,dependent_var_bool)
        print(LogReg_bool.score(independant_vars_scaled,dependent_var_bool))


        y_pred = LogReg_bool.predict(independant_vars_scaled)

        print(metrics.classification_report(dependent_var_bool, y_pred))

        LogReg_ordinal = LogisticRegression()
        LogReg_ordinal.fit(independant_vars_scaled, dependant_var_ordinal)
        print(LogReg_ordinal.score(independant_vars_scaled, dependant_var_ordinal))




if __name__ == "__main__":
    x = Preprocessing()
    x.main()