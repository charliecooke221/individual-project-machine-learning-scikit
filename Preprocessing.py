from sklearn import preprocessing
import pandas as pd
import numpy as np

class Preprocessing:

    def __init__(self):
        self.features_dataframe = pd.read_csv("feature.csv", error_bad_lines=False)

    def main(self):
        old_columns = ['Match ID', 'Date', 'Map', 'Team 1 ID', 'Team 2 ID', 'End Score Diff', 'Winner']
        using_columns = ['Winner','End Score Diff','Team 1 ID', 'Team 2 ID', 'Recent Matches Score Difference', 'Past Encounters Score Difference','Common Opponents Average Score difference','Map Score Difference']

        self.features_dataframe = self.features_dataframe[using_columns]
        print(self.features_dataframe.head())

        # remove rows contaiing empty values 
        self.features_dataframe = self.features_dataframe.dropna(axis=0, how='any')
        print(self.features_dataframe.head())

if __name__ == "__main__":
    x = Preprocessing()
    x.main()