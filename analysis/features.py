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

    # function that calculates the most common words and outputs it to a text file
    def calc_common_words(self, data):
        word_count = Counter()  # Use counter tool to provide counting for word frequencies
        for point in data:
            word_count += Counter(point['text_split'])

        # Write the top 160 most common words to a file
        common_words = [w[0] for w in word_count.most_common(160) if w[0]]
        with open('data/common_words.txt', 'w+') as file:
            file.writelines(f'{word}\n' for word in common_words)

    # Calculate the count of most common words per data point (in this case the data points are comments, the text)

    def calc_words_data(self, data):
        x_counts = []

        with open('data/common_words.txt', 'r+') as file:
            common_words = file.read().splitlines()[:160]
        if(common_words):
            for point in data:
                # get the comment from the data
                comment = Counter(point['text_split'])
                # append to word frequency array
                x_counts.append([comment.get(word, 0)
                                 for word in common_words])

        return x_counts
