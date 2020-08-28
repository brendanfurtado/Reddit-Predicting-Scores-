import json
import pandas as pd
import numpy as np
import math
import os.path as op


pd.options.display.width = 0


class data_analysis:

    DATA_DIR = op.abspath(op.join(__file__, op.pardir, op.pardir, 'data'))
    DATA_PATH = op.join(DATA_DIR, 'clean_data.csv')

    def __init__(self):

        with open(self.DATA_PATH) as file:
            data = json.load(file)
            print(data)

        self.data = data
        self.X = []
        self.y = []

    def initialize(self, data):

        self.X = []
        self.y = []

        for column in data:
            self.X.append(
                [column['children'], column['controversiality'], column['is_root']])
            self.y.append(column['popularity_score'])
