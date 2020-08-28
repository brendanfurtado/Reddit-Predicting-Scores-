import json
import math
import os.path as op
from collections import Counter


class feature_extraction:

    DATA_DIR = op.abspath(op.join(__file__, op.pardir, op.pardir, 'data'))
    DATA_PATH = op.join(DATA_DIR, 'clean_data.json')

    def __init__(self):

        with open(self.DATA_PATH) as file:
            data = json.load(file)

        self.data = data
        self.X = []
        self.y = []

    # More preprocessing and setting up the data
    def process_text(self, data):

        # split the text data
        for point in data:
            point['text_split'] = point['text'].split()

        # split the data into training, validation and testing sets
        return self.data_split(data)

    def data_split(self, data):
        return data[:10000], data[10000:11000], data[11000:]

    def calc_common_words(self, data):
        word_count = Counter()
        for point in data:
            word_count += Counter(point['text_split'])

        # Write the top 160 most common words to a file
        top_words = [w[0] for w in word_count.most_common(160) if w[0]]
        with open("data/common_words.txt", 'w+') as f:
            f.writelines(f'{word}\n' for word in top_words)
