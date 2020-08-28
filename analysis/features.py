import json
import pandas as pd
import numpy as np
import math
import os.path as op


pd.options.display.width = 0


class feature_extraction:

    DATA_DIR = op.abspath(op.join(__file__, op.pardir, op.pardir, 'data'))
    DATA_PATH = op.join(DATA_DIR, 'clean_data.json')

    def __init__(self):

        with open(self.DATA_PATH) as file:
            data = json.load(file)

        self.data = data
        self.X = []
        self.y = []

    def initialize(self, data):

        self.X = []
        self.y = []

        for point in data:
            self.X.append(
                [point['children'], point['controversiality'], point['is_root']])
            self.y.append(point['popularity_score'])

    # More preprocessing and setting up the data
    def process_text(self, data):

        # split the text data
        for point in data:
            point['text_split'] = point['text'].split()

        # split the data into training, validation and testing sets
        return self.data_split(data)

    def data_split(self, data):
        return data[:10000], data[10000:11000], data[11000:]
