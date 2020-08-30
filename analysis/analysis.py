import numpy as np
from features import feature_extraction

dataObj = feature_extraction()
train, validation, test = dataObj.process_text(dataObj.data)
# calculate the most common words in data set
# will output a text file (common_words.txt)
dataObj.calc_common_words(dataObj.data)

# calculate the frequency if common words occurrences per comment
# now each comment has the frequency of all the most common words in the corpus
common_words = dataObj.calc_freq_words(
    dataObj.data)  # common_words is an array
print("done")
